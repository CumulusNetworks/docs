---
title: Critical Resource Monitoring
author: NVIDIA
weight: 690
product: SONiC
version: 202012
siteSlug: sonic
---

The SONiC Critical Resource Monitoring (CRM) tool is a CLI for monitoring utilization of ASIC resources by polling SAI attributes.

## Configure CRM

You can configure the following settings for CRM:

- Polling intervals
- The following thresholds:
  - ACL table, group counter and group entry thresholds
  - Destination NAT thresholds
  - FDB thresholds
  - IPMC thresholds
  - IPv4 and IPv6 route thresholds
  - IPv4 and IPv6 neighbor thresholds
  - IPv4 and IPv6 nexthop thresholds
  - IPv4 and IPv6 nexthop group thresholds
  - Source NAT thresholds

### Configure the Polling Interval

To configure the polling interval for CRM (in seconds), run:

    admin@switch:~$ crm config polling interval SECONDS

### Configure Thresholds

You can configure the following settings for a threshold:

- High threshold value
- Low threshold value
- Type of threshold (which can be a percentage or whether the resource is used or free)

To view the default threshold settings, run:

```
admin@switch:~$ crm show thresholds all
Resource Name         Threshold Type      Low Threshold    High Threshold
--------------------  ----------------  ---------------  ----------------
ipv4_route            percentage                     70                85
ipv6_route            percentage                     70                85
ipv4_nexthop          percentage                     70                85
ipv6_nexthop          percentage                     70                85
ipv4_neighbor         percentage                     70                85
ipv6_neighbor         percentage                     70                85
nexthop_group_member  percentage                     70                85
nexthop_group         percentage                     70                85
acl_table             percentage                     70                85
acl_group             used                           70                85
acl_entry             percentage                     70                85
acl_counter           percentage                     70                85
fdb_entry             percentage                     70                85
```

The following example shows how to change the high end threshold for an ACL group.

{{<tabs "Threshold">}}

{{<tab "SONiC CLI">}}

    admin@leaf01:~$ crm config thresholds acl group high 95

{{</tab>}}

{{<tab "config_db.json">}}

Configure the ACL group high threshold in the CRM table in `/etc/sonic/config_db.json`.

```
admin@switch:~$ sudo vi /etc/sonic/config_db.json

    "CRM": {
        "Config": {
            ...
            "acl_group_high_threshold": "95",
            ...
        }
    },
```

{{</tab>}}

{{</tabs>}}

Save your changes to the configuration:

    admin@switch:~$ sudo config save -y

To verify the new threshold, run:

```
admin@leaf01:~$ crm show thresholds acl group

Resource Name    Threshold Type      Low Threshold    High Threshold
---------------  ----------------  ---------------  ----------------
acl_group        percentage                     70                95
```

<!--
### Configure ACL Thresholds

```
admin@switch:~$ crm config thresholds acl  
group  table
```

```
admin@switch:~$ crm config thresholds acl group
counter  entry    high     low      type (choose from percentage, used, free)
```

```
admin@switch:~$ crm config thresholds acl group counter
high     low      type (percentage, used, free)
```

```
admin@switch:~$ crm config thresholds acl group entry
high  low   type (percentage, used, free)
```

```
admin@switch:~$ crm config thresholds acl group
high     low      type (percentage, used, free)
```

```
admin@switch:~$ crm config thresholds acl table
high  low   type
```

### Configure FDB Thresholds

```
admin@switch:~$ crm config thresholds fdb
high  low   type (percentage, used, free)
```

### Configure IPv4 Thresholds

```
admin@switch:~$ crm config thresholds ipv4
neighbor  nexthop   route
```

```
admin@switch:~$ crm config thresholds ipv4 neighbor
high  low   type (percentage, used, free)
```

```
admin@switch:~$ crm config thresholds ipv4 nexthop
high  low   type
```

### Configure IPv6 Thresholds

```
admin@switch:~$ crm config thresholds ipv6
neighbor  nexthop   route
```

```
admin@switch:~$ crm config thresholds ipv6 neighbor
high  low   type (percentage, used, free)
```

```
admin@switch:~$ crm config thresholds ipv6 nexthop
high  low   type
```

### Configure Nexthop Thresholds

```
admin@switch:~$ crm config thresholds nexthop group member
high  low   type
```

```
admin@switch:~$ crm config thresholds nexthop group object
high  low   type
```
-->

## CRM Show Commands

The CRM `show` commands can display:

- A summary, which shows the polling interval.
- A view of all resources or thresholds.
- IPMC resources and thresholds.
- IPv4 and IPv6 route, neighbor and nexthop resources and thresholds.
- Next hop group member and object resources and thresholds.
- ACL table and group resources and thresholds.
- ACL group entry or counter resources and thresholds.
- FDB resources and thresholds.
- Source and destination NAT resources and thresholds.

### Show Resources

```
admin@switch:~$ crm show resources
acl      all      dnat     fdb      ipmc     ipv4     ipv6     nexthop  snat 
```

```
admin@switch:~$ crm show resources all

Resource Name           Used Count    Available Count
--------------------  ------------  -----------------
ipv4_route                      19              65471
ipv6_route                      11              77749
ipv4_nexthop                     0              28287
ipv6_nexthop                     0              28287
ipv4_neighbor                    0              65471
ipv6_neighbor                    0              12278
nexthop_group_member             0              28287
nexthop_group                    0              28287
fdb_entry                        0              65471


Stage    Bind Point    Resource Name      Used Count    Available Count
-------  ------------  ---------------  ------------  -----------------
INGRESS  PORT          acl_group                   0                199
INGRESS  PORT          acl_table                   0                198
INGRESS  LAG           acl_group                   0                199
INGRESS  LAG           acl_table                   0                198
INGRESS  VLAN          acl_group                   0                199
INGRESS  VLAN          acl_table                   0                198
INGRESS  RIF           acl_group                   0                199
INGRESS  RIF           acl_table                   0                198
INGRESS  SWITCH        acl_group                   0                199
INGRESS  SWITCH        acl_table                   0                198
EGRESS   PORT          acl_group                   0                199
EGRESS   PORT          acl_table                   0                198
EGRESS   LAG           acl_group                   0                199
EGRESS   LAG           acl_table                   0                198
EGRESS   VLAN          acl_group                   0                  0
EGRESS   VLAN          acl_table                   0                  0
EGRESS   RIF           acl_group                   0                199
EGRESS   RIF           acl_table                   0                198
EGRESS   SWITCH        acl_group                   0                199
EGRESS   SWITCH        acl_table                   0                198

Table ID    Resource Name    Used Count    Available Count
----------  ---------------  ------------  -----------------

```

You can filter the results to show only resources for:

- `acl`: Show CRM information for ACL table and group resources.
- `dnat`: Show CRM information for DNAT resources.
- `fdb`: Show CRM information for fdb resources.
- `ipmc`: Show CRM information for IPMC resources.
- `ipv4`: CRM resource IPv4 address family.
- `ipv6`: CRM resource IPv6 address family.
- `nexthop`: Show CRM information for nexthop resources.
- `snat`: Show CRM information for SNAT resources.

For example, to show the resources for ACL groups, run:

```
admin@switch:~$ crm show resources acl group

Stage    Bind Point    Resource Name      Used Count    Available Count
-------  ------------  ---------------  ------------  -----------------
INGRESS  PORT          acl_group                   0                199
INGRESS  PORT          acl_table                   0                198
INGRESS  LAG           acl_group                   0                199
INGRESS  LAG           acl_table                   0                198
INGRESS  VLAN          acl_group                   0                199
INGRESS  VLAN          acl_table                   0                198
INGRESS  RIF           acl_group                   0                199
INGRESS  RIF           acl_table                   0                198
INGRESS  SWITCH        acl_group                   0                199
INGRESS  SWITCH        acl_table                   0                198
EGRESS   PORT          acl_group                   0                199
EGRESS   PORT          acl_table                   0                198
EGRESS   LAG           acl_group                   0                199
EGRESS   LAG           acl_table                   0                198
EGRESS   VLAN          acl_group                   0                  0
EGRESS   VLAN          acl_table                   0                  0
EGRESS   RIF           acl_group                   0                199
EGRESS   RIF           acl_table                   0                198
EGRESS   SWITCH        acl_group                   0                199
EGRESS   SWITCH        acl_table                   0                198
```

<!-- #### Show FDB Resources

```
admin@switch:~$ crm show resources fdb

Resource Name      Used Count    Available Count
---------------  ------------  -----------------
fdb_entry                   0              65471
```

#### Show IPv4 Resources

```
admin@switch:~$ crm show resources ipv4 neighbor

Resource Name      Used Count    Available Count
---------------  ------------  -----------------
ipv4_neighbor               0              65471
```

```
admin@switch:~$ crm show resources ipv4 nexthop

Resource Name      Used Count    Available Count
---------------  ------------  -----------------
ipv4_nexthop                0              28287
```

```
admin@switch:~$ crm show resources ipv4 route

Resource Name      Used Count    Available Count
---------------  ------------  -----------------
ipv4_route                 19              65471
```

#### Show IPv6 Resources

```
admin@switch:~$ crm show resources ipv6 neighbor

Resource Name      Used Count    Available Count
---------------  ------------  -----------------
ipv6_neighbor               0              12278
```

```
admin@switch:~$ crm show resources ipv6 nexthop

---------------  ------------  -----------------
ipv6_nexthop                0              28287
```

```
admin@switch:~$ crm show resources ipv6 route

Resource Name      Used Count    Available Count
---------------  ------------  -----------------
ipv6_route                 11              77749
```

#### Show Nexthop Resources

```
admin@switch:~$ crm show resources nexthop group member 

Resource Name           Used Count    Available Count
--------------------  ------------  -----------------
nexthop_group_member             0              28287
```

```
admin@switch:~$ crm show resources nexthop group object 

---------------  ------------  -----------------
nexthop_group               0              28287
```
-->

### Show Polling Interval

To show the polling interval for CRM (how frequently it polls the system to see whether any thresholds were exceeded), run:
```
admin@switch:~$ crm show summary

Polling Interval: 300 second(s)
```

### Show Thresholds

To view all thresholds currently configured, run:

```
admin@switch:~$ crm show thresholds all
Resource Name         Threshold Type      Low Threshold    High Threshold
--------------------  ----------------  ---------------  ----------------
ipv4_route            percentage                     70                85
ipv6_route            percentage                     70                85
ipv4_nexthop          percentage                     70                85
ipv6_nexthop          percentage                     70                85
ipv4_neighbor         percentage                     70                85
ipv6_neighbor         percentage                     70                85
nexthop_group_member  percentage                     70                85
nexthop_group         percentage                     70                85
acl_table             percentage                     70                85
acl_group             used                           70                85
acl_entry             percentage                     70                85
acl_counter           percentage                     70                85
fdb_entry             percentage                     70                85
```

As with showing resources above, you can filter the results to show only thresholds for:

- `acl`: Show CRM information for acl resource.
- `dnat`: Show CRM information for DNAT resource.
- `fdb`: Show CRM information for fdb resource.
- `ipmc`: Show CRM information for IPMC resource.
- `ipv4`: CRM resource IPv4 address family.
- `ipv6`: CRM resource IPv6 address family.
- `nexthop`: Show CRM information for nexthop resources.
- `snat`: Show CRM information for SNAT resources.
