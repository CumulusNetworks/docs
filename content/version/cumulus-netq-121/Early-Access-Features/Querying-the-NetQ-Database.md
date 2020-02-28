---
title: Querying the NetQ Database
author: Cumulus Networks
weight: 77
aliases:
 - /display/NETQ121/Querying+the+NetQ+Database
 - /pages/viewpage.action?pageId=8356587
pageID: 8356587
product: Cumulus NetQ
version: "1.2"
imgData: cumulus-netq-121
siteSlug: cumulus-netq-121
---
You can query for even more NetQ data using the SQL-like NetQ Query
Language (NetQL) so you can conduct your own custom analysis or
otherwise extend NetQ functionality for your specific environment
without having to write your own custom code. NetQL directly queries the
NetQ database for data that isn't exposed via the check, show and trace
commands.

{{%notice warning%}}

**Early Access Feature**

NetQL is an [early access
feature](https://support.cumulusnetworks.com/hc/en-us/articles/202933878)
in Cumulus NetQ 1.2.

{{%/notice%}}

## Commands</span>

  - netq query

  - netq config add|del experimental

## Enabling NetQL</span>

Since NetQL is an early access feature, you must enable the experimental
option of the NetQ CLI:

    cumulus@switch:~$ netq config add experimental

## Usage</span>

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

## Tables and Fields</span>

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
    Key Fields                           Value Fields
    ------------------------------------ ----------------------------------------------------------------
    hostname, peer_name, asn, vrf        state, peer_router_id, peer_asn, peer_hostname, reason,
                                         ipv4_pfx_rcvd, ipv6_pfx_rcvd, evpn_pfx_rcvd, timestamp,
                                         last_reset_time, conn_estd, conn_dropped, upd8_rx, vrfid,
                                         upd8_tx, up_time, tx_families, objid, rx_families, active,
                                         deleted

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

## Conditions</span>

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

## Grouping Results</span>

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

## Ordering Results</span>

You can specify which columns you want the output sorted on using the
"ORDER BY" clause of the query. The general format of the ORDER BY
clause is:

    ORDER BY <field1> [ASC|DESC] [<field2> [ASC|DESC]...]

As an example, the output of the query in the previous section can be
sorted by the COUNT followed by hostname, as follows:

    cumulus@switch:~$ etq query 'SELECT hostname, COUNT(peer_asn) FROM BgpSession GROUP BY hostname ORDER BY COUNT(peer_asn)'
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

## Regular Expressions</span>

You can use any regular expression that Redis supports. They include,
but are not limited to, the following examples:

  - h?llo matches hello, hallo and hxllo

  - h\*llo matches hllo and heeeello

  - h\[ae\]llo matches hello and hallo, but not hillo

  - h\[^e\]llo matches hallo, hbllo, ... but not hello

  - h\[a-b\]llo matches hallo and hbllo

For example:

    cumulus@switch:~$ netq query 'SELECT hostname, peer_name, peer_hostname, asn, peer_asn, state FROM BgpSession WHERE hostname="*1" AND peer_name="swp[34]"'
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

## JSON Output</span>

Any command's output can be returned in JSON format by ending the
command with the optional `json` keyword, as follows:

    cumulus@switch:~$ netq query 'select count(peer_name) from BgpSession' json  
      [
        {
            "count(peer_name)":25
        }
      ]

