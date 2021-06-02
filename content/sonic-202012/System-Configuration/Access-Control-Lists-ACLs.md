---
title: Access Control Lists - ACLs
author: NVIDIA
weight: 330
product: SONiC
version: 202012
siteSlug: sonic
---

{{<exlink url="http://www.netfilter.org/" text="Netfilter">}} is the packet filtering framework in SONiC as well as most other Linux distributions. There are a number of tools available for configuring *access control lists* (ACLs) in SONiC.

For an in depth discussion of ACLs, read the [Cumulus Linux]({{<ref "/cumulus-linux-43/System-Configuration/Netfilter-ACLs" >}}) user guide.

 <!--   iptables, ip6tables, and ebtables are Linux userspace tools used to administer filtering rules for IPv4 packets, IPv6 packets, and Ethernet frames (layer 2 using MAC addresses).-->

## ACL Configuration Flows

You configure ACLs in SONiC using:

- The SONiC CONFIG_DB, defined in `/etc/sonic/config_db.json`.
- The SONiC CLI.

{{%notice note%}}

You can also configure SONiC using the SONiC management framework and REST API. However, since they are not enabled in SONiC by default, they are beyond the scope of this topic.

{{%/notice%}}

### Configure ACL Tables Using CONFIG_DB

The following table contains the CONFIG_DB schema. The schema is defined according to ABNF RFC 5234 syntax; refer to {{<exlink url="https://tools.ietf.org/html/rfc5234" text="RFC 5234">}} for more information about the schema definition.

| Field | Value | Description |
| ----- | ----- | ----------- |
| key | ACL_TABLE:name | The `name` must be unique within the ACL_TABLE table. The `name` is used to reference this table from other places in the SONiC configuration database. |
| ;field | value | |
| POLICY_DESC | 1*255VCHAR | The `W` of the ACL policy table description, user defined description for the table. |
| TYPE | 1*255VCHAR | Type of ACL table, every type of table defines the match/action a specific set of match and actions. See the next table below for details on the type field. |
| PORTS | [0-INF]*port_name | The list of ports to which this ACL table is applied, this field can be empty. |
| STAGE | "INGRESS"/"EGRESS" | ACL table stage, either ingress or egress. |
| SERVICES | [0-INF]*service_name | List of services, valid only for `TYPE=CTRLPLANE`. |

The `TYPE` field can be one of the following:

| Type | Bind Port Types Supported | Match Fields Supported | Supported ACL Rule Actions |
| ---- | ------------------------- | ---------------------- | -------------------------- |
| L3 | PORT, LAG  | <ul><li>ETHER_TYPE </li><li>IP_TYPE </li><li>IP_PROTOCOL </li><li>SRC_IP </li><li>DST_IP </li><li>ICMP_TYPE </li><li>ICMP_CODE </li><li>L4_SRC_PORT </li><li>L4_DST_PORT </li><li>TCP_FLAGS </li><li>L4_DST_PORT_RANGE </li><li>L4_SRC_PORT_RANGE </li></ul> | <ul><li>PACKET_ACTION </li><li>REDIRECT_ACTION </li><li>DO_NOT_NAT_ACTION </li><li>MIRROR_INGRESS_ACTION </li><li>MIRROR_EGRESS_ACTION  </li><li>MIRROR_ACTION </li></ul> |
| L3V6 | PORT,LAG | <ul><li>ETHER_TYPE </li><li>IP_TYPE </li><li>IP_PROTOCOL </li><li>SRC_IPV6 </li><li>DST_IPV6 </li><li>ICMPV6_TYPE </li><li>ICMPV6_CODE </li><li>L4_SRC_PORT </li><li>L4_DST_PORT </li><li>TCP_FLAGS </li><li>L4_DST_PORT_RANGE </li><li>L4_SRC_PORT_RANGE </li></ul> | <ul><li>PACKET_ACTION </li><li>REDIRECT_ACTION </li><li>DO_NOT_NAT_ACTION </li></ul>|
| MIRROR | PORT,LAG | <ul><li>ETHER_TYPE </li><li>IP_TYPE </li><li>IP_PROTOCOL </li><li>SRC_IP </li><li>DST_IP </li><li>ICMP_TYPE </li><li>ICMP_CODE </li><li>SRC_IPV6 (\*) </li><li>DST_IPV6 (\*) </li><li>ICMPV6_TYPE (\*) </li><li>ICMPV6_CODE (\*) </li><li>L4_SRC_PORT </li><li>L4_DST_PORT </li><li>TCP_FLAGS </li><li>L4_DST_PORT_RANGE </li><li>L4_SRC_PORT_RANGE </li></ul> | <ul><li>MIRROR_INGRESS_ACTION </li><li>MIRROR_EGRESS_ACTION </li><li>MIRROR_ACTION </li></ul> | 
| MIRRORV6 | PORT,LAG | <ul><li>IP_TYPE </li><li>IP_PROTOCOL </li><li>SRC_IP </li><li>DST_IP </li><li>ICMP_TYPE </li><li>ICMP_CODE </li><li>SRC_IPV6 (\*) </li><li>DST_IPV6 (\*) </li><li>ICMPV6_TYPE (\*) </li><li>ICMPV6_CODE (\*) </li><li>L4_SRC_PORT </li><li>L4_DST_PORT </li><li>TCP_FLAGS </li><li>L4_DST_PORT_RANGE </li><li>L4_SRC_PORT_RANGE </li></ul> | <ul><li>MIRROR_INGRESS_ACTION </li><li>MIRROR_EGRESS_ACTION </li><li>MIRROR_ACTION </li></ul>|
| MIRROR_DSCP  | PORT,LAG | <ul><li>DSCP </li></ul> | <ul><li>MIRROR_INGRESS_ACTION </li><li>MIRROR_EGRESS_ACTION </li><li>MIRROR_ACTION </li></ul> |
| PFCWD  | PORT | <ul><li>TC</li></ul> | Used internally by SONiC; not user configurable. |
| DTEL_FLOW_WATCHLIST | SWITCH  | Not supported on NVIDIA Spectrum ASICs. | Not supported on NVIDIA Spectrum ASICs. |
| DTEL_DROP_WATCHLIST | SWITCH  | Not supported on NVIDIA Spectrum ASICs. | Not supported on NVIDIA Spectrum ASICs. |

### Notes

- (*) Depends on whether the ASIC supports mirroring IPv6 packets and supports IPv6 match and IPv4 match in single ACL table. Mellanox ASICs support IPv6 mirroring, however do not support IPv4 and IPv6 match in the same ACL table. SONiC creates two ACL tables in HW, so that from the user perspective configuring IPv6 rules in ACL table MIRROR should be possible.
- MIRROR_ACTION is an alias for MIRROR_INGRESS_ACTION.
- MIRROR_INGRESS_ACTION and MIRROR_EGRESS_ACTION have their own limitations with regard to ACL table stage. See, the ACL rule section below.
- The VLAN bind point is not supported by SONiC; this is a SONiC `orchagent` limitation.
- The bind point is layer 2; currently SONiC does not support binding an ACL table to a RIF.

### Configure ACL Tables Using the SONiC CLI

You create an ACL table with the SONiC CLI using the `config acl add table` command. You need to specify a table name and type (see above for table types). The command takes the following options:

| Option | Description |
| ------ | ----------- |
| -d, --description "TEXT" | A brief description of the table. |
| -p, --ports "TEXT" | A list of ports included in the table. Both physical and virtual ports are acceptable. |
| -s, --stage [ingress\|egress] | ACL table stage, which indicates whether the table is used for ingress or egress. |

Example of ACL table creation and removal:

    admin@switch:~$ sudo config acl add table L3_INGRESS_1 L3 --description="L3 ingress table" --stage=ingress --ports="Ethernet0,Ethernet124,PortChannel0001"
    admin@switch:~$ sudo config save -y

To display ACL tables configured in the system, run:

```
admin@switch:~$ show acl table  
Name          Type    Binding          Description       Stage
------------  ------  ---------------  ----------------  -------
L3_INGRESS_1  L3      Ethernet0        L3 ingress table  ingress
                      Ethernet124
                      PortChannel0001
```

{{%notice info%}}

It's a good idea to check `/var/log/syslog` to verify that the ACL table was created successfully.

{{%/notice%}}

To remove an ACL table, run:

    admin@switch:~$ sudo config acl remove table L3_INGRESS_1
    admin@switch:~$ sudo config save -y


## Configure ACL Rules

You configure ACL rules in JSON format in the SONiC CONFIG_DB; you cannot create ACL rules with the SONiC CLI.

Look at table types above to see if a match and action pair is supported for particular table type. Several match rules are possible.

The following table shows the CONFIG_DB schema.

| Field | Value | Description |
| ----- | ----- | ----------- |
| key | ACL_RULE_TABLE:table_name:rule_name | The key of the rule entry in the table, the sequence is the order of the rules when the packet is filtered by the ACL "policy_name". A rule is always associated with a policy. |
| ;field | value | |
| priority | 1*3DIGIT | The rule priority. Valid values range are platform dependent. For example, on NVIDIA Spectrum switches, the minimum priority is 0 and the maximum priority is 16381. You can always check it in logs:<pre>admin@switch:~$ show log \| grep 'Get ACL entry priority values'<br />Apr 22 16:46:55.967195 switch NOTICE swss#orchagent: :- init: Get ACL entry priority values, min: 0, max: 16381</pre> |
| packet_action | "forward"/"drop"/"redirect:"redirect_parameter/"do_not_nat" | An action when the fields are matched. There is a parameter in case of `packet_action="redirect"`. This parameter defines a destination for redirected packets and can be:<br />- The name of a physical port, like "Ethernet10"<br />- The name of a LAG port, like "PortChannel5".<br />- The next hop IP address (in a global), like "10.0.0.1".<br />- The next hop IP address and VRF, like "10.0.0.2@Vrf2".<br />- The next hop IP address and interface name, like "10.0.0.3@Ethernet1".<br />- The next hop group set of next hops, like "10.0.0.1,10.0.0.3@Ethernet1". |
| redirect_action | 1*255CHAR | The redirect parameter. This parameter defines a destination for redirected packets and can be:<br />- The name of a physical port, like "Ethernet10".<br />- The name of LAG port, like "PortChannel5".<br />- The next hop IP address (in a global), like "10.0.0.1".<br />- The next hop IP address and VRF, like "10.0.0.2@Vrf2".<br />- The next hop IP address and interface name, like "10.0.0.3@Ethernet1".<br />- The next hop group set of next hops, like "10.0.0.1,10.0.0.3@Ethernet1". |
| mirror_action | 1*255VCHAR | Refer to the mirror session. By default this is an ingress mirror action. |
| mirror_ingress_action | 1*255VCHAR | Refer to the mirror session. |
| mirror_egress_action | 1*255VCHAR | Refer to the mirror session. |
| ether_type | h16 | Ethernet type field. |
| ip_type | ip_types | Options for the `l2_protocol_type` field. |
| ip_protocol | h8 | Options for the `l3_protocol_type` field. |
| src_ip | ipv4_prefix | Options for the source IPv4 address (and mask) field. |
| dst_ip | ipv4_prefix | Options for the destination IPv4 address (and mask) field. |
| src_ipv6 | ipv6_prefix | Options for the source IPv6 address (and mask) field. |
| dst_ipv6 | ipv6_prefix | Options for the destination IPv6 address (and mask) field. |
| l4_src_port | port_num | The source L4 port. |
| l4_dst_port | port_num | The destination L4 port. |
| l4_src_port_range | port_num_L-port_num_H | The source port range of the L4 ports field. |
| l4_dst_port_range | port_num_L-port_num_H | The destination port range of the L4 ports field. |
| tcp_flags | h8/h8 | TCP flags field and mask. |
| dscp | h8 | The DSCP field, which is only available for mirror table type. |
| icmp_type | h8/h8 | The ICMP type and mask. |
| icmpv6_type | h8/h8 | The ICMPv6 type and mask. |
| icmp_code | h8/h8 | The ICMP code and mask. |
| icmpv6_code | h8/h8 | The ICMPv6 code and mask. |
| in_ports | string | A comma-separated list of inbound ports to match. |
| out_ports | string | A comma-separated list of outbound ports to match value annotations. |
| ip_types | any \| ip \| ipv4 \| ipv4any \| non_ipv4 \| ipv6any \| non_ipv6 | Type of IP address. On NVIDIA Spectrum switches, an IP type of `any` requires at least one additional match rule besides `any`, such as `"ETHER_TYPE": "2048"`. |
| port_num | 1*5DIGIT | A port number between 0 and 65535. |
| port_num_L | 1*5DIGIT | A port number between 0 and 65535. The `port_num_L` must be lower than `port_num_H`. |
| port_num_H | 1*5DIGIT | A port number between 0 and 65535. The `port_num_H` must be higher than `port_num_L`. |
| ipv6_prefix  | 6( h16 ":" ) ls32 | |
| | "::" 5( h16 ":" ) ls32 | |
| | [               h16 ] "::" 4( h16 ":" ) ls32 | |
| | [ *1( h16 ":" ) h16 ] "::" 3( h16 ":" ) ls32 | |
| | [ *2( h16 ":" ) h16 ] "::" 2( h16 ":" ) ls32 | |
| | [ *3( h16 ":" ) h16 ] "::"    h16 ":"   ls32 | |
| | [ *4( h16 ":" ) h16 ] "::"              ls32 | |
| | [ *5( h16 ":" ) h16 ] "::"              h16 | |
| | [ *6( h16 ":" ) h16 ] "::" | |
| h8 | 1*2HEXDIG | |
| h16 | 1*4HEXDIG | |
| ls32 | ( h16 ":" h16 ) / IPv4address | |
| ipv4_prefix | dec-octet "." dec-octet "." dec-octet "." dec-octet "/" %d1-32 | |
| dec-octet | DIGIT | 0-9 |
| | %x31-39 DIGIT | 10-99 |
| | "1" 2DIGIT | 100-199 |
| | "2" %x30-34 DIGIT | 200-249 |

### ACL Rule Example

```
"ACL_RULE": {
    "DATAACL|DEFAULT_RULE": {
        "PRIORITY": "1",
        "PACKET_ACTION": "DROP",
        "ETHER_TYPE": "2048"
    },
    "DATAACL|RULE_1": {
        "PRIORITY": "9999",
        "PACKET_ACTION": "DROP",
        "SRC_IP": "10.0.0.2/32"
    },
    "DATAACL|RULE_2": {
        "PRIORITY": "9998",
        "PACKET_ACTION": "DROP",
        "DST_IP": "192.168.0.16/32"
    },
}
```
