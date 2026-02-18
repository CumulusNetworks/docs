---
title: Segment Routing
author: NVIDIA
weight: 785
toc: 3
---
Cumulus Linux supports source based routing with <span class="a-tooltip">[SRv6](## "Segment Routing for IPv6")</span>.

The NICs connected to the switch fabric perform SRv6 origination and termination, and the switches act as SRv6-aware nodes. SRv6 allows NICs to directly control the path that traffic takes throughout the fabric by encoding an ordered list of SRv6 segment identifiers (uSIDs) in the packet header.

Cumulus Linux supports uN (End with NEXT-CSID) and uA (End.X with NEXT-CSID) endpoint behaviors, defined in {{<exlink url="https://datatracker.ietf.org/doc/rfc9800/" text="RFC9800" >}}.

{{%notice note%}}
Cumulus Linux supports segment routing:
- On the Spectrum-4 switch only.
- In the default VRF only.
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
  - Configure the static segment identifier endpoint behavior. You can specify uA or uN. For uA segment identifiers, next hop (peer link-local) learning occurs with router advertisements. Spectrum switches enable router advertisements on the interface automatically when you configure a uA segment identifier; however, if the adjacent device is a non-Spectrum switch, you need to enable router advertisements on the adjacent device on the connected interface to ensure proper next hop discovery.

The following table provides the supported formats for block, node, and function length.

| Format | Block Length  | Node Length | Function Length |
|--------|---------------|-------------|-----------------|
|uN      | 32            | 16          | 0               |
|uA + uN | 16            | 16          | 16              |
|uN only | 16            | 16          | 0               |
|uA only | 16            | 0           | 16              |

{{%notice note%}}
Avoid reusing IPv6 prefixes for both static routes and static segment identifiers. Use distinct prefixes to prevent routing table conflicts and ensure correct segment routing behavior. If you configure a static route that overrides a segment identifier or a segment identifier that overrides a static route, unset, then reset the static segment identifier.
{{%/notice%}}

The following example enables segment routing, configures the SRv6 locator called LEAF with the prefix fcbb::/16, and sets the static segment identifier fcbb:fe8::/32:

{{< tabs "TabID980 ">}}
{{< tab "NVUE Commands ">}}

```
cumulus@switch:~$ nv set router segment-routing srv6 state enabled
cumulus@switch:~$ nv set router segment-routing srv6 locator LEAF prefix fcbb::/16 
cumulus@switch:~$ nv set router segment-routing srv6 locator LEAF block-length 16
cumulus@switch:~$ nv set router segment-routing srv6 locator LEAF node-length 0
cumulus@switch:~$ nv set router segment-routing srv6 locator LEAF func-length 16
cumulus@switch:~$ nv set router segment-routing static srv6-sid fcbb:fe8::/32 behavior uA
cumulus@switch:~$ nv set router segment-routing static srv6-sid fcbb:fe8::/32 interface swp1
cumulus@switch:~$ nv set router segment-routing static srv6-sid fcbb:fe8::/32 locator-name LEAF  
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
leaf01(config-srv6-sids)# sid fcbb:fe8::/32 locator LEAF behavior uA interface swp1
leaf01(config-srv6-sids)# exit
leaf01(config-srv6)# locators
leaf01(config-srv6-locators)# locator LEAF
leaf01(config-srv6-locator)# prefix fcbb::/16 block-len 16 node-len 0 func-bits 16
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
  [locator]   LEAF                å
static                            
  [srv6-sid]  fcbb:fe8::/32
```

To show the configuration for all SRv6 locators, run the `nv show router segment-routing srv6 locator` command or the vtysh `show segment-routing srv6 locator` command:

```
cumulus@switch:~$ nv show router segment-routing srv6 locator
SRv6 locator name  prefix             block length  node length  function length  status
-----------------  ----------------   ------------  -----------  ---------------  ------
LEAF               fcbb::/16          16            0            16               up
```

To show the configuration for a specific SRv6 locator, run the NVUE `nv show router segment-routing srv6 locator <locator-id>` command or the vtysh `show segment-routing srv6 locator <locator> detail` command:

```
cumulus@switch:~$ nv show router segment-routing srv6 locator LEAF
              operational      applied          
------------  ---------------  -----------------
prefix        fcbb::/16.       fcbb::/16
block-length  16               16             
node-length   0                0                
func-length   16               16               
status        up
```

To show the configuration for a specific SRv6 static segment identifier, run the NVUE `nv show router segment-routing static srv6 sid <sid>` command or the vtysh `show segment-routing srv6 sid <sid>` command:

```
cumulus@switch:~$ nv show router segment-routing srv6 sid fcbb:fe8::/32
              operational          applied 

------------  -------------------  ------- 
locator-name  LEAF 
behavior      End.X 
interface     swp1 
nexthop-v6    fe80::202:ff:fe00:2
protocol      static 
```

### Show Segment Routing Endpoints

Segment routing endpoints are installed as IPv6 routes into the RIB and FIB. To show segment routing endpoints, view the
IPv6 RIB with the `nv show vrf <vrf-id> router rib ipv6 route` command. You can view a specific route with the `nv show vrf <vrf-id> router rib ipv6 route <route-id>` command.

### Show Segment Routing Statistics

To show SRv6 statistics, run the `nv show router segment-routing srv6 stats` command

```
cumulus@switch:~$ nv show router segment-routing srv6 stats
Hit Counters
------------------------------
SID                                          Packets
---------------------------------------      ----------
fcbb:fe8::/32                                0

Drop Counters
------------------------------
Total no-sid-dropped packets
```

To show information about a specific SRv6 segment identifier, run the NVUE `nv show router segment-routing srv6 stats sid <sid>` command or the vtysh `show segment-routing srv6 sid` command:

```
cumulus@switch:~$ nv show router segment-routing srv6 stats sid fcbb:fe8::/32
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

### Clear SRv6 Statistics

To clear all segment routing statistics, run the `nv action clear router segment-routing srv6 stats` command:

```
cumulus@switch:~$ nv action clear router segment-routing srv6 stats 
```

To clear SRv6 statistics for a specific segment identifier, run the `nv action clear router segment-routing srv6 stats sid <sid>` command:

```
cumulus@switch:~$ nv action clear router segment-routing srv6 stats sid fcbb:fe8::/32 
```

To clear SRv6 statistics for non segment identifier dropped packets, run the `nv action clear router segment-routing srv6 stats no-sid-drops` command:

```
cumulus@switch:~$ nv action clear router segment-routing srv6 stats no-sid-drops 
```

## Related Information

- {{<exlink url="https://datatracker.ietf.org/doc/rfc9800/" text="RFC9800" >}}
- {{<exlink url="https://www.iana.org/assignments/segment-routing/segment-routing.xhtml" text="IANA: Segment Routing" >}}
