---
title: SPAN and ERSPAN
author: NVIDIA
weight: 1145
toc: 4
---
SPAN (Switched Port Analyzer) enables you to mirror all packets that come in from or go out of an interface (the *SPAN source*), and copy and transmit the packets out of a local port or CPU (the *SPAN destination*) for monitoring. The SPAN destination port is also referred to as a mirror-to-port (MTP). The original packet is still switched, while a mirrored copy of the packet is sent out of the MTP.

ERSPAN (Encapsulated Remote SPAN) enables the mirrored packets to be sent to a monitoring node located anywhere across the routed network. The switch finds the outgoing port of the mirrored packets by looking up the destination IP address in its routing table. The original layer 2 packet is encapsulated with GRE for IP delivery. The encapsulated packets have the following format:

```
 ----------------------------------------------------------
| MAC_HEADER | IP_HEADER | GRE_HEADER | L2_Mirrored_Packet |
 ----------------------------------------------------------
```

You can configure SPAN and ERSPAN in one of the following ways:
- With NCLU commands (Mellanox switches only)
- With ACL rules (Mellanox and Broadcom switches)
- Manually by editing the `/etc/cumulus/switchd.d/port-mirror.conf` file - for advanced users (Mellanox switches only)

All three methods are described below.

{{%notice note%}}
- Mirrored traffic is not guaranteed. If the MTP is congested, mirrored packets might be discarded.
- A SPAN and ERSPAN destination interface that is oversubscribed might result in data plane buffer depletion and buffer drops. Exercise caution when enabling SPAN and ERSPAN when the aggregate speed of all source ports exceeds the destination port.
- Because SPAN and ERSPAN is done in hardware, eth0 is not supported as a destination.
- Cut-through mode is not supported for ERSPAN in Cumulus Linux on switches using Broadcom Tomahawk, Trident II+ and Trident II ASICs.
- Cumulus Linux does not support IPv6 ERSPAN destinations.
- ERSPAN does not cause the kernel to send ARP requests to resolve the next hop for the ERSPAN destination. If an ARP entry for the destination or next hop does not already exist in the kernel, you need to manually resolve this before mirrored traffic is sent (use ping or arping).
- Mirroring to the same interface that is being monitored causes a recursive flood of traffic and might impact traffic on other interfaces.
- Cumulus VX does not support ACL rules for SPAN, ERSPAN, or port mirroring. To capture packets in Cumulus VX, use the `tcpdump` command line network traffic analyzer.
{{%/notice%}}

## NCLU Configuration

- To configure SPAN with NCLU, run the `net add port-mirror session <session-id> (ingress|egress) span src-port <interface> dst-port <interface>` command.
- To configure ERSPAN with NCLU, run the `net add port-mirror session <session-id> (ingress|egress) erspan src-port <interface> src-ip <interface> dst-ip <ip-address>` command.

The command parameters are described below.

| <div style="width:250px">Parameter | Description |
| --------- | ----------- |
| `session <id>` | The session ID. This is a number between 0 and 7. |
| `ingress` or `egress` | The session direction:<ul><li> Ingress, where packets received on a port are sent to a sniffer port (SPAN) or destination IP address (ERSPAN).</li><li>Egress, where packets transmitted by the port are sent to the sniffer port (SPAN) or destination IP address (ERSPAN).</li></ul><br>To configure both ingress and egress, create two sessions.|
| `src-port <interface>` | The interface or list of interfaces on which the mirror session applies. You can specify swp or bond interfaces. Separate the interfaces in the list with a comma; for example swp1,swp45,swp46.{{%notice note%}}For ERSPAN, you can specify only one interface.{{%/notice%}}|
| `dst-port <interface>` | The interface to which the frame is mirrored for SPAN. A traffic analyzer, monitor or a host can be connected to this interface to observe the traffic sniffed from the source interface. Only swp interfaces are supported.<br><br>On Broadcom switches, Cumulus Linux supports a maximum of four ingress interfaces and four egress interfaces. You can configure a maximum of four mirroring sessions per switch.<br><br> On Mellanox Spectrum switches, Cumulus Linux supports a maximum of three analyzer ports. On Mellanox switches with the Spectrum-2 and Spectrum-3 ASIC, Cumulus Linux supports a maximum of eight analyzer ports. You can configure multiple sessions to a single analyzer port.|
| `src-ip <ip-address>` | The source IP address for ERSPAN encapsulation. This is typically the loopback address of the switch. |
| `dst-ip <ip-address>` | The destination IP address for ERSPAN encapsulation. This is typically the loopback address of the destination device.|

The NCLU commands save the configuration in the `/etc/cumulus/switchd.d/port-mirror.conf` file.

### Example Commands

The following example commands mirror all packets received on swp1, and copy and transmit the packets to swp2 for monitoring:

```
cumulus@switch:~$ net add port-mirror session 1 ingress span src-port swp1 dst-port swp2
cumulus@switch:~$ net pending
cumulus@switch:~$ net commit
```

The following example commands mirror all packets that are sent out of swp1, and copy and transmit the packets to swp2 for monitoring:

```
cumulus@switch:~$ net add port-mirror session 1 egress span src-port swp1 dst-port swp2
cumulus@switch:~$ net pending
cumulus@switch:~$ net commit
```

The following example commands mirror all packets recieved on swp1, and copy and transmit the packets from source IP address 10.10.10.1 to destination IP address 10.10.10.234 through a GRE tunnel:

```
cumulus@switch:~$ net add port-mirror session 1 ingress erspan src-port swp1 src-ip 10.10.10.1 dst-ip 10.10.10.234
cumulus@switch:~$ net pending
cumulus@switch:~$ net commit
```

The following example commands mirror all packets that are sent out of swp1, and copy and transmit the packets from source IP address 10.10.10.1 to destination IP address 10.10.10.234 through a GRE tunnel:

```
cumulus@switch:~$ net add port-mirror session 1 egress erspan src-port swp1 src-ip 10.10.10.1 dst-ip 10.10.10.234
cumulus@switch:~$ net pending
cumulus@switch:~$ net commit
```

### Show Session Configuration

Run the following commands to show the currently configured SPAN and ERSPAN sessions:

To show SPAN and ERSPAN configuration for a specific session:

```
cumulus@switch:~$ net show port-mirror session 1
session-id  direction  type  src   dest
----------  ---------  ----  ----  -----
         1  ingress    span  swp1  swp2
```

To show SPAN and ERSPAN configuration for all sessions:

```
cumulus@switch:~$ net show port-mirror session all
session-id  direction  type  src   dest
----------  ---------  ----  ----  -----
         1  ingress    span  swp1  swp2
```

### Delete Sessions

To delete a SPAN or ERSPAN session, run the `net del port-mirror session <session-id>` command. For example:

```
cumulus@switch:~$ net del port-mirror session 1
cumulus@switch:~$ net pending
cumulus@switch:~$ net commit
```

You can delete all SPAN or ERSPAN sessions with the `net del port-mirror session all` command. For example:

```
cumulus@switch:~$ net del port-mirror session all
cumulus@switch:~$ net pending
cumulus@switch:~$ net commit
```

## cl-acltool Configuration

You can configure SPAN and ERSPAN with `cl-acltool`, the {{<link url="Netfilter-ACLs" text="same utility used for security ACL configuration">}}. The match criteria for SPAN and ERSPAN is usually an interface; for more granular match terms, use {{<link url="#selective-spanning" text="selective spanning">}}. The SPAN source interface can be a port, a subinterface, or a bond interface. Ingress traffic on interfaces can be matched, and on switches with {{<exlink url="www.nvidia.com/en-us/networking/ethernet-switching/hardware-compatibility-list/" text="Spectrum ASICs">}}, egress traffic can be matched.

{{%notice note%}}

Always place your rule files under `/etc/cumulus/acl/policy.d/`.

{{%/notice%}}

### Limitations

- For Broadcom switches, Cumulus Linux supports a maximum of two SPAN destinations.
- For Mellanox switches with the Spectrum-2 ASIC or later, Cumulus Linux supports four SPAN destinations in atomic mode or eight SPAN destinations in non-atomic mode. On a switch with the Spectrum 1 ASIC, Cumulus Linux supports only a single SPAN destination in atomic mode or three SPAN destinations in non-atomic mode.
- To configure SPAN or ERSPAN on a Tomahawk or Trident3 switch, you must enable {{<link url="Netfilter-ACLs#nonatomic-update-mode-and-atomic-update-mode" text="non-atomic update  mode">}}.
- Mellanox Spectrum switches reject SPAN ACL rules for an output interface that is a subinterface.
- Multiple rules (SPAN sources) can point to the same SPAN destination, but a given SPAN source *cannot* specify two SPAN destinations.

### SPAN for Switch Ports

Follow the procedure below to set up, install, and verify SPAN rules.

The example commands span (mirror) swp1 input traffic and swp1 output traffic to destination swp2.

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

4. Verify that the SPAN rules are installed:

   ```
   cumulus@switch:~$ sudo cl-acltool -L all | grep SPAN
   38025 7034K SPAN       all  --  swp1   any     anywhere             anywhere             dport:swp2
   50832   55M SPAN       all  --  any    swp1    anywhere             anywhere             dport:swp2
   ```

### SPAN Sessions that Reference an Outgoing Interface

SPAN sessions that reference an outgoing interface create the mirrored packets based on the ingress interface before the routing decision. For example, the following rule captures traffic that is ultimately destined to leave swp1 but mirrors the packets when they arrive on swp49. The rule transmits packets that reference the original VLAN tag and source/destination MAC address at the time the packet is originally received on swp49.

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

3. Verify that the SPAN rules are installed:

   ```
   cumulus@switch:~$ sudo iptables -L -v | grep SPAN
       19  1938 SPAN       all  --  any    bond0   anywhere         anywhere         dport:bond1
   ```

### CPU port as the SPAN Destination

You can set the CPU port as a SPAN destination interface to mirror data plane traffic to the CPU. The SPAN traffic is sent to a separate network interface mirror where you can analyze it with `tcpdump`. This is a useful feature if you do not have any free external ports on the switch for monitoring. SPAN traffic does not appear on switch ports.

Cumulus Linux controls how much traffic reaches the CPU so that mirrored traffic does not overwhelm the CPU.

{{%notice note%}}

- CPU port as a SPAN destination interface is supported on Mellanox switches only.
- Egress mirroring for control plane generated traffic to the CPU port is not supported.

{{%/notice%}}

To use the CPU port as the SPAN destination, create a file in the `/etc/cumulus/acl/policy.d/` directory and add the rules. The following example rule matches on swp1 ingress traffic that has the source IP Address 10.10.1.1. When a match occurs, the traffic is mirrored to the CPU:

```
[iptables]
     -A FORWARD -i swp1 -s 10.10.1.1 -j SPAN --dport cpu
```

This example rule matches on swp1 egress traffic that has the source IP Address 10.10.1.1.
When a match occurs, the traffic is mirrored to the CPU:

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

{{%notice note%}}

{{<link url="Buffer-and-Queue-Management#configure-cut-through-mode-and-store-and-forward-switching" text="Cut-through mode">}} is **not** supported for ERSPAN in Cumulus Linux on switches using Broadcom Tomahawk, Trident II+, and Trident II ASICs.

Cut-through mode **is** supported for ERSPAN in Cumulus Linux on switches using Mellanox Spectrum ASICs.

{{%/notice%}}

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

3. Verify that the ERSPAN rules are installed:

     ```
     cumulus@switch:~$ sudo iptables -L -v | grep SPAN
     69  6804 ERSPAN     all  --  swp1   any     anywhere      anywhere       ERSPAN src-ip:10.0.0.1 dst-ip:10.10.10.234
     ```

The `src-ip` option can be any IP address, even if it does not exist in the routing table. The `dst-ip` option must be an IP address reachable through the routing table. The destination IP address must be reachable from a front-panel port; not the management port. Use `ping` or `ip route get <ip>` to verify that the destination IP address is reachable. Setting the `--ttl` option is recommended.

If a SPAN destination IP address is not available, or if the interface type prevents using a laptop as a SPAN destination, refer to [knowledge base article]({{<ref "/knowledge-base/Configuration-and-Usage/Administration/Configure-ERSPAN-to-a-Cumulus-Linux-Switch" >}}).

{{%notice note%}}

- When using {{<exlink url="https://www.wireshark.org" text="Wireshark">}} to review the ERSPAN output, Wireshark may report the message "Unknown version, please report or test to use fake ERSPAN preference", and the trace is unreadable. To resolve this issue, go to the General preferences for Wireshark, then go to **Protocols \ ERSPAN** and check the **Force to decode fake ERSPAN frame** option.
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

To mirror forwarded UDP packets received from port swp1s0, towards destination IP address 10.10.10.234 and destination port 53:

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

To reduce the volume of copied data, you can configure SPAN and ERSPAN traffic rules to limit the traffic spanned.

Cumulus Linux supports selective spanning for `iptables` only. `ip6tables` and `ebtables` are not supported.

The following matching fields are supported:

- IPv4 SIP/DIP
- IP protocol
- Layer 4 (TCP/UDP) src/dst port
- TCP flags
- An ingress port/wildcard (swp+) can be specified in addition

With ERSPAN, a maximum of two `--src-ip --dst-ip` pairs are supported. Exceeding this limit produces an error when you install the rules with `cl-acltool`.

### Remove Rules

To remove your SPAN or ERSPAN rules, remove the rules file, then reload the default rules. For example:

```
cumulus@switch:~$ sudo rm  /etc/cumulus/acl/policy.d/span.rules
cumulus@switch:~$ sudo cl-acltool -i
```

To verify that the rules are removed:

```
cumulus@switch:~$ sudo cl-acltool -L all | grep SPAN
```

## Manual Configuration (Advanced)

You can configure SPAN and ERSPAN by editing the `/etc/cumulus/switchd.d/port-mirror.conf` file. The NCLU commands save SPAN and ERSPAN configuration to this file.

The following example SPAN configuration mirrors all packets received on swp1, and copies and transmits the packets to swp2 for monitoring:

```
cumulus@switch:~$ sudo nano /etc/cumulus/switchd.d/port-mirror.conf
...
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
