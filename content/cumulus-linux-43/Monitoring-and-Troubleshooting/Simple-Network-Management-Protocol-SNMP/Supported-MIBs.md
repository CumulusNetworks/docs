---
title: Supported MIBs
author: NVIDIA
weight: 1170
toc: 4
---

Below are the MIBs supported by Cumulus Linux, as well as suggested uses for them. The overall Cumulus Linux MIB is defined in the `/usr/share/snmp/mibs/Cumulus-Snmp-MIB.txt` file.
<!-- vale off -->
| <div style="width:250px">MIB Name | Suggested Uses |
| -------- | -------------- |
| {{<mib_link url="mibs/BGP4-MIB.txt" text="BGP4-MIB">}}<br>{{<mib_link url="mibs/OSPFv2-MIB.txt" text="OSPFv2-MIB">}}<br>{{<mib_link url="mibs/OSPFv3-MIB.txt" text="OSPFv3-MIB">}}<br>{{<mib_link url="mibs/RIPv2-MIB.txt" text="RIPv2-MIB">}} | You can enable FRRouting SNMP support to provide support for OSPF-MIB (RFC-1850), OSPFV3-MIB (RFC-5643), and BGP4-MIB (RFC-1657). See the FRRouting section above. |
| {{<mib_link url="mibs/CUMULUS-BGPUN-MIB.txt" text="CUMULUS-BGPVRF-MIB">}} | Cumulus Linux also includes its own BGP unnumbered MIB for BGP unnumbered peers, defined in `/usr/share/snmp/mibs/Cumulus-BGPUN-MIB.txt`, which has the OID `1.3.6.1.4.1.40310.7`. CUMULUS-BGPVRF-MIB replaces CUMULUS-BGPUN-MIB.|
| {{<mib_link url="mibs/CUMULUS-COUNTERS-MIB.txt" text="CUMULUS-COUNTERS-MIB">}} | Discard counters: Cumulus Linux also includes its own counters MIB, defined in `/usr/share/snmp/mibs/Cumulus-Counters-MIB.txt`. It has the OID `.1.3.6.1.4.1.40310.2`. |
| {{<mib_link url="mibs/CUMULUS-POE-MIB.txt" text="CUMULUS-POE-MIB">}} | The custom {{<link url="Power-over-Ethernet-PoE" text="Power over Ethernet PoE MIB">}} defined in the `/usr/share/snmp/mibs/Cumulus-POE-MIB.txt` file. For devices that provide PoE, this provides users with the system wide power information in `poeSystemValues` as well as per interface `PoeObjectsEntry` values for the `poeObjectsTable`. Most of this information comes from the `poectl` command. To enable this MIB, uncomment the following line in `/etc/snmp/snmpd.conf`:<pre>#pass_persist .1.3.6.1.4.1.40310.3 /usr/share/snmp/cl_poe_pp.py</pre> |
| {{<mib_link url="mibs/CUMULUS-RESOURCE-QUERY-MIB.txt" text="CUMULUS-RESOURCE-QUERY-MIB">}} | Cumulus Linux includes its own resource utilization MIB, which is similar to using `cl-resource-query`. This MIB monitors layer 3 entries by host, route, nexthops, ECMP groups, and layer 2 MAC/BDPU entries. The MIB is defined in `/usr/share/snmp/mibs/Cumulus-Resource-Query-MIB.txt` and has the OID `.1.3.6.1.4.1.40310.1`. |
| {{<mib_link url="mibs/CUMULUS-SNMP-MIB.txt" text="CUMULUS-SNMP-MIB">}} | SNMP counters. For information on exposing CPU and memory information with SNMP, see this [knowledge base article]({{<ref "/knowledge-base/Configuration-and-Usage/Monitoring/Expose-CPU-and-Memory-Information-via-SNMP" >}}). |
| {{<mib_link url="mibs/DISMAN-EVENT-MIB.txt" text="DISMAN-EVENT-MIB">}} | Trap monitoring. |
| {{<mib_link url="mibs/ENTITY-MIB.txt" text="ENTITY-MIB">}} | From RFC 4133, the temperature sensors, fan sensors, power sensors, and ports are covered.<br><br>**Note:** The ENTITY-MIB does not show the chassis information in Cumulus Linux. |
| {{<mib_link url="mibs/ENTITY-SENSOR-MIB.txt" text="ENTITY-SENSOR-MIB">}} | Physical sensor information (temperature, fan, and power supply) from RFC 3433. |
<mib_link url="mibs/HOST-RESOURCES-MIB.txt" text="HOST-RESOURCES-MIB">}} | Users, storage, interfaces, process info, run parameters. |
| {{<mib_link url="mibs/BRIDGE-MIB.txt" text="BRIDGE-MIB">}}<br />{{<mib_link url="mibs/Q-BRIDGE-MIB.txt" text="Q-BRIDGE-MIB">}} | The `dot1dBasePortEntry` and `dot1dBasePortIfIndex` tables in the BRIDGE-MIB and `dot1qBase`, `dot1qFdbEntry`, `dot1qTpFdbEntry`, `dot1qTpFdbStatus`, and `dot1qVlanStaticName` tables in the Q-BRIDGE-MIB tables. You must uncomment the `bridge_pp.py pass_persist` script in `/etc/snmp/snmpd.conf`. |
| {{<mib_link url="mibs/IEEE8023-LAG-MIB.txt" text="IEEE8023-LAG-MIB">}} | Implementation of the IEEE 8023-LAG-MIB includes the `dot3adAggTable` and `dot3adAggPortListTable` tables. To enable this, edit `/etc/snmp/snmpd.conf` and uncomment or add the following lines:<pre>view systemonly included .1.2.840.10006.300.43<br>pass_persist .1.2.840.10006.300.43 /usr/share/snmp/ieee8023_lag_pp.py</pre> |
| {{<mib_link url="mibs/IF-MIB.txt" text="IF-MIB">}} | Interface description, type, MTU, speed, MAC, admin, operation status, counters.<br><br>**Note**: The IF-MIB cache is disabled by default. The non-caching code path in the IF-MIB treats 64-bit counters like 32-bit counters (a 64-bit counter rolls over after the value increments to a value that extends beyond 32 bits). To enable the counter to reflect traffic statistics using 64-bit counters, remove the `-y` option from the `SNMPDOPTS` line in the `/etc/default/snmpd` file. The example below first shows the original line, commented out, then the modified line without the `-y` option:<pre>cumulus@switch:~$ cat /etc/default/snmpd<br># SNMPDOPTS=&#39;-y -LS 0-4 d -Lf /dev/null -u snmp -g snmp -I -smux -p /run/snmpd.pid&#39;<br>SNMPDOPTS=&#39;-LS 0-4 d -Lf /dev/null -u snmp -g snmp -I -smux -p /run/snmpd.pid</pre> |
| {{<mib_link url="mibs/IP-FORWARD-MIB.txt" text="IP-FORWARD-MIB">}} | IP routing table. |
| {{<mib_link url="mibs/IP-MIB.txt" text="IP-MIB (includes ICMP)">}} | IPv4, IPv4 addresses counters, netmasks. |
| {{<mib_link url="mibs/IPV6-MIB.txt" text="IPv6-MIB">}} | IPv6 counters. |
| {{<mib_link url="mibs/LLDP-MIB.txt" text="LLDP-MIB">}} | Layer 2 neighbor information from `lldpd` (you need to {{<link url="Link-Layer-Discovery-Protocol#enable-the-snmp-subagent-in-lldp" text="enable the SNMP subagent">}} in LLDP). You need to start `lldpd` with the `-x` option to enable connectivity to `snmpd`(AgentX). |
| {{<mib_link url="mibs/LM-SENSORS-MIB.txt" text="LM-SENSORS MIB">}} | Fan speed, temperature sensor values, voltages. This is deprecated since the ENTITY-SENSOR MIB has been added. |
| {{<mib_link url="mibs/NET-SNMP-AGENT-MIB.txt" text="NET-SNMP-AGENT-MIB">}} | Agent timers, user, group config. |
| {{<mib_link url="mibs/NET-SNMP-VACM-MIB.txt" text="NET-SNMP-VACM-MIB">}} | Agent timers, user, group config. |
| {{<mib_link url="mibs/NOTIFICATION-LOG-MIB.txt" text="NOTIFICATION-LOG-MIB">}} | Local logging. |
| {{<mib_link url="mibs/SNMP-FRAMEWORK-MIB.txt" text="SNMP-FRAMEWORK-MIB">}}|Users, access. |
| {{<mib_link url="mibs/SNMP-MPD.txt" text="SNMP-MPD-MIB">}} | Users, access. |
| {{<mib_link url="mibs/SNMP-TARGET.txt" text="SNMP-TARGET-MIB">}} | SNMP-TARGET-MIB. |
| {{<mib_link url="mibs/SNMP-USER-BASED-SM.txt" text="SNMP-USER-BASED-SM-MIBS">}} | Users, access. |
| {{<mib_link url="mibs/SNMP-VIEW-BASED-ACM.txt" text="SNMP-VIEW-BASED-ACM-MIB">}} | Users, access. |
| {{<mib_link url="mibs/TCP-MIB.txt" text="TCP-MIB">}} | TCP-related information. |
| {{<mib_link url="mibs/UCD-SNMP-MIB.txt" text="UCD-SNMP-MIB">}} | System memory, load, CPU, disk IO. |
| {{<mib_link url="mibs/UDP-MIB.txt" text="UDP-MIB">}} | UDP-related information. |
<!-- vale on -->
## List All Installed MIBs

Due to licensing restrictions, not all supported MIBs are installed in Cumulus Linux. The MIBs that are not installed require the "non-free" archive to be added to `/etc/apt/sources.list`. To see which MIBs are installed on your switch, run `ls /usr/share/snmp/mibs/`.

To install more MIBs, you need to install `snmp-mibs-downloader` and then either remove or comment out the "non-free" repository in `/etc/apt/sources.list`. This is described {{<link url="Configure-SNMP-Traps/#enable-mib-to-oid-translation" text="here">}}.

{{<expand "Installed MIBs">}}

    cumulus@switch:~$ ls /usr/share/snmp/mibs/
    AGENTX-MIB.txt                       NET-SNMP-PASS-MIB.txt
    BRIDGE-MIB.txt                       NET-SNMP-PERIODIC-NOTIFY-MIB.txt
    Cumulus-Counters-MIB.txt             NET-SNMP-SYSTEM-MIB.txt
    Cumulus-POE-MIB.txt                  NET-SNMP-TC.txt
    Cumulus-Resource-Query-MIB.txt       NET-SNMP-VACM-MIB.txt
    Cumulus-Snmp-MIB.txt                 NETWORK-SERVICES-MIB.txt
    DISMAN-EVENT-MIB.txt                 NOTIFICATION-LOG-MIB.txt
    DISMAN-EXPRESSION-MIB.txt            RFC1155-SMI.txt
    DISMAN-NSLOOKUP-MIB.txt              RFC1213-MIB.txt
    DISMAN-PING-MIB.txt                  RFC-1215.txt
    DISMAN-SCHEDULE-MIB.txt              RMON-MIB.txt
    DISMAN-SCRIPT-MIB.txt                SCTP-MIB.txt
    DISMAN-TRACEROUTE-MIB.txt            SMUX-MIB.txt
    EtherLike-MIB.txt                    SNMP-COMMUNITY-MIB.txt
    GNOME-SMI.txt                        SNMP-FRAMEWORK-MIB.txt
    HCNUM-TC.txt                         SNMP-MPD-MIB.txt
    HOST-RESOURCES-MIB.txt               SNMP-NOTIFICATION-MIB.txt
    HOST-RESOURCES-TYPES.txt             SNMP-PROXY-MIB.txt
    iana                                 SNMP-TARGET-MIB.txt
    IANA-ADDRESS-FAMILY-NUMBERS-MIB.txt  SNMP-TLS-TM-MIB.txt
    IANAifType-MIB.txt                   SNMP-TSM-MIB.txt
    IANA-LANGUAGE-MIB.txt                SNMP-USER-BASED-SM-MIB.txt
    IANA-RTPROTO-MIB.txt                 SNMP-USM-AES-MIB.txt
    ietf                                 SNMP-USM-DH-OBJECTS-MIB.txt
    IF-INVERTED-STACK-MIB.txt            SNMP-USM-HMAC-SHA2-MIB.txt
    IF-MIB.txt                           SNMPv2-CONF.txt
    INET-ADDRESS-MIB.txt                 SNMPv2-MIB.txt
    IP-FORWARD-MIB.txt                   SNMPv2-SMI.txt
    IP-MIB.txt                           SNMPv2-TC.txt
    IPV6-FLOW-LABEL-MIB.txt              SNMPv2-TM.txt
    IPV6-ICMP-MIB.txt                    SNMP-VIEW-BASED-ACM-MIB.txt
    IPV6-MIB.txt                         TCP-MIB.txt
    IPV6-TCP-MIB.txt                     TRANSPORT-ADDRESS-MIB.txt
    IPV6-TC.txt                          TUNNEL-MIB.txt
    IPV6-UDP-MIB.txt                     UCD-DEMO-MIB.txt
    LM-SENSORS-MIB.txt                   UCD-DISKIO-MIB.txt
    MTA-MIB.txt                          UCD-DLMOD-MIB.txt
    NET-SNMP-AGENT-MIB.txt               UCD-IPFILTER-MIB.txt
    NET-SNMP-EXAMPLES-MIB.txt            UCD-IPFWACC-MIB.txt
    NET-SNMP-EXTEND-MIB.txt              UCD-SNMP-MIB-OLD.txt
    NET-SNMP-MIB.txt                     UCD-SNMP-MIB.txt
    NET-SNMP-MONITOR-MIB.txt             UDP-MIB.txt

{{</expand>}}
