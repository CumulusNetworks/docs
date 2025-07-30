---
title: Segment Routing
author: NVIDIA
weight: 785
toc: 3
---
Cumulus Linux supports multipathing with <span class="a-tooltip">[SRv6](## "Segment Routing for IPv6")</span> that enables you to tunnel packets from the source NIC to the destination NIC through the switch fabric using SRv6 micro segment identifiers (uSIDs). The SRv6 origination and termination is on the NIC and the switches merely act as SRv6-aware (transit) nodes. Cumulus Linux provides SRv6 uSID support with uN (END_CSID ) and uA (End.X_CSID ) endpoints.

{{%notice note%}}
Cumulus Linux supports segment routing on the Spectrum-4 switch.
{{%/notice%}}

### Configure Segment Routing

To configure segment routing:
- Enable segment routing.
- Configure the SRv6 locator settings and the static IDs. You can configure a maximum of 256 locators.
  - Configure the SRv6 locator prefix. The prefix length must match the sum of block length and the node length.
  - Configure the SRv6 locator block length. You can specify a value between 16 and 64. The default value is 16.
  - Configure the SRv6 locator function length. You can specify a value between 0 and 64. The default value is 0.
  - Configure the SRv6 locator node length. You can specify a value between 0 and 64. The default value is 16.
  - Configure the static segment identifier locator name. The static segment identifier must be part of the locator prefix.  
  - Configure the static segment identifier endpoint behavior. You can specify uA or uN. If you specify uA, you must also provide the interface. Cumulus Linux enables route advertisements on the interface on which you configure uA.

The following table provides the supported formats for block, node, and function length.

| Format | Block Length  | Node Length | Function Length |
|--------|---------------|-------------|-----------------|
|uN      | 32            | 16          | 0               |
|uA + uN | 16            | 16          | 16              |
|uN only | 16            | 16          | 0               |
|uA only | 16            | 0           | 16              |

The following example enables segment routing, and configures the SRv6 locator called LEAF and the static segment identifier 2001:db8:1:1::100/48:

{{< tabs "TabID980 ">}}
{{< tab "NVUE Commands ">}}

```
cumulus@switch:~$ nv set router segment-routing srv6 state enabled
cumulus@switch:~$ nv set router segment-routing srv6 locator LEAF prefix 2001:db8:1:1::/32
cumulus@switch:~$ nv set router segment-routing srv6 locator LEAF block-length 16
cumulus@switch:~$ nv set router segment-routing srv6 locator LEAF func-length 0
cumulus@switch:~$ nv set router segment-routing srv6 locator LEAF node-length 16
cumulus@switch:~$ nv set router segment-routing static srv6-sid 2001:db8:1:1::100/48 locator-name LEAF  
cumulus@switch:~$ nv set router segment-routing static srv6-sid 2001:db8:1:1::100/48 behavior uA
cumulus@switch:~$ nv set router segment-routing static srv6-sid 2001:db8:1:1::100/48 interface swp1
cumulus@switch:~$ nv config apply
```

- To disable segment routing, run the `nv set router segment-routing srv6 state disabled` command.
- To unset all SRv6 locators, run the `nv unset router segment-routing srv6 locator` command.
- To unset all static segment identifiers, run the `nv unset router segment-routing static srv6-sid` command.
- To unset a static segment identifier, run the `nv unset router segment-routing static srv6-sid <prefix>` command.

{{< /tab >}}
{{< tab "Linux Commands ">}}

```
cumulus@switch:~$ sudo vtysh
...
leaf01# configure t
leaf01(config)# segment-routing 
leaf01(config-sr)# srv6
leaf01(config-srv6)# static-sids
leaf01(config-srv6-sids)# sid 2001:db8:1:1::100/48 locator LEAF behavior uA
leaf01(config-srv6-sids)# exit
leaf01(config-srv6)# locators
leaf01(config-srv6-locators)# locator LEAF
leaf01(config-srv6-locator)# prefix 2001:db8:1:1::/48 block-len 16 func-bits 0
leaf01(config-srv6-locator)# prefix 2001:db8:1:1::/48 node-len 16
leaf01(config-srv6-locator)# end
leaf01# exit
```

{{< /tab >}}
{{< /tabs >}}

### Show Segment Routing Configuration

To show if segment routing is enabled, and to show the configured locators and SRv6 segment identifiers, run the `nv show router segment-routing` command:

```
cumulus@switch:~$ nv show router segment-routing 
              applied             
------------  --------------------
srv6                              
  state       enabled             
  [locator]   LEAF                
static                            
  [srv6-sid]  2001:db8:1:1::100/48
```

To show the configuration for all SRv6 locators, run the `nv show router segment-routing srv6 locator` command or the vtysh `show segment-routing srv6 locator` command:

```
cumulus@switch:~$ nv show router segment-routing srv6 locator
SRv6 locator name  prefix             block length  node length  function length  status
-----------------  ----------------   ------------  -----------  ---------------  ------
LEAF               2001:db8:1:1::/48  32            16           0                up
```

To show the configuration for a specific SRv6 locator, run the NVUE `nv show router segment-routing srv6 locator <locator-id>` command or the vtysh `show segment-routing srv6 locator <locator> detail` command:

```
cumulus@switch:~$ nv show router segment-routing srv6 locator LEAF
              operational      applied          
------------  ---------------  -----------------
prefix        2001:db8:1::/48  2001:db8:1:1::/48
block-length  32               32               
node-length   16               16               
func-length   0                0                
status        up
```

To show the configuration for a specific SRv6 static segment identifier, run the NVUE `nv show router segment-routing static srv6 sid <sid>` command or the vtysh `show segment-routing srv6 sid <sid>` command:

```
cumulus@switch:~$ nv show router segment-routing srv6 sid 2001:db8:1:1::100/48
              operational          applied 

------------  -------------------  ------- 
locator-name  LOC3 
behavior      End.X 
interface     swp1 
nexthop-v6    2001:db8:1:1::106/48
protocol      static 
```

### Show Segment Routing Endpoints

Segment routing endpoints are installed as IPv6 routes into the RIB and FIB. To show segment routing endpoints, view the
IPv6 RIB with the `nv show vrf <vrf-id> router rib ipv6 route` command. You can view a specific route with the `nv show vrf <vrf-id> router rib ipv6 route <route-id>` command.

### Show SRv6 Statistics

To show SRv6 statistics, run the `nv show router segment-routing srv6 stats` command

```
cumulus@switch:~$ nv show router segment-routing srv6 stats
Hit Counters
------------------------------
SID                                             Packets
---------------------------------------      ----------
2001:db8:1:1::100/48                                   0
2001:db8:1:1::101/48                                   0

Drop Counters
------------------------------
Total no-sid-dropped packets
```

To show information about a specific SRv6 segment identifier, run the NVUE `nv show router segment-routing srv6 stats sid <sid>` command or the vtysh `show segment-routing srv6 sid` command:

```
cumulus@switch:~$ nv show router segment-routing srv6 stats sid 2001:db8:1:1::100/48
```

To show information about non segment identifier dropped packets, run the `nv show router segment-routing srv6 stats no-sid-drop` command:

```
cumulus@switch:~$ nv show router segment-routing srv6 stats no-sid-drops
                        operational
----------------------  -----------
no-sid-dropped-packets  0
```

{{%notice note%}}
When you enable {{<link url="Packet-Trimming" text="packet trimming">}} with segment routing, Cumulus Linux counts the trimmed packet twice in the SRv6 statistics.
{{%/notice%}}

### Clear RSv6 Statistics

To clear all SRv6 statistics, run the `nv action clear router segment-routing srv6 stats` command:

```
cumulus@switch:~$ nv action clear router segment-routing srv6 stats 
```

To clear SRv6 statistics for a specific segment identifier, run the `nv action clear router segment-routing srv6 stats sid <sid>` command:

```
cumulus@switch:~$ nv action clear router segment-routing srv6 stats sid 2001:db8:1:1::100/48 
```

To clear SRv6 statistics for non segment identifier dropped packets, run the `nv action clear router segment-routing srv6 stats no-sid-drops` command:

```
cumulus@switch:~$ nv action clear router segment-routing srv6 stats no-sid-drops 
```
