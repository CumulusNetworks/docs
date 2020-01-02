---
title: Query the NetQ Database
author: Cumulus Networks
weight: 109
aliases:
 - /display/NETQ141/Query+the+NetQ+Database
 - /pages/viewpage.action?pageId=10453496
pageID: 10453496
product: Cumulus NetQ
version: 1.4.1
imgData: cumulus-netq-141
siteSlug: cumulus-netq-141
---
You can query for even more NetQ data using the SQL-like NetQ Query
Language (NetQL) so you can conduct your own custom analysis or
otherwise extend NetQ functionality for your specific environment
without having to write your own custom code. NetQL directly queries the
NetQ database for data that isn't exposed via the check, show and trace
commands.

{{%notice note%}}

NetQL is an [early access feature](https://support.cumulusnetworks.com/hc/en-us/articles/202933878)
in Cumulus NetQ 1.3 and later.

{{%/notice%}}

## Commands

  - netq query
  - netq config add|del experimental

## Enable NetQL

Since NetQL is an early access feature, you must enable the experimental
option of the NetQ CLI:

    cumulus@switch:~$ netq config add experimental

## Usage

NetQL is a generic structured query language modeled on SQL. The general
command syntax is:

    cumulus@switch:~$ netq query 'SELECT <fields> FROM <tables> WHERE <conditions> GROUP BY <fields> ORDER BY <fields>[asc|desc]' [json]

NetQL supports tab completion. When you press the TAB key after typing
*FROM*, a list of objects appears from which you can select.

Between the SELECT, FROM, WHERE, GROUP BY and ORDER BY keywords are the
following variables:

| Variable       | Definition                                                              |
| -------------- | ----------------------------------------------------------------------- |
| \<fields\>     | One or more key or non-key fields from one of the NetQ database tables. |
| \<tables\>     | One or more tables in the NetQ database.                                |
| \<conditions\> | Qualifiers to the data being queried.                                   |

These items are defined below.

The following is a real-world example:

    cumulus@switch:~$ netq query 'SELECT hostname, peer_name, peer_hostname, asn, peer_asn, state FROM BgpSession'
    hostname    peer_name        peer_hostname    asn     peer_asn    state
    ----------  ---------------  ---------------  ------  ----------  -----------
    leaf01      swp3             spine01          655536  655435      Established
    leaf01      swp6             firewall01       655536  655538      Established
    leaf01      swp7             firewall02       655536  655539      Established
    leaf01      swp4             spine02          655536  655435      Established
    leaf01      swp5             spine03          655536  655435      Established
    leaf01      swp6.4           firewall01       655536  655538      Established
    ...

The keywords are not case sensitive, so you can use *SELECT*, *Select*
or *select*. The all caps usage is for easier parsing of the queries.

## Tables and Fields

One example field is *hostname*, which is present in every table.
Example tables include Route, Link and BgpSession.

{{%notice note%}}

At this time, you cannot have multiple copies of the same table.

{{%/notice%}}

You can get a list of all the tables known to NetQ by running this
command:

    cumulus@switch:~$ netq query show tables
    Class                Key Fields
    -------------------  ---------------------------------------------------------------------------------------
    ASIC                 hostname, vendor, model, model_id, core_bw, ports
    Address              hostname, ifname, prefix, mask, is_ipv6, vrf
    BgpSession           hostname, peer_name, asn, vrf
    Board                hostname, vendor, model, base_mac, part_number, mfg_date, serial_number, label_revision
    CPU                  hostname, arch, nos, model, max_freq, mem_total
    ClagSession          hostname, clag_sysmac
    Description          hostname, objtype, descrid
    Disk                 hostname, name, size, d_type, vendor, transport, rev, model
    ...

You can get a list of all the fields in a table by running this command:

    cumulus@switch:~$ netq query show fields BgpSession
    Table           Key Fields                                                                                           Value Fields
    --------------- ---------------------------------------------------------------------------------------------------- ----------------------------------------------------------------------------------------------------
    BgpSession      hostname, peer_name, asn, vrf                                                                        state, peer_router_id, peer_asn, peer_hostname, reason, ipv4_pfx_rcvd, ipv6_pfx_rcvd,
                                                                                                                         evpn_pfx_rcvd, timestamp, last_reset_time, conn_estd, conn_dropped, upd8_rx, vrfid, upd8_tx,
                                                                                                                         up_time, tx_families, objid, rx_families, active, deleted
     
     
    cumulus@switch:~$ netq query show fields Port
    Table           Key Fields                                                                                           Value Fields
    --------------- ---------------------------------------------------------------------------------------------------- ----------------------------------------------------------------------------------------------------
    Port            hostname, ifname                                                                                     identifier, speed, autoneg, state, transreceiver, connector, length, vendor_name, part_number,
                                                                                                                         serial_number, fec, supported_fec, advertised_fec, active, deleted, timestamp

{{%notice tip%}}

The *fec*, *supported\_fec*, and *advertised\_fec* are new in NetQ
1.4.0.

{{%/notice%}}

An example query on a single table is:

    cumulus@switch:~$ netq query 'SELECT hostname, peer_name, peer_hostname, asn, peer_asn, state FROM BgpSession'
    hostname    peer_name        peer_hostname    asn     peer_asn    state
    ----------  ---------------  ---------------  ------  ----------  -----------
    exit01      swp3             spine01          655536  655435      Established
    exit01      swp6             firewall01       655536  655538      Established
    exit01      swp7             firewall02       655536  655539      Established
    exit01      swp4             spine02          655536  655435      Established
    exit01      swp5             spine03          655536  655435      Established
    exit01      swp6.4           firewall01       655536  655538      Established
    ...

NetQL displays the values of the specified fields in tabular output.

## Conditions

Conditions select what data is presented. An example of a condition is
*hostname="leaf01"*. Use double quotes ("") for the specific values you
want to match on. You can also use \!= to indicate non-matching entries.

AND is the only condition supported currently. You cannot perform
queries using parenthesized conditions at this time.

An example conditional query is:

    cumulus@switch:~$ netq query 'SELECT hostname, peer_name, peer_hostname, asn, peer_asn, state FROM BgpSession WHERE hostname="*1" AND peer_name="swp3*"'
    hostname    peer_name    peer_hostname    asn     peer_asn    state
    ----------  -----------  ---------------  ------  ----------  -----------
    exit01      swp3         spine01          655536  655435      Established
    exit01      swp3.4       spine01          655536  655435      Established
    exit01      swp3.2       spine01          655536  655435      Established
    exit01      swp3.3       spine01          655536  655435      Established
    spine01     swp3         leaf01           655435  655561      Established
    spine01     swp3.4       leaf01           655435  655561      Established
    spine01     swp3.2       leaf01           655435  655561      Established
    spine01     swp3.3       leaf01           655435  655561      Established
    leaf01      swp3         spine01          655559  655435      Established
    leaf01      swp3.4       spine01          655559  655435      Established
    leaf01      swp3.2       spine01          655559  655435      Established
    leaf01      swp3.3       spine01          655559  655435      Established
    leaf01      swp3         spine01          655561  655435      Established
    leaf01      swp3.4       spine01          655561  655435      Established
    leaf01      swp3.2       spine01          655561  655435      Established
    leaf01      swp3.3       spine01          655561  655435      Established
    leaf02      swp3         spine01          655563  655435      Established
    leaf02      swp3.4       spine01          655563  655435      Established
    leaf02      swp3.2       spine01          655563  655435      Established
    leaf02      swp3.3       spine01          655563  655435      Established

## Group Results

When you want to see not only the value of a field, but also the
aggregated output such as a count or sum, you must specify on which
field to aggregate the data. For example, to get the number of peer ASNs
for each host, the query is:

    cumulus@switch:~$ netq query 'SELECT hostname, count(peer_asn) FROM BgpSession GROUP BY hostname'
    hostname      count(peer_asn)
    ----------  -----------------
    exit01                     20
    exit02                     20
    spine01                    32
    spine02                    32
    spine03                    32
    leaf01                     12
    leaf02                     12
    leaf03                     13
    leaf04                     13
    leaf05                     13
    leaf06                     13

## Order Results

You can specify which columns you want the output sorted on using the
"ORDER BY" clause of the query. The general format of the ORDER BY
clause is:

    ORDER BY <field1> [ASC|DESC] [<field2> [ASC|DESC]...]

As an example, the output of the query in the previous section can be
sorted by the COUNT followed by hostname, as follows:

    cumulus@switch:~$ netq query 'SELECT hostname, COUNT(peer_asn) FROM BgpSession GROUP BY hostname ORDER BY COUNT(peer_asn)'
    hostname      count(peer_asn)
    ----------  -----------------
    leaf01                     12
    leaf02                     12
    leaf03                     13
    leaf04                     13
    leaf05                     13
    leaf06                     13
    exit02                     20
    exit01                     20
    spine01                    32
    spine03                    32

This sorts the count in ascending order, which is the default and does
not have to be specified. To sort by descending order, use the DESC
keyword, as follows:

    cumulus@switch:~$ netq query 'SELECT hostname, COUNT(peer_asn) FROM BgpSession GROUP BY hostname ORDER BY count(peer_asn) DESC, hostname'
    hostname      count(peer_asn)
    ----------  -----------------
    spine01                    32
    spine02                    32
    spine03                    32
    exit01                     20
    exit02                     20
    leaf03                     13
    leaf04                     13
    leaf05                     13
    leaf06                     13
    leaf01                     12
    leaf02                     12

The DESC keyword applies only to the field preceding it. Thus, in the
example above, the output is sorted by the nodes with the most peer
ASNs, and nodes with the same number of peer ASNs are sorted based on
the ascending alphabetical sort of the hostname. If you want the
hostnames to be also sorted in reverse alphabetical order, follow the
hostname field also with the DESC keyword, as follows:

    cumulus@switch:~$ netq query 'SELECT hostname, COUNT(peer_asn) FROM BgpSession GROUP BY hostname ORDER BY count(peer_asn) DESC, hostname DESC'
    hostname      count(peer_asn)
    ----------  -----------------
    spine03                    32
    spine02                    32
    spine01                    32
    exit02                     20
    exit01                     20
    leaf06                     13
    leaf05                     13
    leaf04                     13
    leaf03                     13
    leaf02                     12
    leaf01                     12

The `distinct` keyword, when used with `count`, counts only distinct or
unique values. For example, the following queries show the total number
of ASNs in use in the fabric, the number of distinct ASNs, and then the
list of each ASN:

    cumulus@switch:~$ netq query 'SELECT COUNT(peer_asn) FROM BgpSession'
      count(peer_asn)
    -----------------
                  228
    cumulus@switch:~$ netq query 'SELECT COUNT(distinct peer_asn) FROM BgpSession'
      count(distinct peer_asn)
    --------------------------
                            11
    cumulus@switch:~$ netq query 'SELECT set(peer_asn) FROM BgpSession'
    set(peer_asn)
    --------------------------------------------------------------------------------------------------------
    set([655435L, 655559L, 655560L, 655561L, 655562L, 655563L, 655564L, 655536L, 655537L, 655538L, 655539L])

## Regular Expressions

You can use any regular expression that Redis supports. They include,
but are not limited to, the following examples:

  - h?llo matches hello, hallo and hxllo
  - h\*llo matches hllo and heeeello
  - h\[ae\]llo matches hello and hallo, but not hillo
  - h\[^e\]llo matches hallo, hbllo, ... but not hello
  - h\[a-b\]llo matches hallo and hbllo

For example:

    cumulus@switch:~$ netq query 'SELECT hostname, peer_name, peer_hostname, asn, peer_asn, state FROM BgpSession WHERE hostname="\*1" AND peer_name="swp[34]"'
    hostname    peer_name    peer_hostname    asn     peer_asn    state
    ----------  -----------  ---------------  ------  ----------  -----------
    exit01      swp3         spine01          655536  655435      Established
    exit01      swp4         spine02          655536  655435      Established
    firewall01  swp4         exit02           655538  655537      Established
    firewall01  swp3         exit01           655538  655536      Established
    spine01     swp3         leaf01           655435  655561      Established
    spine01     swp4         leaf02           655435  655562      Established
    leaf01      swp3         spine01          655559  655435      Established
    leaf01      swp4         spine02          655559  655435      Established

## JSON Output

Any command's output can be returned in JSON format by ending the
command with the optional `json` keyword, as follows:

    cumulus@hostd-11:~$ netq query 'select hostname, peer_name, tx_families, rx_families from BgpSession where hostname=tor-1 and peer_name=swp3' json
    [
        {
            "tx_families":[
                "ipv4",
                "ipv6",
                "evpn"
            ],
            "hostname":"tor-1",
            "rx_families":[
                "ipv4",
                "ipv6",
                "evpn"
            ],
            "peer_name":"swp3"
        }
    ]

Here's the output without JSON:

    cumulus@hostd-11:~$ netq query 'select hostname, peer_name, tx_families, rx_families from BgpSession where hostname=tor-1 and peer_name=swp3'
    hostname          peer_name tx_families rx_families
    ----------------- --------- ----------- -----------
    tor-1             swp3      [u'ipv4',   [u'ipv4',
                                u'ipv6',    u'ipv6',
                                u'evpn']    u'evpn']

## Recommended Tables and Fields

The following tables and fields are supported as part of Early Access.

There are key fields and value fields for each table. You can get a list
of the key and value fields by running the `netq show query fields`
command. For example:

```
cumulus@hostd-11:~$ netq query show fields Temp
Table        Key Fields                               Value Fields
------------ ---------------------------------------- ----------------------------------------------------------
Temp         hostname, s_name, s_desc                 timestamp, s_state, s_prev_state, s_input, s_msg, s_crit,
                                                      s_min, s_max, s_lcrit                                                             
```

| Table | Key Fields | Value Field |
| ----- | ---------- | ----------- |
| ASIC  | hostname, vendor, model, model\_id, core\_bw, ports | timestamp |
| Address            | hostname, ifname, prefix, mask, is\_ipv6, vrf                                                | timestamp, active, deleted                                                                                                                                                                                                                                                                        |
| BgpSession         | hostname, peer\_name, asn, vrf                                                               | state, peer\_router\_id, peer\_asn, peer\_hostname, reason, ipv4\_pfx\_rcvd, ipv6\_pfx\_rcvd, evpn\_pfx\_rcvd, timestamp, last\_reset\_time, conn\_estd, conn\_dropped, upd8\_rx, vrfid, upd8\_tx, up\_time, tx\_families, objid, rx\_families, active, deleted                                   |
| Board              | hostname, vendor, model, base\_mac, part\_number, mfg\_date, serial\_number, label\_revision | timestamp                                                                                                                                                                                                                                                                                         |
| CPU                | hostname, arch, nos, model, max\_freq, mem\_total                                            | timestamp                                                                                                                                                                                                                                                                                         |
| ClagSession        | hostname, clag\_sysmac                                                                       | peer\_role, role, peer\_state, peer\_if, backup\_ip, backup\_ip\_active, single\_bonds, dual\_bonds, timestamp, conflicted\_bonds, vxlan\_anycast, proto\_down\_bonds, active, deleted                                                                                                            |
| Description        | hostname, objtype, descrid                                                                   | description, timestamp, active, deleted                                                                                                                                                                                                                                                           |
| Disk               | hostname, name, size, d\_type, vendor, transport, rev, model                                 | timestamp                                                                                                                                                                                                                                                                                         |
| DockerContainer    | hostname, name, image, network\_name, ip, mac, service\_name                                 | timestamp, container\_id, status, network\_id, gw, prefix\_len, port\_list, service\_id, start\_time, active, deleted                                                                                                                                                                             |
| DockerHost         | hostname, docker\_version                                                                    | images, containers, containers\_running, ip\_forwarding, timestamp, active, deleted                                                                                                                                                                                                               |
| DockerNetwork      | hostname, network\_name, driver                                                              | gateway, parent\_interface, vxlan\_id, network\_id, mtu, host\_binding, ipv6\_enabled, ip\_masquerade, encrypted, default\_bridge, ipam\_driver, subnet, container\_list, timestamp, active, deleted                                                                                              |
| DockerPortMap      | hostname, name, container\_ip, proto, container\_port, host\_ip, host\_port, network\_name   | timestamp, container\_id, network\_id, image, mac, node\_id, active, deleted                                                                                                                                                                                                                      |
| DockerService      | hostname, service\_name, mode                                                                | image, replicas, parallelism, service\_id, port\_list, network\_list, vip, version, timestamp, active, deleted                                                                                                                                                                                    |
| DockerSwarmCluster | hostname, cluster\_name                                                                      | docker\_version, cluster\_version, cluster\_id, num\_nodes, num\_managers, managers, timestamp, nodes, active, deleted                                                                                                                                                                            |
| DockerSwarmNode    | hostname, cluster\_name, node\_name                                                          | timestamp, docker\_version, cluster\_id, node\_id, node\_state, role, plugins, availability, active, deleted                                                                                                                                                                                      |
| Fan                | hostname, s\_name, s\_desc                                                                   | timestamp, s\_state, s\_prev\_state, s\_input, s\_msg, s\_max, s\_min                                                                                                                                                                                                                             |
| License            | hostname, name                                                                               | state, license, timestamp                                                                                                                                                                                                                                                                         |
| Link               | hostname, ifname, kind, vni, master                                                          | admin\_state, oper\_state, managed, mtu, ifindex, is\_vlan\_filtering, timestamp, vlans, access\_vlan, localip, down\_reason, vrf, rt\_table\_id, parent\_if, stp\_state, mac\_address, dstport, learning\_en, objid, arp\_suppress\_en, active, deleted                                          |
| Liveness           | hostname                                                                                     | hostname                                                                                                                                                                                                                                                                                          |
| Lldp               | hostname, ifname, peer\_hostname                                                             | peer\_ifname, lldp\_peer\_bridge, lldp\_peer\_router, lldp\_peer\_station, lldp\_peer\_os, lldp\_peer\_osv, timestamp, active, deleted                                                                                                                                                            |
| LnvSession         | hostname, role                                                                               | role, snd\_ip, rd\_peers, snd\_peers, vnis, state, repl\_mode, version, active, deleted, timestamp                                                                                                                                                                                                |
| MacFdb             | hostname, mac\_address, vlan                                                                 | origin, nexthop, dst, port, timestamp, is\_remote, is\_static, active, deleted                                                                                                                                                                                                                    |
| Memory             | hostname, name, size, speed, m\_type, vendor, serial\_number                                 | timestamp                                                                                                                                                                                                                                                                                         |
| MstpInfo           | hostname, bridge\_name                                                                       | root\_port\_name, topo\_chg\_ports, time\_since\_tcn, topo\_chg\_cntr, ports, edge\_ports, state, network\_ports, disputed\_ports, bpduguard\_ports, root\_bridge, bridge\_id, bpduguard\_err\_ports, ba\_inconsistent\_ports, bpdufilter\_ports, is\_vlan\_filtering, active, deleted, timestamp |
| Neighbor           | hostname, ifname, ip\_address, mac\_address, is\_ipv6, vrf                                   | ifindex, timestamp, is\_remote, active, deleted                                                                                                                                                                                                                                                   |
| Node               | hostname                                                                                     | lastboot, sys\_uptime, last\_reinit, ntp\_state, version                                                                                                                                                                                                                                          |
| Ntp                | hostname                                                                                     | current\_server, stratum, ntp\_sync, timestamp, ntp\_app, active, deleted                                                                                                                                                                                                                         |
| OS                 | hostname                                                                                     | timestamp, name, version, version\_id                                                                                                                                                                                                                                                             |
| OspfIf             | hostname, ifname, area                                                                       | network\_type, timestamp, nbr\_count, if\_up, nbr\_adj\_count, is\_unnumbered, is\_passive, cost, mtu, dead\_time, rexmit\_time, hello\_time, router\_id, area, active, deleted                                                                                                                   |
| OspfNbr            | hostname, ifname, peer\_id, area                                                             | state, timestamp, ifname, is\_ipv6, peer\_addr, area, active, deleted                                                                                                                                                                                                                             |
| PSU                | hostname, s\_name                                                                            | timestamp, s\_state, s\_prev\_state, s\_msg                                                                                                                                                                                                                                                       |
| Port               | hostname, ifname                                                                             | identifier, speed, autoneg, state, transreceiver, connector, length, vendor\_name, part\_number, serial\_number, fec, supported\_fec, advertised\_fec, deleted, timestamp                                                                                                                         |
| Route              | hostname, prefix, route\_type, rt\_table\_id, is\_ipv6, origin, protocol, vrf                | nexthops, src, timestamp, active, deleted                                                                                                                                                                                                                                                         |
| Services           | hostname, name, vrf                                                                          | is\_enabled, is\_active, status, is\_monitored, start\_time, pid, timestamp, active, deleted                                                                                                                                                                                                      |
| Temp               | hostname, s\_name, s\_desc                                                                   | timestamp, s\_state, s\_prev\_state, s\_input, s\_msg, s\_crit, s\_max, s\_min, s\_lcrit                                                                                                                                                                                                          |
| VxlanRemoteDest    | hostname, vni, rdst                                                                          | vni, rdst, active, deleted, timestamp                                                                                                                                                                                                                                                             |
