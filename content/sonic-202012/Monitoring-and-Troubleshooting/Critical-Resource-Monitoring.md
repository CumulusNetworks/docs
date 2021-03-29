---
title: Critical Resource Monitoring
author: Cumulus Networks
weight: 690
product: SONiC
version: 202012
siteSlug: sonic
---

The SONiC Critical Resource Monitoring (CRM) tool is a CLI for monitoring utilization of ASIC resources by polling SAI attributes.

## Configure CRM

You can configure the following settings for CRM:

- ACL table, group counter and group entry thresholds
- FDB thresholds
- IPv4 and IPv6 route thresholds
- IPv4 and IPv6 neighbor thresholds
- IPv4 and IPv6 nexthop thresholds
- IPv4 and IPv6 nexthop group thresholds
- Polling intervals

### Configure the Polling Interval

To configure the polling interval for CRM (in seconds), run:

    admin@switch:~$ crm config polling interval SECONDS

### Configure Thresholds

You can configure the following settings for a threshold:

- High threshold value
- Low threshold value
- Type of threshold (which can be a percentage or whether the resource is used or free)



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

- A summary, which shows the polling interval
- A view of all resources or thresholds
- IPv4 and IPv6 route, neighbor and nexthop resources and thresholds
- Nexthop group member and object resources and thresholds
- ACL table and group resources and thresholds
- ACL group entry or counter resources and thresholds
- FDB resources and thresholds

<!--
### Show Resources

```
admin@switch:~$ crm show resources
acl      all      fdb      ipv4     ipv6     nexthop
```

```
admin@switch:~$ crm show resources all

CRM counters are not ready. They would be populated after the polling interval.


Resource Name    Used Count    Available Count
---------------  ------------  -----------------



Stage    Bind Point    Resource Name    Used Count    Available Count
-------  ------------  ---------------  ------------  -----------------



Table ID    Resource Name    Used Count    Available Count
----------  ---------------  ------------  -----------------

```

#### Show ACL Resources

```
admin@switch:~$ crm show resources acl table


Table ID    Resource Name    Used Count    Available Count
----------  ---------------  ------------  -----------------


```

```
admin@switch:~$ crm show resources acl group 


Stage    Bind Point    Resource Name    Used Count    Available Count
-------  ------------  ---------------  ------------  -----------------

```

#### Show FDB Resources

```
admin@switch:~$ crm show resources fdb

CRM counters are not ready. They would be populated after the polling interval.


Resource Name    Used Count    Available Count
---------------  ------------  -----------------

```

#### Show IPv4 Resources

```
admin@switch:~$ crm show resources ipv4 neighbor

CRM counters are not ready. They would be populated after the polling interval.


Resource Name    Used Count    Available Count
---------------  ------------  -----------------

```

```
admin@switch:~$ crm show resources ipv4 nexthop

CRM counters are not ready. They would be populated after the polling interval.


Resource Name    Used Count    Available Count
---------------  ------------  -----------------

```

```
admin@switch:~$ crm show resources ipv4 route

CRM counters are not ready. They would be populated after the polling interval.


Resource Name    Used Count    Available Count
---------------  ------------  -----------------

```

#### Show IPv6 Resources

```
admin@switch:~$ crm show resources ipv6 neighbor

CRM counters are not ready. They would be populated after the polling interval.


Resource Name    Used Count    Available Count
---------------  ------------  -----------------

```

```
admin@switch:~$ crm show resources ipv6 nexthop

CRM counters are not ready. They would be populated after the polling interval.


Resource Name    Used Count    Available Count
---------------  ------------  -----------------


```

```
admin@switch:~$ crm show resources ipv6 route

CRM counters are not ready. They would be populated after the polling interval.


Resource Name    Used Count    Available Count
---------------  ------------  -----------------

```

#### Show Nexthop Resources

```
admin@switch:~$ crm show resources nexthop group member 

CRM counters are not ready. They would be populated after the polling interval.


Resource Name    Used Count    Available Count
---------------  ------------  -----------------

```

```
admin@switch:~$ crm show resources nexthop group object 

CRM counters are not ready. They would be populated after the polling interval.


Resource Name    Used Count    Available Count
---------------  ------------  -----------------

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
