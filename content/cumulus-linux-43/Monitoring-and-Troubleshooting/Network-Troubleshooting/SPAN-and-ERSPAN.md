---
title: SPAN and ERSPAN
author: NVIDIA
weight: 1145
toc: 4
---
SPAN (Switched Port Analyzer) enables you to mirror all packets coming in from or going out of an interface (the *SPAN source*), and being copied and transmitted out of a local port or CPU (the *SPAN destination*) for monitoring. The SPAN destination port is also referred to as a mirror-to-port (MTP). The original packet is still switched, while a mirrored copy of the packet is sent out of the MTP.

ERSPAN (Encapsulated Remote SPAN) enables the mirrored packets to be sent to a monitoring node located anywhere across the routed network. The switch finds the outgoing port of the mirrored packets by doing a lookup of the destination IP address in its routing table. The original L2 packet is encapsulated with GRE for IP delivery. The encapsulated packets have the following format:

```
 ----------------------------------------------------------
| MAC_HEADER | IP_HEADER | GRE_HEADER | L2_Mirrored_Packet |
 ----------------------------------------------------------
```

{{%notice note%}}

- Mirrored traffic is not guaranteed. If the MTP is congested, mirrored packets might be discarded.
- A SPAN and ERSPAN destination interface that is oversubscribed might result in data plane buffer depletion and buffer drops. Exercise caution when enabling SPAN and ERSPAN when the aggregate speeds of all source ports exceeds the destination port. Selective SPAN is recommended when possible to limit traffic in this scenario.

{{%/notice%}}

## Configure SPAN and ERSPAN with cl-acltool

You can configure SPAN and ERSPAN with `cl-acltool`, the {{<link url="Netfilter-ACLs" text="same utility for security ACL configuration">}}. The match criteria for SPAN and ERSPAN is usually an interface; for more granular match terms, use {{<link url="#selective-spanning" text="selective spanning">}}. The SPAN source interface can be a port, a subinterface, or a bond interface. Ingress traffic on interfaces can be matched, and on switches with {{<exlink url="https://cumulusnetworks.com/products/hardware-compatibility-list/?asic%5B0%5D=Mellanox%20Spectrum&asic%5B1%5D=Mellanox%20Spectrum_A1" text="Spectrum ASICs">}}, egress traffic can be matched. See the {{<link url="#limitations-for-span-and-erspan" text="list of limitations">}} below.

Cumulus Linux supports a maximum of two SPAN destinations. Multiple rules (SPAN sources) can point to the same SPAN destination, although a given SPAN source cannot specify two SPAN destinations. The SPAN destination (MTP) interface can be a physical port, subinterface, bond interface or CPU.  The SPAN and ERSPAN action is independent of security ACL actions. If packets match both a security ACL rule and a SPAN rule, both actions are carried out.

{{%notice note%}}

Always place your rule files under `/etc/cumulus/acl/policy.d/`.

{{%/notice%}}

- For Broadcom switches, Cumulus Linux supports a maximum of two SPAN destinations.
- Because SPAN and ERSPAN is done in hardware, eth0 is not supported as a destination.
- For Mellanox Spectrum switches, Cumulus Linux supports only a single SPAN destination in atomic mode or three SPAN destinations in non-atomic mode.
- Multiple rules (SPAN sources) can point to the same SPAN destination, but a given SPAN source *cannot* specify two SPAN destinations.
- To configure SPAN or ERSPAN on a Tomahawk or Trident3 switch, you must enable {{<link url="Netfilter-ACLs#nonatomic-update-mode-and-atomic-update-mode" text="non-atomic update  mode">}}.
- Mellanox Spectrum switches reject SPAN ACL rules for an output interface that is a subinterface.
- Cut-through mode is not supported for ERSPAN in Cumulus Linux on switches using Broadcom Tomahawk, Trident II+ and Trident II ASICs.
- On Broadcom switches, SPAN does not capture egress traffic.
- Cumulus Linux does not support IPv6 ERSPAN destinations.
- ERSPAN does not cause the kernel to send ARP requests to resolve the next hop for the ERSPAN destination. If an ARP entry for the destination/next hop does not already exist in the kernel, you need to manually resolve this before mirrored traffic is sent (using ping or arping).
- Mirroring to the same interface that is being monitored causes a recursive flood of traffic and might impact traffic on other interfaces.

### SPAN for Switch Ports

This section describes how to set up, install, and verify SPAN rules. In the example commands span (mirror) swp4 input traffic and swp4 output traffic to destination swp19.

1. Create a rules file in `/etc/cumulus/acl/policy.d/`:

   ```
   cumulus@switch:~$ sudo bash -c 'cat <<EOF > /etc/cumulus/acl/policy.d/span.rules
   [iptables]
   -A FORWARD --in-interface swp4 -j SPAN --dport swp19
   -A FORWARD --out-interface swp4 -j SPAN --dport swp19
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
        0     0 POLICE     tcp  --  any    any     anywhere             anywhere             tcp dpt:5342 POLICE  mode:pkt rate:2000 burst:2000
        0     0 SETCLASS   tcp  --  swp+   any     anywhere             anywhere             tcp spt:5342 SETCLASS  class:7
        0     0 POLICE     tcp  --  any    any     anywhere             anywhere             tcp spt:5342 POLICE  mode:pkt rate:2000 burst:2000
        0     0 SETCLASS   icmp --  swp+   any     anywhere             anywhere             SETCLASS  class:2
        0     0 POLICE     icmp --  any    any     anywhere             anywhere             POLICE  mode:pkt rate:100 burst:40
       15  5205 SETCLASS   udp  --  swp+   any     anywhere             anywhere             udp  dpts:bootps:bootpc SETCLASS  class:2
       11  3865 POLICE     udp  --  any    any     anywhere             anywhere             udp dpt:bootps POLICE  mode:pkt rate:100 burst:100
        0     0 POLICE     udp  --  any    any     anywhere             anywhere             udp dpt:bootpc POLICE  mode:pkt rate:100 burst:100
        0     0 SETCLASS   tcp  --  swp+   any     anywhere             anywhere             tcp dpts:bootps:bootpc SETCLASS  class:2
        0     0 POLICE     tcp  --  any    any     anywhere             anywhere             tcp dpt:bootps POLICE  mode:pkt rate:100 burst:100
        0     0 POLICE     tcp  --  any    any     anywhere             anywhere             tcp dpt:bootpc POLICE  mode:pkt rate:100 burst:100
       17  1088 SETCLASS   igmp --  swp+   any     anywhere             anywhere             SETCLASS class:6
       17  1156 POLICE     igmp --  any    any     anywhere             anywhere             POLICE  mode:pkt rate:300 burst:100
       394 41060 POLICE    all  --  swp+   any     anywhere             anywhere             ADDRTYPE match dst-type LOCAL POLICE  mode:pkt rate:1000 burst:1000 class:0
        0     0 POLICE     all  --  swp+   any     anywhere             anywhere             ADDRTYPE match dst-type IPROUTER POLICE  mode:pkt rate:400 burst:100 class:0
       988  279K SETCLASS  all  --  swp+   any      anywhere            anywhere             SETCLASS  class:0

   Chain FORWARD (policy ACCEPT 0 packets, 0 bytes)
     pkts bytes target     prot opt in     out     source               destination
        0     0 DROP       all  --  swp+   any     240.0.0.0/5          anywhere
        0     0 DROP       all  --  swp+   any     loopback/8           anywhere
        0     0 DROP       all  --  swp+   any     base-address.mcast.net/8  anywhere
        0     0 DROP       all  --  swp+   any     255.255.255.255      anywhere
    26864 4672K SPAN       all  --  swp4   any     anywhere             anywhere             dport:swp19  <---- input packets on swp4

   40722   47M  SPAN       all  --  any    swp4     anywhere             anywhere             dport:swp19  <---- output packets on swp4

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
   38025 7034K SPAN       all  --  swp4   any     anywhere             anywhere             dport:swp19
   50832   55M SPAN       all  --  any    swp4    anywhere             anywhere             dport:swp19
   ```

### SPAN Sessions that Reference an Outgoing Interface

SPAN sessions that reference an outgoing interface create the mirrored packets based on the ingress interface before the routing decision. For example, the following rule captures traffic that is ultimately destined to leave swp2 but mirrors the packets when they arrive on swp3. The rule transmits packets that reference the original VLAN tag and source/destination MAC address at the time the packet is originally received on swp3.

```
-A FORWARD --out-interface swp2 -j SPAN --dport swp1
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
       19  1938 SPAN       all  --  any    bond0   anywhere             anywhere             dport:bond1
   ```

### CPU port as the SPAN Destination

You can set the CPU port as a SPAN destination interface to mirror data plane traffic to the CPU. The SPAN traffic is sent to a separate network interface mirror where you can analyze it with `tcpdump`. This is a useful feature if you do not have any free external ports  on the switch for monitoring purposes. SPAN traffic does not appear on switch ports.

Cumulus Linux controls how much traffic reaches the CPU so that mirrored traffic does not overwhelm the CPU.

{{%notice note%}}

- CPU port as a SPAN destination interface is supported on Mellanox switches only.
- Egress Mirroring for control plane generated traffic to the CPU port is not supported.

{{%/notice%}}

To use the CPU port as the SPAN destination, create a file in the `/etc/cumulus/acl/policy.d/` directory and add the rules. The following example rule matches on swp1 ingress traffic that has the source IP Address 10.10.1.1. When a match occurs, the traffic is mirrored to the CPU:

```
[iptables]
     -A FORWARD -i swp1 -s 10.10.1.1 -j SPAN --dport cpu
```

This example rule matches on swp1 egress traffic that has the source IP Address 10.10.1.1.
When a match occurs, the traffic is is mirrored to the CPU:

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

To mirror forwarded packets from all ports matching SIP 20.0.1.0 and DIP 20.0.1.2 to port swp1s1:

```
-A FORWARD --in-interface swp+ -s 20.0.0.2 -d 20.0.1.2 -j SPAN --dport swp1s2
```

To mirror icmp packets from all ports to swp1s2:

```
-A FORWARD --in-interface swp+ -s 20.0.0.2 -p icmp -j SPAN --dport swp1s2
```

To mirror forwarded UDP packets received from port swp1s0, towards DIP 20.0.1.2 and destination port 53:

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

### Remove SPAN Rules

To remove your SPAN rules, remove the rules file, then reload the default rules:

```
cumulus@switch:~$ sudo rm  /etc/cumulus/acl/policy.d/span.rules
cumulus@switch:~$ sudo cl-acltool -i
```

To verify that the SPAN rules are removed:

```
cumulus@switch:~$ sudo cl-acltool -L all | grep SPAN
```

### ERSPAN

This section describes how to configure ERSPAN for all packets coming in from `swp1` to 12.0.0.2.

{{%notice note%}}

{{<link url="Buffer-and-Queue-Management#configure-cut-through-mode-and-store-and-forward-switching" text="Cut-through mode">}} is **not** supported for ERSPAN in Cumulus Linux on switches using Broadcom Tomahawk, Trident II+, and Trident II ASICs.

Cut-through mode **is** supported for ERSPAN in Cumulus Linux on switches using Mellanox Spectrum ASICs.

{{%/notice%}}

1. Create a rules file in `/etc/cumulus/acl/policy.d/`:

     ```
     cumulus@switch:~$ sudo bash -c 'cat <<EOF > /etc/cumulus/acl/policy.d/erspan.rules
     [iptables]
     -A FORWARD --in-interface swp1 -j ERSPAN --src-ip 12.0.0.1 --dst-ip 12.0.0.2  --ttl 64
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
     69  6804 ERSPAN     all  --  swp1   any     anywhere             anywhere             ERSPAN src-ip:12.0.0.1 dst-ip:12.0.0.2
     ```

The `src-ip` option can be any IP address, even if it dosen't exists in the routing table. The `dst-ip` option must be an IP address reachable through the routing table. The destination IP address must be reachable from a front-panel port; not the management port. Use `ping` or `ip route get <ip>` to verify that the destination IP address is reachable. Setting the `--ttl` option is recommended.

If a SPAN destination IP address is not available, or if the interface type or types prevent using a laptop as a SPAN destination, read this {{<exlink url="https://docs.cumulusnetworks.com/knowledge-base/Configuration-and-Usage/Administration/Configure-ERSPAN-to-a-Cumulus-Linux-Switch/360040711774" text="knowledge base article">}} for a workaround.

{{%notice note%}}

- When using {{<exlink url="https://www.wireshark.org" text="Wireshark">}} to review the ERSPAN output, Wireshark may report the message "Unknown version, please report or test to use fake ERSPAN preference", and the trace is unreadable. To resolve this issue, go to the General preferences for Wireshark, then go to **Protocols \ ERSPAN** and check the **Force to decode fake ERSPAN frame** option.
- To set up a {{<exlink url="https://www.wireshark.org/docs/wsug_html_chunked/ChCapCaptureFilterSection.html" text="capture filter">}} on the destination switch that filters for a specific IP protocol, use `ip.proto == 47` to filter for GRE-encapsulated (IP protocol 47) traffic.

{{%/notice%}}

### Example ERSPAN Rules

To mirror forwarded packets from all ports matching SIP 20.0.1.0 and DIP 20.0.1.2:

```
-A FORWARD --in-interface swp+ -s 20.0.0.2 -d 20.0.1.2 -j ERSPAN --src-ip 90.0.0.1 --dst-ip 20.0.2.2
```

To mirror ICMP packets from all ports:

```
-A FORWARD --in-interface swp+ -s 20.0.0.2 -p icmp -j ERSPAN --src-ip 90.0.0.1 --dst-ip 20.0.2.2
```

To mirror forwarded UDP packets received from port swp1s0, towards DIP 20.0.1.2 and destination port 53:

```
-A FORWARD --in-interface swp1s0 -d 20.0.1.2 -p udp --dport 53 -j ERSPAN --src-ip 90.0.0.1 --dst-ip 20.0.2.2
```

To mirror all forwarded TCP packets with only SYN set:

```
-A FORWARD --in-interface swp+ -p tcp --tcp-flags ALL SYN -j ERSPAN --src-ip 90.0.0.1 --dst-ip 20.0.2.2
```

To mirror all forwarded TCP packets with only FIN set:

```
-A FORWARD --in-interface swp+ -p tcp --tcp-flags ALL FIN -j ERSPAN --src-ip 90.0.0.1 --dst-ip 20.0.2.2
```

### Selective Spanning

To reduce the volume of copied data, you can configure SPAN and ERSPAN traffic rules to limit the traffic spanned.

Cumulus Linux supports selective spanning for `iptables` only. `ip6tables` and `ebtables` are not supported.

The following matching fields are supported:

- IPv4 SIP/DIP
- IP protocol
- L4 (TCP/UDP) src/dst port
- TCP flags
- An ingress port/wildcard (swp+) can be specified in addition

With ERSPAN, a maximum of two `--src-ip --dst-ip` pairs are supported. Exceeding this limit produces an error when you install the rules with `cl-acltool`.

## Configure SPAN and ERSPAN with NCLU

