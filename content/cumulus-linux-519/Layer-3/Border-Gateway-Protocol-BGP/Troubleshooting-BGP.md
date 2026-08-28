---
title: Troubleshooting BGP
author: NVIDIA
weight: 870
toc: 3
---
Use the following commands to troubleshoot BGP.

## Show BGP configuration Summary

To show a summary of the BGP configuration on the switch, run the NVUE `nv show router bgp` command or the vtysh `show ip bgp summary` command (you can also run the vtysh `show bgp router json` or
`show bgp vrfs default json` command). For example:

```
cumulus@switch:~$ nv show router bgp
                                operational  applied     
------------------------------  -----------  ----------- 
state                           enabled      enabled     
autonomous-system               65101        65101       
router-id                       10.10.10.1   10.10.10.1  
policy-update-timer             5            5           
graceful-shutdown               disabled     disabled    
wait-for-install                disabled     disabled    
graceful-restart                                         
  mode                          helper-only  helper-only 
  restart-time                  120          120         
  path-selection-deferral-time  120          120         
  stale-routes-time             360          360         
convergence-wait                                         
  time                          0            0           
  establish-wait-time           0            0           
queue-limit                                              
  input                         10000        10000       
  output                        10000        10000       
```

```
cumulus@switch:~$ sudo vtysh
...
switch# show ip bgp summary

IPv4 Unicast Summary:
BGP router identifier 10.10.10.101, local AS number 65199 VRF default vrf-id 0
BGP table version 94
RIB entries 13, using 1664 bytes of memory
Peers 6, using 120 KiB of memory
Peer groups 1, using 64 bytes of memory

Neighbor        V         AS   MsgRcvd   MsgSent   TblVer  InQ OutQ  Up/Down State/PfxRcd   PfxSnt Desc
leaf01(swp1)    4      65101     29176     29225        0    0    0 02:25:16      Connect        0 FRRouting/10.0.3
leaf02(swp2)    4      65102     29251     29270        0    0    0 02:22:56      Connect        0 FRRouting/10.0.3
leaf03(swp3)    4      65103     32142     32123       94    0    0 1d02h29m            3        7 FRRouting/10.0.3
leaf04(swp4)    4      65104     32144     32137       94    0    0 02:27:40            3        7 FRRouting/10.0.3
border01(swp5)  4      65253     32229     32141       94    0    0 02:27:41            3        7 FRRouting/10.0.3
border02(swp6)  4      65254     32235     32123       94    0    0 1d02h29m            3        7 FRRouting/10.0.3

Total number of neighbors 6
```

To view the routing table as defined by BGP, run the vtysh `show ip bgp ipv4 unicast` command. For example:

```
cumulus@leaf01:~$ sudo vtysh
...
leaf01# show ip bgp ipv4 unicast
BGP table version is 88, local router ID is 10.10.10.1, vrf id 0
Default local pref 100, local AS 65101
Status codes:  s suppressed, d damped, h history, * valid, > best, = multipath,
               i internal, r RIB-failure, S Stale, R Removed
Nexthop codes: @NNN nexthop's vrf id, < announce-nh-self
Origin codes:  i - IGP, e - EGP, ? - incomplete

   Network          Next Hop            Metric LocPrf Weight Path
* i10.0.1.1/32      peerlink.4094            0    100      0 ?
*>                  0.0.0.0                  0         32768 ?
*= 10.0.1.2/32      swp54                                  0 65199 65102 ?
*=                  swp52                                  0 65199 65102 ?
* i                 peerlink.4094                 100      0 65199 65102 ?
*=                  swp53                                  0 65199 65102 ?
*>                  swp51                                  0 65199 65102 ?
*= 10.0.1.254/32    swp54                                  0 65199 65132 ?
*=                  swp52                                  0 65199 65132 ?
* i                 peerlink.4094                 100      0 65199 65132 ?
*=                  swp53                                  0 65199 65132 ?
*>                  swp51                                  0 65199 65132 ?
*> 10.10.10.1/32    0.0.0.0                  0         32768 ?
*>i10.10.10.2/32    peerlink.4094            0    100      0 ?
*= 10.10.10.3/32    swp54                                  0 65199 65102 ?
*=                  swp52                                  0 65199 65102 ?
* i                 peerlink.4094                 100      0 65199 65102 ?
*=                  swp53                                  0 65199 65102 ?
*>                  swp51                                  0 65199 65102 ?
...
```

To show a more detailed breakdown of a specific neighbor, run the NVUE `nv show vrf <vrf-id> router bgp neighbor <neighbor-id>` command or the vtysh `show bgp vrf default neighbors <neighbor-id> json` command.

```
cumulus@switch:~$ nv show vrf default router bgp neighbor swp51
                               operational               applied
-----------------------------  ------------------------  ------------------
password                                                 *
enforce-first-as               enabled                   enabled
passive-mode                   enabled                   enabled
nexthop-connected-check        enabled                   enabled
description                    test                      test
shutdown                       enabled                   enabled
graceful-shutdown              disabled                  disabled
bfd
  profile                      fabric-bfd-profile        fabric-bfd-profile
  status                       unknown
ttl-security
  state                        enabled                   enabled
  hops                         1                         1
local-as
  state                                                  enabled
  asn                          200                       200
  prepend                      disabled                  disabled
  replace                      enabled                   enabled
timers
  keepalive                    3                         10
  hold                         10                        10
  connection-retry             5                         5
  route-advertisement          5                         5
address-family
  ipv4-unicast
    state                                                enabled
    route-reflector-client                               disabled
    soft-reconfiguration       enabled                   enabled
    nexthop-setting            force                     force
    add-path-tx                all-paths                 all-paths
    attribute-mod
      aspath                   enabled                   enabled
      med                      enabled                   enabled
      nexthop                  enabled                   enabled
    aspath
      replace-peer-as          enabled                   enabled
      private-as               replace                   replace
      allow-my-asn
        state                  enabled                   enabled
        occurrences            3                         3
        route-map              v4-route-map              v4-route-map
    tx-prefix                  0
    rx-prefix                  0
    graceful-restart
      rx-eof-rib               off
      tx-eof-rib               off
    weight                     9                         9
    community-advertise
      regular                  enabled                   enabled
      extended                 enabled                   enabled
      large                    enabled                   enabled
    conditional-advertise
      state                    enabled                   enabled
      advertise-map            adv-map                   adv-map
      exist-map                ex-map                    ex-map
      non-exist-map            EXIST
      advertise-status         Advertise
    policy
      inbound
        route-map              v4-in-rmap                v4-in-rmap
        prefix-list            v4-in-pfx                 v4-in-pfx
        aspath-list            in-as-path                in-as-path
      outbound
        route-map              v4-out-rmap               v4-out-rmap
        unsuppress-map         v4-u-map                  v4-u-map
        prefix-list            v4-out-pfx                v4-out-pfx
        aspath-list            out-as-path               out-as-path
    default-route-origination
      state                    enabled                   enabled
      policy                   def-rt-policy             def-rt-policy
    prefix-limits
      inbound
        maximum                123                       123
        warning-threshold      80                        80
        warning-only           enabled                   enabled
  ipv6-unicast
    state                                                enabled
    route-reflector-client                               disabled
    soft-reconfiguration       enabled                   enabled
    nexthop-setting            self                      self
    add-path-tx                best-per-as               best-per-as
    attribute-mod
      aspath                   enabled                   enabled
      med                      enabled                   enabled
      nexthop                  enabled                   enabled
    aspath
      replace-peer-as          enabled                   enabled
      private-as               replace                   replace
      allow-my-asn
        state                  enabled                   enabled
        occurrences            3                         3
    tx-prefix                  0
    rx-prefix                  0
    graceful-restart
      rx-eof-rib               off
      tx-eof-rib               off
    weight                     9                         9
    community-advertise
      regular                  enabled                   enabled
      extended                 enabled                   enabled
      large                    enabled                   enabled
    conditional-advertise
      state                    enabled                   enabled
      advertise-map            adv-map                   adv-map
      exist-map                ex-map                    ex-map
      non-exist-map            EXIST
      advertise-status         Advertise
    policy
      inbound
        route-map              v6-in-rmap                v6-in-rmap
        prefix-list            v6-in-pfx                 v6-in-pfx
        aspath-list            in-as-path                in-as-path
      outbound
        route-map              v6-out-rmap               v6-out-rmap
        unsuppress-map         v6-u-map                  v6-u-map
        prefix-list            v6-out-pfx                v6-out-pfx
        aspath-list            out-as-path               out-as-path
    default-route-origination
      state                    enabled                   enabled
      policy                   def-rt-policy             def-rt-policy
    prefix-limits
      inbound
        maximum                123                       123
        warning-threshold      80                        80
        warning-only           enabled                   enabled
  l2vpn-evpn
    state                                                enabled
    route-reflector-client                               disabled
    soft-reconfiguration       enabled                   enabled
    nexthop-setting            self                      self
    add-path-tx                off                       off
    attribute-mod
      aspath                   enabled                   enabled
      med                      enabled                   enabled
      nexthop                  enabled                   enabled
    aspath
      replace-peer-as          disabled                  disabled
      private-as               none                      none
      allow-my-asn
        state                  enabled                   enabled
        occurrences            3                         3
    tx-prefix                  0
    rx-prefix                  0
    graceful-restart
      rx-eof-rib               off
      tx-eof-rib               off
    policy
      inbound
        route-map              evpn-in-rmap              evpn-in-rmap
      outbound
        route-map              evpn-out-rmap             evpn-out-rmap
    prefix-limits
      inbound
        maximum                123                       123
        warning-threshold      80                        80
        warning-only           enabled                   enabled
  ipv4-unreachability
    state                                                disabled
  ipv6-unreachability
    state                                                disabled
state                                                    enabled
type                           unnumbered                unnumbered
peer-group                     ISL                       ISL
remote-as                      65101                     auto
capabilities
  extended-nexthop                                       auto
graceful-restart
  remote-mode                  NotApplicable
  rx-restart-time              120
  mode                         auto                      auto
bgp-version                    4
remote-router-id               10.10.10.3
session-state                  idle
connection-type                shared-network
connections-established        1
connections-dropped            1
last-reset-time                0:02:15
last-reset-reason              Address family activated
last-reset-code                10
local-ip                       fe80::202:ff:fe00:21
remote-ip                      fe80::202:ff:fe00:b
local-port                     56344
remote-port                    179
nexthop
  ipv4                         10.10.10.101
  ipv6-global                  fe80::7c41:fff:fe93:b711
  ipv6-local                   fe80::7c41:fff:fe93:b711
message-stats
  input-queue                  0
  output-queue                 0
  rx-opens                     1
  tx-opens                     1
  rx-keepalives                48
  tx-keepalives                48
  rx-route-refreshes           1
  tx-route-refreshes           1
  tx-total                     61
  rx-total                     63                    0
```

```
cumulus@switch:mgmt:~$ sudo vtysh -c "show bgp vrf default neighbors swp1 json"
{
  "swp1":{
    "bgpNeighborAddr":"fe80::202:ff:fe00:b",
    "passive":true,
    "disableConnectedCheck":false,
    "gracefulShutdown":false,
    "enforceFirstAs":true,
    "capabilityExtendedNexthop":true,
    "remoteAs":65101,
    "localAs":200,
    "localAsNoPrepend":true,
    "localAsReplaceAs":true,
    "nbrExternalLink":true,
    "localRole":"undefined",
    "remoteRole":"undefined",
    "nbrDesc":"test",
    "hostname":"leaf-11",
    "peerGroup":"ISL",
    "adminShutDown":true,
    "bgpVersion":4,
    "remoteRouterId":"6.0.0.5",
    "localRouterId":"6.0.0.11",
    "bgpState":"Idle",
    "bgpTimerLastRead":1840000,
    "bgpTimerLastWrite":1838000,
    "bgpInUpdateElapsedTimeMsecs":2253000,
    "bgpTimerConfiguredHoldTimeMsecs":10000,
    "bgpTimerConfiguredKeepAliveIntervalMsecs":3000,
    "bgpTimerHoldTimeMsecs":10000,
    "bgpTimerKeepAliveIntervalMsecs":3000,
    "bgpTcpMssConfigured":0,
    "bgpTcpMssSynced":0,
    "extendedOptionalParametersLength":false,
    "bgpTimerConfiguredConditionalAdvertisementsSec":60,
    "bgpTimerUntilConditionalAdvertisementsSec":22,
    "gracefulRestartInfo":{
      "endOfRibSend":{
      },
      "endOfRibRecv":{
      },
      "localGrMode":"Helper*",
      "remoteGrMode":"NotApplicable",
      "rBit":false,
      "nBit":false,
      "timers":{
        "configuredRestartTimer":120,
        "configuredLlgrStaleTime":0,
        "receivedRestartTimer":120
      }
    },
    "messageStats":{
      "depthInq":0,
      "depthOutq":0,
      "opensSent":1,
      "opensRecv":1,
      "notificationsSent":1,
      "notificationsRecv":0,
      "updatesSent":10,
      "updatesRecv":13,
      "keepalivesSent":48,
      "keepalivesRecv":48,
      "routeRefreshSent":1,
      "routeRefreshRecv":1,
      "capabilitySent":0,
      "capabilityRecv":0,
      "totalSent":61,
      "totalRecv":63
    },
    "minBtwnAdvertisementRunsTimerMsecs":5000,
    "addressFamilyInfo":{
      "ipv4Unicast":{
        "peerGroupMember":"ISL",
        "weight":9,
        "inboundSoftConfigPermit":true,
        "privateAsNumsAllReplacedInUpdatesToNbr":true,
        "allowAsInCount":3,
        "allowAsInRouteMap":"v4-route-map",
        "addpathTxAllPaths":true,
        "overrideASNsInOutboundUpdates":"ifAspathEqualRemoteAs",
        "routerAlwaysNextHop":true,
        "forceRouterAlwaysNextHop":true,
        "unchangedAsPathPropogatedToNbr":true,
        "unchangedNextHopPropogatedToNbr":true,
        "unchangedMedPropogatedToNbr":true,
        "commAttriSentToNbr":"standardAndextendedAndlarge",
        "defaultRouteMap":"def-rt-policy",
        "defaultNotSent":true,
        "inboundPathPolicyConfig":true,
        "outboundPathPolicyConfig":true,
        "incomingUpdatePrefixFilterList":"v4-in-pfx",
        "outgoingUpdatePrefixFilterList":"v4-out-pfx",
        "incomingUpdateAsPathFilterList":"in-as-path",
        "outgoingUpdateAsPathFilterList":"out-as-path",
        "routeMapForIncomingAdvertisements":"v4-in-rmap",
        "routeMapForOutgoingAdvertisements":"v4-out-rmap",
        "selectiveUnsuppressRouteMap":"v4-u-map",
        "advertiseMap":{
          "condition":"EXIST",
          "conditionMap":"ex-map",
          "advertiseMap":"adv-map",
          "advertiseStatus":"Advertise"
        },
        "acceptedPrefixCounter":0,
        "prefixAllowedMax":123,
        "prefixAllowedMaxWarning":true,
        "prefixAllowedWarningThresh":80
      },
      "ipv6Unicast":{
        "peerGroupMember":"ISL",
        "weight":9,
        "inboundSoftConfigPermit":true,
        "privateAsNumsAllReplacedInUpdatesToNbr":true,
        "allowAsInCount":3,
        "addpathTxBestpathPerAS":true,
        "overrideASNsInOutboundUpdates":"ifAspathEqualRemoteAs",
        "routerAlwaysNextHop":true,
        "forceRouterAlwaysNextHop":false,
        "unchangedAsPathPropogatedToNbr":true,
        "unchangedNextHopPropogatedToNbr":true,
        "unchangedMedPropogatedToNbr":true,
        "commAttriSentToNbr":"standardAndextendedAndlarge",
        "defaultRouteMap":"def-rt-policy",
        "defaultNotSent":true,
        "inboundPathPolicyConfig":true,
        "outboundPathPolicyConfig":true,
        "incomingUpdatePrefixFilterList":"v6-in-pfx",
        "outgoingUpdatePrefixFilterList":"v6-out-pfx",
        "incomingUpdateAsPathFilterList":"in-as-path",
        "outgoingUpdateAsPathFilterList":"out-as-path",
        "routeMapForIncomingAdvertisements":"v6-in-rmap",
        "routeMapForOutgoingAdvertisements":"v6-out-rmap",
        "selectiveUnsuppressRouteMap":"v6-u-map",
        "advertiseMap":{
          "condition":"EXIST",
          "conditionMap":"ex-map",
          "advertiseMap":"adv-map",
          "advertiseStatus":"Advertise"
        },
        "acceptedPrefixCounter":0,
        "prefixAllowedMax":123,
        "prefixAllowedMaxWarning":true,
        "prefixAllowedWarningThresh":80
      },
      "l2VpnEvpn":{
        "peerGroupMember":"ISL",
        "inboundSoftConfigPermit":true,
        "allowAsInCount":3,
        "routerAlwaysNextHop":true,
        "forceRouterAlwaysNextHop":false,
        "unchangedAsPathPropogatedToNbr":true,
        "unchangedNextHopPropogatedToNbr":true,
        "unchangedMedPropogatedToNbr":true,
        "commAttriSentToNbr":"standardAndextendedAndlarge",
        "inboundPathPolicyConfig":true,
        "outboundPathPolicyConfig":true,
        "routeMapForIncomingAdvertisements":"evpn-in-rmap",
        "routeMapForOutgoingAdvertisements":"evpn-out-rmap",
        "acceptedPrefixCounter":0,
        "prefixAllowedMax":123,
        "prefixAllowedMaxWarning":true,
        "prefixAllowedWarningThresh":80
      }
    },
...
```

To show address-family information for a specific neighbor, run the `nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family` command:

```
cumulus@switch:mgmt:~$ nv show vrf default router bgp neighbor swp1 address-family
                             operational    applied
---------------------------  -------------  -------------
ipv4-unicast
  state                                     enabled
  route-reflector-client                    disabled
  soft-reconfiguration       enabled        enabled
  nexthop-setting            force          force
  add-path-tx                all-paths      all-paths
  attribute-mod
    aspath                   enabled        enabled
    med                      enabled        enabled
    nexthop                  enabled        enabled
  aspath
    replace-peer-as          enabled        enabled
    private-as               replace        replace
    allow-my-asn
      state                  enabled        enabled
      occurrences            3              3
      route-map              v4-route-map   v4-route-map
  tx-prefix                  0
  rx-prefix                  0
  graceful-restart
    rx-eof-rib               off
    tx-eof-rib               off
  weight                     9              9
  community-advertise
    regular                  enabled        enabled
    extended                 enabled        enabled
    large                    enabled        enabled
  conditional-advertise
    state                    enabled        enabled
    advertise-map            adv-map        adv-map
    exist-map                ex-map         ex-map
    non-exist-map            EXIST
    advertise-status         Advertise
  policy
    inbound
      route-map              v4-in-rmap     v4-in-rmap
      prefix-list            v4-in-pfx      v4-in-pfx
      aspath-list            in-as-path     in-as-path
    outbound
      route-map              v4-out-rmap    v4-out-rmap
      unsuppress-map         v4-u-map       v4-u-map
      prefix-list            v4-out-pfx     v4-out-pfx
      aspath-list            out-as-path    out-as-path
  default-route-origination
    state                    enabled        enabled
    policy                   def-rt-policy  def-rt-policy
  prefix-limits
    inbound
      maximum                123            123
      warning-threshold      80             80
      warning-only           enabled        enabled
ipv6-unicast
  state                                     enabled
  route-reflector-client                    disabled
  soft-reconfiguration       enabled        enabled
  nexthop-setting            self           self
  add-path-tx                best-per-as    best-per-as
  attribute-mod
    aspath                   enabled        enabled
    med                      enabled        enabled
    nexthop                  enabled        enabled
  aspath
    replace-peer-as          enabled        enabled
    private-as               replace        replace
    allow-my-asn
      state                  enabled        enabled
      occurrences            3              3
  tx-prefix                  0
  rx-prefix                  0
  graceful-restart
    rx-eof-rib               off
    tx-eof-rib               off
  weight                     9              9
  community-advertise
    regular                  enabled        enabled
    extended                 enabled        enabled
    large                    enabled        enabled
  conditional-advertise
    state                    enabled        enabled
    advertise-map            adv-map        adv-map
    exist-map                ex-map         ex-map
    non-exist-map            EXIST
    advertise-status         Advertise
  policy
    inbound
      route-map              v6-in-rmap     v6-in-rmap
      prefix-list            v6-in-pfx      v6-in-pfx
      aspath-list            in-as-path     in-as-path
    outbound
      route-map              v6-out-rmap    v6-out-rmap
      unsuppress-map         v6-u-map       v6-u-map
      prefix-list            v6-out-pfx     v6-out-pfx
      aspath-list            out-as-path    out-as-path
  default-route-origination
    state                    enabled        enabled
    policy                   def-rt-policy  def-rt-policy
  prefix-limits
    inbound
      maximum                123            123
      warning-threshold      80             80
      warning-only           enabled        enabled
l2vpn-evpn
  state                                     enabled
  route-reflector-client                    disabled
  soft-reconfiguration       enabled        enabled
  nexthop-setting            self           self
  add-path-tx                off            off
  attribute-mod
    aspath                   enabled        enabled
    med                      enabled        enabled
    nexthop                  enabled        enabled
  aspath
    replace-peer-as          disabled       disabled
    private-as               none           none
    allow-my-asn
      state                  enabled        enabled
      occurrences            3              3
  tx-prefix                  0
  rx-prefix                  0
  graceful-restart
    rx-eof-rib               off
    tx-eof-rib               off
  policy
    inbound
      route-map              evpn-in-rmap   evpn-in-rmap
    outbound
      route-map              evpn-out-rmap  evpn-out-rmap
  prefix-limits
    inbound
      maximum                123            123
      warning-threshold      80             80
      warning-only           enabled        enabled
ipv4-unreachability
  state                                     disabled
ipv6-unreachability
  state
```

- To show IPv4 address family information for a specific neighbor, run the `nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast` command. 
- To show IPv6 address family information for a specific neighbor, run the `nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast` command.
- To show EVPN address family information for a specific neighbor, run the `nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family l2vpn-evpn` command.

```
cumulus@switch:mgmt:~$ 
nv show vrf default router bgp neighbor swp1 address-family ipv4-unicast
                           operational    applied
-------------------------  -------------  -------------
state                                     enabled
route-reflector-client                    disabled
soft-reconfiguration       enabled        enabled
nexthop-setting            force          force
add-path-tx                all-paths      all-paths
attribute-mod
  aspath                   enabled        enabled
  med                      enabled        enabled
  nexthop                  enabled        enabled
aspath
  replace-peer-as          enabled        enabled
  private-as               replace        replace
  allow-my-asn
    state                  enabled        enabled
    occurrences            3              3
    route-map              v4-route-map   v4-route-map
tx-prefix                  0
rx-prefix                  0
graceful-restart
  rx-eof-rib               off
  tx-eof-rib               off
weight                     9              9
community-advertise
  regular                  enabled        enabled
  extended                 enabled        enabled
  large                    enabled        enabled
conditional-advertise
  state                    enabled        enabled
  advertise-map            adv-map        adv-map
  exist-map                ex-map         ex-map
  non-exist-map            EXIST
  advertise-status         Advertise
policy
  inbound
    route-map              v4-in-rmap     v4-in-rmap
    prefix-list            v4-in-pfx      v4-in-pfx
    aspath-list            in-as-path     in-as-path
  outbound
    route-map              v4-out-rmap    v4-out-rmap
    unsuppress-map         v4-u-map       v4-u-map
    prefix-list            v4-out-pfx     v4-out-pfx
    aspath-list            out-as-path    out-as-path
default-route-origination
  state                    enabled        enabled
  policy                   def-rt-policy  def-rt-policy
prefix-limits
  inbound
    maximum                123            123
    warning-threshold      80             80
    warning-only           enabled        enabled
```

To show a summary of the BGP configuration on the switch for a specific VRF, run the `nv show vrf <vrf-id> router bgp` command:

```
cumulus@switch:mgmt:~$ nv show vrf BLUE router bgp 
                                   operational  applied    
---------------------------------  -----------  ---------- 
state                                           enabled    
autonomous-system                  65101        65101      
router-id                          10.10.10.1   10.10.10.1 
rd                                              none       
address-family                                             
  ipv4-unicast                                             
    rib-filter                                  none       
    route-export                                           
      to-evpn                                              
        state                                   enabled    
        route-map                               none       
        default-route-origination  disabled     disabled   
      to-vrf                                               
        [list]                     none                    
      [route-target]               none                    
      rd                           none                    
    route-import                                           
      from-vrf                                             
        state                                   disabled   
        [list]                     none                    
      [route-target]               none                    
    admin-distance                                         
      external                     20           20         
      internal                     200          200        
    multipaths                                             
      ebgp                         64           64         
      ibgp                         64           64         
      compare-cluster-length       disabled     disabled   
    state                                       enabled    
    redistribute                                           
      static                                               
        state                      disabled     disabled   
      connected                                            
        state                      enabled      enabled    
        metric                     auto         auto       
        route-map                  none         none       
      kernel                                               
        state                      disabled     disabled   
      ospf                                                 
        state                      disabled     disabled   
    [network]                                              
    [aggregate-route]                                      
  ipv6-unicast                                             
    route-export                                           
      to-evpn                                              
        default-route-origination  disabled                
      to-vrf                                               
        [list]                     none                    
      [route-target]               none                    
      rd                           none                    
    route-import                                           
      from-vrf                                             
        [list]                     none                    
      [route-target]               none                    
    multipaths                                             
      compare-cluster-length       disabled                
    state                                       disabled   
    redistribute                                           
      static                                               
        state                      disabled                
      connected                                            
        state                      disabled                
      kernel                                               
        state                      disabled                
      ospf6                                                
        state                      disabled                
  l2vpn-evpn                                               
    state                                       disabled   
[neighbor]                                                 
[peer-group]                                               
path-selection                                             
  routerid-compare                 disabled     disabled   
  aspath                                                   
    compare-lengths                enabled      enabled    
    compare-confed                 disabled     disabled   
  med                                                      
    compare-always                 disabled     disabled   
    compare-deterministic          enabled      enabled    
    compare-confed                 disabled     disabled   
    missing-as-max                 disabled     disabled   
  multipath                                                
    aspath-ignore                  disabled     disabled   
    generate-asset                 disabled     disabled   
    bandwidth                      all-paths    all-paths  
route-reflection                                           
  state                                         disabled   
  reflect-between-clients          enabled                 
  outbound-policy                  disabled                
route-export                                               
  to-evpn                                                  
    [route-target]                              auto       
route-import                                               
  from-evpn                                                
    [route-target]                              auto       
timers                                                     
  keepalive                                     3          
  hold                                          9          
  connection-retry                              10         
  route-advertisement                           none       
  conditional-advertise                         60         
confederation                                              
  id                                            none       
  [member-as]                                              
dynamic-neighbor                                           
  [listen-range]                                           
  limit                                         100        
configured-neighbors               0                       
established-neighbors              0             
```

## Show BGP Peer Information

To show detailed information about all BGP neighbors, run the `nv show vrf <vrf-id> router bgp neighbor --view=detail -o json` command:

```
cumulus@leaf01:mgmt:~$ nv show vrf default router bgp neighbor --view=detail -o json
{
  "peerlink.4094": {
    "address-family": {
      "ipv4-unicast": {
        "aspath": {
          "allow-my-asn": {
            "state": "disabled"
          },
          "private-as": "none",
          "replace-peer-as": "disabled"
        },
        "attribute-mod": {
          "aspath": "disabled",
          "med": "disabled",
          "nexthop": "disabled"
        },
        "capabilities": {
          "rx-addpath": "on",
          "rx-graceful-restart": "on",
          "rx-mpbgp": "on",
          "rx-restart-f-bit": "off",
          "tx-addpath": "off",
          "tx-mpbgp": "on"
        },
        "community-advertise": {
          "extended": "enabled",
          "large": "enabled",
          "regular": "enabled"
        },
        "graceful-restart": {
          "rx-eof-rib": "on",
          "timers": {
            "stale-path": {
              "timer-sec": 360
            }
          },
          "tx-eof-rib": "on",
          "tx-eof-rib-sent-after-update": "off"
        },
        "prefix-limits": {
          "inbound": {
            "warning-only": "disabled"
          }
        },
        "rx-prefix": 12,
        "tx-prefix": 13,
        "update-group": 1
      },
      "l2vpn-evpn": {
        "aspath": {
          "allow-my-asn": {
            "state": "disabled"
          },
          "private-as": "none",
          "replace-peer-as": "disabled"
        },
        "attribute-mod": {
          "aspath": "disabled",
          "med": "disabled",
          "nexthop": "enabled"
        },
        "capabilities": {
          "rx-addpath": "on",
          "rx-graceful-restart": "on",
          "rx-mpbgp": "on",
          "rx-restart-f-bit": "off",
          "tx-addpath": "off",
          "tx-mpbgp": "on"
        },
        "graceful-restart": {
          "rx-eof-rib": "on",
          "timers": {
            "stale-path": {
              "timer-sec": 360
            }
          },
          "tx-eof-rib": "on",
          "tx-eof-rib-sent-after-update": "off"
        },
        "prefix-limits": {
          "inbound": {
            "warning-only": "disabled"
          }
        },
        "rx-prefix": 57,
        "tx-prefix": 81,
        "update-group": 2
      }
    },
    "bgp-version": 4,
    "capabilities": {
      "extended-nexthop": "enabled",
      "rx-asn32": "off",
      "rx-extended-nexthop": "off",
      "rx-graceful-restart": "on",
      "rx-restart-r-bit": "off",
      "rx-route-refresh": "on",
      "tx-asn32": "on",
      "tx-graceful-restart": "on",
      "tx-route-refresh": "on"
    },
    "connection-type": "shared-network",
    "connections-dropped": 1,
    "connections-established": 2,
    "ebgp-policy": {},
    "graceful-restart": {
      "mode": "auto",
      "remote-mode": "helper-only",
      "rx-restart-time": 120
    },
    "last-reset-code": 32,
    "last-reset-reason": "Waiting for peer OPEN",
    "last-reset-time": 46204000,
    "local-as": {
      "asn": 65101,
      "prepend": "enabled",
      "replace": "disabled"
    },
    "local-domain": "n/a",
    "local-hostname": "leaf01",
    "local-ip": "fe80::4ab0:2dff:fed4:bb2d",
    "local-port": 179,
    "message-stats": {
      "input-queue": 0,
      "output-queue": 0,
      "rx-keepalives": 28435,
      "rx-opens": 3,
      "rx-route-refreshes": 0,
      "rx-total": 28644,
      "tx-keepalives": 28436,
      "tx-opens": 4,
      "tx-route-refreshes": 0,
      "tx-total": 28657
...
```

To see a summary of the connection information for all BGP peers, such as the state (`established`, `idle`), uptime, number of messages received and sent, and the time the connections establish, run the `nv show vrf <vrf-id> router bgp neighbor` command.

```
cumulus@switch:~$ nv show vrf default router bgp neighbor

AS - Remote Autonomous System, Uptime - BGP session up time, ResetTime - Last
connection reset time, Afi-Safi - Address family, PfxSent - Transmitted prefix
counter, PfxRcvd - Recieved prefix counter

Neighbor       AS     State        Uptime    ResetTime  MsgRcvd  MsgSent  Afi-Safi      PfxSent  PfxRcvd
-------------  -----  -----------  --------  ---------  -------  -------  ------------  -------  -------
peerlink.4094  65102  established  12:53:26  12:53:31   28713    28726    ipv4-unicast  13       12     
                                                                          l2vpn-evpn    81       57     
swp51          65199  established  23:45:21  23:45:22   28703    28712    ipv4-unicast  13       9      
                                                                          l2vpn-evpn    81       57     
swp52          65199  established  12:53:27  12:53:28   28733    28739    ipv4-unicast  13       9      
                                                                          l2vpn-evpn    81       57     
swp53          65199  established  23:45:21  23:45:22   28702    28712    ipv4-unicast  13       9      
                                                                          l2vpn-evpn    81       57     
swp54          65199  established  12:53:25  12:53:26   28733    28738    ipv4-unicast  13       9      
                                                                          l2vpn-evpn    81       57
```

Run the `nv show vrf default router bgp neighbor -o json` command to show a summary of the connection information for all BGP neighbors in json format.

{{%notice note%}}
In Cumulus Linux 5.11 and earlier, the `nv show vrf default router bgp neighbor -o json` command output shows more detailed information about BGP peers. To show the more detailed BGP peer information in Cumulus Linux 5.12 and later, run the `nv show vrf <vrf-id> router bgp neighbor --view=detail -o json` command, shown above.
{{%/notice%}}

## Check BGP Timer Settings

To check BGP timers, such as the BGP keepalive interval, hold time, and advertisement interval, run the NVUE `nv show vrf <vrf-id> router bgp neighbor <neighbor> timers` command or the vtysh `show ip bgp neighbor <peer>` command. For example:

```
cumulus@leaf01:~$ nv show vrf default router bgp neighbor swp51 timers
                     operational  applied
-------------------  -----------  -------
keepalive            3            auto   
hold                 9            auto   
connection-retry     10           auto   
route-advertisement  none         auto
```

## Check BGP Redistribute Settings

To check BGP address family redistribute settings, such as the BGP redistribute protocol, route-map and metric, run the NVUE `nv show vrf <vrf-id> router bgp address-family ipv4-unicast redistribute` command or the `nv show vrf <vrf-id> router bgp address-family ipv6-unicast redistribute` command. You can also run the vtysh `show bgp vrf <vrf-id> ipv4 unicast redistribute json` or `show bgp vrf <vrf-id> ipv6 unicast redistribute json` command.

```
cumulus@leaf01:~$ nv show vrf default router bgp address-family ipv4-unicast redistribute
             operational  applied   pending 
-----------  -----------  --------  --------
static                                      
  state      disabled     disabled  disabled
connected                                   
  state      enabled      enabled   enabled 
  metric     auto         auto      auto    
  route-map  none         none      none    
kernel                                      
  state      disabled     disabled  disabled
ospf                                        
  state      disabled     disabled  disabled
```

```
cumulus@leaf01:~$ sudo vtysh
...
leaf01# show bgp vrf default ipv4 unicast redistribute json
{
  "redistribute":{
    "kernel":{
      "metric":3,
      "routeMap":"rmap3"
    },
    "connected":{
      "metric":2,
      "routeMap":"rmap2"
    },
    "static":{
      "metric":1,
      "routeMap":"rmap1"
    },
    "ospf":{
      "metric":4,
      "routeMap":"rmap4"
    }
  }
}
```

## BGP Update Groups

You can show information about update group events or information about a specific IPv4 or IPv6 update group.

To show information about update group events, run the vtysh `show bgp update-group` command or run these NVUE commands:
- `nv show vrf <vrf-id> router bgp address-family ipv4-unicast update-group` for IPv4
- `nv show vrf <vrf-id> router bgp address-family ipv6-unicast update-group` for IPv6

```
cumulus@leaf01:~$ nv show vrf default router bgp address-family ipv4-unicast update-group
RouteMap - Outbound route map, MinAdvInterval - Minimum route advertisement     
interval, CreationTime - Time when the update group was created, LocalAsChange -
LocalAs changes for inbound route, Flags - r - replace-as, x - no-prepend       

UpdateGrp  RouteMap  MinAdvInterval  CreationTime    LocalAsChange  Flags
---------  --------  --------------  --------------  -------------  -----
1                    0               0:59:50                
3                    0               0:59:50       
```

To show information about a specific update group, such as the number of peer refresh events, prune events, and packet queue length, run the vtysh `show bgp update-group <group-id>` command or run these NVUE commands:
- `nv show vrf <vrf-id> router bgp address-family ipv4-unicast update-group <group-id> -o json` for IPv4
- `nv show vrf <vrf-id> router bgp address-family ipv6-unicast update-group <group-id> -o json` for IPv6

```
cumulus@leaf01:~$ nv show vrf default router bgp address-family ipv4-unicast update-group 1 -o json
{
  "create-time": 85630,
  "min-route-advertisement-interval": 0,
  "sub-group": {
    "1": {
      "adjacency-count": 13,
      "coalesce-time": 1300,
      "counters": {
        "join-events": 8,
        "merge-check-events": 0,
        "merge-events": 3,
        "peer-refresh-events": 0,
        "prune-events": 3,
        "split-events": 0,
        "switch-events": 0
      },
      "create-time": 85630,
      "needs-refresh": "off",
      "neighbor": {
        "peerlink.4094": {},
        "swp51": {},
        "swp52": {},
        "swp53": {},
        "swp54": {}
      },
      "packet-counters": {
        "queue-hwm-len": 4,
        "queue-len": 0,
        "queue-total": 22,
        "total-enqueued": 22
      },
      "sub-group-id": 1,
      "version": 126
    }
  },
  "update-group-id": "1"
}
```

## Show BGP Route Information

You can run NVUE commands to show route statistics for a BGP neighbor, such as the number of routes, and information about advertised and received routes.

To show the routing table for IPv4 routes, run the `nv show vrf <vrf-id> router rib ipv4 route` command. To show the RIB table for IPv6 routes, run the `nv show vrf <vrf-id> router rib ipv6 route` command.

```
cumulus@leaf01:mgmt:~$ nv show vrf default router rib ipv4 route
                                                                                
Flags - * - selected, q - queued, o - offloaded, i - installed, S - fib-        
selected, x - failed                                                            
                                                                                
Route            Protocol   Distance  Uptime                NHGId  Metric  Flags
---------------  ---------  --------  --------------------  -----  ------  -----
10.1.10.0/24     connected  0         0:42:5                46     0       *Sio 
10.1.20.0/24     connected  0         0:42:5                47     0       *Sio 
10.1.30.0/24     connected  0         0:42:5                48     0       *Sio 
10.1.40.0/24     bgp        20        23:21:18              57     0       *Si  
10.1.50.0/24     bgp        20        0:42:54               57     0       *Si  
10.1.60.0/24     bgp        20        0:42:54               57     0       *Si  
10.10.10.1/32    connected  0         0:42:54               7      0       *Sio 
10.10.10.2/32    bgp        20        0:42:54               34     0       *Si  
10.10.10.3/32    bgp        20        0:42:5                57     0       *Si  
10.10.10.4/32    bgp        20        0:42:5                57     0       *Si  
10.10.10.101/32  bgp        20        23:26:25              50     0       *Si  
10.10.10.102/32  bgp        20        23:26:25              58     0       *Si
```

To show the routes in the local routing table, run the `nv show vrf <vrf-id> router bgp address-family ipv4-unicast route` command for IPv4 or the `nv show vrf <vrf-id> router bgp address-family ipv6-unicast route` for IPv6. You can also run the command with `-o json` to show the received routes in json format.

```
cumulus@leaf02:~$ nv show vrf default router bgp address-family ipv4-unicast route 
PathCount - Number of paths present for the prefix, MultipathCount - Number of  
paths that are part of the ECMP, DestFlags - * - bestpath-exists, w - fib-wait- 
for-install, s - fib-suppress, i - fib-installed, x - fib-install-failed        
                                                                                
Prefix           PathCount  MultipathCount  DestFlags
---------------  ---------  --------------  ---------
10.0.1.12/32     2          1               *        
10.0.1.34/32     5          4               *        
10.0.1.255/32    5          4               *        
10.10.10.1/32    1          1               *        
10.10.10.2/32    5          1               *        
10.10.10.3/32    5          4               *        
10.10.10.4/32    5          4               *        
10.10.10.63/32   5          4               *        
10.10.10.64/32   5          4               *        
10.10.10.101/32  2          1               *        
10.10.10.102/32  2          1               *        
10.10.10.103/32  2          1               *        
10.10.10.104/32  2          1               * 
```

To filter the routes by a specific neighbor (numbered or unnumbered), use the `--filter=”neighbor=<neighbor>"` option. Run the `nv show vrf <vrf-id> router bgp address-family ipv4-unicast route --filter=”neighbor=<neighbor>"` command for IPv4 or the `nv show vrf <vrf-id> router bgp address-family ipv6-unicast route --filter=”neighbor=<neighbor>"` for IPv6.

```
cumulus@leaf01:~$ nv show vrf default router bgp address-family ipv4-unicast route --filter="neighbor=swp51"

PathCount - Number of paths present for the prefix, MultipathCount - Number of
paths that are part of the ECMP, DestFlags - * - bestpath-exists, w - fib-wait-
for-install, s - fib-suppress, i - fib-installed, x - fib-install-failed

Prefix           PathCount  MultipathCount  DestFlags
---------------  ---------  --------------  ---------
10.0.1.34/32     1          1                        
10.0.1.255/32    1          1               *        
10.10.10.2/32    1          0                        
10.10.10.3/32    1          1                        
10.10.10.4/32    1          1                        
10.10.10.63/32   1          1               *        
10.10.10.64/32   1          1               *        
10.10.10.101/32  1          1               *
```

To show information about a specific route in the local routing table, run the `nv show vrf <vrf-id> router bgp address-family ipv4-unicast route <route>` for IPv4 or `nv show vrf <vrf-id> router bgp address-family ipv6-unicast route <route>` for IPv6.

The above IPv4 and IPv6 command shows the local routing table route information in brief format to improve performance for high scale environments. You can also run the command with `-o json` to show the received routes in json format.

```
cumulus@leaf01:~$ nv show vrf default router bgp address-family ipv4-unicast route 10.10.10.64/32
                 operational
---------------  -----------
path-count       5          
multipath-count  4          

path
=======

    Origin - Route origin, Local - Locally originated route, Sourced - Sourced
    route, Weight - Route weight, Metric - Route metric, LocalPref - Route local
    preference, PathFrom - Route path origin, LastUpdate - Route last update,
    NexthopCnt - Number of nexthops, Flags - = - multipath, * - bestpath, v - valid,
    s - suppressed, R - removed, S - stale

    Path  Origin      Local  Sourced  Weight  Metric  LocalPref  PathFrom  LastUpdate  NexthopCnt  Flags
    ----  ----------  -----  -------  ------  ------  ---------  --------  ----------  ----------  -----
    1     incomplete                                             external  23:48:16    2           =*v  
    2     incomplete                                             external  12:56:31    2           =v   
    3     incomplete                                             external  23:48:16    2           =v   
    4     incomplete                                             external  12:56:29    2           =v   
    5     incomplete                                             external  12:56:31    2           *v   

advertised-to
================
    Neighbor       hostname
    -------------  --------
    peerlink.4094  leaf02  
    swp51          spine01 
    swp52          spine02 
    swp53          spine03 
    swp54          spine04
```

To show the route count, run the `nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast route-counters` command for IPv4 or the `nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast route-counters` for IPv6.

```
cumulus@leaf01:~$ nv show vrf default router bgp neighbor swp51 address-family ipv4-unicast route-counters
                operational
--------------  -----------
route-count     8          
adj-rib-in      0          
damped          0          
removed         0          
history         0          
stale           0          
valid           8          
all-rib         8          
routes-counted  8          
best-routes     7          
usable          8 
```

To show all advertised routes, run the `nv show vrf <vrf-id> router bgp neighbor <neighbor> address-family ipv4-unicast advertised-routes` command for IPv4 or the `nv show vrf <vrf-id> router bgp neighbor <neighbor> address-family ipv6-unicast advertised-routes` for IPv6.

The above IPv4 and IPv6 command shows advertised routes in brief format to improve performance for high scale environments. You can also run the command with `-o json` to show the received routes in json format.

```
cumulus@leaf01:~$ nv show vrf default router bgp neighbor swp51 address-family ipv4-unicast advertised-routes 
PathCount - Number of paths present for the prefix, MultipathCount - Number of  
paths that are part of the ECMP                                                 
                                                                                
IPv4 Prefix      PathCount  MultipathCount  DestFlags      
---------------  ---------  --------------  ---------------
10.1.10.0/24     3          1               bestpath-exists
10.1.20.0/24     3          1               bestpath-exists
10.1.30.0/24     3          1               bestpath-exists
10.1.40.0/24     3          2               bestpath-exists
10.1.50.0/24     3          2               bestpath-exists
10.1.60.0/24     3          2               bestpath-exists
10.10.10.1/32    2          1               bestpath-exists
10.10.10.2/32    3          1               bestpath-exists
10.10.10.3/32    3          2               bestpath-exists
10.10.10.4/32    3          2               bestpath-exists
10.10.10.101/32  2          1               bestpath-exists
10.10.10.102/32  2          1               bestpath-exists
```

To show information about a specific advertised route, run the`nv show <vrf-id> default router bgp neighbor <neighbor> address-family ipv4-unicast advertised-routes <route>` for IPv4 or `nv show <vrf-id> default router bgp neighbor <neighbor> address-family ipv6-unicast advertised-routes <route>` for IPv6.

```
cumulus@leaf01:~$ nv show vrf default router bgp neighbor swp51 address-family ipv4-unicast advertised-route 10.10.10.1/32
                 operational
---------------  -----------
path-count       2          
multipath-count  1
path
====================
                                                                                
    Origin - Route origin, Local - Locally originated route, Sourced - Sourced      
    route, Weight - Route weight, Metric - Route metric, LocalPref - Route local    
    preference, PathFrom - Route path origin, LastUpdate - Route last update,       
    NexthopCnt - Number of nexthops, Flags - = - multipath, * - bestpath, v - valid,
    s - suppressed, R - removed, S - stale                                          
                                                                                
    Path  Origin      Local  Sourced  Weight  Metric  LocalPref  PathFrom  LastUpdate            NexthopCnt  Flags
    ----  ----------  -----  -------  ------  ------  ---------  --------  --------------------  ----------  -----
    1     IGP         on     on       32768   0                            23:50:58              1           *v   
    2     incomplete         on       32768   0                            23:50:58              1           v 
...
```

To show all the received routes, run the `nv show vrf <vrf-id> router bgp neighbor <neighbor> address-family ipv4-unicast received-routes` command for IPv4 or `nv show vrf <vrf-id> router bgp neighbor <neighbor> address-family ipv6-unicast received-routes` command for IPv6. These commands show received routes in brief format to improve performance for high scale environments. You can also run the command with `--view=detail` to see more detailed information or with `-o json` to show the received routes in json format.

To show information about a specific received route, run the `nv show vrf <vrf-id> router bgp neighbor <neighbor> address-family ipv4-unicast received-routes <route> -o json` for IPv4 or `nv show vrf <vrf-id> router bgp neighbor <neighbor> address-family ipv6-unicast received-routes <route> -o json` for IPv6.

## Show Next Hop Information

To show a summary of all the BGP IPv4 or IPv6 next hops, run the `nv show vrf <vrf-id> router bgp nexthop ipv4` or `nv show vrf <vrf-id> router bgp nexthop ipv6` command. The output shows the IGP metric, the number of paths pointing to a next hop, and the address or interface used to reach a next hop.

```
cumulus@leaf01:mgmt:~$ nv show vrf default router bgp nexthop ipv4
Nexthops
===========

    PathCnt - Number of paths pointing to this Nexthop, ResolvedVia - Resolved via
    address or interface, Interface - Resolved via interface

    Address      IGPMetric  Valid  PathCnt  ResolvedVia                Interface    
    -----------  ---------  -----  -------  -------------------------  -------------
    10.0.1.34    0          yes    210      fe80::4ab0:2dff:fe1e:ac31  swp52        
                                                                       swp54        
                                                                       swp53        
                                                                       swp51        
    10.10.10.2   0          yes    15       fe80::4ab0:2dff:fe46:7968  peerlink.4094
    10.10.10.3   0          yes    15       fe80::4ab0:2dff:fe1e:ac31  swp52        
                                                                       swp54        
                                                                       swp53        
                                                                       swp51        
    10.10.10.4   0          yes    15       fe80::4ab0:2dff:fe1e:ac31  swp52        
                                                                       swp54        
                                                                       swp53        
                                                                       swp51        
    10.10.10.63  0          yes    15       fe80::4ab0:2dff:fe1e:ac31  swp52        
                                                                       swp54        
                                                                       swp53        
                                                                       swp51        
    10.10.10.64  0          yes    15       fe80::4ab0:2dff:fe1e:ac31  swp52        
                                                                       swp54        
                                                                       swp53        
                                                                       swp51    
```

To show information about a specific next hop, run the vtysh NVUE `nv show vrf <vrf-id> router bgp nexthop ipv4 ip-address <ip-address>` command for IPv4 or `nv show vrf <vrf-id> router bgp nexthop ipv6 ip-address <ip-address>` for IPv6. You can also run the vtysh `show bgp vrf default nexthop <ip-address>` command.

```
cumulus@leaf01:mgmt:~$ nv show vrf default router bgp nexthop ipv4 ip-address 10.10.10.2
                  operational              
----------------  -------------------------
valid             yes                      
complete          on                       
igp-metric        0                        
path-count        15                       
last-update-time  13:00:52    
[resolved-via]    fe80::4ab0:2dff:fee8:57ba
```

To show through which address and interface BGP resolves a specific next hop, run the `nv show vrf <vrf-id> router bgp nexthop ipv4 ip-address <ip-address-id> resolved-via` command for IPv4 or the `nv show vrf <vrf-id> router bgp nexthop ipv6 ip-address <ip-address-id> resolved-via` command for IPv6.

```
cumulus@leaf01:~$ nv show vrf default router bgp nexthop ipv4 ip-address 10.10.10.2 resolved-via
Nexthop                    interface
-------------------------  ---------
fe80::4ab0:2dff:fe20:ac25  swp51    
fe80::4ab0:2dff:fe93:d92d  swp52
```

## Check BGP Path Selection Settings

To check BGP path selection for a specific VRF, such as the aspath, med and multi-path, run the NVUE `nv show vrf <vrf-id> router bgp path-selection` command or the vtysh `show bgp vrf <vrf-id> bestpath json` command:

```
cumulus@leaf01:~$ nv show vrf default router bgp path-selection
                         operational  applied   
-----------------------  -----------  --------- 
routerid-compare         disabled     disabled  
aspath                                          
  compare-lengths        enabled      enabled   
  compare-confed         disabled     disabled  
med                                             
  compare-always         disabled     disabled  
  compare-deterministic  enabled      enabled   
  compare-confed         disabled     disabled  
  missing-as-max         disabled     disabled  
multipath                                       
  aspath-ignore          disabled     disabled  
  generate-asset         disabled     disabled  
  bandwidth              all-paths    all-paths 
```

```
cumulus@leaf01:~$ sudo vtysh
...
leaf01# show bgp vrf default bestpath json
{
  "default":{
    "bestPath":{
      "asPathIgnore":false,
      "asPathConfed":false,
      "asPathMultiPathRelaxEnabled":false,
      "peerTypeRelax":false,
      "compareRouterId":false,
      "medConfed":false,
      "medMissingASWorst":false,
      "linkBandwidth":"ecmp(default)",
      "alwaysCompareMed":false,
      "deterministicMed":true
    }
  }
}
```

## Check BGP local-as and aspath Settings

To check BGP local-as and aspath for a specific neighbour, run the NVUE `nv show vrf <vrf-id> router bgp neighbor <neighbour>  address-family <afi> aspath` command or the vtysh `show bgp vrf <vrf-id> neighbors <neighbor> json` command:

```
cumulus@leaf01:~$ nv show vrf default router bgp neighbor swp51 local-as
         operational  applied   pending
-------  -----------  -------   -------
state                 disabled  disabled    
asn      65101                        
prepend  enabled                           
replace  disabled 
```

```
``
cumulus@leaf01:~$ nv show vrf default router bgp neighbor swp51 address-family ipv4-unicast aspath
                 operational  applied  
---------------  -----------  -------- 
replace-peer-as  disabled     disabled 
private-as       none         none     
allow-my-asn                           
  state          disabled     disabled 
```

```
cumulus@leaf01:~$ sudo vtysh
...
leaf01# show bgp vrf default neighbors swp51 json
{
  "swp51":{
    "bgpNeighborAddr":"fe80::4ab0:2dff:fe51:4a5e",
    "remoteAs":65199,
    "localAs":65101,
    "nbrExternalLink":true,
    "localRole":"undefined",
    "remoteRole":"undefined",
    "hostname":"spine01",
    "peerGroup":"underlay",
    "bgpVersion":4,
    "remoteRouterId":"10.10.10.101",
    "localRouterId":"10.10.10.1",
    "bgpState":"Established",
    "bgpTimerUpMsec":104603000,
    "bgpTimerUpString":"1d05h03m",
    "bgpTimerUpEstablishedEpoch":1751974398,
    "bgpTimerLastRead":2000,
    "bgpTimerLastWrite":2000,
    "bgpInUpdateElapsedTimeMsecs":75141000,
    "bgpTimerConfiguredHoldTimeMsecs":9000,
    "bgpTimerConfiguredKeepAliveIntervalMsecs":3000,
    "bgpTimerHoldTimeMsecs":9000,
    "bgpTimerKeepAliveIntervalMsecs":3000,
    "bgpTcpMssConfigured":0,
    "bgpTcpMssSynced":9144,
    "extendedOptionalParametersLength":false,
    "bgpTimerConfiguredConditionalAdvertisementsSec":60,
    "neighborCapabilities":{
      "4byteAs":"advertisedAndReceived",
      "extendedMessage":"advertisedAndReceived",
      "addPath":{
        "ipv4Unicast":{
          "rxAdvertisedAndReceived":true
        },
        "l2VpnEvpn":{
          "rxAdvertisedAndReceived":true
        }
      },
      "extendedNexthop":"advertisedAndReceived",
      "extendedNexthopFamililesByPeer":{
        "ipv4Unicast":"recieved"
      },
      "longLivedGracefulRestart":"advertisedAndReceived",
      "longLivedGracefulRestartByPeer":{
        "ipv4Unicast":"received"
      },
      "routeRefresh":"advertisedAndReceived",
      "enhancedRouteRefresh":"advertisedAndReceived",
      "multiprotocolExtensions":{
        "ipv4Unicast":{
          "advertisedAndReceived":true
        },
        "l2VpnEvpn":{
          "advertisedAndReceived":true
        }
...
```

## Show DC Prefix Independent Convergence Information

When you enable {{<link url="Optional-BGP-Configuration/#bgp-dc-prefix-independent-convergence" text="BGP DC Prefix Independent Convergence (BGP DC PIC)">}}, you can use the following commands to show information about route-origin extended community (SOO) routes and SOO peer bit index mapping for the routes.

{{< tabs "1585 ">}}
{{< tab "NVUE Commands ">}}

To show information about all route-origin extended community (SOO) routes, run the `nv show <vrf-id> default router bgp address-family <address-family> soo-route` command:

```
cumulus@spine01:~$ nv show vrf default router bgp address-family ipv4-unicast soo-route 

PathCnt - Number of paths for this SoO., RouteCnt - Number of routes with this
SoO, SoONhgID - Nexthop group id used by this SoO, SoORouteFlag - Indicates
Site-of-Origin route flag - I - Installed, NhgRouteCnt - Number of routes using
SoO NHG, NhgFlag - V - valid, Ip - install-pending, Dp - delete-pending

SoORouteID  PathCnt  RouteCnt  SoONhgID  SoORouteFlag  NhgRouteCnt  NhgFlag
----------  -------  --------  --------  ------------  -----------  -------
10.10.10.1  1        1         70328885  I             1            V  
```

To show information about a specific SOO route, run the `nv show <vrf-id> default router bgp address-family <address-family> soo-route` command:

```
cumulus@spine01:~$ nv show vrf default router bgp address-family ipv4-unicast soo-route 10.10.10.1
                          operational              
------------------------  -------------------------
num-paths                 1                        
nexthop-group-id          70328885                 
num-routes-with-soo       1                        
num-routes-using-soo-nhg  1                        
soo-route-flag            I                        
nhg-flags-string          V                        
nhg-flags                                          
  nhg-valid               yes                      
  nhg-install-pending     no                       
  nhg-delete-pending      no                       
[peer-index]              fe80::4ab0:2dff:fe3a:a928
bit-map                                            
  selected-path-bitmap     1                       
  installed-path-bitmap    1                       
[route-with-soo]          10.0.1.12/32
```

To show peer-bit index mapping information about a specific SOO route, run the `nv show <vrf-id> default router bgp address-family <address-family> soo-route <prefix>` command:

```
cumulus@spine01:~$ nv show vrf default router bgp address-family ipv4-unicast soo-route 6.0.0.9
                          operational
------------------------  -------------------
num-paths                 6
nexthop-group-id          73545797
num-routes-with-soo       13
num-routes-using-soo-nhg  13
soo-route-flag            I
nhg-flags-string          V
nhg-flags
  nhg-valid               yes
  nhg-install-pending     no
  nhg-delete-pending      no
[peer-index]              fe80::202:ff:fe11:1
[peer-index]              fe80::202:ff:fe22:2
bit-map
  selected-path-bitmap     1 2 3 4 5 6
  installed-path-bitmap    1 2 3 4 5 6
[route-with-soo]          21.5.0.0/16
[route-with-soo]          21.5.0.0/24
[route-with-soo]          21.5.20.0/24
[route-with-soo]          21.5.21.0/24
[route-with-soo]          21.5.22.0/24
[route-with-soo]          21.5.23.0/24
[route-with-soo]          21.5.24.0/24
[route-with-soo]          21.5.25.0/24
[route-with-soo]          21.5.26.0/24
[route-with-soo]          21.5.27.0/24
[route-with-soo]          21.5.28.0/24
[route-with-soo]          21.5.29.0/24
[route-with-soo]          144.144.144.1/32

peer-bit
===========

    PeerIP - Peer IP address, SooPeerBitIndex - Indicates Site-of-Origin peer bit
    index mapping

    Peer  PeerIP               SooPeerBitIndex
    ----  -------------------  ---------------
    swp2  fe80::202:ff:fe11:1  1
    swp3  fe80::202:ff:fe11:1  2
    swp4  fe80::202:ff:fe11:1  3
    swp5  fe80::202:ff:fe22:2  4
    swp6  fe80::202:ff:fe22:2  5
    swp7  fe80::202:ff:fe22:2  6
```

To show the SOO peer bit mapping for an SOO route, run the `nv show <vrf-id> default router bgp address-family <address-family> soo-route <prefix> peer-bit` command. To show the information in json format, run the `nv show <vrf-id> default router bgp address-family <address-family> soo-route <prefix> peer-bit -o json` command.

```
cumulus@spine01:~$ nv show vrf default router bgp address-family ipv4-unicast soo-route 6.0.0.9 peer-bit
PeerIP - Peer IP address, SooPeerBitIndex - Indicates Site-of-Origin peer bit
index mapping

Peer  PeerIP               SooPeerBitIndex
----  -------------------  ---------------
swp2  fe80::202:ff:fe11:1  1
swp3  fe80::202:ff:fe11:1  2
swp4  fe80::202:ff:fe11:1  3
swp5  fe80::202:ff:fe22:2  4
swp6  fe80::202:ff:fe22:2  5
swp7  fe80::202:ff:fe22:2  6
```

```
cumulus@spine01:~$ nv show vrf default router bgp address-family ipv4-unicast soo-route 6.0.0.9 peer-bit -o json
{
  "swp2": {
    "bit-index": 1,
    "peer-ip": "fe80::202:ff:fe11:1"
  },
  "swp3": {
    "bit-index": 2,
    "peer-ip": "fe80::202:ff:fe11:1"
  },
  "swp4": {
    "bit-index": 3,
    "peer-ip": "fe80::202:ff:fe11:1"
  },
  "swp5": {
    "bit-index": 4,
    "peer-ip": "fe80::202:ff:fe22:2"
  },
  "swp6": {
    "bit-index": 5,
    "peer-ip": "fe80::202:ff:fe22:2"
  },
  "swp7": {
    "bit-index": 6,
    "peer-ip": "fe80::202:ff:fe22:2"
  }
}
```

To show the SOO peer bit index mapping for an SOO route, run the `nv show <vrf-id> default router bgp address-family <address-family> soo-route <prefix> peer-index` command:

```
cumulus@spine01:~$ nv show vrf default router bgp address-family ipv4-unicast soo-route 10.10.10.1 peer-index
SooPeerBitIndex - Indicates Site-of-Origin peer bit index mapping

IPAddress                  SooPeerBitIndex
-------------------------  ---------------
fe80::4ab0:2dff:fe3a:a928  1
```

To show if a specific route uses BGP DC PIC, run the `nv show <vrf-id> default router bgp address-family <address-family> soo-route <prefix> route-with-soo` command:

```
cumulus@spine01:~$ nv show vrf default router bgp address-family ipv4-unicast soo-route 10.10.10.1 route-with-soo 
UseSooNhg - Indicates this route-with-soo uses SooNhg, SelectedPathBitmap -
Details of Site-of-Origin selected path bitmap

Prefix        UseSooNhg  SelectedPathBitmap
------------  ---------  ------------------
10.0.1.12/32  yes         1
```

{{< /tab >}}
{{< tab "vtysh Commands ">}}

To show information about SOO routes in brief format, run the `show bgp <address-family> unicast soo route` command:

```
cumulus@spine01:~$ sudo vtysh
...
leaf01# show bgp ipv4 unicast soo route
BGP: VRF default

PathCnt - Number of paths for this SoORouteCnt - Number of routes with this
SoO, SoONhgID - Nexthop group id used by this SoO
SoORouteFlag - Indicates Site-of-Origin route flag: I - InstalledNhgRouteCnt - Number of routes using
SoO NHG, NhgFlag - V - valid, Ip - install-pending, Dp - delete-pending

SoORouteID              PathCnt  RouteCnt  SoONhgID  SoORouteFlag  NhgRouteCnt  NhgFlag
----------------------  -------  --------  --------  ------------  -----------  -------
10.10.10.1                 6        1         70328887  I             1            V
```

To show detailed information about SOO routes, run the `show bgp <address-family> unicast soo route detail` command:

```
cumulus@spine01:~$ sudo vtysh
...
leaf01# show bgp ipv4 unicast soo route detail
BGP: VRF default

SoO: 10.10.10.1
  NHG:
    NHG ID: 70328887
    NHG flags: Valid, Installed
  SoO route:
    Number of paths: 1
    Number of Routes with SoO: 1
    Number of Routes with SoO using SoO NHG: 1
    SoO route flags: Installed
  Nexthop cache:
      fe80::4ab0:2dff:feec:f8e/128 NH ifidx: 3 type: 5 flags: 5 lbw: 0
  Peer BitIndex Mappings:
    fe80::4ab0:2dff:feec:f8e: 1
  Bitmaps:
    Selected path info bitmap  bits set: 1
    Installed path info bitmap bits set: 1
  Route with SoO:
      10.0.1.12/32 uses SoO NHG Selected path info bitmap bits set: 1
SoO: 10.10.10.3
  NHG:
    NHG ID: 70328889
    NHG flags: Valid, Installed
  SoO route:
    Number of paths: 1
    Number of Routes with SoO: 1
    Number of Routes with SoO using SoO NHG: 1
    SoO route flags: Installed
  Nexthop cache:
      fe80::4ab0:2dff:fef2:6bc5/128 NH ifidx: 5 type: 5 flags: 5 lbw: 0
  Peer BitIndex Mappings:
    fe80::4ab0:2dff:fef2:6bc5: 3
  Bitmaps:
    Selected path info bitmap  bits set: 3
    Installed path info bitmap bits set: 3
  Route with SoO:
      10.0.1.34/32 uses SoO NHG Selected path info bitmap bits set: 3
SoO: 10.10.10.2
  NHG:
    NHG ID: 70328888
    NHG flags: Valid, Installed
  SoO route:
    Number of paths: 1
    Number of Routes with SoO: 1
    Number of Routes with SoO using SoO NHG: 0
    SoO route flags: Installed
  Nexthop cache:
      fe80::4ab0:2dff:fe5d:6456/128 NH ifidx: 4 type: 5 flags: 5 lbw: 0
  Peer BitIndex Mappings:
    fe80::4ab0:2dff:fe5d:6456: 2
  Bitmaps:
    Selected path info bitmap  bits set: 2
    Installed path info bitmap bits set: 2
  Route with SoO:
      10.0.1.12/32 Selected path info bitmap bits set: 2
```

To show information about a specific SOO route, run the `show bgp <address-family> unicast soo route <prefix>` command:

```
cumulus@spine01:~$ sudo vtysh
...
spine01# show bgp ipv4 unicast soo route 10.10.10.3
BGP: VRF default

SoO: 10.10.10.3
  NHG:
    NHG ID: 70328889
    NHG flags: Valid, Installed
  SoO route:
    Number of paths: 1
    Number of Routes with SoO: 1
    Number of Routes with SoO using SoO NHG: 1
    SoO route flags: Installed
  Nexthop cache:
      fe80::4ab0:2dff:fef2:6bc5/128 NH ifidx: 5 type: 5 flags: 5 lbw: 0
  Peer BitIndex Mappings:
    fe80::4ab0:2dff:fef2:6bc5: 3
  Bitmaps:
    Selected path info bitmap  bits set: 3
    Installed path info bitmap bits set: 3
  Route with SoO:
      10.0.1.34/32 uses SoO NHG Selected path info bitmap bits set: 3
```

You can show the above commands in json format. For example:

```
cumulus@spine01:~$ sudo vtysh
...
spine01# show bgp ipv4 unicast soo route json
{
  "default":[
    {
      "SoORoute":"10.10.10.1",
      "numPaths":6,
      "numRoutesWithSoO":13,
      "nexthopgroupId":70328887,
      "SoORouteFlag":"Installed",
      "numRoutesWithSoOUsingSoONHG":13,
      "nhgValid":true,
      "nhgInstallPending":false,
      "nhgDeletePending":false
    }
  ]
}
```

```
cumulus@spine01:~$ sudo vtysh
...
spine01# show bgp ipv4 unicast soo route detail json 
{
  "default":[
    {
      "SoORoute":"10.10.10.1",
      "numPaths":1,
      "nexthopgroupId":70328887,
      "numRoutesWithSoO":1,
      "numRoutesWithSoOUsingSoONHG":1,
      "nhgValid":true,
      "nhgInstallPending":false,
      "nhgDeletePending":false,
      "SoORouteFlag":"Installed",
      "nextHopCache":[
        {
          "prefix":"fe80::4ab0:2dff:feec:f8e/128",
          "ifIndex":3,
          "type":5,
          "flags":5,
          "lbw":0
        }
      ],
      "peerBitIndexMapping":[
        {
          "peerIp":"fe80::4ab0:2dff:feec:f8e",
          "bitIndex":1
        }
      ],
      "bitMaps":[
        {
          "selectedPathBitmap":" 1",
          "installedPathBitmap":" 1"
        }
      ],
      "routeWithSoO":[
        {
          "prefix":"10.0.1.12/32",
          "usesSoONhg":true,
          "selectedPathBitmap":" 1"
        }
      ]
    },
    {
      "SoORoute":"10.10.10.3",
      "numPaths":1,
      "nexthopgroupId":70328889,
      "numRoutesWithSoO":1,
      "numRoutesWithSoOUsingSoONHG":1,
      "nhgValid":true,
      "nhgInstallPending":false,
      "nhgDeletePending":false,
      "SoORouteFlag":"Installed",
      "nextHopCache":[
        {
          "prefix":"fe80::4ab0:2dff:fef2:6bc5/128",
          "ifIndex":5,
          "type":5,
          "flags":5,
          "lbw":0
        }
      ],
      "peerBitIndexMapping":[
        {
          "peerIp":"fe80::4ab0:2dff:fef2:6bc5",
          "bitIndex":3
        }
      ],
      "bitMaps":[
        {
          "selectedPathBitmap":" 3",
          "installedPathBitmap":" 3"
        }
      ],
      "routeWithSoO":[
        {
          "prefix":"10.0.1.34/32",
          "usesSoONhg":true,
          "selectedPathBitmap":" 3"
        }
      ]
    },
    {
      "SoORoute":"10.10.10.2",
      "numPaths":1,
      "nexthopgroupId":70328888,
      "numRoutesWithSoO":1,
      "numRoutesWithSoOUsingSoONHG":0,
      "nhgValid":true,
      "nhgInstallPending":false,
      "nhgDeletePending":false,
      "SoORouteFlag":"Installed",
      "nextHopCache":[
        {
          "prefix":"fe80::4ab0:2dff:fe5d:6456/128",
          "ifIndex":4,
          "type":5,
          "flags":5,
          "lbw":0
        }
      ],
      "peerBitIndexMapping":[
        {
          "peerIp":"fe80::4ab0:2dff:fe5d:6456",
          "bitIndex":2
        }
      ],
      "bitMaps":[
        {
          "selectedPathBitmap":" 2",
          "installedPathBitmap":" 2"
        }
      ],
      "routeWithSoO":[
        {
          "prefix":"10.0.1.12/32",
          "usesSoONhg":false,
          "selectedPathBitmap":" 2"
        }
      ]
    }
  ]
}
```

{{< /tab >}}
{{< /tabs >}}

## Check BGP BFD Settings

To show the BFD settings for a specific BGP neighbor, including the profile and status information, run the NVUE `nv show vrf <vrf-id> router bgp neighbor <neighbor> bfd` command or the vtysh `show bgp vrf <vrf-id> neighbors <neighbor>` command:

```
cumulus@leaf01:~$ nv show vrf default router bgp neighbor swp51 bfd
         operational         applied
-------  ------------------  ------------------
profile  fabric-bfd-profile  fabric-bfd-profile
status   up
```

```
cumulus@leaf01:~$ sudo vtysh
leaf01# show bgp vrf default neighbors swp51
BGP neighbor is swp51, remote AS 10, local AS 20, external link
  Local Role: undefined
  Remote Role: undefined
Hostname: top0
  BGP version 4, remote router ID 10.1.1.1, local router ID 20.1.1.1
  BGP state = Established, up for 00:01:18
  Last read 00:00:03, Last write 00:00:03
  Hold time is 10 seconds, keepalive interval is 3 seconds
  Configured hold time is 10 seconds, keepalive interval is 3 seconds
  Configured tcp-mss is 0, synced tcp-mss is 9164
  Configured conditional advertisements interval is 60 seconds
  Neighbor capabilities:
    4 Byte AS: advertised and received
    Extended Message: advertised and received
    AddPath:
      IPv4 Unicast: RX advertised and received
    Long-lived Graceful Restart: advertised and received
      Address families by peer:
    Route refresh: advertised and received
    Enhanced Route Refresh: advertised and received
    Address Family IPv4 Unicast: advertised and received
    Hostname Capability: advertised (name: top1,domain name: n/a) received (name: top0,domain name: n/a)
    Version Capability: advertised software version (FRRouting/10.0.3) received software version (FRRouting/10.0.3)
    Graceful Restart Capability: advertised and received
      Remote Restart timer is 120 seconds
      Address families by peer:
            Graceful Restart Capability: advertised and received
      Remote Restart timer is 120 seconds
      Address families by peer:
        none
  Graceful restart information:
    End-of-RIB send: IPv4 Unicast
    End-of-RIB received: IPv4 Unicast
    Local GR Mode: Helper*
    Remote GR Mode: Helper
 
    R bit: False
    N bit: False
    Timers:
      Configured Restart Time(sec): 120
      Received Restart Time(sec): 120
      Configured LLGR Stale Path Time(sec): 0
    IPv4 Unicast:
      F bit: False
      End-of-RIB sent: Yes
      End-of-RIB sent after update: Yes
      End-of-RIB received: Yes
      Timers:
        Configured Stale Path Time(sec): 360
        LLGR Stale Path Time(sec): 0
  Message statistics:
    Inq depth is 0
    Outq depth is 0
                         Sent       Rcvd
    Opens:                  2          2
    Notifications:          0          0
    Updates:                4          4
    Keepalives:            44         44
    Route Refresh:          0          0
    Capability:             0          0
    Total:                 50         50
  Minimum time between advertisement runs is 5 seconds
 
 For address family: IPv4 Unicast
  Update group 1, subgroup 1
  Packet Queue length 0
  Community attribute sent to this neighbor(all)
  0 accepted prefixes
 
  Connections established 2; dropped 1
  Last reset 00:01:29,  Waiting for peer OPEN (FRRouting/10.0.3)
  External BGP neighbor may be up to 1 hops away.
Local host: 9.9.9.2, Local port: 51442
Foreign host: 9.9.9.1, Foreign port: 179
Nexthop: 9.9.9.2
Nexthop global: fe80::202:ff:fe00:a
Nexthop local: fe80::202:ff:fe00:a
BGP connection: shared network
BGP Connect Retry Timer in Seconds: 10
Estimated round trip time: 9 ms
Read thread: on  Write thread: on  FD used: 83
 
  BFD: Type: single hop
  Profile: fabric-bfd-profile
  Status: Up, Last update: 0:00:01:17
```

## Troubleshoot BGP Unnumbered

To verify that FRR learns the neighboring link-local IPv6 address through the IPv6 neighbor discovery router advertisements on a given interface, run the vtysh `show interface <interface-id>` command.

If you do not enable `ipv6 nd suppress-ra` on both ends of the interface, `Neighbor address(s):` shows the link-local address of the other end (the address that BGP uses when that interface uses BGP).

{{%notice note%}}
Cumulus Linux automatically enables IPv6 route advertisements (RAs) on an interface with IPv6 addresses. You do not need to run the `no ipv6 nd suppress-ra` command for BGP unnumbered.
{{%/notice%}}

```
cumulus@switch:~$ sudo vtysh
...
switch# show interface swp51
  Interface swp51 is up, line protocol is up
  Link ups:       0    last: (never)
  Link downs:     0    last: (never)
  PTM status: disabled
  vrf: default
  OS Description: leaf to spine
  index 8 metric 0 mtu 9216 speed 1000
  flags: <UP,BROADCAST,RUNNING,MULTICAST>
  Type: Ethernet
  HWaddr: 10:d8:68:d4:a6:81
  inet6 fe80::12d8:68ff:fed4:a681/6
  Interface Type Other
  protodown: off
  ND advertised reachable time is 0 milliseconds
  ND advertised retransmit interval is 0 milliseconds
  ND advertised hop-count limit is 64 hops
  ND router advertisements sent: 217 rcvd: 216
  ND router advertisements are sent every 10 seconds
  ND router advertisements lifetime tracks ra-interval
  ND router advertisement default router preference is medium
  Hosts use stateless autoconfig for addresses.
  Neighbor address(s):
  inet6 fe80::f208:5fff:fe12:cc8c/128
```

## Troubleshoot IPv4 Prefixes Learned with IPv6 Next Hops

To show IPv4 prefixes learned with IPv6 next hops, run the following commands.

The following examples show an IPv4 prefix learned from a BGP peer over an IPv6 session using IPv6 global addresses, but where the next hop installed by BGP is a link-local IPv6 address. This occurs when the session is directly between peers, and the BGP update for the prefix includes both link-local and global IPv6 addresses as next hops. If both global and link-local next hops exist, BGP prefers the link-local address for route installation.

```
cumulus@spine01:mgmt:~$ sudo vtysh
...
spine01# show ip bgp ipv4 unicast summary
BGP router identifier 10.10.10.101, local AS number 65199 vrf-id 0
BGP table version 3
RIB entries 3, using 576 bytes of memory
Peers 1, using 21 KiB of memory

Neighbor                   V      AS   MsgRcvd   MsgSent   TblVer  InQ OutQ  Up/Down State/PfxRcd
leaf01(2001:db8:2::a00:1) 4     65101       22        22        0    0    0  00:01:00           0

Total number of neighbors 1
```

```
cumulus@spine01:mgmt:~$ sudo vtysh
...
spine01# show ip bgp ipv4 unicast
BGP table version is 3, local router ID is 10.10.10.101, vrf id 0
Default local pref 100, local AS 65199
Status codes:  s suppressed, d damped, h history, * valid, > best, = multipath,
               i internal, r RIB-failure, S Stale, R Removed
Nexthop codes: @NNN nexthop's vrf id, < announce-nh-self
Origin codes:  i - IGP, e - EGP, ? - incomplete

   Network          Next Hop                Metric LocPrf Weight Path
   10.10.10.101/32   fe80::a00:27ff:fea6:b9fe      0     0   32768 i

Displayed  1 routes and 1 total paths
```

```
cumulus@spine01:~$ sudo vtysh
...
spine01# show ip bgp ipv4 unicast 10.10.10.101/32
BGP routing table entry for 10.10.10.101/32
Paths: (1 available, best #1, table default)
  Advertised to non peer-group peers:
  Leaf01(2001:db8:0002::0a00:1)
  3
    2001:db8:0002::0a00:1 from Leaf01(2001:db8:0002::0a00:1) (10.10.10.101)
    (fe80::a00:27ff:fea6:b9fe) (used)
      Origin IGP, metric 0, valid, external, bestpath-from-AS 3, best (First path received)
      AddPath ID: RX 0, TX 3
      Last update: Mon Oct 22 08:09:22 2018
```

The example output below shows the results of installing the route in the FRR RIB as well as the kernel FIB. The next hop installed in the FRR RIB is the link-local IPv6 address, which Cumulus Linux converts into an IPv4 link-local address, as required for installation into the kernel FIB.

```
cumulus@spine01:~$ sudo vtysh
...
spine01# show ip route 10.10.10.101/32
RIB entry for 10.10.10.101/32
===========================
Routing entry for 10.10.10.101/32
  Known via "bgp", distance 20, metric 0, best
  Last update 2d17h05m ago
  * fe80::a00:27ff:fea6:b9fe, via swp1

FIB entry for 10.10.10.101/32
===========================
10.10.10.101/32 via 10.0.1.0 dev swp1 proto bgp metric 20 onlink
```

If BGP learns an IPv4 prefix with only an IPv6 global next hop address (when it learns the route through a route reflector), the command output shows the IPv6 global address as the next hop value. The command also shows that it learns recursively through the link-local address of the route reflector. When you use a global IPv6 address as a next hop for route installation in the FRR RIB, the switch still converts it into an IPv4 link-local address for installation into the kernel.

```
cumulus@leaf01:~$ sudo vtysh
...
leaf01# show ip bgp ipv4 unicast summary
BGP router identifier 10.10.10.1, local AS number 65101 vrf-id 0
BGP table version 1
RIB entries 1, using 152 bytes of memory
Peers 1, using 19 KiB of memory

Neighbor             V AS MsgRcvd  MsgSent  TblVer  InQ  OutQ  Up/Down  State/PfxRcd
Spine01(2001:db8:0002::0a00:2) 4 1   74       68         0     0     0     00:00:45      1

Total number of neighbors 1
```

```
cumulus@leaf01:~$ sudo vtysh
...
leaf01# show ip bgp ipv4 unicast summary
  BGP table version is 1, local router ID is 10.10.10.1
  Status codes: s suppressed, d damped, h history, * valid, > best, = multipath,
                i internal, r RIB-failure, S Stale, R Removed
  Origin codes: i - IGP, e - EGP, ? - incomplete

Network          Next Hop    Metric LocPrf Weight Path
*>i10.1.10.0/24 2001:2:2::4       0    100      0    i

Displayed 1 routes and 1 total paths
```

```
cumulus@leaf01:~$ sudo vtysh
...
leaf01# show ip bgp ipv4 unicast 10.10.10.101/32
BGP routing table entry for 10.10.10.101/32
Paths: (1 available, best #1, table default)
  Not advertised to any peer
  Local
  2001:2:2::4 from Spine01(2001:1:1::1) (10.10.10.104)
    Origin IGP, metric 0, localpref 100, valid, internal, bestpath-from-AS Local, best (First path received)
    Originator: 10.0.0.14, Cluster list: 10.10.10.111
    AddPath ID: RX 0, TX 5
    Last update: Mon Oct 22 14:25:30 2018
```

```
cumulus@leaf01:~$ sudo vtysh
...
leaf01# show ip route 10.10.10.1/32
RIB entry for 10.10.10.1/32
===========================
Routing entry for 10.10.10.1/32
  Known via "bgp", distance 200, metric 0, best
  Last update 00:01:13 ago
  2001:2:2::4 (recursive)
  * fe80::a00:27ff:fe5a:84ae, via swp1

FIB entry for 10.10.10.1/32
===========================
10.10.10.1/32 via 10.0.1.1 dev swp1 proto bgp metric 20 onlink
```

To only use IPv6 global addresses for route installation into the FRR RIB, you must add an additional route map to the neighbor or peer group statement in the appropriate address family. When the route map command `set ipv6 next-hop prefer-global` applies to a neighbor, if both a link-local and global IPv6 address are in the BGP update for a prefix, BGP uses the IPv6 global address for route installation.

With this additional configuration, the output in the FRR RIB changes in the direct neighbor case as shown below:

```
router bgp 65101
  bgp router-id 10.10.10.1
  neighbor 2001:db8:2::a00:1 remote-as internal
  neighbor 2001:db8:2::a00:1 capability extended-nexthop
  !
  address-family ipv4 unicast
  neighbor 2001:db8:2::a00:1 route-map GLOBAL in
  exit-address-family
!
route-map GLOBAL permit 20
  set ipv6 next-hop prefer-global
!
```

The resulting FRR RIB output is as follows:

```
cumulus@leaf01:~$ sudo vtysh
...
leaf01# show ip route
Codes: K - kernel route, C - connected, S - static, R - RIP,
    O - OSPF, I - IS-IS, B - BGP, E - EIGRP, N - NHRP,
    T - Table, v - VNC, V - VNC-Direct, A - Babel, D - SHARP,
    F - PBR,
    > - selected route, * - FIB route

B 0.0.0.0/0 [200/0] via 2001:2:2::4, swp2, 00:01:00
K 0.0.0.0/0 [0/0] via 10.0.2.2, eth0, 1d02h29m
C>* 10.0.0.9/32 is directly connected, lo, 5d18h32m
C>* 10.0.2.0/24 is directly connected, eth0, 03:51:31
B>* 172.16.4.0/24 [200/0] via 2001:2:2::4, swp2, 00:01:00ß
C>* 172.16.10.0/24 is directly connected, swp3, 5d18h32m
```

When the switch learns the route through a route reflector, it appears like this:

```
router bgp 65101
  bgp router-id 10.10.10.1
  neighbor 2001:db8:2::a00:2 remote-as internal
  neighbor 2001:db8:2::a00:2 capability extended-nexthop
  !
  address-family ipv6 unicast
  neighbor 2001:db8:2::a00:2 activate
  neighbor 2001:db8:2::a00:2 route-map GLOBAL in
  exit-address-family
!
route-map GLOBAL permit 10
  set ipv6 next-hop prefer-global
```

```
cumulus@leaf01:~$ sudo vtysh
...
leaf01# show ip route
Codes: K - kernel route, C - connected, S - static, R - RIP,
       O - OSPF, I - IS-IS, B - BGP, E - EIGRP, N - NHRP,
       T - Table, v - VNC, V - VNC-Direct, A - Babel, D - SHARP,
       F - PBR,
       > - selected route, * - FIB route

B   0.0.0.0/0 [200/0] via 2001:2:2::4, 00:00:01
K   0.0.0.0/0 [0/0] via 10.0.2.2, eth0, 3d00h26m
C>* 10.0.0.8/32 is directly connected, lo, 3d00h26m
C>* 10.0.2.0/24 is directly connected, eth0, 03:39:18
C>* 172.16.3.0/24 is directly connected, swp2, 3d00h26m
B>  172.16.4.0/24 [200/0] via 2001:2:2::4 (recursive), 00:00:01
  *                         via 2001:1:1::1, swp1, 00:00:01
C>* 172.16.10.0/24 is directly connected, swp3, 3d00h26m
```

## Neighbor State Change Log

Cumulus Linux records the changes that a neighbor goes through in `syslog` and in the `/var/log/frr/frr.log` file. For example:

```
020-10-05T15:51:32.621773-07:00 leaf01 bgpd[10104]: %NOTIFICATION: sent to neighbor peerlink.4094 6/7 (Cease/Connection collision resolution) 0 bytes
2020-10-05T15:51:32.623023-07:00 leaf01 bgpd[10104]: %ADJCHANGE: neighbor peerlink.4094(leaf02) in vrf default Up
2020-10-05T15:51:32.623156-07:00 leaf01 bgpd[10104]: %NOTIFICATION: sent to neighbor peerlink.4094 6/7 (Cease/Connection collision resolution) 0 bytes
2020-10-05T15:51:32.623496-07:00 leaf01 bgpd[10104]: %ADJCHANGE: neighbor peerlink.4094(leaf02) in vrf default Down No AFI/SAFI activated for peer
2020-10-05T15:51:33.040332-07:00 leaf01 bgpd[10104]: [EC 33554454] swp53 [Error] bgp_read_packet error: Connection reset by peer
2020-10-05T15:51:33.279468-07:00 leaf01 bgpd[10104]: [EC 33554454] swp52 [Error] bgp_read_packet error: Connection reset by peer
2020-10-05T15:51:33.339487-07:00 leaf01 bgpd[10104]: %ADJCHANGE: neighbor swp54(spine04) in vrf default Up
2020-10-05T15:51:33.340893-07:00 leaf01 bgpd[10104]: %ADJCHANGE: neighbor swp53(spine03) in vrf default Up
2020-10-05T15:51:33.341648-07:00 leaf01 bgpd[10104]: %ADJCHANGE: neighbor swp52(spine02) in vrf default Up
2020-10-05T15:51:33.342369-07:00 leaf01 bgpd[10104]: %ADJCHANGE: neighbor swp51(spine01) in vrf default Up
2020-10-05T15:51:33.627958-07:00 leaf01 bgpd[10104]: %ADJCHANGE: neighbor peerlink.4094(leaf02) in vrf default Up
```

## Clear BGP Routes

NVUE provides commands to clear and refresh routes in the BGP table. You can clear all routes in the BGP table or all routes for an address family (IPv4, IPv6, or EVPN) in a VRF.

The BGP clear commands do not clear counters in the kernel or hardware.

{{%notice note%}}
- BGP clear route commands that specify a direction (`in` or `out`) do not reset BGP neighbor adjacencies.
- When the switch has a neighbor configured with `soft-reconfiguration inbound` enabled, performing a clear in or soft clear in clears the routes in the soft reconfiguration table for the address family. This results in reevaluating routes in the BGP table against any applied input policies.
- When the switch has a neighbor configured without the `soft-reconfiguration inbound` option enabled, performing a clear in or soft in sends the peer a route refresh message.
- Outbound BGP clear commands (either out or soft out) readvertise all routes to BGP peers.
- BGP soft clear commands that do not specify a direction (`in` or `out`) do not reset BGP neighbor adjacencies, and affect both inbound and outbound routes, as described above, depending on if you enable `soft-reconfiguration inbound`.
{{%/notice%}}

{{< tabs "742 ">}}
{{< tab "NVUE Commands ">}}

To clear and refresh all IPv4 inbound routes:

```
cumulus@leaf01:~$ nv action clear vrf default router bgp address-family ipv4-unicast soft in
Action executing ...
Sent default afi ipv4-unicast route-refresh unless using 'soft-reconfiguration inbound'
Action executing ...
Action succeeded
```

To clear and resend all IPv6 outbound routes:

```
cumulus@leaf01:~$ nv action clear vrf default router bgp address-family ipv6-unicast soft out
Action executing ...
Resent default afi ipv6-unicast outbound updates
Action executing ...
Action succeeded
```

To clear and refresh all EVPN inbound routes:

```
cumulus@leaf01:~$ nv action clear vrf default router bgp address-family l2vpn-evpn soft in
Action executing ...
Sent default afi l2vpn-evpn route-refresh unless using 'soft-reconfiguration inbound'
Action executing ...
Action succeeded
```

To clear and resend all outbound IPv4 routes:

```
cumulus@leaf01:~$ nv action clear vrf default router bgp address-family ipv4-unicast soft out
Action executing ...
Resent default afi ipv4-unicast outbound updates
Action executing ...
Action succeeded
```

To clear and resend all IPv6 outbound routes to BGP neighbor 10.10.10.101:

```
cumulus@leaf01:~$ nv action clear vrf default router bgp neighbor 10.10.10.101 address-family ipv6-unicast out
Action executing ...
Resent default neighbor 10.10.10.101 afi ipv6-unicast outbound updates
Action executing ...
Action succeeded
```

To clear and resend outbound routes for all address families (IPv4, IPv6, and l2vpn-evpn) for the BGP peer group SPINES:

```
cumulus@leaf01:~$ nv action clear vrf default router bgp peer-group SPINES out
Action executing ...
Resent default peer-group SPINES outbound updates
Action executing ...
Action succeeded
```

To clear and refresh all IPv4 inbound routes for all VRFs and address families:

```
cumulus@switch:~$ nv action clear router bgp soft in
Action executing ...
Sent route-refresh unless using 'soft-reconfiguration inbound'
Action executing ...
Action succeeded
```

To clear and refresh inbound routes for all neighbors, address families, and VRFs and to refresh the outbound route filtering prefix-list:

```
cumulus@switch:~$ nv action clear router bgp in prefix-filter
Action executing ...
sent route-refresh updates prefix_filter=True
Action executing ...
Action succeeded
```

To clear BGP sessions with all neighbors, forcing the neighbors to restart:

```
cumulus@switch:~$ nv action clear router bgp
Action executing ...
Cleared all peers
Action executing ...
Action succeeded
```

{{< /tab >}}
{{< tab "vtysh Commands ">}}

To clear and refresh all IPv4 inbound routes:

```
cumulus@spine01:~$ sudo vtysh
...
switch# clear bgp vrf default ipv4 unicast * soft in
switch# exit
```

To clear and resend all IPv6 outbound routes:

```
cumulus@spine01:~$ sudo vtysh
...
switch# clear bgp vrf default ipv6 unicast * soft out
switch# exit
```

To clear and refresh all EVPN inbound routes:

```
cumulus@spine01:~$ sudo vtysh
...
switch# clear bgp vrf default l2vpn evpn * soft in
switch# exit
```

To clear and resend all outbound IPv4 routes:

```
cumulus@spine01:~$ sudo vtysh
...
switch# clear bgp vrf default ipv4 unicast * soft out
switch# exit
```

To clear and resend all IPv6 outbound routes to BGP neighbor 10.10.10.101:

```
cumulus@spine01:~$ sudo vtysh
...
switch# clear bgp vrf default ipv6 unicast 10.10.10.101 out
switch# exit
```

To clear and resend outbound routes for all address families (IPv4, IPv6, and l2vpn-evpn) for the BGP peer group SPINES:

```
cumulus@spine01:~$ sudo vtysh
...
switch# clear bgp vrf default peer-group SPINES out
switch# exit
```

To clear and refresh inbound routes for all neighbors, address families, and VRFs and to refresh the outbound route filtering prefix-list:

```
cumulus@spine01:~$ sudo vtysh
...
switch# clear bgp in prefix-filter
switch# exit
```

To clear BGP sessions with all neighbors, forcing the neighbors to restart:

```
cumulus@switch:~$ sudo vtysh
...
switch# clear bgp *
switch# write memory
switch# exit
```

{{< /tab >}}
{{< /tabs >}}
