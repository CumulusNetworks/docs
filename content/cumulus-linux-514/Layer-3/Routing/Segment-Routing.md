---
title: Segment Routing
author: NVIDIA
weight: 785
toc: 3
---
Cumulus Linux supports multipathing with <span class="a-tooltip">[SRv6](## "Segment Routing for IPv6")</span> that enables you to tunnel packets from the source NIC to the destination NIC through the switch fabric using SRv6 micro segment identifiers (uSIDs). The SRv6 origination and termination is on the NIC and the switches merely act as SRv6-aware (transit) nodes. Cumulus Linux provides SRv6 uSID support with uN (END_CSID ) and uA (End.X_CSID ) endpoints.

{{%notice note%}}
Cumulus Linux supports SRv6 on the Spectrum-4 and Spectrum-5 switch only.
{{%/notice%}}

### Configure SRv6

To configure SRv6:
- Enable SRv6.
- Configure the SRv6 locator settings and the static IDs. You can configure a maximum of 32 locators.
  - Configure the SRv6 locator prefix.
  - Configure the SRv6 locator block length. Cumulus Linux currently supports a value of 32.
  - Configure the SRv6 locator function length. Cumulus Linux currently supports a value of 0.
  - Configure the SRv6 locator node length. Cumulus Linux currently supports a value of 16.
  - Configure the static segment identifier locator name. The static segment identifier must be part of the locator prefix.  
  - Configure the static segment identifier endpoint behavior. You can specify uA or uN. If you specify uA, you must also provide the interface.

The following example enables SRv6, and configures the locator called LEAF and the static SID 2001:db8:1:1::100/48:

{{< tabs "TabID980 ">}}
{{< tab "NVUE Commands ">}}

```
cumulus@switch:~$ nv set router segment-routing srv6 state enabled
cumulus@switch:~$ nv set router segment-routing srv6 locator LEAF prefix 2001:db8:1:1::/48
cumulus@switch:~$ nv set router segment-routing srv6 locator LEAF block-length 32
cumulus@switch:~$ nv set router segment-routing srv6 locator LEAF func-length 0
cumulus@switch:~$ nv set router segment-routing srv6 locator LEAF node-length 16
cumulus@switch:~$ nv set router segment-routing static srv6-sid 2001:db8:1:1::100/48 locator-name LEAF  
cumulus@switch:~$ nv set router segment-routing static srv6-sid 2001:db8:1:1::100/48 behavior uA
cumulus@switch:~$ nv set router segment-routing static srv6-sid 2001:db8:1:1::100/48 interface swp1
cumulus@switch:~$ nv config apply
```

- To disable SRv6, run the `nv set router segment-routing srv6 state disabled` command.
- To unset all locators, run the `nv unset router segment-routing  srv6 locator` command.
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
leaf01(config-srv6-locator)# prefix 2001:db8:1:1::/48 block-len 32 func-bits 0
leaf01(config-srv6-locator)# prefix 2001:db8:1:1::/48 node-len 16
leaf01(config-srv6-locator)# end
leaf01# exit
```

{{< /tab >}}
{{< /tabs >}}

{{%notice note%}}
Cumulus Linux only supports the SF3216 format (block-len(32) and node-len(16)).
{{%/notice%}}

### Show SRv6 Configuration

To show if SRv6 is enabled and to show the configured locators, run the `nv show router segment-routing` command:

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

To show configuration information for all SRv6 locators, run the `nv show router segment-routing srv6 locator` command or the vtysh `show segment-routing srv6 locator` command:

```
cumulus@switch:~$ nv show router segment-routing srv6 locator
SRv6 locator name  prefix             block length  node length  function length  status
-----------------  ----------------   ------------  -----------  ---------------  ------
LEAF               2001:db8:1:1::/48  32            16           0                up
```

To show configuration information about a specific locator, run the NVUE `nv show router segment-routing srv6 locator <locator-id>` command or the vtysh `show segment-routing srv6 locator <locator> detail` command:

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

To show the SRv6 static segment identifiers, run the NVUE `nv show router segment-routing static srv6 sid` command or the vtysh `show segment-routing srv6 sid` command:

```
cumulus@switch:~$ nv show router segment-routing srv6 sid
SRv6 SID - IPv6 address  behavior  interface  locator-name  nexthop-v6           protocol 
-----------------------  --------  ---------  ------------  -------------------  -------- 

2001:db8:1:1::100/48     End.X     swp1       LOC4          fe80::202:ff:fe00:9  static 
2001:db8:1:1::101/48     End                  LOC2                               static 
```

To show information for a specific SRv6 static segment identifier, run the NVUE `nv show router segment-routing static srv6 sid <sid>` command or the vtysh `show segment-routing srv6 sid <sid>` command:

```
cumulus@switch:~$ nv show router segment-routing static srv6 sid 2001:db8:1:1::100/48
              operational          applied 

------------  -------------------  ------- 
locator-name  LOC3 
behavior      End.X 
interface     swp1 
nexthop-v6    2001:db8:1:1::106/48
protocol      static 
```

### Show SRv6 Endpoints

SRv6 endpoints are installed as IPv6 routes into the RIB and FIB. To show SRv6 endpoints, view the
IPv6 RIB with the `nv show vrf <vrf> router rib ipv6 route` command. You can view a specific route with the `nv show vrf <vrf> router rib ipv6 route <route-id>` command.------------------------------------

### Show SRv6 Statistics

To show all SRv6 information, run the `nv show router segment-routing srv6 stats` command

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

To show information about a specific SRv6 SID, run the NVUE `nv show router segment-routing srv6 stats sid <sid>` command or the vtysh `show segment-routing srv6 sid` command:

```
cumulus@switch:~$ nv show router segment-routing srv6 stats sid 2001:db8:1:1::100/48
```

To show information about non-SID dropped packets, run the `nv show router segment-routing srv6 stats no-sid-drop` command:

```
cumulus@switch:~$ nv show router segment-routing srv6 stats no-sid-drops
                        operational
----------------------  -----------
no-sid-dropped-packets  0
```

### Clear SRv6 Statistics

To clear all SRv6 statistics, run the `nv action clear router segment-routing srv6 stats` command:

```
cumulus@switch:~$ nv action clear router segment-routing srv6 stats 
```

To clear SRv6 statistics for a specific SID, run the `nv action clear router segment-routing srv6 stats sid <sid>` command:

```
cumulus@switch:~$ nv action clear router segment-routing srv6 stats sid 2001:db8:1:1::100/48 
```

To clear SRv6 statistics for no-SID dropped packets, run the `nv action clear router segment-routing srv6 stats no-sid-drops` command:

```
cumulus@switch:~$ nv action clear router segment-routing srv6 stats no-sid-drops 
```
