---
title: Unset Commands
author: Cumulus Networks
weight: 40
product: Cumulus Linux
---
## nv unset router
### Usage

  nv unset router [options] [<attribute> ...]

### Description

  A router

### Atrributes

  nexthop-group     Nexthops
  pbr               PBR global configuration.
  policy            A router
  bgp               BGP global configuration.
  ospf              OSPF global configuration.
  pim               PIM global configuration.
  igmp              IGMP global configuration.
  vrrp              VRRP global configuration.
  vrr               VRR global configuration.
  adaptive-routing  Adaptive routing global configuration.

## nv unset router nexthop-group
### Usage

  nv unset router nexthop-group [options] [<nexthop-group-id> ...]

### Description

  Nexthops

### Identifiers

  <nexthop-group-id>  Nexthop group ID




## nv unset router nexthop-group <nexthop-group-id>

### Usage

  nv unset router nexthop-group <nexthop-group-id> [options] [<attribute> ...]

### Description

  A nexthop-group

### Identifiers

  <nexthop-group-id>  Nexthop group ID

### Atrributes

  via                 Nexthops




## nv unset router nexthop-group <nexthop-group-id> via

### Usage

  nv unset router nexthop-group <nexthop-group-id> via [options] [<via-id> ...]

### Description

  Nexthops

### Identifiers

  <nexthop-group-id>  Nexthop group ID
  <via-id>            IP address

## nv unset router nexthop-group <nexthop-group-id> via <via-id>
### Usage

  nv unset router nexthop-group <nexthop-group-id> via <via-id> [options] [<attribute> ...]

### Description

  A nexthop

### Identifiers

  <nexthop-group-id>  Nexthop group ID
  <via-id>            IP address

### Atrributes

  interface           The interface to use for egress. If not specified, it
                      will automatically be determined. Only valid when the
                      via's type is ipv4-address or ipv6-address.
  vrf                 The VRF to use for egress. If not specified, the route's
                      VRF will be used. Only valid when the via's type is
                      ipv4-address or ipv6-address.

## nv unset router nexthop-group <nexthop-group-id> via <via-id> interface
### Usage

  nv unset router nexthop-group <nexthop-group-id> via <via-id> interface [options]

### Description

  The interface to use for egress.  If not specified, it will automatically be determined.  Only valid when the via's type is ipv4-address or ipv6-address.

### Identifiers

  <nexthop-group-id>  Nexthop group ID
  <via-id>            IP address

## nv unset router nexthop-group <nexthop-group-id> via <via-id> vrf
### Usage

  nv unset router nexthop-group <nexthop-group-id> via <via-id> vrf [options]

### Description

  The VRF to use for egress.  If not specified, the route's VRF will be used.  Only valid when the via's type is ipv4-address or ipv6-address.

### Identifiers

  <nexthop-group-id>  Nexthop group ID
  <via-id>            IP address

## nv unset router pbr
### Usage

  nv unset router pbr [options] [<attribute> ...]

### Description

  PBR global configuration.

### Atrributes

  map         Collection of PBR Maps
  enable      Turn the feature 'on' or 'off'. The default is 'off'.

## nv unset router pbr map
### Usage

  nv unset router pbr map [options] [<pbr-map-id> ...]

### Description

  Collection of PBR Maps

### Identifiers

  <pbr-map-id>  Route Map ID

## nv unset router pbr map <pbr-map-id>
### Usage

  nv unset router pbr map <pbr-map-id> [options] [<attribute> ...]

### Description

  A pbr map is used for policy configuration.

### Identifiers

  <pbr-map-id>  Route Map ID

### Atrributes

  rule          PBR Map rule

## nv unset router pbr map <pbr-map-id> rule <rule-id>
### Usage

  nv unset router pbr map <pbr-map-id> rule <rule-id> [options] [<attribute> ...]

### Description

  Route Map Matching/setting criteria and action rule

### Identifiers

  <pbr-map-id>  Route Map ID
  <rule-id>     PBR rule number

### Atrributes

  match         PBR match
  action        PBR set

## nv unset router pbr map <pbr-map-id> rule <rule-id> match
### Usage

  nv unset router pbr map <pbr-map-id> rule <rule-id> match [options] [<attribute> ...]

### Description

  Route map rule match

### Identifiers

  <pbr-map-id>    Route Map ID
  <rule-id>       PBR rule number

### Atrributes

  destination-ip  Destination IP prefix
  dscp            DSCP
  ecn             ECN
  source-ip       Source IP prefix
## nv unset router pbr map <pbr-map-id> rule <rule-id> match source-ip
### Usage

  nv unset router pbr map <pbr-map-id> rule <rule-id> match source-ip [options]

### Description

  Source IP prefix

### Identifiers

  <pbr-map-id>  Route Map ID
  <rule-id>     PBR rule number

## nv unset router pbr map <pbr-map-id> rule <rule-id> match destination-ip
### Usage

  nv unset router pbr map <pbr-map-id> rule <rule-id> match destination-ip [options]

### Description

  Destination IP prefix

### Identifiers

  <pbr-map-id>  Route Map ID
  <rule-id>     PBR rule number

## nv unset router pbr map <pbr-map-id> rule <rule-id> match dscp
### Usage

  nv unset router pbr map <pbr-map-id> rule <rule-id> match dscp [options]

### Description

  DSCP

### Identifiers

  <pbr-map-id>  Route Map ID
  <rule-id>     PBR rule number

## nv unset router pbr map <pbr-map-id> rule <rule-id> match ecn
### Usage

  nv unset router pbr map <pbr-map-id> rule <rule-id> match ecn [options]

### Description

  ECN

### Identifiers

  <pbr-map-id>  Route Map ID
  <rule-id>     PBR rule number

## nv unset router pbr map <pbr-map-id> rule <rule-id> action
### Usage

  nv unset router pbr map <pbr-map-id> rule <rule-id> action [options] [<attribute> ...]

### Description

  PBR map rule action

### Identifiers

  <pbr-map-id>   Route Map ID
  <rule-id>      PBR rule number

### Atrributes

  nexthop-group  Route with nexthop-group
  vrf            Route through VRF

## nv unset router pbr map <pbr-map-id> rule <rule-id> action nexthop-group <nexthop-group-id>
### Usage

  nv unset router pbr map <pbr-map-id> rule <rule-id> action nexthop-group <nexthop-group-id> [options]

### Description

  A nexthop-group

### Identifiers

  <pbr-map-id>        Route Map ID
  <rule-id>           PBR rule number
  <nexthop-group-id>  Nexthop group ID

## nv unset router pbr map <pbr-map-id> rule <rule-id> action vrf
### Usage

  nv unset router pbr map <pbr-map-id> rule <rule-id> action vrf [options]

### Description

  Route through VRF

### Identifiers

  <pbr-map-id>  Route Map ID
  <rule-id>     PBR rule number

## nv unset router pbr enable

### Usage

  nv unset router pbr enable [options]

### Description

  Turn the feature 'on' or 'off'.  The default is 'off'.



## nv unset router policy

### Usage

  nv unset router policy [options] [<attribute> ...]

### Description

  A router

### Atrributes

  community-list        Community lists
  as-path-list          AS Path lists
  ext-community-list    Extended Community lists
  large-community-list  Large Community lists
  prefix-list           Prefix list rules
  route-map             Collection of Route Maps

## nv unset router policy community-list

### Usage

  nv unset router policy community-list [options] [<list-id> ...]

### Description

  Community lists

### Identifiers

  <list-id>   Community List ID



## nv unset router policy community-list <list-id>

### Usage

  nv unset router policy community-list <list-id> [options] [<attribute> ...]

### Description

  A community list is used for matching BGP community policies.

### Identifiers

  <list-id>   Community List ID

### Atrributes

  rule        Community List rule



## nv unset router policy community-list <list-id> rule

### Usage

  nv unset router policy community-list <list-id> rule [options] [<rule-id> ...]

### Description

  Community list rules

### Identifiers

  <list-id>   Community List ID
  <rule-id>   Prefix List rule number



## nv unset router policy community-list <list-id> rule <rule-id>

### Usage

  nv unset router policy community-list <list-id> rule <rule-id> [options] [<attribute> ...]

### Description

  Community list Matching criteria and action rule

### Identifiers

  <list-id>   Community List ID
  <rule-id>   Prefix List rule number

### Atrributes

  community   Community expression
  action      Action to be taken for community list match



## nv unset router policy community-list <list-id> rule <rule-id> community

### Usage

  nv unset router policy community-list <list-id> rule <rule-id> community [options] [<community-id> ...]

### Description

  Set of community names for community-list

### Identifiers

  <list-id>       Community List ID
  <rule-id>       Prefix List rule number
  <community-id>  Community number in AA:NN format or well known name

## nv unset router policy community-list <list-id> rule <rule-id> community <community-id>

### Usage

  nv unset router policy community-list <list-id> rule <rule-id> community <community-id> [options]

### Description

  A community name

### Identifiers

  <list-id>       Community List ID
  <rule-id>       Prefix List rule number
  <community-id>  Community number in AA:NN format or well known name

## nv unset router policy community-list <list-id> rule <rule-id> action

### Usage

  nv unset router policy community-list <list-id> rule <rule-id> action [options]

### Description

  Action to be taken for community list match

### Identifiers

  <list-id>   Community List ID
  <rule-id>   Prefix List rule number



## nv unset router policy as-path-list

### Usage

  nv unset router policy as-path-list [options] [<list-id> ...]

### Description

  AS Path lists

### Identifiers

  <list-id>   AS Path List ID



## nv unset router policy as-path-list <list-id>

### Usage

  nv unset router policy as-path-list <list-id> [options] [<attribute> ...]

### Description

  An AS Path list is used for matching BGP AS Path

### Identifiers

  <list-id>   AS Path List ID

### Atrributes

  rule        AS Path List rule



## nv unset router policy as-path-list <list-id> rule <rule-id>

### Usage

  nv unset router policy as-path-list <list-id> rule <rule-id> [options] [<attribute> ...]

### Description

  AS Path list Matching criteria and action rule

### Identifiers

  <list-id>   AS Path List ID
  <rule-id>   Prefix List rule number

### Atrributes

  action      Action to be taken for AS path list match
  aspath-exp  Regular expression to match BGP AS Paths



## nv unset router policy as-path-list <list-id> rule <rule-id> action

### Usage

  nv unset router policy as-path-list <list-id> rule <rule-id> action [options]

### Description

  Action to be taken for AS path list match

### Identifiers

  <list-id>   AS Path List ID
  <rule-id>   Prefix List rule number



## nv unset router policy as-path-list <list-id> rule <rule-id> aspath-exp

### Usage

  nv unset router policy as-path-list <list-id> rule <rule-id> aspath-exp [options]

### Description

  Regular expression to match BGP AS Paths

### Identifiers

  <list-id>   AS Path List ID
  <rule-id>   Prefix List rule number



## nv unset router policy ext-community-list

### Usage

  nv unset router policy ext-community-list [options] [<list-id> ...]

### Description

  Extended Community lists

### Identifiers

  <list-id>   Community List ID



## nv unset router policy ext-community-list <list-id>

### Usage

  nv unset router policy ext-community-list <list-id> [options] [<attribute> ...]

### Description

  A Extended Community list used for matching BGP communities

### Identifiers

  <list-id>   Community List ID

### Atrributes

  rule        Extended Community List rule



## nv unset router policy ext-community-list <list-id> rule

### Usage

  nv unset router policy ext-community-list <list-id> rule [options] [<rule-id> ...]

### Description

  Extended Community list rules

### Identifiers

  <list-id>   Community List ID
  <rule-id>   Prefix List rule number



## nv unset router policy ext-community-list <list-id> rule <rule-id>

### Usage

  nv unset router policy ext-community-list <list-id> rule <rule-id> [options] [<attribute> ...]

### Description

  Extended Community list Matching criteria and action rule

### Identifiers

  <list-id>      Community List ID
  <rule-id>      Prefix List rule number

### Atrributes

  ext-community  Extended Community expression
  action         Action to be taken for extended community list match

## nv unset router policy ext-community-list <list-id> rule <rule-id> ext-community

### Usage

  nv unset router policy ext-community-list <list-id> rule <rule-id> ext-community [options] [<attribute> ...]

### Description

  A Extended community name

### Identifiers

  <list-id>   Community List ID
  <rule-id>   Prefix List rule number

### Atrributes

  rt          Route Target Extended Community
  soo         Site of Origin Extended Community



## nv unset router policy ext-community-list <list-id> rule <rule-id> ext-community rt

### Usage

  nv unset router policy ext-community-list <list-id> rule <rule-id> ext-community rt [options] [<ext-community-id> ...]

### Description

  Set of extended communities

### Identifiers

  <list-id>           Community List ID
  <rule-id>           Prefix List rule number
  <ext-community-id>  Community number in AA:NN or IP:NN format




## nv unset router policy ext-community-list <list-id> rule <rule-id> ext-community rt <ext-community-id>

### Usage

  nv unset router policy ext-community-list <list-id> rule <rule-id> ext-community rt <ext-community-id> [options]

### Description

  A extended community name

### Identifiers

  <list-id>           Community List ID
  <rule-id>           Prefix List rule number
  <ext-community-id>  Community number in AA:NN or IP:NN format




## nv unset router policy ext-community-list <list-id> rule <rule-id> ext-community soo

### Usage

  nv unset router policy ext-community-list <list-id> rule <rule-id> ext-community soo [options] [<ext-community-id> ...]

### Description

  Set of extended communities

### Identifiers

  <list-id>           Community List ID
  <rule-id>           Prefix List rule number
  <ext-community-id>  Community number in AA:NN or IP:NN format




## nv unset router policy ext-community-list <list-id> rule <rule-id> ext-community soo <ext-community-id>

### Usage

  nv unset router policy ext-community-list <list-id> rule <rule-id> ext-community soo <ext-community-id> [options]

### Description

  A extended community name

### Identifiers

  <list-id>           Community List ID
  <rule-id>           Prefix List rule number
  <ext-community-id>  Community number in AA:NN or IP:NN format




## nv unset router policy ext-community-list <list-id> rule <rule-id> action

### Usage

  nv unset router policy ext-community-list <list-id> rule <rule-id> action [options]

### Description

  Action to be taken for extended community list match

### Identifiers

  <list-id>   Community List ID
  <rule-id>   Prefix List rule number



## nv unset router policy large-community-list

### Usage

  nv unset router policy large-community-list [options] [<list-id> ...]

### Description

  Large Community lists

### Identifiers

  <list-id>   Community List ID



## nv unset router policy large-community-list <list-id>

### Usage

  nv unset router policy large-community-list <list-id> [options] [<attribute> ...]

### Description

  A Large Community list used for matching community based BGP policies

### Identifiers

  <list-id>   Community List ID

### Atrributes

  rule        Large Community List rules



## nv unset router policy large-community-list <list-id> rule

### Usage

  nv unset router policy large-community-list <list-id> rule [options] [<rule-id> ...]

### Description

  Large Community list rules

### Identifiers

  <list-id>   Community List ID
  <rule-id>   Prefix List rule number



## nv unset router policy large-community-list <list-id> rule <rule-id>

### Usage

  nv unset router policy large-community-list <list-id> rule <rule-id> [options] [<attribute> ...]

### Description

  Large Community list Matching criteria and action rule

### Identifiers

  <list-id>        Community List ID
  <rule-id>        Prefix List rule number

### Atrributes

  large-community  Large Community expression
  action           Action to be taken for community list match

## nv unset router policy large-community-list <list-id> rule <rule-id> large-community

### Usage

  nv unset router policy large-community-list <list-id> rule <rule-id> large-community [options] [<large-community-id> ...]

### Description

  Set of community names for large community list

### Identifiers

  <list-id>             Community List ID
  <rule-id>             Prefix List rule number
  <large-community-id>  Community number in AA:BB:CC format

## nv unset router policy large-community-list <list-id> rule <rule-id> large-community <large-community-id>

### Usage

  nv unset router policy large-community-list <list-id> rule <rule-id> large-community <large-community-id> [options]

### Description

  Set of community names for large community list

### Identifiers

  <list-id>             Community List ID
  <rule-id>             Prefix List rule number
  <large-community-id>  Community number in AA:BB:CC format

## nv unset router policy large-community-list <list-id> rule <rule-id> action

### Usage

  nv unset router policy large-community-list <list-id> rule <rule-id> action [options]

### Description

  Action to be taken for community list match

### Identifiers

  <list-id>   Community List ID
  <rule-id>   Prefix List rule number



## nv unset router policy prefix-list

### Usage

  nv unset router policy prefix-list [options] [<prefix-list-id> ...]

### Description

  Prefix list rules

### Identifiers

  <prefix-list-id>  Prefix List ID

## nv unset router policy prefix-list <prefix-list-id>

### Usage

  nv unset router policy prefix-list <prefix-list-id> [options] [<attribute> ...]

### Description

  A prefix list is used for matching IPv4 and IPv6 address prefixes.

### Identifiers

  <prefix-list-id>  Prefix List ID

### Atrributes

  rule              Prefix List rule
  type              prefix list type

## nv unset router policy prefix-list <prefix-list-id> rule <rule-id>

### Usage

  nv unset router policy prefix-list <prefix-list-id> rule <rule-id> [options] [<attribute> ...]

### Description

  Prefix list Matching criteria and action rule

### Identifiers

  <prefix-list-id>  Prefix List ID
  <rule-id>         Prefix List rule number

### Atrributes

  match             Prefix List rule
  action            Action to be taken for prefix list match

## nv unset router policy prefix-list <prefix-list-id> rule <rule-id> match <match-id>

### Usage

  nv unset router policy prefix-list <prefix-list-id> rule <rule-id> match <match-id> [options] [<attribute> ...]

### Description

  A prefix match

### Identifiers

  <prefix-list-id>  Prefix List ID
  <rule-id>         Prefix List rule number
  <match-id>        ip v4/v6 prefix, or any

### Atrributes

  max-prefix-len    Maximum prefix length to be matched
  min-prefix-len    Minimum prefix length to be matched

## nv unset router policy prefix-list <prefix-list-id> rule <rule-id> match <match-id> min-prefix-len

### Usage

  nv unset router policy prefix-list <prefix-list-id> rule <rule-id> match <match-id> min-prefix-len [options]

### Description

  Minimum prefix length to be matched

### Identifiers

  <prefix-list-id>  Prefix List ID
  <rule-id>         Prefix List rule number
  <match-id>        ip v4/v6 prefix, or any

## nv unset router policy prefix-list <prefix-list-id> rule <rule-id> match <match-id> max-prefix-len

### Usage

  nv unset router policy prefix-list <prefix-list-id> rule <rule-id> match <match-id> max-prefix-len [options]

### Description

  Maximum prefix length to be matched

### Identifiers

  <prefix-list-id>  Prefix List ID
  <rule-id>         Prefix List rule number
  <match-id>        ip v4/v6 prefix, or any

## nv unset router policy prefix-list <prefix-list-id> rule <rule-id> action

### Usage

  nv unset router policy prefix-list <prefix-list-id> rule <rule-id> action [options]

### Description

  Action to be taken for prefix list match

### Identifiers

  <prefix-list-id>  Prefix List ID
  <rule-id>         Prefix List rule number

## nv unset router policy prefix-list <prefix-list-id> type

### Usage

  nv unset router policy prefix-list <prefix-list-id> type [options]

### Description

  prefix list type

### Identifiers

  <prefix-list-id>  Prefix List ID

## nv unset router policy route-map

### Usage

  nv unset router policy route-map [options] [<route-map-id> ...]

### Description

  Collection of Route Maps

### Identifiers

  <route-map-id>  Route Map ID

## nv unset router policy route-map <route-map-id>

### Usage

  nv unset router policy route-map <route-map-id> [options] [<attribute> ...]

### Description

  A route map is used for policy configuration.

### Identifiers

  <route-map-id>  Route Map ID

### Atrributes

  rule            Route Map rule

## nv unset router policy route-map <route-map-id> rule <rule-id>

### Usage

  nv unset router policy route-map <route-map-id> rule <rule-id> [options] [<attribute> ...]

### Description

  Route Map Matching/setting criteria and action rule

### Identifiers

  <route-map-id>  Route Map ID
  <rule-id>       Sequence to insert or delete from the route-map

### Atrributes

  match           Route Map match
  set             Route Map set
  action          Route Map set

## nv unset router policy route-map <route-map-id> rule <rule-id> match

### Usage

  nv unset router policy route-map <route-map-id> rule <rule-id> match [options] [<attribute> ...]

### Description

  Route map rule match

### Identifiers

  <route-map-id>        Route Map ID
  <rule-id>             Sequence to insert or delete from the route-map

### Atrributes

  as-path-list          BGP AS path list
  community-list        BGP community list
  evpn-route-type       EVPN route type
  evpn-vni              VNI ID
  interface             First hop interface or VRF
  ip-nexthop            IP nexthop address
  ip-nexthop-len        IP nexthop prefix length
  ip-nexthop-list       IP prefix list
  ip-nexthop-type       IP nexthop type
  ip-prefix-len         IP address prefix length
  ip-prefix-list        IP prefix list
  large-community-list  BGP large community list
  local-preference      Local preference of route
  metric                Metric of route
  origin                BGP origin
  peer                  BGP peer
  source-protocol       Protocol via which the route was learnt
  source-vrf            Source VRF
  tag                   Tag
  type                  match prefix type

## nv unset router policy route-map <route-map-id> rule <rule-id> match ip-prefix-list

### Usage

  nv unset router policy route-map <route-map-id> rule <rule-id> match ip-prefix-list [options]

### Description

  IP prefix list

### Identifiers

  <route-map-id>  Route Map ID
  <rule-id>       Sequence to insert or delete from the route-map

## nv unset router policy route-map <route-map-id> rule <rule-id> match ip-prefix-len

### Usage

  nv unset router policy route-map <route-map-id> rule <rule-id> match ip-prefix-len [options]

### Description

  IP address prefix length

### Identifiers

  <route-map-id>  Route Map ID
  <rule-id>       Sequence to insert or delete from the route-map

## nv unset router policy route-map <route-map-id> rule <rule-id> match ip-nexthop-list

### Usage

  nv unset router policy route-map <route-map-id> rule <rule-id> match ip-nexthop-list [options]

### Description

  IP prefix list

### Identifiers

  <route-map-id>  Route Map ID
  <rule-id>       Sequence to insert or delete from the route-map

## nv unset router policy route-map <route-map-id> rule <rule-id> match ip-nexthop-len

### Usage

  nv unset router policy route-map <route-map-id> rule <rule-id> match ip-nexthop-len [options]

### Description

  IP nexthop prefix length

### Identifiers

  <route-map-id>  Route Map ID
  <rule-id>       Sequence to insert or delete from the route-map

## nv unset router policy route-map <route-map-id> rule <rule-id> match ip-nexthop

### Usage

  nv unset router policy route-map <route-map-id> rule <rule-id> match ip-nexthop [options]

### Description

  IP nexthop address

### Identifiers

  <route-map-id>  Route Map ID
  <rule-id>       Sequence to insert or delete from the route-map

## nv unset router policy route-map <route-map-id> rule <rule-id> match ip-nexthop-type

### Usage

  nv unset router policy route-map <route-map-id> rule <rule-id> match ip-nexthop-type [options]

### Description

  IP nexthop type

### Identifiers

  <route-map-id>  Route Map ID
  <rule-id>       Sequence to insert or delete from the route-map

## nv unset router policy route-map <route-map-id> rule <rule-id> match as-path-list

### Usage

  nv unset router policy route-map <route-map-id> rule <rule-id> match as-path-list [options]

### Description

  BGP AS path list

### Identifiers

  <route-map-id>  Route Map ID
  <rule-id>       Sequence to insert or delete from the route-map

## nv unset router policy route-map <route-map-id> rule <rule-id> match community-list

### Usage

  nv unset router policy route-map <route-map-id> rule <rule-id> match community-list [options]

### Description

  BGP community list

### Identifiers

  <route-map-id>  Route Map ID
  <rule-id>       Sequence to insert or delete from the route-map

## nv unset router policy route-map <route-map-id> rule <rule-id> match large-community-list

### Usage

  nv unset router policy route-map <route-map-id> rule <rule-id> match large-community-list [options]

### Description

  BGP large community list

### Identifiers

  <route-map-id>  Route Map ID
  <rule-id>       Sequence to insert or delete from the route-map

## nv unset router policy route-map <route-map-id> rule <rule-id> match metric

### Usage

  nv unset router policy route-map <route-map-id> rule <rule-id> match metric [options]

### Description

  Metric of route

### Identifiers

  <route-map-id>  Route Map ID
  <rule-id>       Sequence to insert or delete from the route-map

## nv unset router policy route-map <route-map-id> rule <rule-id> match interface

### Usage

  nv unset router policy route-map <route-map-id> rule <rule-id> match interface [options]

### Description

  First hop interface or VRF

### Identifiers

  <route-map-id>  Route Map ID
  <rule-id>       Sequence to insert or delete from the route-map

## nv unset router policy route-map <route-map-id> rule <rule-id> match tag

### Usage

  nv unset router policy route-map <route-map-id> rule <rule-id> match tag [options]

### Description

  Tag

### Identifiers

  <route-map-id>  Route Map ID
  <rule-id>       Sequence to insert or delete from the route-map

## nv unset router policy route-map <route-map-id> rule <rule-id> match source-protocol

### Usage

  nv unset router policy route-map <route-map-id> rule <rule-id> match source-protocol [options]

### Description

  Protocol via which the route was learnt

### Identifiers

  <route-map-id>  Route Map ID
  <rule-id>       Sequence to insert or delete from the route-map

## nv unset router policy route-map <route-map-id> rule <rule-id> match origin

### Usage

  nv unset router policy route-map <route-map-id> rule <rule-id> match origin [options]

### Description

  BGP origin

### Identifiers

  <route-map-id>  Route Map ID
  <rule-id>       Sequence to insert or delete from the route-map

## nv unset router policy route-map <route-map-id> rule <rule-id> match peer

### Usage

  nv unset router policy route-map <route-map-id> rule <rule-id> match peer [options]

### Description

  BGP peer

### Identifiers

  <route-map-id>  Route Map ID
  <rule-id>       Sequence to insert or delete from the route-map

## nv unset router policy route-map <route-map-id> rule <rule-id> match local-preference

### Usage

  nv unset router policy route-map <route-map-id> rule <rule-id> match local-preference [options]

### Description

  Local preference of route

### Identifiers

  <route-map-id>  Route Map ID
  <rule-id>       Sequence to insert or delete from the route-map

## nv unset router policy route-map <route-map-id> rule <rule-id> match evpn-route-type

### Usage

  nv unset router policy route-map <route-map-id> rule <rule-id> match evpn-route-type [options]

### Description

  EVPN route type

### Identifiers

  <route-map-id>  Route Map ID
  <rule-id>       Sequence to insert or delete from the route-map

## nv unset router policy route-map <route-map-id> rule <rule-id> match evpn-vni

### Usage

  nv unset router policy route-map <route-map-id> rule <rule-id> match evpn-vni [options]

### Description

  VNI ID

### Identifiers

  <route-map-id>  Route Map ID
  <rule-id>       Sequence to insert or delete from the route-map

## nv unset router policy route-map <route-map-id> rule <rule-id> match source-vrf

### Usage

  nv unset router policy route-map <route-map-id> rule <rule-id> match source-vrf [options]

### Description

  Source VRF

### Identifiers

  <route-map-id>  Route Map ID
  <rule-id>       Sequence to insert or delete from the route-map

## nv unset router policy route-map <route-map-id> rule <rule-id> match type

### Usage

  nv unset router policy route-map <route-map-id> rule <rule-id> match type [options]

### Description

  match prefix type

### Identifiers

  <route-map-id>  Route Map ID
  <rule-id>       Sequence to insert or delete from the route-map

## nv unset router policy route-map <route-map-id> rule <rule-id> set

### Usage

  nv unset router policy route-map <route-map-id> rule <rule-id> set [options] [<attribute> ...]

### Description

  Route map rule set

### Identifiers

  <route-map-id>        Route Map ID
  <rule-id>             Sequence to insert or delete from the route-map

### Atrributes

  as-path-prepend       AS Path prepend
  community             Collection of BGP communities
  large-community       Collection of large BGP communities
  aggregator-as         Collection of aggregator AS
  as-path-exclude       Exclude from AS path
  atomic-aggregate      BGP atomic aggregate
  community-delete-list
                        Delete community list
  ext-community-bw      Extended community link bandwidth
  ext-community-rt      Route target extended community
  ext-community-soo     Site of origin extended community
  ip-nexthop            IP nexthop
  ipv6-nexthop-global   IPv6 nexthop global address
  ipv6-nexthop-local    IPv6 nexthop local address
  ipv6-nexthop-prefer-global
                        Prefer to use the global address as the IPV6 nexthop
  large-community-delete-list
                        Delete large community list
  local-preference      Local preference
  metric                Metric value for destination routing protocol
  metric-type           Type of metric
  origin                BGP origin
  source-ip             Source IP address
  tag                   Tag value for routing protocol
  weight                BGP weight

## nv unset router policy route-map <route-map-id> rule <rule-id> set as-path-prepend

### Usage

  nv unset router policy route-map <route-map-id> rule <rule-id> set as-path-prepend [options] [<attribute> ...]

### Description

  AS Path prepend

### Identifiers

  <route-map-id>  Route Map ID
  <rule-id>       Sequence to insert or delete from the route-map

### Atrributes

  as              AS number
  last-as         Number of times to insert peer's AS number

## nv unset router policy route-map <route-map-id> rule <rule-id> set as-path-prepend as

### Usage

  nv unset router policy route-map <route-map-id> rule <rule-id> set as-path-prepend as [options]

### Description

  AS number

### Identifiers

  <route-map-id>  Route Map ID
  <rule-id>       Sequence to insert or delete from the route-map

## nv unset router policy route-map <route-map-id> rule <rule-id> set as-path-prepend last-as

### Usage

  nv unset router policy route-map <route-map-id> rule <rule-id> set as-path-prepend last-as [options]

### Description

  Number of times to insert peer's AS number

### Identifiers

  <route-map-id>  Route Map ID
  <rule-id>       Sequence to insert or delete from the route-map

## nv unset router policy route-map <route-map-id> rule <rule-id> set community <community-id>

### Usage

  nv unset router policy route-map <route-map-id> rule <rule-id> set community <community-id> [options]

### Description

  BGP Community

### Identifiers

  <route-map-id>  Route Map ID
  <rule-id>       Sequence to insert or delete from the route-map
  <community-id>  Community number

## nv unset router policy route-map <route-map-id> rule <rule-id> set large-community <large-community-id>

### Usage

  nv unset router policy route-map <route-map-id> rule <rule-id> set large-community <large-community-id> [options]

### Description

  Large BGP Community

### Identifiers

  <route-map-id>        Route Map ID
  <rule-id>             Sequence to insert or delete from the route-map
  <large-community-id>  Large Community number

## nv unset router policy route-map <route-map-id> rule <rule-id> set aggregator-as <asn-id>

### Usage

  nv unset router policy route-map <route-map-id> rule <rule-id> set aggregator-as <asn-id> [options] [<attribute> ...]

### Description

  Aggregator AS Number

### Identifiers

  <route-map-id>  Route Map ID
  <rule-id>       Sequence to insert or delete from the route-map
  <asn-id>        Autonomous number

### Atrributes

  address         Set of IPv4 addresses

## nv unset router policy route-map <route-map-id> rule <rule-id> set aggregator-as <asn-id> address <ipv4-address-id>

### Usage

  nv unset router policy route-map <route-map-id> rule <rule-id> set aggregator-as <asn-id> address <ipv4-address-id> [options]

### Description

  An IPv4 address

### Identifiers

  <route-map-id>     Route Map ID
  <rule-id>          Sequence to insert or delete from the route-map
  <asn-id>           Autonomous number
  <ipv4-address-id>  IPv4 address

## nv unset router policy route-map <route-map-id> rule <rule-id> set as-path-exclude

### Usage

  nv unset router policy route-map <route-map-id> rule <rule-id> set as-path-exclude [options]

### Description

  Exclude from AS path

### Identifiers

  <route-map-id>  Route Map ID
  <rule-id>       Sequence to insert or delete from the route-map

## nv unset router policy route-map <route-map-id> rule <rule-id> set atomic-aggregate

### Usage

  nv unset router policy route-map <route-map-id> rule <rule-id> set atomic-aggregate [options]

### Description

  BGP atomic aggregate

### Identifiers

  <route-map-id>  Route Map ID
  <rule-id>       Sequence to insert or delete from the route-map

## nv unset router policy route-map <route-map-id> rule <rule-id> set ext-community-rt

### Usage

  nv unset router policy route-map <route-map-id> rule <rule-id> set ext-community-rt [options]

### Description

  Route target extended community

### Identifiers

  <route-map-id>  Route Map ID
  <rule-id>       Sequence to insert or delete from the route-map

## nv unset router policy route-map <route-map-id> rule <rule-id> set ext-community-soo

### Usage

  nv unset router policy route-map <route-map-id> rule <rule-id> set ext-community-soo [options]

### Description

  Site of origin extended community

### Identifiers

  <route-map-id>  Route Map ID
  <rule-id>       Sequence to insert or delete from the route-map

## nv unset router policy route-map <route-map-id> rule <rule-id> set ext-community-bw

### Usage

  nv unset router policy route-map <route-map-id> rule <rule-id> set ext-community-bw [options]

### Description

  Extended community link bandwidth

### Identifiers

  <route-map-id>  Route Map ID
  <rule-id>       Sequence to insert or delete from the route-map

## nv unset router policy route-map <route-map-id> rule <rule-id> set local-preference

### Usage

  nv unset router policy route-map <route-map-id> rule <rule-id> set local-preference [options]

### Description

  Local preference

### Identifiers

  <route-map-id>  Route Map ID
  <rule-id>       Sequence to insert or delete from the route-map

## nv unset router policy route-map <route-map-id> rule <rule-id> set weight

### Usage

  nv unset router policy route-map <route-map-id> rule <rule-id> set weight [options]

### Description

  BGP weight

### Identifiers

  <route-map-id>  Route Map ID
  <rule-id>       Sequence to insert or delete from the route-map

## nv unset router policy route-map <route-map-id> rule <rule-id> set metric

### Usage

  nv unset router policy route-map <route-map-id> rule <rule-id> set metric [options]

### Description

  Metric value for destination routing protocol

### Identifiers

  <route-map-id>  Route Map ID
  <rule-id>       Sequence to insert or delete from the route-map

## nv unset router policy route-map <route-map-id> rule <rule-id> set metric-type

### Usage

  nv unset router policy route-map <route-map-id> rule <rule-id> set metric-type [options]

### Description

  Type of metric

### Identifiers

  <route-map-id>  Route Map ID
  <rule-id>       Sequence to insert or delete from the route-map

## nv unset router policy route-map <route-map-id> rule <rule-id> set origin

### Usage

  nv unset router policy route-map <route-map-id> rule <rule-id> set origin [options]

### Description

  BGP origin

### Identifiers

  <route-map-id>  Route Map ID
  <rule-id>       Sequence to insert or delete from the route-map

## nv unset router policy route-map <route-map-id> rule <rule-id> set tag

### Usage

  nv unset router policy route-map <route-map-id> rule <rule-id> set tag [options]

### Description

  Tag value for routing protocol

### Identifiers

  <route-map-id>  Route Map ID
  <rule-id>       Sequence to insert or delete from the route-map

## nv unset router policy route-map <route-map-id> rule <rule-id> set ipv6-nexthop-global

### Usage

  nv unset router policy route-map <route-map-id> rule <rule-id> set ipv6-nexthop-global [options]

### Description

  IPv6 nexthop global address

### Identifiers

  <route-map-id>  Route Map ID
  <rule-id>       Sequence to insert or delete from the route-map

## nv unset router policy route-map <route-map-id> rule <rule-id> set ipv6-nexthop-local

### Usage

  nv unset router policy route-map <route-map-id> rule <rule-id> set ipv6-nexthop-local [options]

### Description

  IPv6 nexthop local address

### Identifiers

  <route-map-id>  Route Map ID
  <rule-id>       Sequence to insert or delete from the route-map

## nv unset router policy route-map <route-map-id> rule <rule-id> set ipv6-nexthop-prefer-global

### Usage

  nv unset router policy route-map <route-map-id> rule <rule-id> set ipv6-nexthop-prefer-global [options]

### Description

  Prefer to use the global address as the IPV6 nexthop

### Identifiers

  <route-map-id>  Route Map ID
  <rule-id>       Sequence to insert or delete from the route-map

## nv unset router policy route-map <route-map-id> rule <rule-id> set ip-nexthop

### Usage

  nv unset router policy route-map <route-map-id> rule <rule-id> set ip-nexthop [options]

### Description

  IP nexthop

### Identifiers

  <route-map-id>  Route Map ID
  <rule-id>       Sequence to insert or delete from the route-map

## nv unset router policy route-map <route-map-id> rule <rule-id> set source-ip

### Usage

  nv unset router policy route-map <route-map-id> rule <rule-id> set source-ip [options]

### Description

  Source IP address

### Identifiers

  <route-map-id>  Route Map ID
  <rule-id>       Sequence to insert or delete from the route-map

## nv unset router policy route-map <route-map-id> rule <rule-id> set community-delete-list

### Usage

  nv unset router policy route-map <route-map-id> rule <rule-id> set community-delete-list [options]

### Description

  Delete community list

### Identifiers

  <route-map-id>  Route Map ID
  <rule-id>       Sequence to insert or delete from the route-map

## nv unset router policy route-map <route-map-id> rule <rule-id> set large-community-delete-list

### Usage

  nv unset router policy route-map <route-map-id> rule <rule-id> set large-community-delete-list [options]

### Description

  Delete large community list

### Identifiers

  <route-map-id>  Route Map ID
  <rule-id>       Sequence to insert or delete from the route-map

## nv unset router policy route-map <route-map-id> rule <rule-id> action

### Usage

  nv unset router policy route-map <route-map-id> rule <rule-id> action [options] [<attribute> ...]

### Description

  Route map rule action

### Identifiers

  <route-map-id>  Route Map ID
  <rule-id>       Sequence to insert or delete from the route-map

### Atrributes

  deny            Deny action
  permit          Permit action

## nv unset router policy route-map <route-map-id> rule <rule-id> action deny

### Usage

  nv unset router policy route-map <route-map-id> rule <rule-id> action deny [options]

### Description

  State details

### Identifiers

  <route-map-id>  Route Map ID
  <rule-id>       Sequence to insert or delete from the route-map

## nv unset router policy route-map <route-map-id> rule <rule-id> action permit

### Usage

  nv unset router policy route-map <route-map-id> rule <rule-id> action permit [options] [<attribute> ...]

### Description

  permit action

### Identifiers

  <route-map-id>  Route Map ID
  <rule-id>       Sequence to insert or delete from the route-map

### Atrributes

  exit-policy     Permit action exit policy

## nv unset router policy route-map <route-map-id> rule <rule-id> action permit exit-policy

### Usage

  nv unset router policy route-map <route-map-id> rule <rule-id> action permit exit-policy [options] [<attribute> ...]

### Description

  Permit action exit policy

### Identifiers

  <route-map-id>  Route Map ID
  <rule-id>       Sequence to insert or delete from the route-map

### Atrributes

  rule            jump to specific rule

## nv unset router policy route-map <route-map-id> rule <rule-id> action permit exit-policy rule

### Usage

  nv unset router policy route-map <route-map-id> rule <rule-id> action permit exit-policy rule [options]

### Description

  jump to specific rule

### Identifiers

  <route-map-id>  Route Map ID
  <rule-id>       Sequence to insert or delete from the route-map

## nv unset router bgp

### Usage

  nv unset router bgp [options] [<attribute> ...]

### Description

  BGP global configuration.

### Atrributes

  graceful-restart     BGP Graceful restart global configuration.
  convergence-wait     BGP Graceful restart global configuration.
  enable               Turn the feature 'on' or 'off'. The default is 'off'.
  autonomous-system    ASN for all VRFs, if a single AS is in use. If "none",
                       then ASN must be set for every VRF. This is the
                       default.
  graceful-shutdown    Graceful shutdown enable will initiate the GSHUT
                       community to be announced to all EBGP peers in all
                       instances and low LOCAL_PREF to all IBGP peers in all
                       instances.
  policy-update-timer  Wait time in seconds before processing updates to
                       policies to ensure that a series of changes are
                       processed together.
  router-id            BGP router-id for all VRFs, if a common one is used. If
                       "none", then router-id must be set for every VRF. This
                       is the default.
  wait-for-install     bgp waits for routes to be installed into kernel/asic
                       before advertising

## nv unset router bgp graceful-restart

### Usage

  nv unset router bgp graceful-restart [options] [<attribute> ...]

### Description

  BGP Graceful restart global configuration.

### Atrributes

  mode                  Role of router during graceful restart. helper-only,
                        router is in helper role. full, router is in both
                        helper and restarter role. off, GR is disabled for the
                        router
  path-selection-deferral-time
                        Used by the restarter as an upper-bounds for waiting
                        for peering establishment and end-of-RIB from peers
                        post restart before it starts path-selection.
  restart-time          Amount of time taken to restart by router. It is
                        advertised to the peer
  stale-routes-time     Specifies an upper-bounds on how long we retain routes
                        from a restarting peer before flusing them.

## nv unset router bgp graceful-restart mode

### Usage

  nv unset router bgp graceful-restart mode [options]

### Description

  Role of router during graceful restart. helper-only, router is in helper role. full, router is in both helper and restarter role. off, GR is disabled for the router



## nv unset router bgp graceful-restart restart-time

### Usage

  nv unset router bgp graceful-restart restart-time [options]

### Description

  Amount of time taken to restart by router. It is advertised to the peer



## nv unset router bgp graceful-restart path-selection-deferral-time

### Usage

  nv unset router bgp graceful-restart path-selection-deferral-time [options]

### Description

  Used by the restarter as an upper-bounds for waiting for peering establishment and end-of-RIB from peers post restart before it starts path-selection.



## nv unset router bgp graceful-restart stale-routes-time

### Usage

  nv unset router bgp graceful-restart stale-routes-time [options]

### Description

  Specifies an upper-bounds on how long we retain routes from a restarting peer before flusing them.



## nv unset router bgp convergence-wait

### Usage

  nv unset router bgp convergence-wait [options] [<attribute> ...]

### Description

  BGP Graceful restart global configuration.

### Atrributes

  establish-wait-time  Maximum time to wait to establish BGP sessions. Any
                       peers which do not come up in this time are not tracked
                       for the convergence-wait purposes. 0 value means there
                       is no max time and peers are tracked for convergence
                       time.
  time                 Time to wait for peers to send end-of-RIB before router
                       performs path selection, install and advertisement.
                       This is used during startup or when all peerings are
                       flapped. 0 value means wait time is not configured

## nv unset router bgp convergence-wait time

### Usage

  nv unset router bgp convergence-wait time [options]

### Description

  Time to wait for peers to send end-of-RIB before router performs path selection, install and advertisement. This is used during startup or when all peerings are flapped. 0 value means wait time is not configured



## nv unset router bgp convergence-wait establish-wait-time

### Usage

  nv unset router bgp convergence-wait establish-wait-time [options]

### Description

  Maximum time to wait to establish BGP sessions. Any peers which do not come up in this time are not tracked for the convergence-wait purposes. 0 value means there is no max time and peers are tracked for convergence time.



## nv unset router bgp enable

### Usage

  nv unset router bgp enable [options]

### Description

  Turn the feature 'on' or 'off'.  The default is 'off'.



## nv unset router bgp autonomous-system

### Usage

  nv unset router bgp autonomous-system [options]

### Description

  ASN for all VRFs, if a single AS is in use.  If "none", then ASN must be set for every VRF.  This is the default.



## nv unset router bgp router-id

### Usage

  nv unset router bgp router-id [options]

### Description

  BGP router-id for all VRFs, if a common one is used.  If "none", then router-id must be set for every VRF.  This is the default.



## nv unset router bgp policy-update-timer

### Usage

  nv unset router bgp policy-update-timer [options]

### Description

  Wait time in seconds before processing updates to policies to ensure that a series of changes are processed together.



## nv unset router bgp graceful-shutdown

### Usage

  nv unset router bgp graceful-shutdown [options]

### Description

  Graceful shutdown enable will initiate the GSHUT community to be announced to all EBGP peers in all instances and low LOCAL_PREF to all IBGP peers in all instances.



## nv unset router bgp wait-for-install

### Usage

  nv unset router bgp wait-for-install [options]

### Description

  bgp waits for routes to be installed into kernel/asic before advertising



## nv unset router ospf

### Usage

  nv unset router ospf [options] [<attribute> ...]

### Description

  OSPF global configuration.

### Atrributes

  timers      Timers
  enable      Turn the feature 'on' or 'off'. The default is 'off'.
  router-id   OSPF router-id for all VRFs, if a common one is used. If "none",
              then router-id must be set for every VRF. This is the default.



## nv unset router ospf timers

### Usage

  nv unset router ospf timers [options] [<attribute> ...]

### Description

  Timers

### Atrributes

  lsa         LSA timers
  spf         SPF timers
  refresh     defines interval (sec) to re-send lsas to keep from aging out.



## nv unset router ospf timers lsa

### Usage

  nv unset router ospf timers lsa [options] [<attribute> ...]

### Description

  LSA timers

### Atrributes

  min-arrival  Minimum delay in receiving new version of a LSA.
  throttle     Delay (msec) between sending LSAs.

## nv unset router ospf timers lsa min-arrival

### Usage

  nv unset router ospf timers lsa min-arrival [options]

### Description

  Minimum delay in receiving new version of a LSA.



## nv unset router ospf timers lsa throttle

### Usage

  nv unset router ospf timers lsa throttle [options]

### Description

  Delay (msec) between sending LSAs.



## nv unset router ospf timers spf

### Usage

  nv unset router ospf timers spf [options] [<attribute> ...]

### Description

  SPF timers

### Atrributes

  delay         Delay (msec) from first change received till SPF calculation.
  holdtime      Initial hold time (msec) between consecutive SPF calculations.
  max-holdtime  Maximum hold time (msec) between consecutive SPF calculations.

## nv unset router ospf timers spf delay
### Usage

  nv unset router ospf timers spf delay [options]

### Description

  Delay (msec) from first change received till SPF calculation.

## nv unset router ospf timers spf holdtime
### Usage

  nv unset router ospf timers spf holdtime [options]

### Description

  Initial hold time (msec) between consecutive SPF calculations.

## nv unset router ospf timers spf max-holdtime
### Usage

  nv unset router ospf timers spf max-holdtime [options]

### Description

  Maximum hold time (msec) between consecutive SPF calculations.

## nv unset router ospf timers refresh
### Usage

  nv unset router ospf timers refresh [options]

### Description

  defines interval (sec) to re-send lsas to keep from aging out.

## nv unset router ospf enable
### Usage

  nv unset router ospf enable [options]

### Description

  Turn the feature 'on' or 'off'.  The default is 'off'.

## nv unset router ospf router-id
### Usage

  nv unset router ospf router-id [options]

### Description

  OSPF router-id for all VRFs, if a common one is used.  If "none", then router-id must be set for every VRF.  This is the default.

## nv unset router pim
### Usage

  nv unset router pim [options] [<attribute> ...]

### Description

  PIM global configuration.

### Atrributes

  timers      Timers
  enable      Turn the feature 'on' or 'off'. The default is 'off'.
  packets     Number of incoming packet processing from neighbor.

## nv unset router pim timers
### Usage

  nv unset router pim timers [options] [<attribute> ...]

### Description

  Timers

### Atrributes

  hello-interval       PIM Hello packets periodic interval. Holdtime is 3.5
                       times the hello-interval, the amount of time neighbor
                       must kept in reachable state.
  join-prune-interval  Periodic multicast Join/Prune msg, in seconds
  keep-alive           Timeout value for S,G stream, in seconds
  register-suppress    FHR supresses the register msg transmit to RP, in
                       seconds
  rp-keep-alive        RP's timeout value, in seconds

## nv unset router pim timers hello-interval
### Usage

  nv unset router pim timers hello-interval [options]

### Description

  PIM Hello packets periodic interval. Holdtime is 3.5 times the hello-interval, the amount of time neighbor must kept in reachable state.

## nv unset router pim timers register-suppress
### Usage

  nv unset router pim timers register-suppress [options]

### Description

  FHR supresses the register msg transmit to RP, in seconds

## nv unset router pim timers join-prune-interval
### Usage

  nv unset router pim timers join-prune-interval [options]

### Description

  Periodic multicast Join/Prune msg, in seconds

## nv unset router pim timers keep-alive
### Usage

  nv unset router pim timers keep-alive [options]

### Description

  Timeout value for S,G stream, in seconds

## nv unset router pim timers rp-keep-alive
### Usage

  nv unset router pim timers rp-keep-alive [options]

### Description

  RP's timeout value, in seconds

## nv unset router pim enable
### Usage

  nv unset router pim enable [options]

### Description

  Turn the feature 'on' or 'off'.  The default is 'off'.

## nv unset router pim packets
### Usage

  nv unset router pim packets [options]

### Description

  Number of incoming packet processing from neighbor.

## nv unset router igmp
### Usage

  nv unset router igmp [options] [<attribute> ...]

### Description

  IGMP global configuration.

### Atrributes

  enable      Turn the feature 'on' or 'off'. The default is 'off'.

## nv unset router igmp enable

### Usage

  nv unset router igmp enable [options]

### Description

  Turn the feature 'on' or 'off'.  The default is 'off'.

## nv unset router vrrp
### Usage

  nv unset router vrrp [options] [<attribute> ...]

### Description

  VRRP global configuration.

### Atrributes

  enable                Turn the feature 'on' or 'off'. The default is 'off'.
  advertisement-interval
                        Sets the interval between successive VRRP
                        advertisements -- RFC 5798 defines this as a 12-bit
                        value expressed as 0.1 seconds, with default 1000
                        milliseconds, i.e., 1 second. Represented in units of
                        milliseconds
  preempt               When set to true, enables preemption by a higher
                        priority backup router of a lower priority master
                        router
  priority              Specifies the sending VRRP interface's priority for
                        the virtual router. Higher values equal higher
                        priority

## nv unset router vrrp enable
### Usage

  nv unset router vrrp enable [options]

### Description

  Turn the feature 'on' or 'off'.  The default is 'off'.

## nv unset router vrrp priority
### Usage

  nv unset router vrrp priority [options]

### Description

  Specifies the sending VRRP interface's priority for the virtual router. Higher values equal higher priority

## nv unset router vrrp preempt
### Usage

  nv unset router vrrp preempt [options]

### Description

  When set to true, enables preemption by a higher priority backup router of a lower priority master router

## nv unset router vrrp advertisement-interval
### Usage

  nv unset router vrrp advertisement-interval [options]

### Description

  Sets the interval between successive VRRP advertisements -- RFC 5798 defines this as a 12-bit value expressed as 0.1 seconds, with default 1000 milliseconds, i.e., 1 second. Represented in units of milliseconds

## nv unset router vrr
### Usage

  nv unset router vrr [options] [<attribute> ...]

### Description

  VRR global configuration.

### Atrributes

  enable      Turn the feature 'on' or 'off'. The default is 'off'.

## nv unset router vrr enable
### Usage

  nv unset router vrr enable [options]

### Description

  Turn the feature 'on' or 'off'.  The default is 'off'.

## nv unset router adaptive-routing
### Usage

  nv unset router adaptive-routing [options] [<attribute> ...]

### Description

  Adaptive routing global configuration.

### Atrributes

  enable      Turn the feature 'on' or 'off'. The default is 'off'.

## nv unset router adaptive-routing enable
### Usage

  nv unset router adaptive-routing enable [options]

### Description

  Turn the feature 'on' or 'off'.  The default is 'off'.

## nv unset platform
### Usage

  nv unset platform [options] [<attribute> ...]

### Description

  Top-level container for the components in the system. This node represents a system component inventory, which includes hardware and software elements.

### Atrributes

  hardware    The platform's hardware

## nv unset platform hardware
### Usage

  nv unset platform hardware [options] [<attribute> ...]

### Description

  Set of components making up the platform.

### Atrributes

  component   A component in the platform.

## nv unset platform hardware component
### Usage

  nv unset platform hardware component [options] [<component-id> ...]

### Description

  Set of components making up the platform.

### Identifiers

  <component-id>  Component identifier

## nv unset platform hardware component <component-id>

### Usage

  nv unset platform hardware component <component-id> [options] [<attribute> ...]

### Description

  A component in the platform.

### Identifiers

  <component-id>  Component identifier

### Atrributes

  linecard        Properties of a linecard component
  admin-state     The component's admin state
  type            The type of this component

## nv unset platform hardware component <component-id> linecard
### Usage

  nv unset platform hardware component <component-id> linecard [options] [<attribute> ...]

### Description

  Properties of a linecard component

### Identifiers

  <component-id>  Component identifier

### Atrributes

  provision       Provision linecard types

## nv unset platform hardware component <component-id> linecard provision
### Usage

  nv unset platform hardware component <component-id> linecard provision [options]

### Description

  Provision linecard types

### Identifiers

  <component-id>  Component identifier

## nv unset platform hardware component <component-id> type
### Usage

  nv unset platform hardware component <component-id> type [options]

### Description

  The type of this component

### Identifiers

  <component-id>  Component identifier

## nv unset platform hardware component <component-id> admin-state
### Usage

  nv unset platform hardware component <component-id> admin-state [options]

### Description

  The component's admin state

### Identifiers

  <component-id>  Component identifier

## nv unset bridge
### Usage

  nv unset bridge [options] [<attribute> ...]

### Description

  Properties associated with an instance of a bridge.

### Atrributes

  domain      Bridge domains

## nv unset bridge domain
### Usage

  nv unset bridge domain [options] [<domain-id> ...]

### Description

  Bridge domains

### Identifiers

  <domain-id>  Domain

## nv unset bridge domain <domain-id>

### Usage

  nv unset bridge domain <domain-id> [options] [<attribute> ...]

### Description

  Bridge domain

### Identifiers

  <domain-id>      Domain

### Atrributes

  stp              attributes related to global stp
  multicast        Configure multicast on the bridge
  vlan             Set of vlans in the bridge domain. Only applicable when the
                   domain type is "vlan-aware".
  encap            Interfaces added to this domain will, by default, use this
                   encapsulation.
  mac-address      Override global mac address
  type             Type of bridge domain.
  untagged         Interfaces added to this domain will, by default, be trunk
                   interfaces with a single untagged vlan. Untagged packets on
                   domain ports will be put in this vlan. If none, then
                   untagged packets will be dropped.
  vlan-vni-offset  A VNI offset while (automatically) mapping VLANs to VNIs

## nv unset bridge domain <domain-id> stp

### Usage

  nv unset bridge domain <domain-id> stp [options] [<attribute> ...]

### Description

  attributes related to global stp

### Identifiers

  <domain-id>  Domain

### Atrributes

  state        The state of STP on the bridge
  priority     stp priority. The priority value must be a number between 4096
               and 32768 and a multiple of 4096.

## nv unset bridge domain <domain-id> stp state
### Usage

  nv unset bridge domain <domain-id> stp state [options]

### Description

  The state of STP on the bridge

### Identifiers

  <domain-id>  Domain

## nv unset bridge domain <domain-id> stp priority
### Usage

  nv unset bridge domain <domain-id> stp priority [options]

### Description

  stp priority. The priority value must be a number between 4096 and 32768 and a multiple of 4096.

### Identifiers

  <domain-id>  Domain

## nv unset bridge domain <domain-id> multicast
### Usage

  nv unset bridge domain <domain-id> multicast [options] [<attribute> ...]

### Description

  Configure multicast on the bridge

### Identifiers

  <domain-id>  Domain

### Atrributes

  snooping     IGMP/MLD snooping configuration

## nv unset bridge domain <domain-id> multicast snooping

### Usage

  nv unset bridge domain <domain-id> multicast snooping [options] [<attribute> ...]

### Description

  IGMP/MLD snooping configuration

### Identifiers

  <domain-id>  Domain

### Atrributes

  querier      IGMP/MLD querier configuration
  enable       Turn the feature 'on' or 'off'. The default is 'off'.

## nv unset bridge domain <domain-id> multicast snooping querier
### Usage

  nv unset bridge domain <domain-id> multicast snooping querier [options] [<attribute> ...]

### Description

  IGMP/MLD querier configuration

### Identifiers

  <domain-id>  Domain

### Atrributes

  enable       Turn the feature 'on' or 'off'. The default is 'off'.

## nv unset bridge domain <domain-id> multicast snooping querier enable
### Usage

  nv unset bridge domain <domain-id> multicast snooping querier enable [options]

### Description

  Turn the feature 'on' or 'off'.  The default is 'off'.

### Identifiers

  <domain-id>  Domain

## nv unset bridge domain <domain-id> multicast snooping enable

### Usage

  nv unset bridge domain <domain-id> multicast snooping enable [options]

### Description

  Turn the feature 'on' or 'off'.  The default is 'off'.

### Identifiers

  <domain-id>  Domain

## nv unset bridge domain <domain-id> vlan <vid>
### Usage

  nv unset bridge domain <domain-id> vlan <vid> [options] [<attribute> ...]

### Description

  A VLAN tag identifier

### Identifiers

  <domain-id>  Domain
  <vid>        VLAN ID

### Atrributes

  vni          L2 VNI
  ptp          VLAN PTP configuration. Inherited by interfaces in this VLAN.
  multicast    Configure multicast on the vlan

## nv unset bridge domain <domain-id> vlan <vid> vni <vni-id>
### Usage

  nv unset bridge domain <domain-id> vlan <vid> vni <vni-id> [options] [<attribute> ...]

### Description

  VNI

### Identifiers

  <domain-id>   Domain
  <vid>         VLAN ID
  <vni-id>      VxLAN ID

### Atrributes

  flooding      Handling of BUM traffic
  mac-learning  Controls dynamic MAC learning over VXLAN tunnels based on
                received packets. This applies to all overlays (VNIs), but can
                be overridden by VNI-specific configuration.

## nv unset bridge domain <domain-id> vlan <vid> vni <vni-id> flooding
### Usage

  nv unset bridge domain <domain-id> vlan <vid> vni <vni-id> flooding [options] [<attribute> ...]

### Description

  Handling of BUM traffic

### Identifiers

  <domain-id>           Domain
  <vid>                 VLAN ID
  <vni-id>              VxLAN ID

### Atrributes

  head-end-replication  BUM traffic is replicated and individual copies sent
                        to remote destinations.
  enable                Turn the feature 'on', 'off', or 'auto'. The default
                        is 'auto'.
  multicast-group       BUM traffic is sent to the specified multicast group
                        and will be received by receivers who are interested
                        in that group. This usually requires PIM-SM to be used
                        in the network.

## nv unset bridge domain <domain-id> vlan <vid> vni <vni-id> flooding head-end-replication <hrep-id>
### Usage

  nv unset bridge domain <domain-id> vlan <vid> vni <vni-id> flooding head-end-replication <hrep-id> [options]

### Description

  Set of IPv4 unicast addresses or "evpn".

### Identifiers

  <domain-id>  Domain
  <vid>        VLAN ID
  <vni-id>     VxLAN ID
  <hrep-id>    IPv4 unicast addresses or "evpn"

## nv unset bridge domain <domain-id> vlan <vid> vni <vni-id> flooding enable

### Usage

  nv unset bridge domain <domain-id> vlan <vid> vni <vni-id> flooding enable [options]

### Description

  Turn the feature 'on', 'off', or 'auto'.  The default is 'auto'.

### Identifiers

  <domain-id>  Domain
  <vid>        VLAN ID
  <vni-id>     VxLAN ID

## nv unset bridge domain <domain-id> vlan <vid> vni <vni-id> flooding multicast-group
### Usage

  nv unset bridge domain <domain-id> vlan <vid> vni <vni-id> flooding multicast-group [options]

### Description

  BUM traffic is sent to the specified multicast group and will be received by receivers who are interested in that group. This usually requires PIM-SM to be used in the network.

### Identifiers

  <domain-id>  Domain
  <vid>        VLAN ID
  <vni-id>     VxLAN ID

## nv unset bridge domain <domain-id> vlan <vid> vni <vni-id> mac-learning
### Usage

  nv unset bridge domain <domain-id> vlan <vid> vni <vni-id> mac-learning [options]

### Description

  Controls dynamic MAC learning over VXLAN tunnels based on received packets. This applies to all overlays (VNIs), but can be overridden by VNI-specific configuration.

### Identifiers

  <domain-id>  Domain
  <vid>        VLAN ID
  <vni-id>     VxLAN ID

## nv unset bridge domain <domain-id> vlan <vid> ptp
### Usage

  nv unset bridge domain <domain-id> vlan <vid> ptp [options] [<attribute> ...]

### Description

  VLAN PTP configuration.  Inherited by interfaces in this VLAN.

### Identifiers

  <domain-id>  Domain
  <vid>        VLAN ID

### Atrributes

  enable       Turn the feature 'on' or 'off'. The default is 'off'.

## nv unset bridge domain <domain-id> vlan <vid> ptp enable
### Usage

  nv unset bridge domain <domain-id> vlan <vid> ptp enable [options]

### Description

  Turn the feature 'on' or 'off'.  The default is 'off'.

### Identifiers

  <domain-id>  Domain
  <vid>        VLAN ID

## nv unset bridge domain <domain-id> vlan <vid> multicast
### Usage

  nv unset bridge domain <domain-id> vlan <vid> multicast [options] [<attribute> ...]

### Description

  Configure multicast on the vlan

### Identifiers

  <domain-id>  Domain
  <vid>        VLAN ID

### Atrributes

  snooping     IGMP/MLD snooping configuration

## nv unset bridge domain <domain-id> vlan <vid> multicast snooping
### Usage

  nv unset bridge domain <domain-id> vlan <vid> multicast snooping [options] [<attribute> ...]

### Description

  IGMP/MLD snooping configuration

### Identifiers

  <domain-id>  Domain
  <vid>        VLAN ID

### Atrributes

  querier      IGMP/MLD querier configuration

## nv unset bridge domain <domain-id> vlan <vid> multicast snooping querier

### Usage

  nv unset bridge domain <domain-id> vlan <vid> multicast snooping querier [options] [<attribute> ...]

### Description

  IGMP/MLD querier configuration

### Identifiers

  <domain-id>  Domain
  <vid>        VLAN ID

### Atrributes

  source-ip    Source IP to use when sending IGMP/MLD queries.

## nv unset bridge domain <domain-id> vlan <vid> multicast snooping querier source-ip

### Usage

  nv unset bridge domain <domain-id> vlan <vid> multicast snooping querier source-ip [options]

### Description

  Source IP to use when sending IGMP/MLD queries.

### Identifiers

  <domain-id>  Domain
  <vid>        VLAN ID

## nv unset bridge domain <domain-id> type

### Usage

  nv unset bridge domain <domain-id> type [options]

### Description

  Type of bridge domain.

### Identifiers

  <domain-id>  Domain

## nv unset bridge domain <domain-id> untagged
### Usage

  nv unset bridge domain <domain-id> untagged [options]

### Description

  Interfaces added to this domain will, by default, be trunk interfaces with a single untagged vlan. Untagged packets on domain ports will be put in this vlan.  If none, then untagged packets will be dropped.

### Identifiers

  <domain-id>  Domain

## nv unset bridge domain <domain-id> encap
### Usage

  nv unset bridge domain <domain-id> encap [options]

### Description

  Interfaces added to this domain will, by default, use this encapsulation.

### Identifiers

  <domain-id>  Domain

## nv unset bridge domain <domain-id> mac-address
### Usage

  nv unset bridge domain <domain-id> mac-address [options]

### Description

  Override global mac address

### Identifiers

  <domain-id>  Domain

## nv unset bridge domain <domain-id> vlan-vni-offset
### Usage

  nv unset bridge domain <domain-id> vlan-vni-offset [options]

### Description

  A VNI offset while (automatically) mapping VLANs to VNIs

### Identifiers

  <domain-id>  Domain

## nv unset mlag
### Usage

  nv unset mlag [options] [<attribute> ...]

### Description

  Global Multi-chassis Link Aggregation properties

### Atrributes

  lacp-conflict  Configure the mlag lacp-conflict parameters
  backup         Set of MLAG backups
  enable         Turn the feature 'on' or 'off'. The default is 'off'.
  debug          Enable MLAG debugging
  init-delay     The delay, in seconds, before bonds are brought up.
  mac-address    Override anycast-mac and anycast-id
  peer-ip        Peer Ip Address
  priority       Mlag Priority

## nv unset mlag lacp-conflict

### Usage

  nv unset mlag lacp-conflict [options]

### Description

  Configure the mlag lacp-conflict parameters



## nv unset mlag backup

### Usage

  nv unset mlag backup [options] [<backup-ip> ...]

### Description

  Set of MLAG backups

### Identifiers

  <backup-ip>  Backup IP of MLAG peer

## nv unset mlag backup <backup-ip>

### Usage

  nv unset mlag backup <backup-ip> [options] [<attribute> ...]

### Description

  alternative ip address or interface for peer to reach us

### Identifiers

  <backup-ip>  Backup IP of MLAG peer

### Atrributes

  vrf          The backup IP's VRF.

## nv unset mlag backup <backup-ip> vrf

### Usage

  nv unset mlag backup <backup-ip> vrf [options]

### Description

  The backup IP's VRF.

### Identifiers

  <backup-ip>  Backup IP of MLAG peer

## nv unset mlag enable

### Usage

  nv unset mlag enable [options]

### Description

  Turn the feature 'on' or 'off'.  The default is 'off'.



## nv unset mlag mac-address

### Usage

  nv unset mlag mac-address [options]

### Description

  Override anycast-mac and anycast-id



## nv unset mlag peer-ip

### Usage

  nv unset mlag peer-ip [options]

### Description

  Peer Ip Address



## nv unset mlag priority

### Usage

  nv unset mlag priority [options]

### Description

  Mlag Priority



## nv unset mlag init-delay

### Usage

  nv unset mlag init-delay [options]

### Description

  The delay, in seconds, before bonds are brought up.



## nv unset mlag debug

### Usage

  nv unset mlag debug [options]

### Description

  Enable MLAG debugging



## nv unset evpn

### Usage

  nv unset evpn [options] [<attribute> ...]

### Description

  Enables the EVPN control plane.  When enabled, it also means that the EVPN service offered is vlan-based service and an EVI is auto-created for each extended VLAN.

### Atrributes

  route-advertise  Route advertising
  dad              Advertise
  evi              EVI
  multihoming      Multihoming global configuration parameters
  enable           Turn the feature 'on' or 'off'. The default is 'off'.

## nv unset evpn route-advertise

### Usage

  nv unset evpn route-advertise [options] [<attribute> ...]

### Description

  Route dvertising

### Atrributes

  default-gateway  This configuration should be turned 'on' only in a
                   centralized-routing deployment and only on the centralized
                   GW router(s). If 'on', the IP addresses of SVIs in all EVIs
                   are announced as type-2 routes with the gateway extended
                   community. The purpose is for remote L2-only VTEPs to do
                   ARP suppression and for hosts to learn of the gateway's IP
                   to MAC binding.
  nexthop-setting  Specifies the next hop IP and MAC (Router MAC) to use in
                   the advertisement of type-5 routes and “self” type-2 routes
                   (“self” = SVI IP/MAC). Relevant only in an MLAG
                   configuration.
  svi-ip           If 'on', the IP addresses of SVIs in all EVIs are announced
                   as type-2 routes. This configuration should not be enabled
                   if SVI IPs are reused in the network.

## nv unset evpn route-advertise nexthop-setting

### Usage

  nv unset evpn route-advertise nexthop-setting [options]

### Description

  Specifies the next hop IP and MAC (Router MAC) to use in the advertisement of type-5 routes and “self” type-2 routes (“self” = SVI IP/MAC).  Relevant only in an MLAG configuration.



## nv unset evpn route-advertise svi-ip

### Usage

  nv unset evpn route-advertise svi-ip [options]

### Description

  If 'on', the IP addresses of SVIs in all EVIs are announced as type-2 routes.  This configuration should not be enabled if SVI IPs are reused in the network.



## nv unset evpn route-advertise default-gateway

### Usage

  nv unset evpn route-advertise default-gateway [options]

### Description

  This configuration should be turned 'on' only in a centralized-routing deployment and only on the centralized GW router(s).  If 'on', the IP addresses of SVIs in all EVIs are announced as type-2 routes with the gateway extended community. The purpose is for remote L2-only VTEPs to do ARP suppression and for hosts to learn of the gateway's IP to MAC binding.



## nv unset evpn dad

### Usage

  nv unset evpn dad [options] [<attribute> ...]

### Description

  Duplicate address detection

### Atrributes

  duplicate-action    Action to take when a MAC is flagged as a possible
                      duplicate. If 'warning-only', generates a log message.
                      If 'freeze', further move events for the MAC will not be
                      acted upon.
  enable              Turn the feature 'on' or 'off'. The default is 'off'.
  mac-move-threshold  Number of MAC moves within a time window before the MAC
                      is flagged as a possible duplicate.
  move-window         Time window during which the move threshold applies




## nv unset evpn dad duplicate-action

### Usage

  nv unset evpn dad duplicate-action [options] [<attribute> ...]

### Description

  Handling of BUM traffic

### Atrributes

  freeze      Further move events for the MAC will not be acted upon.



## nv unset evpn dad duplicate-action freeze

### Usage

  nv unset evpn dad duplicate-action freeze [options] [<attribute> ...]

### Description

  Advertise

### Atrributes

  duration    Freeze the MAC for the specified duration or, if 'permanent'
              until the operator intervenes.



## nv unset evpn dad duplicate-action freeze duration

### Usage

  nv unset evpn dad duplicate-action freeze duration [options]

### Description

  Freeze the MAC for the specified duration or, if 'permanent' until the operator intervenes.



## nv unset evpn dad enable

### Usage

  nv unset evpn dad enable [options]

### Description

  Turn the feature 'on' or 'off'.  The default is 'off'.



## nv unset evpn dad mac-move-threshold

### Usage

  nv unset evpn dad mac-move-threshold [options]

### Description

  Number of MAC moves within a time window before the MAC is flagged as a possible duplicate.



## nv unset evpn dad move-window

### Usage

  nv unset evpn dad move-window [options]

### Description

  Time window during which the move threshold applies



## nv unset evpn evi

### Usage

  nv unset evpn evi [options] [<evi-id> ...]

### Description

  EVIs

### Identifiers

  <evi-id>    VRF



## nv unset evpn evi <evi-id>

### Usage

  nv unset evpn evi <evi-id> [options] [<attribute> ...]

### Description

  Enables the EVPN control plane.  When enabled, it also means that the EVPN service offered is vlan-based service and an EVI is auto-created for each extended VLAN.

### Identifiers

  <evi-id>         VRF

### Atrributes

  route-advertise  Route advertise
  route-target     Route targets
  rd               BGP Route Distinguisher to use for EVPN type-5 routes
                   originated for this VRF.

## nv unset evpn evi <evi-id> route-advertise

### Usage

  nv unset evpn evi <evi-id> route-advertise [options] [<attribute> ...]

### Description

  Route advertise

### Identifiers

  <evi-id>         VRF

### Atrributes

  default-gateway  If 'auto', inherit from global config. This is the default.
                   This configuration should be turned 'on' only in a
                   centralized-routing deployment and only on the centralized
                   GW router(s). If 'on', the IP addresses of SVIs in all EVIs
                   are announced as type-2 routes with the gateway extended
                   community. The purpose is for remote L2-only VTEPs to do
                   ARP suppression and for hosts to learn of the gateway's IP
                   to MAC binding.
  svi-ip           If 'auto', inherit from global config. This is the default.
                   If 'on', the IP addresses of SVIs in all EVIs are announced
                   as type-2 routes. This configuration should not be enabled
                   if SVI IPs are reused in the network.

## nv unset evpn evi <evi-id> route-advertise svi-ip

### Usage

  nv unset evpn evi <evi-id> route-advertise svi-ip [options]

### Description

  If 'auto', inherit from global config.  This is the default.  If 'on', the IP addresses of SVIs in all EVIs are announced as type-2 routes.  This configuration should not be enabled if SVI IPs are reused in the network.

### Identifiers

  <evi-id>    VRF



## nv unset evpn evi <evi-id> route-advertise default-gateway

### Usage

  nv unset evpn evi <evi-id> route-advertise default-gateway [options]

### Description

  If 'auto', inherit from global config.  This is the default. This configuration should be turned 'on' only in a centralized-routing deployment and only on the centralized GW router(s).  If 'on', the IP addresses of SVIs in all EVIs are announced as type-2 routes with the gateway extended community. The purpose is for remote L2-only VTEPs to do ARP suppression and for hosts to learn of the gateway's IP to MAC binding.

### Identifiers

  <evi-id>    VRF



## nv unset evpn evi <evi-id> route-target

### Usage

  nv unset evpn evi <evi-id> route-target [options] [<attribute> ...]

### Description

  EVPN control plane config and info for VRF

### Identifiers

  <evi-id>    VRF

### Atrributes

  export      Route targets to export
  import      Route targets to import
  both        Route targets to import and export



## nv unset evpn evi <evi-id> route-target export

### Usage

  nv unset evpn evi <evi-id> route-target export [options] [<rt-id> ...]

### Description

  Set of route target identifiers

### Identifiers

  <evi-id>    VRF
  <rt-id>     Route target ID



## nv unset evpn evi <evi-id> route-target export <rt-id>

### Usage

  nv unset evpn evi <evi-id> route-target export <rt-id> [options]

### Description

  A route target identifier

### Identifiers

  <evi-id>    VRF
  <rt-id>     Route target ID



## nv unset evpn evi <evi-id> route-target import

### Usage

  nv unset evpn evi <evi-id> route-target import [options] [<rt-id> ...]

### Description

  Set of route target identifiers

### Identifiers

  <evi-id>    VRF
  <rt-id>     Route target ID



## nv unset evpn evi <evi-id> route-target import <rt-id>

### Usage

  nv unset evpn evi <evi-id> route-target import <rt-id> [options]

### Description

  A route target identifier

### Identifiers

  <evi-id>    VRF
  <rt-id>     Route target ID



## nv unset evpn evi <evi-id> route-target both

### Usage

  nv unset evpn evi <evi-id> route-target both [options] [<rt-id> ...]

### Description

  Set of route target identifiers

### Identifiers

  <evi-id>    VRF
  <rt-id>     Route target ID



## nv unset evpn evi <evi-id> route-target both <rt-id>

### Usage

  nv unset evpn evi <evi-id> route-target both <rt-id> [options]

### Description

  A route target identifier

### Identifiers

  <evi-id>    VRF
  <rt-id>     Route target ID



## nv unset evpn evi <evi-id> rd

### Usage

  nv unset evpn evi <evi-id> rd [options]

### Description

  BGP Route Distinguisher to use for EVPN type-5 routes originated for this VRF.

### Identifiers

  <evi-id>    VRF



## nv unset evpn multihoming

### Usage

  nv unset evpn multihoming [options] [<attribute> ...]

### Description

  Multihoming global configuration parameters

### Atrributes

  ead-evi-route      Ethernet Auto-discovery per EVPN instance routes
  segment            Multihoming interface segment
  enable             Turn the feature 'on' or 'off'. The default is 'off'.
  mac-holdtime       During this interval, the switch attempts to
                     independently establish reachability of the MAC on the
                     local ethernet segment. If 'none', there is no holdtime.
  neighbor-holdtime  During this interval, the switch attempts to
                     independently establish reachability of the host on the
                     local ethernet segment.
  startup-delay      The duration for which a switch holds the Ethernet
                     segment-bond in a protodown state after a reboot or
                     process restart.

## nv unset evpn multihoming ead-evi-route

### Usage

  nv unset evpn multihoming ead-evi-route [options] [<attribute> ...]

### Description

  Ethernet Auto-discovery per EVPN instance routes

### Atrributes

  rx          Disable EAD-per-EVI at receiving end.
  tx          Suppress advertisement of EAD-per-EVI routes.



## nv unset evpn multihoming ead-evi-route rx

### Usage

  nv unset evpn multihoming ead-evi-route rx [options]

### Description

  Disable EAD-per-EVI at receiving end.



## nv unset evpn multihoming ead-evi-route tx

### Usage

  nv unset evpn multihoming ead-evi-route tx [options]

### Description

  Suppress advertisement of EAD-per-EVI routes.



## nv unset evpn multihoming segment

### Usage

  nv unset evpn multihoming segment [options] [<attribute> ...]

### Description

  Multihoming interface segment

### Atrributes

  df-preference  Designated forwarder preference value.
  mac-address    MAC address per ethernet segment. Required.

## nv unset evpn multihoming segment mac-address
### Usage

  nv unset evpn multihoming segment mac-address [options]

### Description

  MAC address per ethernet segment.  Required.

## nv unset evpn multihoming segment df-preference
### Usage

  nv unset evpn multihoming segment df-preference [options]

### Description

  Designated forwarder preference value.

## nv unset evpn multihoming enable
### Usage

  nv unset evpn multihoming enable [options]

### Description

  Turn the feature 'on' or 'off'.  The default is 'off'.

## nv unset evpn multihoming mac-holdtime
### Usage

  nv unset evpn multihoming mac-holdtime [options]

### Description

  During this interval, the switch attempts to independently establish reachability of the MAC on the local ethernet segment. If 'none', there is no holdtime.

## nv unset evpn multihoming neighbor-holdtime
### Usage

  nv unset evpn multihoming neighbor-holdtime [options]

### Description

  During this interval, the switch attempts to independently establish reachability of the host on the local ethernet segment.

## nv unset evpn multihoming startup-delay
### Usage

  nv unset evpn multihoming startup-delay [options]

### Description

  The duration for which a switch holds the Ethernet segment-bond in a protodown state after a reboot or process restart.

## nv unset evpn enable
### Usage

  nv unset evpn enable [options]

### Description

  Turn the feature 'on' or 'off'.  The default is 'off'.

## nv unset qos
### Usage

  nv unset qos [options] [<attribute> ...]

### Description

  QOS

### Atrributes

  roce        Properties associated with the RDMA over Converged Ethernet
              (RoCE) feature.

## nv unset qos roce
### Usage

  nv unset qos roce [options] [<attribute> ...]

### Description

  Properties associated with the RDMA over Converged Ethernet (RoCE) feature.

### Atrributes

  enable        Turn the feature 'on' or 'off'. The default is 'off'.
  mode          Roce Mode
  cable-length  Cable Length(in meters) for Roce Lossless Config

## nv unset qos roce enable
### Usage

  nv unset qos roce enable [options]

### Description

  Turn the feature 'on' or 'off'.  The default is 'off'.

## nv unset qos roce mode
### Usage

  nv unset qos roce mode [options]

### Description

  Roce Mode

## nv unset qos roce cable-length
### Usage

  nv unset qos roce cable-length [options]

### Description

  Cable Length(in meters) for Roce Lossless Config

## nv unset interface
### Usage

  nv unset interface [options] [<interface-id> ...]

### Description

  Interfaces

### Identifiers

  <interface-id>  Interface

## nv unset interface <interface-id>
### Usage

  nv unset interface <interface-id> [options] [<attribute> ...]

### Description

  An interface

### Identifiers

  <interface-id>  Interface

### Atrributes

  router          interface router
  bond            The state of the interface
  bridge          attributed related to a bridged interface
  ip              IP configuration for an interface
  lldp            LLDP on for an interface
  link            An physical interface
  evpn            EVPN control plane config and info for VRF
  acl             Interface ACL rules
  ptp             Interface Specific PTP configuration.
  tunnel          The state of the interface
  base-interface  The interface under this interface
  description     Details about the interface
  type            The type of interface
  vlan            VLAN ID

## nv unset interface <interface-id> router
### Usage

  nv unset interface <interface-id> router [options] [<attribute> ...]

### Description

  interface router

### Identifiers

  <interface-id>    Interface

### Atrributes

  pbr               PBR interface configuration.
  ospf              OSPF interface configuration.
  pim               PIM interface configuration.
  adaptive-routing  Adaptive routing interface configuration.

## nv unset interface <interface-id> router pbr

### Usage

  nv unset interface <interface-id> router pbr [options] [<attribute> ...]

### Description

  PBR interface configuration.

### Identifiers

  <interface-id>  Interface

### Atrributes

  map             PBR map to use on this interface

## nv unset interface <interface-id> router pbr map <pbr-map-id>

### Usage

  nv unset interface <interface-id> router pbr map <pbr-map-id> [options]

### Description

  Interface Pbr map

### Identifiers

  <interface-id>  Interface
  <pbr-map-id>    Route Map ID

## nv unset interface <interface-id> router ospf

### Usage

  nv unset interface <interface-id> router ospf [options] [<attribute> ...]

### Description

  OSPF interface configuration.

### Identifiers

  <interface-id>  Interface

### Atrributes

  timers          Timers configuration
  authentication  md5 authentication configuration
  bfd             BFD configuration
  enable          Turn the feature 'on' or 'off'. The default is 'off'.
  area            Area number for enabling ospf on this interface.
  cost            The cost of this link the router lsa. If `auto`, determine
                  the cost based on link speed. This is the default.
  mtu-ignore      Do not test mtu matching for peering.
  network-type    Network type.
  passive         Stops the creation of peers on this interface
  priority        Eligibility of this router to become DR on multi-access
                  network

## nv unset interface <interface-id> router ospf timers

### Usage

  nv unset interface <interface-id> router ospf timers [options] [<attribute> ...]

### Description

  Timers configuration

### Identifiers

  <interface-id>       Interface

### Atrributes

  dead-interval        Length of time, in seconds, without a hello before
                       declaring the neighbor dead. If `minimal`, `hello-
                       multiplier` must be set.
  hello-interval       How often to transmit a hello packet, in seconds. Only
                       valid if `dead-interval` is not `minimal`.
  hello-multiplier     Required and only valid if `dead-interval` is
                       `minimal`.
  retransmit-interval  How often to retransmit a packet not acknowledged, in
                       seconds
  transmit-delay       Delay before sending a new lsa, in seconds

## nv unset interface <interface-id> router ospf timers dead-interval

### Usage

  nv unset interface <interface-id> router ospf timers dead-interval [options]

### Description

  Length of time, in seconds, without a hello before declaring the neighbor dead.  If `minimal`, `hello-multiplier` must be set.

### Identifiers

  <interface-id>  Interface

## nv unset interface <interface-id> router ospf timers hello-multiplier

### Usage

  nv unset interface <interface-id> router ospf timers hello-multiplier [options]

### Description

  Required and only valid if `dead-interval` is `minimal`.

### Identifiers

  <interface-id>  Interface

## nv unset interface <interface-id> router ospf timers hello-interval

### Usage

  nv unset interface <interface-id> router ospf timers hello-interval [options]

### Description

  How often to transmit a hello packet, in seconds.  Only valid if `dead-interval` is not `minimal`.

### Identifiers

  <interface-id>  Interface

## nv unset interface <interface-id> router ospf timers retransmit-interval

### Usage

  nv unset interface <interface-id> router ospf timers retransmit-interval [options]

### Description

  How often to retransmit a packet not acknowledged, in seconds

### Identifiers

  <interface-id>  Interface

## nv unset interface <interface-id> router ospf timers transmit-delay

### Usage

  nv unset interface <interface-id> router ospf timers transmit-delay [options]

### Description

  Delay before sending a new lsa, in seconds

### Identifiers

  <interface-id>  Interface

## nv unset interface <interface-id> router ospf authentication

### Usage

  nv unset interface <interface-id> router ospf authentication [options] [<attribute> ...]

### Description

  md5 authentication configuration

### Identifiers

  <interface-id>      Interface

### Atrributes

  enable              Turn the feature 'on' or 'off'. The default is 'off'.
  md5-key             md5 key
  message-digest-key  Message digest key




## nv unset interface <interface-id> router ospf authentication enable

### Usage

  nv unset interface <interface-id> router ospf authentication enable [options]

### Description

  Turn the feature 'on' or 'off'.  The default is 'off'.

### Identifiers

  <interface-id>  Interface

## nv unset interface <interface-id> router ospf authentication message-digest-key

### Usage

  nv unset interface <interface-id> router ospf authentication message-digest-key [options]

### Description

  Message digest key

### Identifiers

  <interface-id>  Interface

## nv unset interface <interface-id> router ospf authentication md5-key

### Usage

  nv unset interface <interface-id> router ospf authentication md5-key [options]

### Description

  md5 key

### Identifiers

  <interface-id>  Interface

## nv unset interface <interface-id> router ospf bfd

### Usage

  nv unset interface <interface-id> router ospf bfd [options] [<attribute> ...]

### Description

  BFD configuration

### Identifiers

  <interface-id>        Interface

### Atrributes

  enable                Turn the feature 'on' or 'off'. The default is 'off'.
  detect-multiplier     Detect multiplier value
  min-receive-interval  Minimum receive interval in milliseconds
  min-transmit-interval
                        Minimum transmit interval in milliseconds

## nv unset interface <interface-id> router ospf bfd enable

### Usage

  nv unset interface <interface-id> router ospf bfd enable [options]

### Description

  Turn the feature 'on' or 'off'.  The default is 'off'.

### Identifiers

  <interface-id>  Interface

## nv unset interface <interface-id> router ospf bfd detect-multiplier

### Usage

  nv unset interface <interface-id> router ospf bfd detect-multiplier [options]

### Description

  Detect multiplier value

### Identifiers

  <interface-id>  Interface

## nv unset interface <interface-id> router ospf bfd min-receive-interval

### Usage

  nv unset interface <interface-id> router ospf bfd min-receive-interval [options]

### Description

  Minimum receive interval in milliseconds

### Identifiers

  <interface-id>  Interface

## nv unset interface <interface-id> router ospf bfd min-transmit-interval

### Usage

  nv unset interface <interface-id> router ospf bfd min-transmit-interval [options]

### Description

  Minimum transmit interval in milliseconds

### Identifiers

  <interface-id>  Interface

## nv unset interface <interface-id> router ospf enable

### Usage

  nv unset interface <interface-id> router ospf enable [options]

### Description

  Turn the feature 'on' or 'off'.  The default is 'off'.

### Identifiers

  <interface-id>  Interface

## nv unset interface <interface-id> router ospf area

### Usage

  nv unset interface <interface-id> router ospf area [options]

### Description

  Area number for enabling ospf on this interface.

### Identifiers

  <interface-id>  Interface

## nv unset interface <interface-id> router ospf cost

### Usage

  nv unset interface <interface-id> router ospf cost [options]

### Description

  The cost of this link the router lsa.  If `auto`, determine the cost based on link speed.  This is the default.

### Identifiers

  <interface-id>  Interface

## nv unset interface <interface-id> router ospf mtu-ignore

### Usage

  nv unset interface <interface-id> router ospf mtu-ignore [options]

### Description

  Do not test mtu matching for peering.

### Identifiers

  <interface-id>  Interface

## nv unset interface <interface-id> router ospf network-type

### Usage

  nv unset interface <interface-id> router ospf network-type [options]

### Description

  Network type.

### Identifiers

  <interface-id>  Interface

## nv unset interface <interface-id> router ospf passive

### Usage

  nv unset interface <interface-id> router ospf passive [options]

### Description

  Stops the creation of peers on this interface

### Identifiers

  <interface-id>  Interface

## nv unset interface <interface-id> router ospf priority

### Usage

  nv unset interface <interface-id> router ospf priority [options]

### Description

  Eligibility of this router to become DR on multi-access network

### Identifiers

  <interface-id>  Interface

## nv unset interface <interface-id> router pim

### Usage

  nv unset interface <interface-id> router pim [options] [<attribute> ...]

### Description

  PIM interface configuration.

### Identifiers

  <interface-id>  Interface

### Atrributes

  timers          Timers
  bfd             BFD configuration
  address-family  Address family specific configuration
  enable          Turn the feature 'on' or 'off'. The default is 'off'.
  active-active   Enable/disable active-active for PIM MLAG operation on the
                  interface.
  dr-priority     Designated Router Election priority.

## nv unset interface <interface-id> router pim timers

### Usage

  nv unset interface <interface-id> router pim timers [options] [<attribute> ...]

### Description

  Timers

### Identifiers

  <interface-id>  Interface

### Atrributes

  hello-interval  PIM Hello packets periodic interval. If "auto", inherit from
                  the VRF. This is the default. Holdtime is 3.5 times the
                  hello-interval, the amount of time neighbor must kept in
                  reachable state.

## nv unset interface <interface-id> router pim timers hello-interval

### Usage

  nv unset interface <interface-id> router pim timers hello-interval [options]

### Description

  PIM Hello packets periodic interval. If "auto", inherit from the VRF.  This is the default. Holdtime is 3.5 times the hello-interval, the amount of time neighbor must kept in reachable state.

### Identifiers

  <interface-id>  Interface

## nv unset interface <interface-id> router pim bfd

### Usage

  nv unset interface <interface-id> router pim bfd [options] [<attribute> ...]

### Description

  BFD configuration

### Identifiers

  <interface-id>        Interface

### Atrributes

  enable                Turn the feature 'on' or 'off'. The default is 'off'.
  detect-multiplier     Detect multiplier value
  min-receive-interval  Minimum receive interval in milliseconds
  min-transmit-interval
                        Minimum transmit interval in milliseconds

## nv unset interface <interface-id> router pim bfd enable

### Usage

  nv unset interface <interface-id> router pim bfd enable [options]

### Description

  Turn the feature 'on' or 'off'.  The default is 'off'.

### Identifiers

  <interface-id>  Interface

## nv unset interface <interface-id> router pim bfd detect-multiplier

### Usage

  nv unset interface <interface-id> router pim bfd detect-multiplier [options]

### Description

  Detect multiplier value

### Identifiers

  <interface-id>  Interface

## nv unset interface <interface-id> router pim bfd min-receive-interval

### Usage

  nv unset interface <interface-id> router pim bfd min-receive-interval [options]

### Description

  Minimum receive interval in milliseconds

### Identifiers

  <interface-id>  Interface

## nv unset interface <interface-id> router pim bfd min-transmit-interval

### Usage

  nv unset interface <interface-id> router pim bfd min-transmit-interval [options]

### Description

  Minimum transmit interval in milliseconds

### Identifiers

  <interface-id>  Interface

## nv unset interface <interface-id> router pim address-family

### Usage

  nv unset interface <interface-id> router pim address-family [options] [<attribute> ...]

### Description

  Address family specific configuration

### Identifiers

  <interface-id>  Interface

### Atrributes

  ipv4-unicast    IPv4 unicast address family

## nv unset interface <interface-id> router pim address-family ipv4-unicast

### Usage

  nv unset interface <interface-id> router pim address-family ipv4-unicast [options] [<attribute> ...]

### Description

  IPv4 unicast address family

### Identifiers

  <interface-id>        Interface

### Atrributes

  allow-rp              Allow RP feature, which allows RP address to be
                        accepts for the received
  multicast-boundary-oil
                        PIM join/prunes are accepted or dropped based upon the
                        prefix-list filter apply on outgoing filter list on
                        the specified interface.
  use-source            Use unique source address in PIM Hello source field.

## nv unset interface <interface-id> router pim address-family ipv4-unicast allow-rp

### Usage

  nv unset interface <interface-id> router pim address-family ipv4-unicast allow-rp [options] [<attribute> ...]

### Description

  Allow RP feature, which allows RP address to be accepts for the received

### Identifiers

  <interface-id>  Interface

### Atrributes

  enable          Turn the feature 'on' or 'off'. The default is 'off'.
  rp-list         The prefix-list provides the list of group addresses to
                  accept downstream (*,G) joins and propogate towards the
                  allowed-rp.

## nv unset interface <interface-id> router pim address-family ipv4-unicast allow-rp enable

### Usage

  nv unset interface <interface-id> router pim address-family ipv4-unicast allow-rp enable [options]

### Description

  Turn the feature 'on' or 'off'.  The default is 'off'.

### Identifiers

  <interface-id>  Interface

## nv unset interface <interface-id> router pim address-family ipv4-unicast allow-rp rp-list

### Usage

  nv unset interface <interface-id> router pim address-family ipv4-unicast allow-rp rp-list [options]

### Description

  The prefix-list provides the list of group addresses to accept downstream (*,G) joins and propogate towards the allowed-rp.

### Identifiers

  <interface-id>  Interface

## nv unset interface <interface-id> router pim address-family ipv4-unicast multicast-boundary-oil

### Usage

  nv unset interface <interface-id> router pim address-family ipv4-unicast multicast-boundary-oil [options]

### Description

  PIM join/prunes are accepted or dropped based upon the prefix-list filter apply on outgoing filter list on the specified interface.

### Identifiers

  <interface-id>  Interface

## nv unset interface <interface-id> router pim address-family ipv4-unicast use-source

### Usage

  nv unset interface <interface-id> router pim address-family ipv4-unicast use-source [options]

### Description

  Use unique source address in PIM Hello source field.

### Identifiers

  <interface-id>  Interface

## nv unset interface <interface-id> router pim enable

### Usage

  nv unset interface <interface-id> router pim enable [options]

### Description

  Turn the feature 'on' or 'off'.  The default is 'off'.

### Identifiers

  <interface-id>  Interface

## nv unset interface <interface-id> router pim dr-priority

### Usage

  nv unset interface <interface-id> router pim dr-priority [options]

### Description

  Designated Router Election priority.

### Identifiers

  <interface-id>  Interface

## nv unset interface <interface-id> router pim active-active

### Usage

  nv unset interface <interface-id> router pim active-active [options]

### Description

  Enable/disable active-active for PIM MLAG operation on the interface.

### Identifiers

  <interface-id>  Interface

## nv unset interface <interface-id> router adaptive-routing

### Usage

  nv unset interface <interface-id> router adaptive-routing [options] [<attribute> ...]

### Description

  Adaptive routing interface configuration.

### Identifiers

  <interface-id>        Interface

### Atrributes

  enable                Turn the feature 'on' or 'off'. The default is 'off'.
  link-utilization-threshold
                        Link utilization threshold percentage

## nv unset interface <interface-id> router adaptive-routing enable

### Usage

  nv unset interface <interface-id> router adaptive-routing enable [options]

### Description

  Turn the feature 'on' or 'off'.  The default is 'off'.

### Identifiers

  <interface-id>  Interface

## nv unset interface <interface-id> router adaptive-routing link-utilization-threshold

### Usage

  nv unset interface <interface-id> router adaptive-routing link-utilization-threshold [options]

### Description

  Link utilization threshold percentage

### Identifiers

  <interface-id>  Interface

## nv unset interface <interface-id> bond

### Usage

  nv unset interface <interface-id> bond [options] [<attribute> ...]

### Description

  The state of the interface

### Identifiers

  <interface-id>  Interface

### Atrributes

  member          Set of bond members
  mlag            MLAG configuration on the bond interface
  down-delay      bond down delay
  lacp-bypass     lacp bypass
  lacp-rate       lacp rate
  mode            bond mode
  up-delay        bond up delay

## nv unset interface <interface-id> bond member <member-id>

### Usage

  nv unset interface <interface-id> bond member <member-id> [options]

### Description

  A bond member

### Identifiers

  <interface-id>  Interface
  <member-id>     Bond memer interface

## nv unset interface <interface-id> bond mlag

### Usage

  nv unset interface <interface-id> bond mlag [options] [<attribute> ...]

### Description

  MLAG configuration on the bond interface

### Identifiers

  <interface-id>  Interface

### Atrributes

  lacp-conflict   Configure the mlag lacp-conflict parameters
  enable          Turn the feature 'on' or 'off'. The default is 'off'.
  id              MLAG id

## nv unset interface <interface-id> bond mlag lacp-conflict

### Usage

  nv unset interface <interface-id> bond mlag lacp-conflict [options]

### Description

  Configure the mlag lacp-conflict parameters

### Identifiers

  <interface-id>  Interface

## nv unset interface <interface-id> bond mlag enable

### Usage

  nv unset interface <interface-id> bond mlag enable [options]

### Description

  Turn the feature 'on' or 'off'.  The default is 'off'.

### Identifiers

  <interface-id>  Interface

## nv unset interface <interface-id> bond mlag id

### Usage

  nv unset interface <interface-id> bond mlag id [options]

### Description

  MLAG id

### Identifiers

  <interface-id>  Interface

## nv unset interface <interface-id> bond down-delay

### Usage

  nv unset interface <interface-id> bond down-delay [options]

### Description

  bond down delay

### Identifiers

  <interface-id>  Interface

## nv unset interface <interface-id> bond lacp-bypass

### Usage

  nv unset interface <interface-id> bond lacp-bypass [options]

### Description

  lacp bypass

### Identifiers

  <interface-id>  Interface

## nv unset interface <interface-id> bond lacp-rate

### Usage

  nv unset interface <interface-id> bond lacp-rate [options]

### Description

  lacp rate

### Identifiers

  <interface-id>  Interface

## nv unset interface <interface-id> bond mode

### Usage

  nv unset interface <interface-id> bond mode [options]

### Description

  bond mode

### Identifiers

  <interface-id>  Interface

## nv unset interface <interface-id> bond up-delay

### Usage

  nv unset interface <interface-id> bond up-delay [options]

### Description

  bond up delay

### Identifiers

  <interface-id>  Interface

## nv unset interface <interface-id> bridge

### Usage

  nv unset interface <interface-id> bridge [options] [<attribute> ...]

### Description

  attributed related to a bridged interface

### Identifiers

  <interface-id>  Interface

### Atrributes

  domain          Bridge domains on this interface

## nv unset interface <interface-id> bridge domain <domain-id>

### Usage

  nv unset interface <interface-id> bridge domain <domain-id> [options] [<attribute> ...]

### Description

  Bridge domain on this interface

### Identifiers

  <interface-id>  Interface
  <domain-id>     Domain

### Atrributes

  stp             attributed related to a stpd interface
  vlan            Set of allowed vlans for this bridge domain on this
                  interface. If "all", inherit all vlans from the bridge
                  domain, if appropriate. This is the default.
  access          Untagged packets ingressing on this interface will be put in
                  this vlan. Tagged packets will be dropped. Egress packets
                  will be untagged. If auto, inherit from bridge domain.
  learning        source mac address learning for this bridge domain on this
                  interface
  untagged        Untagged packets ingressing on the interface will be put in
                  this vlan. Egress packets are always tagged. If none, then
                  untagged packets will be dropped. If auto, inherit from
                  bridge domain.

## nv unset interface <interface-id> bridge domain <domain-id> stp

### Usage

  nv unset interface <interface-id> bridge domain <domain-id> stp [options] [<attribute> ...]

### Description

  attributed related to a stpd interface

### Identifiers

  <interface-id>  Interface
  <domain-id>     Domain

### Atrributes

  admin-edge      Edge state of the port
  auto-edge       Auto transition to/from edge state of the port
  bpdu-filter     BPDU filter on a port
  bpdu-guard      Bridge Protocol Data Unit guard
  network         Bridge assurance capability for a port
  restrrole       enable/disable port ability to take root role of the port
                  (need better name)

## nv unset interface <interface-id> bridge domain <domain-id> stp bpdu-filter

### Usage

  nv unset interface <interface-id> bridge domain <domain-id> stp bpdu-filter [options]

### Description

  BPDU filter on a port

### Identifiers

  <interface-id>  Interface
  <domain-id>     Domain

## nv unset interface <interface-id> bridge domain <domain-id> stp bpdu-guard

### Usage

  nv unset interface <interface-id> bridge domain <domain-id> stp bpdu-guard [options]

### Description

  Bridge Protocol Data Unit guard

### Identifiers

  <interface-id>  Interface
  <domain-id>     Domain

## nv unset interface <interface-id> bridge domain <domain-id> stp admin-edge

### Usage

  nv unset interface <interface-id> bridge domain <domain-id> stp admin-edge [options]

### Description

  Edge state of the port

### Identifiers

  <interface-id>  Interface
  <domain-id>     Domain

## nv unset interface <interface-id> bridge domain <domain-id> stp auto-edge

### Usage

  nv unset interface <interface-id> bridge domain <domain-id> stp auto-edge [options]

### Description

  Auto transition to/from edge state of the port

### Identifiers

  <interface-id>  Interface
  <domain-id>     Domain

## nv unset interface <interface-id> bridge domain <domain-id> stp network

### Usage

  nv unset interface <interface-id> bridge domain <domain-id> stp network [options]

### Description

  Bridge assurance capability for a port

### Identifiers

  <interface-id>  Interface
  <domain-id>     Domain

## nv unset interface <interface-id> bridge domain <domain-id> stp restrrole

### Usage

  nv unset interface <interface-id> bridge domain <domain-id> stp restrrole [options]

### Description

  enable/disable port ability to take root role of the port (need better name)

### Identifiers

  <interface-id>  Interface
  <domain-id>     Domain

## nv unset interface <interface-id> bridge domain <domain-id> vlan <vid>

### Usage

  nv unset interface <interface-id> bridge domain <domain-id> vlan <vid> [options]

### Description

  A VLAN tag identifier

### Identifiers

  <interface-id>  Interface
  <domain-id>     Domain
  <vid>           VLAN ID, or all

## nv unset interface <interface-id> bridge domain <domain-id> learning

### Usage

  nv unset interface <interface-id> bridge domain <domain-id> learning [options]

### Description

  source mac address learning for this bridge domain on this interface

### Identifiers

  <interface-id>  Interface
  <domain-id>     Domain

## nv unset interface <interface-id> bridge domain <domain-id> untagged

### Usage

  nv unset interface <interface-id> bridge domain <domain-id> untagged [options]

### Description

  Untagged packets ingressing on the interface will be put in this vlan.  Egress packets are always tagged.  If none, then untagged packets will be dropped.  If auto, inherit from bridge domain.

### Identifiers

  <interface-id>  Interface
  <domain-id>     Domain

## nv unset interface <interface-id> bridge domain <domain-id> access

### Usage

  nv unset interface <interface-id> bridge domain <domain-id> access [options]

### Description

  Untagged packets ingressing on this interface will be put in this vlan.  Tagged packets will be dropped.  Egress packets will be untagged.  If auto, inherit from bridge domain.

### Identifiers

  <interface-id>  Interface
  <domain-id>     Domain

## nv unset interface <interface-id> ip

### Usage

  nv unset interface <interface-id> ip [options] [<attribute> ...]

### Description

  IP configuration for an interface

### Identifiers

  <interface-id>      Interface

### Atrributes

  address             ipv4 and ipv6 address
  vrr                 Configuration for VRR
  gateway             default ipv4 and ipv6 gateways
  ipv4                IPv4 configuration for an interface
  ipv6                IPv6 configuration for an interface
  igmp                Configuration for IGMP
  vrrp                Configuration for VRRP
  neighbor-discovery  Neighbor discovery configuration for an interface
  vrf                 Virtual routing and forwarding




## nv unset interface <interface-id> ip address <ip-prefix-id>

### Usage

  nv unset interface <interface-id> ip address <ip-prefix-id> [options]

### Description

  An IP address with prefix

### Identifiers

  <interface-id>  Interface
  <ip-prefix-id>  IPv4 or IPv6 address and route prefix in CIDR notation

## nv unset interface <interface-id> ip vrr

### Usage

  nv unset interface <interface-id> ip vrr [options] [<attribute> ...]

### Description

  Configuration for VRR

### Identifiers

  <interface-id>  Interface

### Atrributes

  address         Virtual addresses with prefixes
  state           The state of the interface
  enable          Turn the feature 'on' or 'off'. The default is 'off'.
  mac-address     Override anycast-mac
  mac-id          Override fabric-id

## nv unset interface <interface-id> ip vrr address <ip-prefix-id>

### Usage

  nv unset interface <interface-id> ip vrr address <ip-prefix-id> [options]

### Description

  An IP address with prefix

### Identifiers

  <interface-id>  Interface
  <ip-prefix-id>  IPv4 or IPv6 address and route prefix in CIDR notation

## nv unset interface <interface-id> ip vrr state

### Usage

  nv unset interface <interface-id> ip vrr state [options]

### Description

  The state of the interface

### Identifiers

  <interface-id>  Interface

## nv unset interface <interface-id> ip vrr enable

### Usage

  nv unset interface <interface-id> ip vrr enable [options]

### Description

  Turn the feature 'on' or 'off'.  The default is 'off'.

### Identifiers

  <interface-id>  Interface

## nv unset interface <interface-id> ip vrr mac-id

### Usage

  nv unset interface <interface-id> ip vrr mac-id [options]

### Description

  Override fabric-id

### Identifiers

  <interface-id>  Interface

## nv unset interface <interface-id> ip vrr mac-address

### Usage

  nv unset interface <interface-id> ip vrr mac-address [options]

### Description

  Override anycast-mac

### Identifiers

  <interface-id>  Interface

## nv unset interface <interface-id> ip gateway <ip-address-id>

### Usage

  nv unset interface <interface-id> ip gateway <ip-address-id> [options]

### Description

  An IP address

### Identifiers

  <interface-id>   Interface
  <ip-address-id>  IPv4 or IPv6 address

## nv unset interface <interface-id> ip ipv4

### Usage

  nv unset interface <interface-id> ip ipv4 [options] [<attribute> ...]

### Description

  IPv4 configuration for an interface

### Identifiers

  <interface-id>  Interface

### Atrributes

  forward         Enable or disable forwarding.

## nv unset interface <interface-id> ip ipv4 forward

### Usage

  nv unset interface <interface-id> ip ipv4 forward [options]

### Description

  Enable or disable forwarding.

### Identifiers

  <interface-id>  Interface

## nv unset interface <interface-id> ip ipv6

### Usage

  nv unset interface <interface-id> ip ipv6 [options] [<attribute> ...]

### Description

  IPv6 configuration for an interface

### Identifiers

  <interface-id>  Interface

### Atrributes

  enable          Turn the feature 'on' or 'off'. The default is 'on'.
  forward         Enable or disable forwarding.

## nv unset interface <interface-id> ip ipv6 enable

### Usage

  nv unset interface <interface-id> ip ipv6 enable [options]

### Description

  Turn the feature 'on' or 'off'.  The default is 'on'.

### Identifiers

  <interface-id>  Interface

## nv unset interface <interface-id> ip ipv6 forward

### Usage

  nv unset interface <interface-id> ip ipv6 forward [options]

### Description

  Enable or disable forwarding.

### Identifiers

  <interface-id>  Interface

## nv unset interface <interface-id> ip igmp

### Usage

  nv unset interface <interface-id> ip igmp [options] [<attribute> ...]

### Description

  Configuration for IGMP

### Identifiers

  <interface-id>        Interface

### Atrributes

  static-group          IGMP static mutlicast mroutes
  enable                Turn the feature 'on' or 'off'. The default is 'off'.
  last-member-query-interval
                        Last member query interval.
  query-interval        Query interval, in seconds.
  query-max-response-time
                        Max query response time, in seconds.
  version               Protocol version

## nv unset interface <interface-id> ip igmp static-group <static-group-id>

### Usage

  nv unset interface <interface-id> ip igmp static-group <static-group-id> [options] [<attribute> ...]

### Description

  IGMP static multicast mroute

### Identifiers

  <interface-id>     Interface
  <static-group-id>  IGMP static multicast mroute destination

### Atrributes

  source-address     IGMP static multicast mroute source.

## nv unset interface <interface-id> ip igmp static-group <static-group-id> source-address

### Usage

  nv unset interface <interface-id> ip igmp static-group <static-group-id> source-address [options]

### Description

  IGMP static multicast mroute source.

### Identifiers

  <interface-id>     Interface
  <static-group-id>  IGMP static multicast mroute destination

## nv unset interface <interface-id> ip igmp enable

### Usage

  nv unset interface <interface-id> ip igmp enable [options]

### Description

  Turn the feature 'on' or 'off'.  The default is 'off'.

### Identifiers

  <interface-id>  Interface

## nv unset interface <interface-id> ip igmp version

### Usage

  nv unset interface <interface-id> ip igmp version [options]

### Description

  Protocol version

### Identifiers

  <interface-id>  Interface

## nv unset interface <interface-id> ip igmp query-interval

### Usage

  nv unset interface <interface-id> ip igmp query-interval [options]

### Description

  Query interval, in seconds.

### Identifiers

  <interface-id>  Interface

## nv unset interface <interface-id> ip igmp query-max-response-time

### Usage

  nv unset interface <interface-id> ip igmp query-max-response-time [options]

### Description

  Max query response time, in seconds.

### Identifiers

  <interface-id>  Interface

## nv unset interface <interface-id> ip igmp last-member-query-interval

### Usage

  nv unset interface <interface-id> ip igmp last-member-query-interval [options]

### Description

  Last member query interval.

### Identifiers

  <interface-id>  Interface

## nv unset interface <interface-id> ip vrrp

### Usage

  nv unset interface <interface-id> ip vrrp [options] [<attribute> ...]

### Description

  Configuration for VRRP

### Identifiers

  <interface-id>  Interface

### Atrributes

  virtual-router  Group of virtual gateways implemented with VRRP
  enable          Turn the feature 'on' or 'off'. The default is 'off'.

## nv unset interface <interface-id> ip vrrp virtual-router <virtual-router-id>

### Usage

  nv unset interface <interface-id> ip vrrp virtual-router <virtual-router-id> [options] [<attribute> ...]

### Description

  A virtual gateway implemented with VRRP

### Identifiers

  <interface-id>        Interface
  <virtual-router-id>   Virtual Router IDentifier (VRID)

### Atrributes

  address               A set of virtual addresses for VRRPv3
  advertisement-interval
                        Sets the interval between successive VRRP
                        advertisements -- RFC 5798 defines this as a 12-bit
                        value expressed as 0.1 seconds, with default 1000
                        milliseconds, i.e., 1 second. Represented in units of
                        milliseconds
  preempt               When set to true, enables preemption by a higher
                        priority backup router of a lower priority master
                        router
  priority              Specifies the sending VRRP interface's priority for
                        the virtual router. Higher values equal higher
                        priority
  version               Protocol version

## nv unset interface <interface-id> ip vrrp virtual-router <virtual-router-id> address <ip-address-id>

### Usage

  nv unset interface <interface-id> ip vrrp virtual-router <virtual-router-id> address <ip-address-id> [options]

### Description

  An IP address

### Identifiers

  <interface-id>       Interface
  <virtual-router-id>  Virtual Router IDentifier (VRID)
  <ip-address-id>      IPv4 or IPv6 address

## nv unset interface <interface-id> ip vrrp virtual-router <virtual-router-id> version

### Usage

  nv unset interface <interface-id> ip vrrp virtual-router <virtual-router-id> version [options]

### Description

  Protocol version

### Identifiers

  <interface-id>       Interface
  <virtual-router-id>  Virtual Router IDentifier (VRID)

## nv unset interface <interface-id> ip vrrp virtual-router <virtual-router-id> priority

### Usage

  nv unset interface <interface-id> ip vrrp virtual-router <virtual-router-id> priority [options]

### Description

  Specifies the sending VRRP interface's priority for the virtual router. Higher values equal higher priority

### Identifiers

  <interface-id>       Interface
  <virtual-router-id>  Virtual Router IDentifier (VRID)

## nv unset interface <interface-id> ip vrrp virtual-router <virtual-router-id> preempt

### Usage

  nv unset interface <interface-id> ip vrrp virtual-router <virtual-router-id> preempt [options]

### Description

  When set to true, enables preemption by a higher priority backup router of a lower priority master router

### Identifiers

  <interface-id>       Interface
  <virtual-router-id>  Virtual Router IDentifier (VRID)

## nv unset interface <interface-id> ip vrrp virtual-router <virtual-router-id> advertisement-interval

### Usage

  nv unset interface <interface-id> ip vrrp virtual-router <virtual-router-id> advertisement-interval [options]

### Description

  Sets the interval between successive VRRP advertisements -- RFC 5798 defines this as a 12-bit value expressed as 0.1 seconds, with default 1000 milliseconds, i.e., 1 second. Represented in units of milliseconds

### Identifiers

  <interface-id>       Interface
  <virtual-router-id>  Virtual Router IDentifier (VRID)

## nv unset interface <interface-id> ip vrrp enable

### Usage

  nv unset interface <interface-id> ip vrrp enable [options]

### Description

  Turn the feature 'on' or 'off'.  The default is 'off'.

### Identifiers

  <interface-id>  Interface

## nv unset interface <interface-id> ip neighbor-discovery

### Usage

  nv unset interface <interface-id> ip neighbor-discovery [options] [<attribute> ...]

### Description

  Neighbor discovery configuration for an interface

### Identifiers

  <interface-id>        Interface

### Atrributes

  rdnss                 Recursive DNS server addresses to be advertised using
                        type 25 option RFC8016
  prefix                IPv6 prefix configuration
  dnssl                 Advertise DNS search list using type 31 option RFC8106
  router-advertisement  Router advertisement
  home-agent            Home agent configuration
  enable                Turn the feature 'on' or 'off'. The default is 'on'.
  mtu                   MTU option for neighbor discovery messages

## nv unset interface <interface-id> ip neighbor-discovery rdnss <ipv6-address-id>

### Usage

  nv unset interface <interface-id> ip neighbor-discovery rdnss <ipv6-address-id> [options] [<attribute> ...]

### Description

  A recursive DNS server

### Identifiers

  <interface-id>     Interface
  <ipv6-address-id>  IPv6 address

### Atrributes

  lifetime           Maximum time in seconds for which the server may be used
                     for domain name resolution

## nv unset interface <interface-id> ip neighbor-discovery rdnss <ipv6-address-id> lifetime

### Usage

  nv unset interface <interface-id> ip neighbor-discovery rdnss <ipv6-address-id> lifetime [options]

### Description

  Maximum time in seconds for which the server may be used for domain name resolution

### Identifiers

  <interface-id>     Interface
  <ipv6-address-id>  IPv6 address

## nv unset interface <interface-id> ip neighbor-discovery prefix <ipv6-prefix-id>

### Usage

  nv unset interface <interface-id> ip neighbor-discovery prefix <ipv6-prefix-id> [options] [<attribute> ...]

### Description

  A IPv6 prefix

### Identifiers

  <interface-id>      Interface
  <ipv6-prefix-id>    IPv6 address and route prefix in CIDR notation

### Atrributes

  autoconfig          Indicates to hosts on the local link that the specified
                      prefix can be used for v6 autoconfiguration
  off-link            Indicates that adverisement makes no statement about on-
                      link or off-link properties of the prefix
  preferred-lifetime  Time in seconds that addresses generated from a prefix
                      remain preferred
  router-address      Indicates to hosts on the local link that the specified
                      prefix contains a complete IP address by setting R flag
  valid-lifetime      Time in seconds the prefix is valid for on-link
                      determination




## nv unset interface <interface-id> ip neighbor-discovery prefix <ipv6-prefix-id> valid-lifetime

### Usage

  nv unset interface <interface-id> ip neighbor-discovery prefix <ipv6-prefix-id> valid-lifetime [options]

### Description

  Time in seconds the prefix is valid for on-link determination

### Identifiers

  <interface-id>    Interface
  <ipv6-prefix-id>  IPv6 address and route prefix in CIDR notation

## nv unset interface <interface-id> ip neighbor-discovery prefix <ipv6-prefix-id> preferred-lifetime
### Usage

  nv unset interface <interface-id> ip neighbor-discovery prefix <ipv6-prefix-id> preferred-lifetime [options]

### Description

  Time in seconds that addresses generated from a prefix remain preferred

### Identifiers

  <interface-id>    Interface
  <ipv6-prefix-id>  IPv6 address and route prefix in CIDR notation

## nv unset interface <interface-id> ip neighbor-discovery prefix <ipv6-prefix-id> off-link
### Usage

  nv unset interface <interface-id> ip neighbor-discovery prefix <ipv6-prefix-id> off-link [options]

### Description

  Indicates that adverisement makes no statement about on-link or off-link properties of the prefix

### Identifiers

  <interface-id>    Interface
  <ipv6-prefix-id>  IPv6 address and route prefix in CIDR notation

## nv unset interface <interface-id> ip neighbor-discovery prefix <ipv6-prefix-id> autoconfig
### Usage

  nv unset interface <interface-id> ip neighbor-discovery prefix <ipv6-prefix-id> autoconfig [options]

### Description

  Indicates to hosts on the local link that the specified prefix can be used for v6 autoconfiguration

### Identifiers

  <interface-id>    Interface
  <ipv6-prefix-id>  IPv6 address and route prefix in CIDR notation

## nv unset interface <interface-id> ip neighbor-discovery prefix <ipv6-prefix-id> router-address
### Usage

  nv unset interface <interface-id> ip neighbor-discovery prefix <ipv6-prefix-id> router-address [options]

### Description

  Indicates to hosts on the local link that the specified prefix contains a complete IP address by setting R flag

### Identifiers

  <interface-id>    Interface
  <ipv6-prefix-id>  IPv6 address and route prefix in CIDR notation

## nv unset interface <interface-id> ip neighbor-discovery dnssl <domain-name-id>
### Usage

  nv unset interface <interface-id> ip neighbor-discovery dnssl <domain-name-id> [options] [<attribute> ...]

### Description

  A DNS search list

### Identifiers

  <interface-id>    Interface
  <domain-name-id>  The domain portion of a hostname (RFC 1123) or an
                    internationalized hostname (RFC 5890).

### Atrributes

  lifetime          Maximum time in seconds for which the domain suffix may be
                    used for domain name resolution

## nv unset interface <interface-id> ip neighbor-discovery dnssl <domain-name-id> lifetime
### Usage

  nv unset interface <interface-id> ip neighbor-discovery dnssl <domain-name-id> lifetime [options]

### Description

  Maximum time in seconds for which the domain suffix may be used for domain name resolution

### Identifiers

  <interface-id>    Interface
  <domain-name-id>  The domain portion of a hostname (RFC 1123) or an
                    internationalized hostname (RFC 5890).

## nv unset interface <interface-id> ip neighbor-discovery router-advertisement
### Usage

  nv unset interface <interface-id> ip neighbor-discovery router-advertisement [options] [<attribute> ...]

### Description

  Router advertisement configuration for an interface

### Identifiers

  <interface-id>     Interface

### Atrributes

  enable             Turn the feature 'on' or 'off'. The default is 'on'.
  fast-retransmit    Allow consecutive RA packets more frequently than every 3
                     seconds
  hop-limit          Value in hop count field in IP header of the outgoing
                     router advertisement packet
  interval           Maximum time in milliseconds allowed between sending
                     unsolicited multicast RA from the interface
  interval-option    Indicates hosts that the router will use advertisement
                     interval to send router advertisements
  lifetime           Maximum time in seconds that the router can be treated as
                     default gateway
  managed-config     Knob to allow dynamic host to use managed (stateful)
                     protocol for address autoconfiguration in addition to any
                     addresses autoconfigured using stateless address
                     autoconfig
  other-config       Knob to allow dynamic host to use managed (stateful)
                     protocol for autoconfiguration information other than
                     addresses
  reachable-time     Time in milliseconds that a IPv6 node is considered
                     reachable
  retransmit-time    Time in milliseconds between retransmission of neighbor
                     solicitation messages
  router-preference  Hosts use router preference in selection of the default
                     router

## nv unset interface <interface-id> ip neighbor-discovery router-advertisement enable

### Usage

  nv unset interface <interface-id> ip neighbor-discovery router-advertisement enable [options]

### Description

  Turn the feature 'on' or 'off'.  The default is 'on'.

### Identifiers

  <interface-id>  Interface

## nv unset interface <interface-id> ip neighbor-discovery router-advertisement interval

### Usage

  nv unset interface <interface-id> ip neighbor-discovery router-advertisement interval [options]

### Description

  Maximum time in milliseconds allowed between sending unsolicited multicast RA from the interface

### Identifiers

  <interface-id>  Interface

## nv unset interface <interface-id> ip neighbor-discovery router-advertisement interval-option

### Usage

  nv unset interface <interface-id> ip neighbor-discovery router-advertisement interval-option [options]

### Description

  Indicates hosts that the router will use advertisement interval to send router advertisements

### Identifiers

  <interface-id>  Interface

## nv unset interface <interface-id> ip neighbor-discovery router-advertisement fast-retransmit

### Usage

  nv unset interface <interface-id> ip neighbor-discovery router-advertisement fast-retransmit [options]

### Description

  Allow consecutive RA packets more frequently than every 3 seconds

### Identifiers

  <interface-id>  Interface

## nv unset interface <interface-id> ip neighbor-discovery router-advertisement lifetime

### Usage

  nv unset interface <interface-id> ip neighbor-discovery router-advertisement lifetime [options]

### Description

  Maximum time in seconds that the router can be treated as default gateway

### Identifiers

  <interface-id>  Interface

## nv unset interface <interface-id> ip neighbor-discovery router-advertisement reachable-time

### Usage

  nv unset interface <interface-id> ip neighbor-discovery router-advertisement reachable-time [options]

### Description

  Time in milliseconds that a IPv6 node is considered reachable

### Identifiers

  <interface-id>  Interface

## nv unset interface <interface-id> ip neighbor-discovery router-advertisement retransmit-time

### Usage

  nv unset interface <interface-id> ip neighbor-discovery router-advertisement retransmit-time [options]

### Description

  Time in milliseconds between retransmission of neighbor solicitation messages

### Identifiers

  <interface-id>  Interface

## nv unset interface <interface-id> ip neighbor-discovery router-advertisement managed-config

### Usage

  nv unset interface <interface-id> ip neighbor-discovery router-advertisement managed-config [options]

### Description

  Knob to allow dynamic host to use managed (stateful) protocol for address autoconfiguration in addition to any addresses autoconfigured using stateless address autoconfig

### Identifiers

  <interface-id>  Interface

## nv unset interface <interface-id> ip neighbor-discovery router-advertisement other-config

### Usage

  nv unset interface <interface-id> ip neighbor-discovery router-advertisement other-config [options]

### Description

  Knob to allow dynamic host to use managed (stateful) protocol for autoconfiguration information other than addresses

### Identifiers

  <interface-id>  Interface

## nv unset interface <interface-id> ip neighbor-discovery router-advertisement hop-limit

### Usage

  nv unset interface <interface-id> ip neighbor-discovery router-advertisement hop-limit [options]

### Description

  Value in hop count field in IP header of the outgoing router advertisement packet

### Identifiers

  <interface-id>  Interface

## nv unset interface <interface-id> ip neighbor-discovery router-advertisement router-preference

### Usage

  nv unset interface <interface-id> ip neighbor-discovery router-advertisement router-preference [options]

### Description

  Hosts use router preference in selection of the default router

### Identifiers

  <interface-id>  Interface

## nv unset interface <interface-id> ip neighbor-discovery home-agent

### Usage

  nv unset interface <interface-id> ip neighbor-discovery home-agent [options] [<attribute> ...]

### Description

  Indicates to neighbors that this router acts as a Home Agent and includes a Home Agent Option. Not defined by default

### Identifiers

  <interface-id>  Interface

### Atrributes

  lifetime        Lifetime of a home agent in seconds
  preference      Home agent's preference value that is used to order the
                  addresses returned in the home agent address discovery
                  reply.

## nv unset interface <interface-id> ip neighbor-discovery home-agent lifetime

### Usage

  nv unset interface <interface-id> ip neighbor-discovery home-agent lifetime [options]

### Description

  Lifetime of a home agent in seconds

### Identifiers

  <interface-id>  Interface

## nv unset interface <interface-id> ip neighbor-discovery home-agent preference

### Usage

  nv unset interface <interface-id> ip neighbor-discovery home-agent preference [options]

### Description

  Home agent's preference value that is used to order the addresses returned in the home agent address discovery reply.

### Identifiers

  <interface-id>  Interface

## nv unset interface <interface-id> ip neighbor-discovery enable

### Usage

  nv unset interface <interface-id> ip neighbor-discovery enable [options]

### Description

  Turn the feature 'on' or 'off'.  The default is 'on'.

### Identifiers

  <interface-id>  Interface

## nv unset interface <interface-id> ip neighbor-discovery mtu

### Usage

  nv unset interface <interface-id> ip neighbor-discovery mtu [options]

### Description

  MTU option for neighbor discovery messages

### Identifiers

  <interface-id>  Interface

## nv unset interface <interface-id> ip vrf

### Usage

  nv unset interface <interface-id> ip vrf [options]

### Description

  Virtual routing and forwarding

### Identifiers

  <interface-id>  Interface

## nv unset interface <interface-id> lldp

### Usage

  nv unset interface <interface-id> lldp [options] [<attribute> ...]

### Description

  LLDP on for an interface

### Identifiers

  <interface-id>       Interface

### Atrributes

  dcbx-ets-config-tlv  DCBX ETS config TLV flag
  dcbx-ets-recomm-tlv  DCBX ETS recommendation TLV flag
  dcbx-pfc-tlv         DCBX PFC TLV flag

## nv unset interface <interface-id> lldp dcbx-pfc-tlv

### Usage

  nv unset interface <interface-id> lldp dcbx-pfc-tlv [options]

### Description

  DCBX PFC TLV flag

### Identifiers

  <interface-id>  Interface

## nv unset interface <interface-id> lldp dcbx-ets-config-tlv

### Usage

  nv unset interface <interface-id> lldp dcbx-ets-config-tlv [options]

### Description

  DCBX ETS config TLV flag

### Identifiers

  <interface-id>  Interface

## nv unset interface <interface-id> lldp dcbx-ets-recomm-tlv

### Usage

  nv unset interface <interface-id> lldp dcbx-ets-recomm-tlv [options]

### Description

  DCBX ETS recommendation TLV flag

### Identifiers

  <interface-id>  Interface

## nv unset interface <interface-id> link

### Usage

  nv unset interface <interface-id> link [options] [<attribute> ...]

### Description

  An physical interface

### Identifiers

  <interface-id>  Interface

### Atrributes

  state           The state of the interface
  dot1x           An physical interface
  auto-negotiate  Link speed and characteristic auto negotiation
  breakout        sub-divide or disable ports (only valid on plug interfaces)
  duplex          Link duplex
  fec             Link forward error correction mechanism
  mtu             interface mtu
  speed           Link speed

## nv unset interface <interface-id> link state

### Usage

  nv unset interface <interface-id> link state [options]

### Description

  The state of the interface

### Identifiers

  <interface-id>  Interface

## nv unset interface <interface-id> link dot1x

### Usage

  nv unset interface <interface-id> link dot1x [options] [<attribute> ...]

### Description

  An physical interface

### Identifiers

  <interface-id>  Interface

### Atrributes

  mab             bypass MAC authentication
  parking-vlan    VLAN for unauthorized MAC addresses

## nv unset interface <interface-id> link dot1x mab

### Usage

  nv unset interface <interface-id> link dot1x mab [options]

### Description

  bypass MAC authentication

### Identifiers

  <interface-id>  Interface

## nv unset interface <interface-id> link dot1x parking-vlan

### Usage

  nv unset interface <interface-id> link dot1x parking-vlan [options]

### Description

  VLAN for unauthorized MAC addresses

### Identifiers

  <interface-id>  Interface

## nv unset interface <interface-id> link auto-negotiate

### Usage

  nv unset interface <interface-id> link auto-negotiate [options]

### Description

  Link speed and characteristic auto negotiation

### Identifiers

  <interface-id>  Interface

## nv unset interface <interface-id> link breakout

### Usage

  nv unset interface <interface-id> link breakout [options]

### Description

  sub-divide or disable ports (only valid on plug interfaces)

### Identifiers

  <interface-id>  Interface

## nv unset interface <interface-id> link duplex

### Usage

  nv unset interface <interface-id> link duplex [options]

### Description

  Link duplex

### Identifiers

  <interface-id>  Interface

## nv unset interface <interface-id> link speed

### Usage

  nv unset interface <interface-id> link speed [options]

### Description

  Link speed

### Identifiers

  <interface-id>  Interface

## nv unset interface <interface-id> link fec

### Usage

  nv unset interface <interface-id> link fec [options]

### Description

  Link forward error correction mechanism

### Identifiers

  <interface-id>  Interface

## nv unset interface <interface-id> link mtu

### Usage

  nv unset interface <interface-id> link mtu [options]

### Description

  interface mtu

### Identifiers

  <interface-id>  Interface

## nv unset interface <interface-id> evpn

### Usage

  nv unset interface <interface-id> evpn [options] [<attribute> ...]

### Description

  EVPN control plane config and info for VRF

### Identifiers

  <interface-id>  Interface

### Atrributes

  multihoming     Multihoming interface configuration parameters

## nv unset interface <interface-id> evpn multihoming

### Usage

  nv unset interface <interface-id> evpn multihoming [options] [<attribute> ...]

### Description

  Multihoming interface configuration parameters

### Identifiers

  <interface-id>  Interface

### Atrributes

  segment         Multihoming interface segment
  uplink          Enable evpn multihoming tracking to prevent traffic loss due
                  to NVE connectivity loss, uplink's operational state is
                  tracked when enabled.

## nv unset interface <interface-id> evpn multihoming segment

### Usage

  nv unset interface <interface-id> evpn multihoming segment [options] [<attribute> ...]

### Description

  Multihoming interface segment

### Identifiers

  <interface-id>  Interface

### Atrributes

  enable          Turn the feature 'on' or 'off'. The default is 'off'.
  df-preference   Designated forwarder preference value for this ethernet
                  segment. If 'auto', the global evpn multihoming preference
                  will be used. This is the default.
  identifier      Ethernet segment identifier. This must be unique for each
                  segment and match other bonds in the segment.
  local-id        Ethernet segment local-id. If provided, it will be combined
                  with the global multihoming `mac-address` to create the
                  ethernet segment identifier, which must be unique for each
                  segment and match other bonds in the segment.
  mac-address     MAC address for this ethernet segment. If 'auto', the global
                  evpn multihoming mac-address will be used. This is the
                  default.

## nv unset interface <interface-id> evpn multihoming segment enable

### Usage

  nv unset interface <interface-id> evpn multihoming segment enable [options]

### Description

  Turn the feature 'on' or 'off'.  The default is 'off'.

### Identifiers

  <interface-id>  Interface

## nv unset interface <interface-id> evpn multihoming segment local-id

### Usage

  nv unset interface <interface-id> evpn multihoming segment local-id [options]

### Description

  Ethernet segment local-id.  If provided, it will be combined with the global multihoming `mac-address` to create the ethernet segment identifier, which must be unique for each segment and match other bonds in the segment.

### Identifiers

  <interface-id>  Interface

## nv unset interface <interface-id> evpn multihoming segment identifier

### Usage

  nv unset interface <interface-id> evpn multihoming segment identifier [options]

### Description

  Ethernet segment identifier.  This must be unique for each segment and match other bonds in the segment.

### Identifiers

  <interface-id>  Interface

## nv unset interface <interface-id> evpn multihoming segment mac-address

### Usage

  nv unset interface <interface-id> evpn multihoming segment mac-address [options]

### Description

  MAC address for this ethernet segment.  If 'auto', the global evpn multihoming mac-address will be used.  This is the default.

### Identifiers

  <interface-id>  Interface

## nv unset interface <interface-id> evpn multihoming segment df-preference

### Usage

  nv unset interface <interface-id> evpn multihoming segment df-preference [options]

### Description

  Designated forwarder preference value for this ethernet segment. If 'auto', the global evpn multihoming preference will be used. This is the default.

### Identifiers

  <interface-id>  Interface

## nv unset interface <interface-id> evpn multihoming uplink

### Usage

  nv unset interface <interface-id> evpn multihoming uplink [options]

### Description

  Enable evpn multihoming tracking to prevent traffic loss due to NVE connectivity loss, uplink's operational state is tracked when enabled.

### Identifiers

  <interface-id>  Interface

## nv unset interface <interface-id> acl <acl-id>

### Usage

  nv unset interface <interface-id> acl <acl-id> [options] [<attribute> ...]

### Description

  An ACL is used for matching packets and take actions

### Identifiers

  <interface-id>  Interface
  <acl-id>        ACL ID

### Atrributes

  inbound         ACL applied for inbound direction
  outbound        ACL applied for outbound direction

## nv unset interface <interface-id> acl <acl-id> inbound

### Usage

  nv unset interface <interface-id> acl <acl-id> inbound [options] [<attribute> ...]

### Description

  inbound direction

### Identifiers

  <interface-id>  Interface
  <acl-id>        ACL ID

### Atrributes

  control-plane   ACL applied for control plane

## nv unset interface <interface-id> acl <acl-id> inbound control-plane

### Usage

  nv unset interface <interface-id> acl <acl-id> inbound control-plane [options]

### Description

  State details

### Identifiers

  <interface-id>  Interface
  <acl-id>        ACL ID

## nv unset interface <interface-id> acl <acl-id> outbound

### Usage

  nv unset interface <interface-id> acl <acl-id> outbound [options] [<attribute> ...]

### Description

  State details

### Identifiers

  <interface-id>  Interface
  <acl-id>        ACL ID

### Atrributes

  control-plane

## nv unset interface <interface-id> acl <acl-id> outbound control-plane

### Usage

  nv unset interface <interface-id> acl <acl-id> outbound control-plane [options]

### Description

  State details

### Identifiers

  <interface-id>  Interface
  <acl-id>        ACL ID

## nv unset interface <interface-id> ptp

### Usage

  nv unset interface <interface-id> ptp [options] [<attribute> ...]

### Description

  Interface Specific PTP configuration.

### Identifiers

  <interface-id>     Interface

### Atrributes

  timers             Interface PTP timerss
  enable             Turn the feature 'on' or 'off'. The default is 'off'.
  acceptable-master  Determines if acceptable master check is enabled for this
                     interface.
  delay-mechanism    Mode in which PTP message is transmitted.
  forced-master      Configures PTP interfaces to forced master state.
  instance           PTP instance number.
  message-mode       Mode in which PTP delay message is transmitted.
  transport          Transport method for the PTP messages.
  ttl                Maximum number of hops the PTP messages can make before
                     it gets dropped.

## nv unset interface <interface-id> ptp timers
### Usage

  nv unset interface <interface-id> ptp timers [options] [<attribute> ...]

### Description

  Interface PTP timerss

### Identifiers

  <interface-id>      Interface

### Atrributes

  announce-interval   Mean time interval between successive Announce messages.
                      It's specified as a power of two in seconds.
  announce-timeout    The number of announceIntervals that have to pass
                      without receipt of an Announce message before the
                      occurrence of the timeout event
  delay-req-interval  The minimum permitted mean time interval between
                      successive Delay Req messages. It's specified as a power
                      of two in seconds.
  sync-interval       The mean SyncInterval for multicast messages. It's
                      specified as a power of two in seconds.

## nv unset interface <interface-id> ptp timers announce-interval
### Usage

  nv unset interface <interface-id> ptp timers announce-interval [options]

### Description

  Mean time interval between successive Announce messages.  It's specified as a power of two in seconds.

### Identifiers

  <interface-id>  Interface

## nv unset interface <interface-id> ptp timers sync-interval
### Usage

  nv unset interface <interface-id> ptp timers sync-interval [options]

### Description

  The mean SyncInterval for multicast messages.  It's specified as a power of two in seconds.

### Identifiers

  <interface-id>  Interface

## nv unset interface <interface-id> ptp timers delay-req-interval
### Usage

  nv unset interface <interface-id> ptp timers delay-req-interval [options]

### Description

  The minimum permitted mean time interval between successive Delay Req messages.  It's specified as a power of two in seconds.

### Identifiers

  <interface-id>  Interface

## nv unset interface <interface-id> ptp timers announce-timeout
### Usage

  nv unset interface <interface-id> ptp timers announce-timeout [options]

### Description

  The number of announceIntervals that have to pass without receipt of an Announce message before the occurrence of the timeout event

### Identifiers

  <interface-id>  Interface

## nv unset interface <interface-id> ptp enable
### Usage

  nv unset interface <interface-id> ptp enable [options]

### Description

  Turn the feature 'on' or 'off'.  The default is 'off'.

### Identifiers

  <interface-id>  Interface

## nv unset interface <interface-id> ptp instance
### Usage

  nv unset interface <interface-id> ptp instance [options]

### Description

  PTP instance number.

### Identifiers

  <interface-id>  Interface

## nv unset interface <interface-id> ptp forced-master
### Usage

  nv unset interface <interface-id> ptp forced-master [options]

### Description

  Configures PTP interfaces to forced master state.

### Identifiers

  <interface-id>  Interface

## nv unset interface <interface-id> ptp acceptable-master
### Usage

  nv unset interface <interface-id> ptp acceptable-master [options]

### Description

  Determines if acceptable master check is enabled for this interface.

### Identifiers

  <interface-id>  Interface

## nv unset interface <interface-id> ptp delay-mechanism
### Usage

  nv unset interface <interface-id> ptp delay-mechanism [options]

### Description

  Mode in which PTP message is transmitted.

### Identifiers

  <interface-id>  Interface

## nv unset interface <interface-id> ptp transport
### Usage

  nv unset interface <interface-id> ptp transport [options]

### Description

  Transport method for the PTP messages.

### Identifiers

  <interface-id>  Interface

## nv unset interface <interface-id> ptp ttl
### Usage

  nv unset interface <interface-id> ptp ttl [options]

### Description

  Maximum number of hops the PTP messages can make before it gets dropped.

### Identifiers

  <interface-id>  Interface

## nv unset interface <interface-id> ptp message-mode
### Usage

  nv unset interface <interface-id> ptp message-mode [options]

### Description

  Mode in which PTP delay message is transmitted.

### Identifiers

  <interface-id>  Interface

## nv unset interface <interface-id> tunnel
### Usage

  nv unset interface <interface-id> tunnel [options] [<attribute> ...]

### Description

  The state of the interface

### Identifiers

  <interface-id>  Interface

### Atrributes

  dest-ip         Destination underlay IP address
  interface       Physical underlay interface to used for Tunnel packets
  mode            tunnel mode
  source-ip       Source underlay IP address
  ttl             time to live

## nv unset interface <interface-id> tunnel source-ip
### Usage

  nv unset interface <interface-id> tunnel source-ip [options]

### Description

  Source underlay IP address

### Identifiers

  <interface-id>  Interface

## nv unset interface <interface-id> tunnel dest-ip
### Usage

  nv unset interface <interface-id> tunnel dest-ip [options]

### Description

  Destination underlay IP address

### Identifiers

  <interface-id>  Interface

## nv unset interface <interface-id> tunnel ttl
### Usage

  nv unset interface <interface-id> tunnel ttl [options]

### Description

  time to live

### Identifiers

  <interface-id>  Interface

## nv unset interface <interface-id> tunnel mode
### Usage

  nv unset interface <interface-id> tunnel mode [options]

### Description

  tunnel mode

### Identifiers

  <interface-id>  Interface

## nv unset interface <interface-id> tunnel interface
### Usage

  nv unset interface <interface-id> tunnel interface [options]

### Description

  Physical underlay interface to used for Tunnel packets

### Identifiers

  <interface-id>  Interface

## nv unset interface <interface-id> description
### Usage

  nv unset interface <interface-id> description [options]

### Description

  Details about the interface

### Identifiers

  <interface-id>  Interface

## nv unset interface <interface-id> type
### Usage

  nv unset interface <interface-id> type [options]

### Description

  The type of interface

### Identifiers

  <interface-id>  Interface

## nv unset interface <interface-id> base-interface
### Usage

  nv unset interface <interface-id> base-interface [options]

### Description

  The interface under this interface

### Identifiers

  <interface-id>  Interface

## nv unset interface <interface-id> vlan
### Usage

  nv unset interface <interface-id> vlan [options]

### Description

  VLAN ID

### Identifiers

  <interface-id>  Interface

## nv unset service
### Usage

  nv unset service [options] [<attribute> ...]

### Description

  A service

### Atrributes

  dns           collection of DNS
  syslog        collection of syslog
  ntp           NTPs
  dhcp-relay    DHCP-relays
  dhcp-relay6   DHCP-relays
  ptp           Collection of PTP instances
  dhcp-server   DHCP-servers
  dhcp-server6  DHCP-servers6
  lldp          Global LLDP

## nv unset service dns
### Usage

  nv unset service dns [options] [<vrf-id> ...]

### Description

  collection of DNS

### Identifiers

  <vrf-id>    VRF## nv unset service dns <vrf-id>
### Usage

  nv unset service dns <vrf-id> [options] [<attribute> ...]

### Description

  Domain Name Service

### Identifiers

  <vrf-id>    VRF### Atrributes

  server      Remote DNS servers

## nv unset service dns <vrf-id> server <dns-server-id>
### Usage

  nv unset service dns <vrf-id> server <dns-server-id> [options]

### Description

  A remote DNS server

### Identifiers

  <vrf-id>         VRF
  <dns-server-id>  IPv4 or IPv6 address of a DNS server

## nv unset service syslog
### Usage

  nv unset service syslog [options] [<vrf-id> ...]

### Description

  collection of syslog

### Identifiers

  <vrf-id>    VRF

## nv unset service syslog <vrf-id>

### Usage

  nv unset service syslog <vrf-id> [options] [<attribute> ...]

### Description

  Domain Name Service

### Identifiers

  <vrf-id>    VRF### Atrributes

  server      Remote DNS servers



## nv unset service syslog <vrf-id> server <server-id>

### Usage

  nv unset service syslog <vrf-id> server <server-id> [options] [<attribute> ...]

### Description

  A remote DNS server

### Identifiers

  <vrf-id>     VRF
  <server-id>  Hostname or IP address of a syslog server

### Atrributes

  port         Port number of the remote syslog server
  protocol     Protocol, udp or tcp, of the remote syslog server

## nv unset service syslog <vrf-id> server <server-id> port

### Usage

  nv unset service syslog <vrf-id> server <server-id> port [options]

### Description

  Port number of the remote syslog server

### Identifiers

  <vrf-id>     VRF
  <server-id>  Hostname or IP address of a syslog server

## nv unset service syslog <vrf-id> server <server-id> protocol

### Usage

  nv unset service syslog <vrf-id> server <server-id> protocol [options]

### Description

  Protocol, udp or tcp, of the remote syslog server

### Identifiers

  <vrf-id>     VRF
  <server-id>  Hostname or IP address of a syslog server

## nv unset service ntp

### Usage

  nv unset service ntp [options] [<vrf-id> ...]

### Description

  NTPs

### Identifiers

  <vrf-id>    VRF

## nv unset service ntp <vrf-id>

### Usage

  nv unset service ntp <vrf-id> [options] [<attribute> ...]

### Description

  Network Time Protocol

### Identifiers

  <vrf-id>    VRF### Atrributes

  server      Remote NTP Servers
  pool        Remote NTP Servers
  listen      NTP interface to listen on.



## nv unset service ntp <vrf-id> server <server-id>

### Usage

  nv unset service ntp <vrf-id> server <server-id> [options] [<attribute> ...]

### Description

  A remote NTP Server

### Identifiers

  <vrf-id>     VRF
  <server-id>  Hostname or IP address of the NTP server

### Atrributes

  iburst       When the server is unreachable, send a burst of eight packets
               instead of the usual one.

## nv unset service ntp <vrf-id> server <server-id> iburst

### Usage

  nv unset service ntp <vrf-id> server <server-id> iburst [options]

### Description

  When the server is unreachable, send a burst of eight packets instead of the usual one.

### Identifiers

  <vrf-id>     VRF
  <server-id>  Hostname or IP address of the NTP server

## nv unset service ntp <vrf-id> pool <server-id>

### Usage

  nv unset service ntp <vrf-id> pool <server-id> [options] [<attribute> ...]

### Description

  A remote NTP Server

### Identifiers

  <vrf-id>     VRF
  <server-id>  Hostname or IP address of the NTP server

### Atrributes

  iburst       When the server is unreachable, send a burst of eight packets
               instead of the usual one.

## nv unset service ntp <vrf-id> pool <server-id> iburst

### Usage

  nv unset service ntp <vrf-id> pool <server-id> iburst [options]

### Description

  When the server is unreachable, send a burst of eight packets instead of the usual one.

### Identifiers

  <vrf-id>     VRF
  <server-id>  Hostname or IP address of the NTP server

## nv unset service ntp <vrf-id> listen

### Usage

  nv unset service ntp <vrf-id> listen [options]

### Description

  NTP interface to listen on.

### Identifiers

  <vrf-id>    VRF

## nv unset service dhcp-relay

### Usage

  nv unset service dhcp-relay [options] [<vrf-id> ...]

### Description

  DHCP-relays

### Identifiers

  <vrf-id>    VRF

## nv unset service dhcp-relay <vrf-id>

### Usage

  nv unset service dhcp-relay <vrf-id> [options] [<attribute> ...]

### Description

  DHCP relay

### Identifiers

  <vrf-id>             VRF

### Atrributes

  server               DHCP servers
  interface            Set of interfaces on which to handle DHCP relay traffic
  giaddress-interface  Configures DHCP relay giaddress on the interfaes.
  source-ip            Source IP to use on the relayed packet. If "giaddr", it
                       will be taken from giaddress. Otherwise, if "auto", it
                       will be taken from an L3 interface on this switch using
                       normal routing methods. This is the default.

## nv unset service dhcp-relay <vrf-id> server <server-id>

### Usage

  nv unset service dhcp-relay <vrf-id> server <server-id> [options]

### Description

  A DHCP server

### Identifiers

  <vrf-id>     VRF
  <server-id>  DHCP server

## nv unset service dhcp-relay <vrf-id> interface <interface-id>

### Usage

  nv unset service dhcp-relay <vrf-id> interface <interface-id> [options]

### Description

  An interface on which DHCP relay is configured.

### Identifiers

  <vrf-id>        VRF
  <interface-id>  DHCP relay interface

## nv unset service dhcp-relay <vrf-id> giaddress-interface <interface-id>

### Usage

  nv unset service dhcp-relay <vrf-id> giaddress-interface <interface-id> [options] [<attribute> ...]

### Description

  An interface on which DHCP relay giaddress is configured.

### Identifiers

  <vrf-id>        VRF
  <interface-id>  DHCP relay giaddress interface

### Atrributes

  address         ipv4 address on giaddress interface

## nv unset service dhcp-relay <vrf-id> giaddress-interface <interface-id> address

### Usage

  nv unset service dhcp-relay <vrf-id> giaddress-interface <interface-id> address [options]

### Description

  ipv4 address on giaddress interface

### Identifiers

  <vrf-id>        VRF
  <interface-id>  DHCP relay giaddress interface

## nv unset service dhcp-relay <vrf-id> source-ip

### Usage

  nv unset service dhcp-relay <vrf-id> source-ip [options]

### Description

  Source IP to use on the relayed packet.  If "giaddr", it will be taken from giaddress.  Otherwise, if "auto", it will be taken from an L3 interface on this switch using normal routing methods.  This is the default.

### Identifiers

  <vrf-id>    VRF

## nv unset service dhcp-relay6

### Usage

  nv unset service dhcp-relay6 [options] [<vrf-id> ...]

### Description

  DHCP-relays

### Identifiers

  <vrf-id>    VRF

## nv unset service dhcp-relay6 <vrf-id>

### Usage

  nv unset service dhcp-relay6 <vrf-id> [options] [<attribute> ...]

### Description

  DHCP relay

### Identifiers

  <vrf-id>    VRF### Atrributes

  interface   DHCP relay interfaces



## nv unset service dhcp-relay6 <vrf-id> interface

### Usage

  nv unset service dhcp-relay6 <vrf-id> interface [options] [<attribute> ...]

### Description

  DHCP relay interfaces

### Identifiers

  <vrf-id>    VRF### Atrributes

  upstream    Configures DHCP relay on the interfaes.
  downstream  Configures DHCP relay on the interfaes.



## nv unset service dhcp-relay6 <vrf-id> interface upstream <interface-id>

### Usage

  nv unset service dhcp-relay6 <vrf-id> interface upstream <interface-id> [options] [<attribute> ...]

### Description

  An interface on which DPCH relay is configured.

### Identifiers

  <vrf-id>        VRF
  <interface-id>  DHCP relay interface

### Atrributes

  address         ipv6 address on interface

## nv unset service dhcp-relay6 <vrf-id> interface upstream <interface-id> address

### Usage

  nv unset service dhcp-relay6 <vrf-id> interface upstream <interface-id> address [options]

### Description

  ipv6 address on interface

### Identifiers

  <vrf-id>        VRF
  <interface-id>  DHCP relay interface

## nv unset service dhcp-relay6 <vrf-id> interface downstream <interface-id>

### Usage

  nv unset service dhcp-relay6 <vrf-id> interface downstream <interface-id> [options] [<attribute> ...]

### Description

  An interface on which DPCH relay is configured.

### Identifiers

  <vrf-id>        VRF
  <interface-id>  DHCP relay interface

### Atrributes

  address         ipv6 address on interface

## nv unset service dhcp-relay6 <vrf-id> interface downstream <interface-id> address

### Usage

  nv unset service dhcp-relay6 <vrf-id> interface downstream <interface-id> address [options]

### Description

  ipv6 address on interface

### Identifiers

  <vrf-id>        VRF
  <interface-id>  DHCP relay interface

## nv unset service ptp

### Usage

  nv unset service ptp [options] [<instance-id> ...]

### Description

  Collection of PTP instances

### Identifiers

  <instance-id>  PTP instance number. It is used for management purpose.

## nv unset service ptp <instance-id>

### Usage

  nv unset service ptp <instance-id> [options] [<attribute> ...]

### Description

  Global PTP configuration.

### Identifiers

  <instance-id>      PTP instance number. It is used for management purpose.

### Atrributes

  acceptable-master  Collection of acceptable masters
  monitor            PTP monitor configuration
  enable             Turn the feature 'on' or 'off'. The default is 'off'.
  domain             Domain number of the current syntonization
  ip-dscp            Sets the Diffserv code point for all PTP packets
                     originated locally.
  priority1          Priority1 attribute of the local clock
  priority2          Priority2 attribute of the local clock
  two-step           Determines if the Clock is a 2 step clock

## nv unset service ptp <instance-id> acceptable-master

### Usage

  nv unset service ptp <instance-id> acceptable-master [options] [<clock-id> ...]

### Description

  Collection of acceptable masters

### Identifiers

  <instance-id>  PTP instance number. It is used for management purpose.
  <clock-id>     Clock ID

## nv unset service ptp <instance-id> acceptable-master <clock-id>

### Usage

  nv unset service ptp <instance-id> acceptable-master <clock-id> [options] [<attribute> ...]

### Description

  List of clocks that the local clock can accept as master clock

### Identifiers

  <instance-id>  PTP instance number. It is used for management purpose.
  <clock-id>     Clock ID

### Atrributes

  alt-priority   Alternate priority

## nv unset service ptp <instance-id> acceptable-master <clock-id> alt-priority

### Usage

  nv unset service ptp <instance-id> acceptable-master <clock-id> alt-priority [options]

### Description

  Alternate priority

### Identifiers

  <instance-id>  PTP instance number. It is used for management purpose.
  <clock-id>     Clock ID

## nv unset service ptp <instance-id> monitor

### Usage

  nv unset service ptp <instance-id> monitor [options] [<attribute> ...]

### Description

  PTP monitor configuration

### Identifiers

  <instance-id>         PTP instance number. It is used for management
                        purpose.

### Atrributes

  max-offset-threshold  Maximum offset threshold in nano seconds
  max-timestamp-entries
                        Maximum timestamp entries allowed
  max-violation-log-entries
                        Maximum violation log entries per set
  max-violation-log-sets
                        Maximum violation logs sets allowed
  min-offset-threshold  Minimum offset threshold in nano seconds
  path-delay-threshold  Path delay threshold in nano seconds
  violation-log-interval
                        violation log intervals in seconds

## nv unset service ptp <instance-id> monitor min-offset-threshold

### Usage

  nv unset service ptp <instance-id> monitor min-offset-threshold [options]

### Description

  Minimum offset threshold in nano seconds

### Identifiers

  <instance-id>  PTP instance number. It is used for management purpose.

## nv unset service ptp <instance-id> monitor max-offset-threshold

### Usage

  nv unset service ptp <instance-id> monitor max-offset-threshold [options]

### Description

  Maximum offset threshold in nano seconds

### Identifiers

  <instance-id>  PTP instance number. It is used for management purpose.

## nv unset service ptp <instance-id> monitor path-delay-threshold

### Usage

  nv unset service ptp <instance-id> monitor path-delay-threshold [options]

### Description

  Path delay threshold in nano seconds

### Identifiers

  <instance-id>  PTP instance number. It is used for management purpose.

## nv unset service ptp <instance-id> monitor max-timestamp-entries

### Usage

  nv unset service ptp <instance-id> monitor max-timestamp-entries [options]

### Description

  Maximum timestamp entries allowed

### Identifiers

  <instance-id>  PTP instance number. It is used for management purpose.

## nv unset service ptp <instance-id> monitor max-violation-log-sets

### Usage

  nv unset service ptp <instance-id> monitor max-violation-log-sets [options]

### Description

  Maximum violation logs sets allowed

### Identifiers

  <instance-id>  PTP instance number. It is used for management purpose.

## nv unset service ptp <instance-id> monitor max-violation-log-entries

### Usage

  nv unset service ptp <instance-id> monitor max-violation-log-entries [options]

### Description

  Maximum violation log entries per set

### Identifiers

  <instance-id>  PTP instance number. It is used for management purpose.

## nv unset service ptp <instance-id> monitor violation-log-interval

### Usage

  nv unset service ptp <instance-id> monitor violation-log-interval [options]

### Description

  violation log intervals in seconds

### Identifiers

  <instance-id>  PTP instance number. It is used for management purpose.

## nv unset service ptp <instance-id> enable

### Usage

  nv unset service ptp <instance-id> enable [options]

### Description

  Turn the feature 'on' or 'off'.  The default is 'off'.

### Identifiers

  <instance-id>  PTP instance number. It is used for management purpose.

## nv unset service ptp <instance-id> two-step

### Usage

  nv unset service ptp <instance-id> two-step [options]

### Description

  Determines if the Clock is a 2 step clock

### Identifiers

  <instance-id>  PTP instance number. It is used for management purpose.

## nv unset service ptp <instance-id> priority1

### Usage

  nv unset service ptp <instance-id> priority1 [options]

### Description

  Priority1 attribute of the local clock

### Identifiers

  <instance-id>  PTP instance number. It is used for management purpose.

## nv unset service ptp <instance-id> priority2

### Usage

  nv unset service ptp <instance-id> priority2 [options]

### Description

  Priority2 attribute of the local clock

### Identifiers

  <instance-id>  PTP instance number. It is used for management purpose.

## nv unset service ptp <instance-id> domain

### Usage

  nv unset service ptp <instance-id> domain [options]

### Description

  Domain number of the current syntonization

### Identifiers

  <instance-id>  PTP instance number. It is used for management purpose.

## nv unset service ptp <instance-id> ip-dscp

### Usage

  nv unset service ptp <instance-id> ip-dscp [options]

### Description

  Sets the Diffserv code point for all PTP packets originated locally.

### Identifiers

  <instance-id>  PTP instance number. It is used for management purpose.

## nv unset service dhcp-server

### Usage

  nv unset service dhcp-server [options] [<vrf-id> ...]

### Description

  DHCP-servers

### Identifiers

  <vrf-id>    VRF

## nv unset service dhcp-server <vrf-id>

### Usage

  nv unset service dhcp-server <vrf-id> [options] [<attribute> ...]

### Description

  Dynamic Host Configuration Protocol Server

### Identifiers

  <vrf-id>            VRF

### Atrributes

  interface           Assign DHCP options to clients directly attached to
                      these interfaes.
  pool                DHCP Pools
  domain-name         DHCP domain names
  domain-name-server  DHCP domain name servers
  static              DHCP clients with fixed IP address assignments




## nv unset service dhcp-server <vrf-id> interface <interface-id>

### Usage

  nv unset service dhcp-server <vrf-id> interface <interface-id> [options]

### Description

  An interface on which DPCH clients are attached.

### Identifiers

  <vrf-id>        VRF
  <interface-id>  DHCP client interface

## nv unset service dhcp-server <vrf-id> pool <pool-id>

### Usage

  nv unset service dhcp-server <vrf-id> pool <pool-id> [options] [<attribute> ...]

### Description

  DHCP Pool

### Identifiers

  <vrf-id>              VRF
  <pool-id>             DHCP pool subnet.

### Atrributes

  domain-name-server    DHCP domain name servers
  domain-name           DHCP domain names
  gateway               DHCP gateway
  range                 IP Address range assignments
  cumulus-provision-url
                        Cumulus specific URL for provisioning script
  default-url           TBD
  lease-time            Network address lease time in seconds assigned to DHCP
                        clients.
  ping-check            TBD
  pool-name             Name

## nv unset service dhcp-server <vrf-id> pool <pool-id> domain-name-server <server-id>

### Usage

  nv unset service dhcp-server <vrf-id> pool <pool-id> domain-name-server <server-id> [options]

### Description

  A remote DNS server

### Identifiers

  <vrf-id>     VRF
  <pool-id>    DHCP pool subnet.
  <server-id>  DNS server

## nv unset service dhcp-server <vrf-id> pool <pool-id> domain-name <domain-name-id>

### Usage

  nv unset service dhcp-server <vrf-id> pool <pool-id> domain-name <domain-name-id> [options] [<attribute> ...]

### Description

  TBD

### Identifiers

  <vrf-id>          VRF
  <pool-id>         DHCP pool subnet.
  <domain-name-id>  DHCP domain name

### Atrributes

  domain-name       DHCP domain name

## nv unset service dhcp-server <vrf-id> pool <pool-id> domain-name <domain-name-id> domain-name

### Usage

  nv unset service dhcp-server <vrf-id> pool <pool-id> domain-name <domain-name-id> domain-name [options]

### Description

  DHCP domain name

### Identifiers

  <vrf-id>          VRF
  <pool-id>         DHCP pool subnet.
  <domain-name-id>  DHCP domain name

## nv unset service dhcp-server <vrf-id> pool <pool-id> gateway <gateway-id>

### Usage

  nv unset service dhcp-server <vrf-id> pool <pool-id> gateway <gateway-id> [options]

### Description

  A remote DNS server

### Identifiers

  <vrf-id>      VRF
  <pool-id>     DHCP pool subnet.
  <gateway-id>  Gateway

## nv unset service dhcp-server <vrf-id> pool <pool-id> range <range-id>

### Usage

  nv unset service dhcp-server <vrf-id> pool <pool-id> range <range-id> [options] [<attribute> ...]

### Description

  DHCP Pool range

### Identifiers

  <vrf-id>    VRF
  <pool-id>   DHCP pool subnet.
  <range-id>  DHCP client interface

### Atrributes

  to          End of the range.



## nv unset service dhcp-server <vrf-id> pool <pool-id> range <range-id> to

### Usage

  nv unset service dhcp-server <vrf-id> pool <pool-id> range <range-id> to [options]

### Description

  End of the range.

### Identifiers

  <vrf-id>    VRF
  <pool-id>   DHCP pool subnet.
  <range-id>  DHCP client interface



## nv unset service dhcp-server <vrf-id> pool <pool-id> pool-name

### Usage

  nv unset service dhcp-server <vrf-id> pool <pool-id> pool-name [options]

### Description

  Name

### Identifiers

  <vrf-id>    VRF
  <pool-id>   DHCP pool subnet.



## nv unset service dhcp-server <vrf-id> pool <pool-id> lease-time

### Usage

  nv unset service dhcp-server <vrf-id> pool <pool-id> lease-time [options]

### Description

  Network address lease time in seconds assigned to DHCP clients.

### Identifiers

  <vrf-id>    VRF
  <pool-id>   DHCP pool subnet.



## nv unset service dhcp-server <vrf-id> pool <pool-id> ping-check

### Usage

  nv unset service dhcp-server <vrf-id> pool <pool-id> ping-check [options]

### Description

  TBD

### Identifiers

  <vrf-id>    VRF
  <pool-id>   DHCP pool subnet.



## nv unset service dhcp-server <vrf-id> pool <pool-id> default-url

### Usage

  nv unset service dhcp-server <vrf-id> pool <pool-id> default-url [options]

### Description

  TBD

### Identifiers

  <vrf-id>    VRF
  <pool-id>   DHCP pool subnet.



## nv unset service dhcp-server <vrf-id> pool <pool-id> cumulus-provision-url

### Usage

  nv unset service dhcp-server <vrf-id> pool <pool-id> cumulus-provision-url [options]

### Description

  Cumulus specific URL for provisioning script

### Identifiers

  <vrf-id>    VRF
  <pool-id>   DHCP pool subnet.



## nv unset service dhcp-server <vrf-id> domain-name <domain-name-id>

### Usage

  nv unset service dhcp-server <vrf-id> domain-name <domain-name-id> [options] [<attribute> ...]

### Description

  TBD

### Identifiers

  <vrf-id>          VRF
  <domain-name-id>  DHCP domain name

### Atrributes

  domain-name       DHCP domain name

## nv unset service dhcp-server <vrf-id> domain-name <domain-name-id> domain-name

### Usage

  nv unset service dhcp-server <vrf-id> domain-name <domain-name-id> domain-name [options]

### Description

  DHCP domain name

### Identifiers

  <vrf-id>          VRF
  <domain-name-id>  DHCP domain name

## nv unset service dhcp-server <vrf-id> domain-name-server <server-id>

### Usage

  nv unset service dhcp-server <vrf-id> domain-name-server <server-id> [options]

### Description

  A remote DNS server

### Identifiers

  <vrf-id>     VRF
  <server-id>  DNS server

## nv unset service dhcp-server <vrf-id> static <static-id>

### Usage

  nv unset service dhcp-server <vrf-id> static <static-id> [options] [<attribute> ...]

### Description

  static entry

### Identifiers

  <vrf-id>              VRF
  <static-id>           static mapping nane

### Atrributes

  cumulus-provision-url
                        Cumulus specific URL for provisioning script
  ip-address            IP address
  mac-address           MAC (hardware) address

## nv unset service dhcp-server <vrf-id> static <static-id> mac-address

### Usage

  nv unset service dhcp-server <vrf-id> static <static-id> mac-address [options]

### Description

  MAC (hardware) address

### Identifiers

  <vrf-id>     VRF
  <static-id>  static mapping nane

## nv unset service dhcp-server <vrf-id> static <static-id> ip-address

### Usage

  nv unset service dhcp-server <vrf-id> static <static-id> ip-address [options]

### Description

  IP address

### Identifiers

  <vrf-id>     VRF
  <static-id>  static mapping nane

## nv unset service dhcp-server <vrf-id> static <static-id> cumulus-provision-url

### Usage

  nv unset service dhcp-server <vrf-id> static <static-id> cumulus-provision-url [options]

### Description

  Cumulus specific URL for provisioning script

### Identifiers

  <vrf-id>     VRF
  <static-id>  static mapping nane

## nv unset service dhcp-server6

### Usage

  nv unset service dhcp-server6 [options] [<vrf-id> ...]

### Description

  DHCP-servers6

### Identifiers

  <vrf-id>    VRF

## nv unset service dhcp-server6 <vrf-id>

### Usage

  nv unset service dhcp-server6 <vrf-id> [options] [<attribute> ...]

### Description

  Dynamic Host Configuration Protocol IPv6 Server

### Identifiers

  <vrf-id>            VRF

### Atrributes

  interface           Assign DHCP options to clients directly attached to
                      these interfaes.
  pool                DHCP IP Pools
  domain-name         DHCP domain names
  domain-name-server  DHCP domain name servers
  static              DHCP clients with fixed IP address assignments




## nv unset service dhcp-server6 <vrf-id> interface <interface-id>

### Usage

  nv unset service dhcp-server6 <vrf-id> interface <interface-id> [options]

### Description

  An interface on which DPCH clients are attached.

### Identifiers

  <vrf-id>        VRF
  <interface-id>  DHCP client interface

## nv unset service dhcp-server6 <vrf-id> pool <pool-id>

### Usage

  nv unset service dhcp-server6 <vrf-id> pool <pool-id> [options] [<attribute> ...]

### Description

  DHCP Pool

### Identifiers

  <vrf-id>              VRF
  <pool-id>             DHCP6 pool subnet.

### Atrributes

  domain-name-server    DHCP domain name servers
  domain-name           DHCP domain names
  range                 IP Address range assignments
  cumulus-provision-url
                        Cumulus specific URL for provisioning script
  default-url           TBD
  lease-time            Network address lease time in seconds assigned to DHCP
                        clients.
  ping-check            TBD
  pool-name             Name

## nv unset service dhcp-server6 <vrf-id> pool <pool-id> domain-name-server <server-id>

### Usage

  nv unset service dhcp-server6 <vrf-id> pool <pool-id> domain-name-server <server-id> [options]

### Description

  A remote DNS server

### Identifiers

  <vrf-id>     VRF
  <pool-id>    DHCP6 pool subnet.
  <server-id>  DNS server

## nv unset service dhcp-server6 <vrf-id> pool <pool-id> domain-name <domain-name-id>

### Usage

  nv unset service dhcp-server6 <vrf-id> pool <pool-id> domain-name <domain-name-id> [options] [<attribute> ...]

### Description

  TBD

### Identifiers

  <vrf-id>          VRF
  <pool-id>         DHCP6 pool subnet.
  <domain-name-id>  DHCP domain name

### Atrributes

  domain-name       DHCP domain name

## nv unset service dhcp-server6 <vrf-id> pool <pool-id> domain-name <domain-name-id> domain-name

### Usage

  nv unset service dhcp-server6 <vrf-id> pool <pool-id> domain-name <domain-name-id> domain-name [options]

### Description

  DHCP domain name

### Identifiers

  <vrf-id>          VRF
  <pool-id>         DHCP6 pool subnet.
  <domain-name-id>  DHCP domain name

## nv unset service dhcp-server6 <vrf-id> pool <pool-id> range <range-id>

### Usage

  nv unset service dhcp-server6 <vrf-id> pool <pool-id> range <range-id> [options] [<attribute> ...]

### Description

  DHCP Pool range

### Identifiers

  <vrf-id>    VRF
  <pool-id>   DHCP6 pool subnet.
  <range-id>  DHCP client interface

### Atrributes

  to          End of the range.



## nv unset service dhcp-server6 <vrf-id> pool <pool-id> range <range-id> to

### Usage

  nv unset service dhcp-server6 <vrf-id> pool <pool-id> range <range-id> to [options]

### Description

  End of the range.

### Identifiers

  <vrf-id>    VRF
  <pool-id>   DHCP6 pool subnet.
  <range-id>  DHCP client interface



## nv unset service dhcp-server6 <vrf-id> pool <pool-id> pool-name

### Usage

  nv unset service dhcp-server6 <vrf-id> pool <pool-id> pool-name [options]

### Description

  Name

### Identifiers

  <vrf-id>    VRF
  <pool-id>   DHCP6 pool subnet.



## nv unset service dhcp-server6 <vrf-id> pool <pool-id> lease-time

### Usage

  nv unset service dhcp-server6 <vrf-id> pool <pool-id> lease-time [options]

### Description

  Network address lease time in seconds assigned to DHCP clients.

### Identifiers

  <vrf-id>    VRF
  <pool-id>   DHCP6 pool subnet.



## nv unset service dhcp-server6 <vrf-id> pool <pool-id> ping-check

### Usage

  nv unset service dhcp-server6 <vrf-id> pool <pool-id> ping-check [options]

### Description

  TBD

### Identifiers

  <vrf-id>    VRF
  <pool-id>   DHCP6 pool subnet.



## nv unset service dhcp-server6 <vrf-id> pool <pool-id> default-url

### Usage

  nv unset service dhcp-server6 <vrf-id> pool <pool-id> default-url [options]

### Description

  TBD

### Identifiers

  <vrf-id>    VRF
  <pool-id>   DHCP6 pool subnet.



## nv unset service dhcp-server6 <vrf-id> pool <pool-id> cumulus-provision-url

### Usage

  nv unset service dhcp-server6 <vrf-id> pool <pool-id> cumulus-provision-url [options]

### Description

  Cumulus specific URL for provisioning script

### Identifiers

  <vrf-id>    VRF
  <pool-id>   DHCP6 pool subnet.



## nv unset service dhcp-server6 <vrf-id> domain-name <domain-name-id>

### Usage

  nv unset service dhcp-server6 <vrf-id> domain-name <domain-name-id> [options] [<attribute> ...]

### Description

  TBD

### Identifiers

  <vrf-id>          VRF
  <domain-name-id>  DHCP domain name

### Atrributes

  domain-name       DHCP domain name

## nv unset service dhcp-server6 <vrf-id> domain-name <domain-name-id> domain-name

### Usage

  nv unset service dhcp-server6 <vrf-id> domain-name <domain-name-id> domain-name [options]

### Description

  DHCP domain name

### Identifiers

  <vrf-id>          VRF
  <domain-name-id>  DHCP domain name

## nv unset service dhcp-server6 <vrf-id> domain-name-server <server-id>

### Usage

  nv unset service dhcp-server6 <vrf-id> domain-name-server <server-id> [options]

### Description

  A remote DNS server

### Identifiers

  <vrf-id>     VRF
  <server-id>  DNS server

## nv unset service dhcp-server6 <vrf-id> static <static-id>

### Usage

  nv unset service dhcp-server6 <vrf-id> static <static-id> [options] [<attribute> ...]

### Description

  static entry

### Identifiers

  <vrf-id>              VRF
  <static-id>           static mapping nane

### Atrributes

  cumulus-provision-url
                        Cumulus specific URL for provisioning script
  ip-address            IP address
  mac-address           MAC (hardware) address

## nv unset service dhcp-server6 <vrf-id> static <static-id> mac-address

### Usage

  nv unset service dhcp-server6 <vrf-id> static <static-id> mac-address [options]

### Description

  MAC (hardware) address

### Identifiers

  <vrf-id>     VRF
  <static-id>  static mapping nane

## nv unset service dhcp-server6 <vrf-id> static <static-id> ip-address

### Usage

  nv unset service dhcp-server6 <vrf-id> static <static-id> ip-address [options]

### Description

  IP address

### Identifiers

  <vrf-id>     VRF
  <static-id>  static mapping nane

## nv unset service dhcp-server6 <vrf-id> static <static-id> cumulus-provision-url

### Usage

  nv unset service dhcp-server6 <vrf-id> static <static-id> cumulus-provision-url [options]

### Description

  Cumulus specific URL for provisioning script

### Identifiers

  <vrf-id>     VRF
  <static-id>  static mapping nane

## nv unset service lldp

### Usage

  nv unset service lldp [options] [<attribute> ...]

### Description

  Global LLDP

### Atrributes

  dot1-tlv            Enable dot1 TLV advertisements on enabled ports
  tx-hold-multiplier  < TTL of transmitted packets is calculated by
                      multiplying the tx-interval by the given factor
  tx-interval         change transmit delay




## nv unset service lldp tx-interval

### Usage

  nv unset service lldp tx-interval [options]

### Description

  change transmit delay



## nv unset service lldp tx-hold-multiplier

### Usage

  nv unset service lldp tx-hold-multiplier [options]

### Description

  < TTL of transmitted packets is calculated by multiplying the tx-interval by the given factor



## nv unset service lldp dot1-tlv

### Usage

  nv unset service lldp dot1-tlv [options]

### Description

  Enable dot1 TLV advertisements on enabled ports



## nv unset system

### Usage

  nv unset system [options] [<attribute> ...]

### Description

  Top-level node which contains system-wide properties.

### Atrributes

  control-plane  Control Plane specific configurations
  message        System pre-login and post-login messages
  global         global system configuration
  port-mirror    Port mirror
  config         Affect how config operations are performed.
  hostname       Static hostname for the switch
  timezone       system time zone

## nv unset system control-plane

### Usage

  nv unset system control-plane [options] [<attribute> ...]

### Description

  Control Plane specific configurations

### Atrributes

  trap        Traps
  policer     Policers



## nv unset system control-plane trap <trap-id>

### Usage

  nv unset system control-plane trap <trap-id> [options] [<attribute> ...]

### Description

  Trap

### Identifiers

  <trap-id>   TRAP ID

### Atrributes

  state       trap state



## nv unset system control-plane trap <trap-id> state

### Usage

  nv unset system control-plane trap <trap-id> state [options]

### Description

  trap state

### Identifiers

  <trap-id>   TRAP ID



## nv unset system control-plane policer <policer-id>

### Usage

  nv unset system control-plane policer <policer-id> [options] [<attribute> ...]

### Description

  Policer

### Identifiers

  <policer-id>  Policer ID

### Atrributes

  burst         policer burst value
  rate          policer rate value
  state         policer state

## nv unset system control-plane policer <policer-id> state

### Usage

  nv unset system control-plane policer <policer-id> state [options]

### Description

  policer state

### Identifiers

  <policer-id>  Policer ID

## nv unset system control-plane policer <policer-id> burst

### Usage

  nv unset system control-plane policer <policer-id> burst [options]

### Description

  policer burst value

### Identifiers

  <policer-id>  Policer ID

## nv unset system control-plane policer <policer-id> rate

### Usage

  nv unset system control-plane policer <policer-id> rate [options]

### Description

  policer rate value

### Identifiers

  <policer-id>  Policer ID

## nv unset system message

### Usage

  nv unset system message [options] [<attribute> ...]

### Description

  System pre-login and post-login messages

### Atrributes

  post-login  configure post-login message of the day
  pre-login   configure pre-login banner



## nv unset system message pre-login

### Usage

  nv unset system message pre-login [options]

### Description

  configure pre-login banner



## nv unset system message post-login

### Usage

  nv unset system message post-login [options]

### Description

  configure post-login message of the day



## nv unset system global

### Usage

  nv unset system global [options] [<attribute> ...]

### Description

  global system configuration

### Atrributes

  reserved     reserved ranges
  anycast-id   An integer (1-65535) to select rack MAC address in range
               44:38:39:ff:00:00 to 44:38:39:ff:ff:ff
  anycast-mac  MAC address shared by the rack.
  fabric-id    An integer (1-255) to select first hop router MAC adress in
               range 00:00:5E:00:01:01 to 00:00:5E:00:01:ff
  fabric-mac   First hop router MAC address
  system-mac   full MAC address.

## nv unset system global reserved

### Usage

  nv unset system global reserved [options] [<attribute> ...]

### Description

  reserved ranges

### Atrributes

  routing-table  reserved routing table ranges
  vlan           reserved vlan ranges

## nv unset system global reserved routing-table

### Usage

  nv unset system global reserved routing-table [options] [<attribute> ...]

### Description

  reserved routing table ranges

### Atrributes

  pbr         reserved routing table ranges for PBR



## nv unset system global reserved routing-table pbr

### Usage

  nv unset system global reserved routing-table pbr [options] [<attribute> ...]

### Description

  reserved routing table ranges for PBR

### Atrributes

  begin       Beginning of reserved routing table range for PBR
  end         End of reserved routing table range for PBR



## nv unset system global reserved routing-table pbr begin

### Usage

  nv unset system global reserved routing-table pbr begin [options]

### Description

  Beginning of reserved routing table range for PBR



## nv unset system global reserved routing-table pbr end

### Usage

  nv unset system global reserved routing-table pbr end [options]

### Description

  End of reserved routing table range for PBR



## nv unset system global reserved vlan

### Usage

  nv unset system global reserved vlan [options] [<attribute> ...]

### Description

  reserved vlan ranges

### Atrributes

  l3-vni-vlan  Reserved vlans to be used with l3vni

## nv unset system global reserved vlan l3-vni-vlan

### Usage

  nv unset system global reserved vlan l3-vni-vlan [options] [<attribute> ...]

### Description

  Reserved vlans to be used with l3vni

### Atrributes

  begin       Beginning of reserved vlan range for L3 VNI
  end         End of reserved vlan range for L3 VNI



## nv unset system global reserved vlan l3-vni-vlan begin

### Usage

  nv unset system global reserved vlan l3-vni-vlan begin [options]

### Description

  Beginning of reserved vlan range for L3 VNI



## nv unset system global reserved vlan l3-vni-vlan end

### Usage

  nv unset system global reserved vlan l3-vni-vlan end [options]

### Description

  End of reserved vlan range for L3 VNI



## nv unset system global system-mac

### Usage

  nv unset system global system-mac [options]

### Description

  full MAC address.



## nv unset system global anycast-mac

### Usage

  nv unset system global anycast-mac [options]

### Description

  MAC address shared by the rack.



## nv unset system global anycast-id

### Usage

  nv unset system global anycast-id [options]

### Description

  An integer (1-65535) to select rack MAC address in range 44:38:39:ff:00:00 to 44:38:39:ff:ff:ff



## nv unset system global fabric-mac

### Usage

  nv unset system global fabric-mac [options]

### Description

  First hop router MAC address



## nv unset system global fabric-id

### Usage

  nv unset system global fabric-id [options]

### Description

  An integer (1-255) to select first hop router MAC adress in range 00:00:5E:00:01:01 to 00:00:5E:00:01:ff



## nv unset system port-mirror

### Usage

  nv unset system port-mirror [options] [<attribute> ...]

### Description

  Port mirror

### Atrributes

  session     sessions



## nv unset system port-mirror session

### Usage

  nv unset system port-mirror session [options] [<session-id> ...]

### Description

  sessions

### Identifiers

  <session-id>  port mirror session number

## nv unset system port-mirror session <session-id>

### Usage

  nv unset system port-mirror session <session-id> [options] [<attribute> ...]

### Description

  port mirror session number

### Identifiers

  <session-id>  port mirror session number

### Atrributes

  span          Switched Port Analyzer
  erspan        Encapsulated Remote Switched Port Analyzer.

## nv unset system port-mirror session <session-id> span

### Usage

  nv unset system port-mirror session <session-id> span [options] [<attribute> ...]

### Description

  Switched Port Analyzer

### Identifiers

  <session-id>  port mirror session number

### Atrributes

  source-port   Set of source ports.
  destination   The SPAN destination port.
  truncate      TBD
  enable        Turn the feature 'on' or 'off'. The default is 'off'.
  direction     The direction of traffic through source-port to mirror.

## nv unset system port-mirror session <session-id> span source-port

### Usage

  nv unset system port-mirror session <session-id> span source-port [options] [<port-id> ...]

### Description

  Set of source ports.

### Identifiers

  <session-id>  port mirror session number
  <port-id>     Port interface

## nv unset system port-mirror session <session-id> span source-port <port-id>

### Usage

  nv unset system port-mirror session <session-id> span source-port <port-id> [options]

### Description

  A port-mirror source port (swps or bonds only)

### Identifiers

  <session-id>  port mirror session number
  <port-id>     Port interface

## nv unset system port-mirror session <session-id> span destination

### Usage

  nv unset system port-mirror session <session-id> span destination [options] [<port-id> ...]

### Description

  The SPAN destination port.

### Identifiers

  <session-id>  port mirror session number
  <port-id>     Port interface

## nv unset system port-mirror session <session-id> span destination <port-id>

### Usage

  nv unset system port-mirror session <session-id> span destination <port-id> [options]

### Description

  The SPAN destination port.

### Identifiers

  <session-id>  port mirror session number
  <port-id>     Port interface

## nv unset system port-mirror session <session-id> span truncate

### Usage

  nv unset system port-mirror session <session-id> span truncate [options] [<attribute> ...]

### Description

  TBD

### Identifiers

  <session-id>  port mirror session number

### Atrributes

  enable        Turn the feature 'on' or 'off'. The default is 'off'.
  size          Truncates the mirrored frames at specified number of bytes.
                Truncate size must be between 4 and 4088 bytes and a multiple
                of 4

## nv unset system port-mirror session <session-id> span truncate enable

### Usage

  nv unset system port-mirror session <session-id> span truncate enable [options]

### Description

  Turn the feature 'on' or 'off'.  The default is 'off'.

### Identifiers

  <session-id>  port mirror session number

## nv unset system port-mirror session <session-id> span truncate size

### Usage

  nv unset system port-mirror session <session-id> span truncate size [options]

### Description

  Truncates the mirrored frames at specified number of bytes.  Truncate size must be between 4 and 4088 bytes and a multiple of 4

### Identifiers

  <session-id>  port mirror session number

## nv unset system port-mirror session <session-id> span enable

### Usage

  nv unset system port-mirror session <session-id> span enable [options]

### Description

  Turn the feature 'on' or 'off'.  The default is 'off'.

### Identifiers

  <session-id>  port mirror session number

## nv unset system port-mirror session <session-id> span direction

### Usage

  nv unset system port-mirror session <session-id> span direction [options]

### Description

  The direction of traffic through source-port to mirror.

### Identifiers

  <session-id>  port mirror session number

## nv unset system port-mirror session <session-id> erspan

### Usage

  nv unset system port-mirror session <session-id> erspan [options] [<attribute> ...]

### Description

  Encapsulated Remote Switched Port Analyzer.

### Identifiers

  <session-id>  port mirror session number

### Atrributes

  source-port   Set of source ports.
  destination   erspan destination
  truncate      TBD
  enable        Turn the feature 'on' or 'off'. The default is 'off'.
  direction     The direction of traffic through source-port to mirror.

## nv unset system port-mirror session <session-id> erspan source-port

### Usage

  nv unset system port-mirror session <session-id> erspan source-port [options] [<port-id> ...]

### Description

  Set of source ports.

### Identifiers

  <session-id>  port mirror session number
  <port-id>     Port interface

## nv unset system port-mirror session <session-id> erspan source-port <port-id>

### Usage

  nv unset system port-mirror session <session-id> erspan source-port <port-id> [options]

### Description

  A port-mirror source port (swps or bonds only)

### Identifiers

  <session-id>  port mirror session number
  <port-id>     Port interface

## nv unset system port-mirror session <session-id> erspan destination

### Usage

  nv unset system port-mirror session <session-id> erspan destination [options] [<attribute> ...]

### Description

  erspan destination

### Identifiers

  <session-id>  port mirror session number

### Atrributes

  source-ip     TBD
  dest-ip       TBD

## nv unset system port-mirror session <session-id> erspan destination source-ip

### Usage

  nv unset system port-mirror session <session-id> erspan destination source-ip [options] [<source-ip> ...]

### Description

  Set of IPv4 addresses

### Identifiers

  <session-id>  port mirror session number
  <source-ip>   IPv4 address

## nv unset system port-mirror session <session-id> erspan destination source-ip <source-ip>

### Usage

  nv unset system port-mirror session <session-id> erspan destination source-ip <source-ip> [options]

### Description

  An IPv4 address

### Identifiers

  <session-id>  port mirror session number

## nv unset system port-mirror session <session-id> erspan destination dest-ip

### Usage

  nv unset system port-mirror session <session-id> erspan destination dest-ip [options] [<dest-ip> ...]

### Description

  Set of IPv4 addresses

### Identifiers

  <session-id>  port mirror session number
  <dest-ip>     IPv4 address

## nv unset system port-mirror session <session-id> erspan destination dest-ip <dest-ip>

### Usage

  nv unset system port-mirror session <session-id> erspan destination dest-ip <dest-ip> [options]

### Description

  An IPv4 address

### Identifiers

  <session-id>  port mirror session number

## nv unset system port-mirror session <session-id> erspan truncate

### Usage

  nv unset system port-mirror session <session-id> erspan truncate [options] [<attribute> ...]

### Description

  TBD

### Identifiers

  <session-id>  port mirror session number

### Atrributes

  enable        Turn the feature 'on' or 'off'. The default is 'off'.
  size          Truncates the mirrored frames at specified number of bytes.
                Truncate size must be between 4 and 4088 bytes and a multiple
                of 4

## nv unset system port-mirror session <session-id> erspan truncate enable

### Usage

  nv unset system port-mirror session <session-id> erspan truncate enable [options]

### Description

  Turn the feature 'on' or 'off'.  The default is 'off'.

### Identifiers

  <session-id>  port mirror session number

## nv unset system port-mirror session <session-id> erspan truncate size

### Usage

  nv unset system port-mirror session <session-id> erspan truncate size [options]

### Description

  Truncates the mirrored frames at specified number of bytes.  Truncate size must be between 4 and 4088 bytes and a multiple of 4

### Identifiers

  <session-id>  port mirror session number

## nv unset system port-mirror session <session-id> erspan enable

### Usage

  nv unset system port-mirror session <session-id> erspan enable [options]

### Description

  Turn the feature 'on' or 'off'.  The default is 'off'.

### Identifiers

  <session-id>  port mirror session number

## nv unset system port-mirror session <session-id> erspan direction

### Usage

  nv unset system port-mirror session <session-id> erspan direction [options]

### Description

  The direction of traffic through source-port to mirror.

### Identifiers

  <session-id>  port mirror session number

## nv unset system config

### Usage

  nv unset system config [options] [<attribute> ...]

### Description

  Affect how config operations are performed.

### Atrributes

  apply       Affect how config apply operations are performed.



## nv unset system config apply

### Usage

  nv unset system config apply [options] [<attribute> ...]

### Description

  Affect how config apply operations are performed.

### Atrributes

  ignore      Set of files to ignore during config apply operations.
  overwrite   Determine which files can be overwritten during an apply. When
              "all", then all files can be overwritten. If the file was
              locally modified, then a warning will be issued and the client
              will have an opportunity to abort the apply before the local
              modifications are overwritten. This is the default. When
              "controlled", then only files that were most recently written by
              CUE can be overwritten. If the file was locally modified, a
              warning will be issued, but the file will not be overwritten.



## nv unset system config apply ignore

### Usage

  nv unset system config apply ignore [options] [<ignore-id> ...]

### Description

  Set of files to ignore during config apply operations.

### Identifiers

  <ignore-id>  Ignored file

## nv unset system config apply ignore <ignore-id>

### Usage

  nv unset system config apply ignore <ignore-id> [options]

### Description

  File to ignore during config apply operations.

### Identifiers

  <ignore-id>  Ignored file

## nv unset system config apply overwrite

### Usage

  nv unset system config apply overwrite [options]

### Description

  Determine which files can be overwritten during an apply.
  
  When "all", then all files can be overwritten.  If the file was
  locally modified, then a warning will be issued and the client
  will have an opportunity to abort the apply before the local
  modifications are overwritten.  This is the default.
  
  When "controlled", then only files that were most recently
  written by CUE can be overwritten.  If the file was locally
  modified, a warning will be issued, but the file will not be
  overwritten.



## nv unset system hostname

### Usage

  nv unset system hostname [options]

### Description

  Static hostname for the switch



## nv unset system timezone

### Usage

  nv unset system timezone [options]

### Description

  system time zone



## nv unset vrf

### Usage

  nv unset vrf [options] [<vrf-id> ...]

### Description

  VRFs

### Identifiers

  <vrf-id>    VRF

## nv unset vrf <vrf-id>

### Usage

  nv unset vrf <vrf-id> [options] [<attribute> ...]

### Description

  A VRF

### Identifiers

  <vrf-id>    VRF### Atrributes

  loopback    The loopback IP interface associated with this VRF.
  evpn        EVPN control plane config and info for VRF
  router      A VRF
  ptp         VRF PTP configuration. Inherited by interfaces in this VRF.
  table       The routing table number, between 1001-1255, used by the named
              VRF. If auto, the default, it will be auto generated.



## nv unset vrf <vrf-id> loopback

### Usage

  nv unset vrf <vrf-id> loopback [options] [<attribute> ...]

### Description

  The loopback IP interface associated with this VRF.

### Identifiers

  <vrf-id>    VRF### Atrributes

  ip          Properties associated with the loopback IP address on this VRF.



## nv unset vrf <vrf-id> loopback ip

### Usage

  nv unset vrf <vrf-id> loopback ip [options] [<attribute> ...]

### Description

  IP addresses associated with the VRF's loopback interface.

### Identifiers

  <vrf-id>    VRF### Atrributes

  address     static IPv4 or IPv6 address



## nv unset vrf <vrf-id> loopback ip address <ip-prefix-id>

### Usage

  nv unset vrf <vrf-id> loopback ip address <ip-prefix-id> [options]

### Description

  An IP address with prefix

### Identifiers

  <vrf-id>        VRF
  <ip-prefix-id>  IPv4 or IPv6 address and route prefix in CIDR notation

## nv unset vrf <vrf-id> evpn

### Usage

  nv unset vrf <vrf-id> evpn [options] [<attribute> ...]

### Description

  EVPN control plane config and info for VRF

### Identifiers

  <vrf-id>    VRF### Atrributes

  vni         L3 VNI
  enable      Turn the feature 'on' or 'off'. The default is 'off'.
  vlan        VLAN ID



## nv unset vrf <vrf-id> evpn vni <vni-id>

### Usage

  nv unset vrf <vrf-id> evpn vni <vni-id> [options] [<attribute> ...]

### Description

  VNI

### Identifiers

  <vrf-id>            VRF
  <vni-id>            VxLAN ID

### Atrributes

  prefix-routes-only  Associated L3 VNI and corresponding route targets only
                      with EVPN type-5 routes, not with EVPN type-2 routes.




## nv unset vrf <vrf-id> evpn vni <vni-id> prefix-routes-only

### Usage

  nv unset vrf <vrf-id> evpn vni <vni-id> prefix-routes-only [options]

### Description

  Associated L3 VNI and corresponding route targets only with EVPN type-5 routes, not with EVPN type-2 routes.

### Identifiers

  <vrf-id>    VRF
  <vni-id>    VxLAN ID



## nv unset vrf <vrf-id> evpn enable

### Usage

  nv unset vrf <vrf-id> evpn enable [options]

### Description

  Turn the feature 'on' or 'off'.  The default is 'off'.

### Identifiers

  <vrf-id>    VRF

## nv unset vrf <vrf-id> evpn vlan

### Usage

  nv unset vrf <vrf-id> evpn vlan [options]

### Description

  VLAN ID

### Identifiers

  <vrf-id>    VRF

## nv unset vrf <vrf-id> router

### Usage

  nv unset vrf <vrf-id> router [options] [<attribute> ...]

### Description

  A VRF

### Identifiers

  <vrf-id>    VRF### Atrributes

  rib         RIB Routes
  bgp         BGP VRF configuration.
  static      Routes
  pim         PIM VRF configuration.
  ospf        OSPF VRF configuration.



## nv unset vrf <vrf-id> router rib <afi>

### Usage

  nv unset vrf <vrf-id> router rib <afi> [options] [<attribute> ...]

### Description

  Vrf aware Routing-table per address-family

### Identifiers

  <vrf-id>    VRF
  <afi>       Route address family.

### Atrributes

  protocol    Import protocols from RIB to FIB



## nv unset vrf <vrf-id> router rib <afi> protocol <import-protocol-id>

### Usage

  nv unset vrf <vrf-id> router rib <afi> protocol <import-protocol-id> [options] [<attribute> ...]

### Description

  Import Protocols from where routes are known

### Identifiers

  <vrf-id>              VRF
  <afi>                 Route address family.
  <import-protocol-id>  Import protocol list.

### Atrributes

  fib-filter            Route map to apply on the import prootcol's routes.

## nv unset vrf <vrf-id> router rib <afi> protocol <import-protocol-id> fib-filter

### Usage

  nv unset vrf <vrf-id> router rib <afi> protocol <import-protocol-id> fib-filter [options]

### Description

  Route map to apply on the import prootcol's routes.

### Identifiers

  <vrf-id>              VRF
  <afi>                 Route address family.
  <import-protocol-id>  Import protocol list.

## nv unset vrf <vrf-id> router bgp

### Usage

  nv unset vrf <vrf-id> router bgp [options] [<attribute> ...]

### Description

  BGP VRF configuration.

### Identifiers

  <vrf-id>            VRF

### Atrributes

  address-family      Address family specific configuration
  path-selection      BGP path-selection configuration.
  route-reflection    BGP route-reflection configuration.
  peer-group          Peers
  route-export        Controls for exporting ipv4 and ipv6 routes from this
                      VRF
  route-import        Controls for importing of ipv4 and ipv6 routes from this
                      VRF
  timers              timer values for all peers in this VRF
  confederation       BGP Confederation options.
  neighbor            Peers
  enable              Turn the feature 'on' or 'off'. The default is 'off'.
  autonomous-system   ASN for this VRF. If "auto", inherit from the global
                      config. This is the default.
  dynamic-peer-limit  Maximum number of dynamic neighbors from whom we can
                      accept a connection. Applicable only if 'dynamic-
                      peering' subnet ranges are configured
  rd                  BGP Route Distinguisher to use when this VRF routes have
                      to be exported.
  router-id           BGP router-id for this VRF. If "auto", inherit from the
                      global config. This is the default.




## nv unset vrf <vrf-id> router bgp address-family

### Usage

  nv unset vrf <vrf-id> router bgp address-family [options] [<attribute> ...]

### Description

  Address family specific configuration

### Identifiers

  <vrf-id>      VRF

### Atrributes

  ipv4-unicast  IPv4 unicast address family
  l2vpn-evpn    BGP VRF configuration. L2VPN EVPN address family
  ipv6-unicast  IPv6 unicast address family

## nv unset vrf <vrf-id> router bgp address-family ipv4-unicast

### Usage

  nv unset vrf <vrf-id> router bgp address-family ipv4-unicast [options] [<attribute> ...]

### Description

  IPv4 unicast address family

### Identifiers

  <vrf-id>         VRF

### Atrributes

  redistribute     Route redistribute
  aggregate-route  IPv4 aggregate routes
  network          IPv4 static networks.
  route-import     Route import
  multipaths       Multipaths
  admin-distance   Admin distances.
  route-export     Route export
  rib-filter       Specifies filtering policies to apply prior to route
                   install into the zebra RIB
  enable           Turn the feature 'on' or 'off'. The default is 'on'.

## nv unset vrf <vrf-id> router bgp address-family ipv4-unicast redistribute
### Usage

  nv unset vrf <vrf-id> router bgp address-family ipv4-unicast redistribute [options] [<attribute> ...]

### Description

  Route redistribute

### Identifiers

  <vrf-id>    VRF### Atrributes

  static      Route redistribution of ipv4 static routes
  connected   Route redistribution of ipv4 connected routes
  kernel      Route redistribution of ipv4 kernel routes
  ospf        Route redistribution of ipv4 ospf routes

## nv unset vrf <vrf-id> router bgp address-family ipv4-unicast redistribute static
### Usage

  nv unset vrf <vrf-id> router bgp address-family ipv4-unicast redistribute static [options] [<attribute> ...]

### Description

  Source route type.

### Identifiers

  <vrf-id>    VRF### Atrributes

  enable      Turn the feature 'on' or 'off'. The default is 'off'.
  metric      Metric to use for the redistributed route. If "auto", an
              appropriate value will be chosen based on the type of route.
              This is the default.
  route-map   Route map to apply to the redistributed route.

## nv unset vrf <vrf-id> router bgp address-family ipv4-unicast redistribute static enable
### Usage

  nv unset vrf <vrf-id> router bgp address-family ipv4-unicast redistribute static enable [options]

### Description

  Turn the feature 'on' or 'off'.  The default is 'off'.

### Identifiers

  <vrf-id>    VRF## nv unset vrf <vrf-id> router bgp address-family ipv4-unicast redistribute static metric
### Usage

  nv unset vrf <vrf-id> router bgp address-family ipv4-unicast redistribute static metric [options]

### Description

  Metric to use for the redistributed route.  If "auto", an appropriate value will be chosen based on the type of route.  This is the default.

### Identifiers

  <vrf-id>    VRF## nv unset vrf <vrf-id> router bgp address-family ipv4-unicast redistribute static route-map
### Usage

  nv unset vrf <vrf-id> router bgp address-family ipv4-unicast redistribute static route-map [options]

### Description

  Route map to apply to the redistributed route.

### Identifiers

  <vrf-id>    VRF## nv unset vrf <vrf-id> router bgp address-family ipv4-unicast redistribute connected
### Usage

  nv unset vrf <vrf-id> router bgp address-family ipv4-unicast redistribute connected [options] [<attribute> ...]

### Description

  Source route type.

### Identifiers

  <vrf-id>    VRF### Atrributes

  enable      Turn the feature 'on' or 'off'. The default is 'off'.
  metric      Metric to use for the redistributed route. If "auto", an
              appropriate value will be chosen based on the type of route.
              This is the default.
  route-map   Route map to apply to the redistributed route.

## nv unset vrf <vrf-id> router bgp address-family ipv4-unicast redistribute connected enable
### Usage

  nv unset vrf <vrf-id> router bgp address-family ipv4-unicast redistribute connected enable [options]

### Description

  Turn the feature 'on' or 'off'.  The default is 'off'.

### Identifiers

  <vrf-id>    VRF## nv unset vrf <vrf-id> router bgp address-family ipv4-unicast redistribute connected metric
### Usage

  nv unset vrf <vrf-id> router bgp address-family ipv4-unicast redistribute connected metric [options]

### Description

  Metric to use for the redistributed route.  If "auto", an appropriate value will be chosen based on the type of route.  This is the default.

### Identifiers

  <vrf-id>    VRF## nv unset vrf <vrf-id> router bgp address-family ipv4-unicast redistribute connected route-map
### Usage

  nv unset vrf <vrf-id> router bgp address-family ipv4-unicast redistribute connected route-map [options]

### Description

  Route map to apply to the redistributed route.

### Identifiers

  <vrf-id>    VRF## nv unset vrf <vrf-id> router bgp address-family ipv4-unicast redistribute kernel
### Usage

  nv unset vrf <vrf-id> router bgp address-family ipv4-unicast redistribute kernel [options] [<attribute> ...]

### Description

  Source route type.

### Identifiers

  <vrf-id>    VRF### Atrributes

  enable      Turn the feature 'on' or 'off'. The default is 'off'.
  metric      Metric to use for the redistributed route. If "auto", an
              appropriate value will be chosen based on the type of route.
              This is the default.
  route-map   Route map to apply to the redistributed route.

## nv unset vrf <vrf-id> router bgp address-family ipv4-unicast redistribute kernel enable
### Usage

  nv unset vrf <vrf-id> router bgp address-family ipv4-unicast redistribute kernel enable [options]

### Description

  Turn the feature 'on' or 'off'.  The default is 'off'.

### Identifiers

  <vrf-id>    VRF## nv unset vrf <vrf-id> router bgp address-family ipv4-unicast redistribute kernel metric
### Usage

  nv unset vrf <vrf-id> router bgp address-family ipv4-unicast redistribute kernel metric [options]

### Description

  Metric to use for the redistributed route.  If "auto", an appropriate value will be chosen based on the type of route.  This is the default.

### Identifiers

  <vrf-id>    VRF## nv unset vrf <vrf-id> router bgp address-family ipv4-unicast redistribute kernel route-map
### Usage

  nv unset vrf <vrf-id> router bgp address-family ipv4-unicast redistribute kernel route-map [options]

### Description

  Route map to apply to the redistributed route.

### Identifiers

  <vrf-id>    VRF## nv unset vrf <vrf-id> router bgp address-family ipv4-unicast redistribute ospf
### Usage

  nv unset vrf <vrf-id> router bgp address-family ipv4-unicast redistribute ospf [options] [<attribute> ...]

### Description

  Source route type.

### Identifiers

  <vrf-id>    VRF### Atrributes

  enable      Turn the feature 'on' or 'off'. The default is 'off'.
  metric      Metric to use for the redistributed route. If "auto", an
              appropriate value will be chosen based on the type of route.
              This is the default.
  route-map   Route map to apply to the redistributed route.

## nv unset vrf <vrf-id> router bgp address-family ipv4-unicast redistribute ospf enable
### Usage

  nv unset vrf <vrf-id> router bgp address-family ipv4-unicast redistribute ospf enable [options]

### Description

  Turn the feature 'on' or 'off'.  The default is 'off'.

### Identifiers

  <vrf-id>    VRF## nv unset vrf <vrf-id> router bgp address-family ipv4-unicast redistribute ospf metric
### Usage

  nv unset vrf <vrf-id> router bgp address-family ipv4-unicast redistribute ospf metric [options]

### Description

  Metric to use for the redistributed route.  If "auto", an appropriate value will be chosen based on the type of route.  This is the default.

### Identifiers

  <vrf-id>    VRF## nv unset vrf <vrf-id> router bgp address-family ipv4-unicast redistribute ospf route-map
### Usage

  nv unset vrf <vrf-id> router bgp address-family ipv4-unicast redistribute ospf route-map [options]

### Description

  Route map to apply to the redistributed route.

### Identifiers

  <vrf-id>    VRF## nv unset vrf <vrf-id> router bgp address-family ipv4-unicast aggregate-route <aggregate-route-id>
### Usage

  nv unset vrf <vrf-id> router bgp address-family ipv4-unicast aggregate-route <aggregate-route-id> [options] [<attribute> ...]

### Description

  An IPv4 aggregate route

### Identifiers

  <vrf-id>              VRF
  <aggregate-route-id>  IPv4 address and route prefix in CIDR notation

### Atrributes

  as-set                If 'on', an AS_SET is generated for the aggregate.
  route-map             Optional policy to modify attributes
  summary-only          If 'on', suppress more-specific routes.

## nv unset vrf <vrf-id> router bgp address-family ipv4-unicast aggregate-route <aggregate-route-id> summary-only
### Usage

  nv unset vrf <vrf-id> router bgp address-family ipv4-unicast aggregate-route <aggregate-route-id> summary-only [options]

### Description

  If 'on', suppress more-specific routes.

### Identifiers

  <vrf-id>              VRF
  <aggregate-route-id>  IPv4 address and route prefix in CIDR notation

## nv unset vrf <vrf-id> router bgp address-family ipv4-unicast aggregate-route <aggregate-route-id> as-set
### Usage

  nv unset vrf <vrf-id> router bgp address-family ipv4-unicast aggregate-route <aggregate-route-id> as-set [options]

### Description

  If 'on', an AS_SET is generated for the aggregate.

### Identifiers

  <vrf-id>              VRF
  <aggregate-route-id>  IPv4 address and route prefix in CIDR notation

## nv unset vrf <vrf-id> router bgp address-family ipv4-unicast aggregate-route <aggregate-route-id> route-map
### Usage

  nv unset vrf <vrf-id> router bgp address-family ipv4-unicast aggregate-route <aggregate-route-id> route-map [options]

### Description

  Optional policy to modify attributes

### Identifiers

  <vrf-id>              VRF
  <aggregate-route-id>  IPv4 address and route prefix in CIDR notation

## nv unset vrf <vrf-id> router bgp address-family ipv4-unicast network <static-network-id>
### Usage

  nv unset vrf <vrf-id> router bgp address-family ipv4-unicast network <static-network-id> [options] [<attribute> ...]

### Description

  An IPv4 static network.

### Identifiers

  <vrf-id>             VRF
  <static-network-id>  IPv4 address and route prefix in CIDR notation

### Atrributes

  route-map            Optional policy to modify attributes

## nv unset vrf <vrf-id> router bgp address-family ipv4-unicast network <static-network-id> route-map

### Usage

  nv unset vrf <vrf-id> router bgp address-family ipv4-unicast network <static-network-id> route-map [options]

### Description

  Optional policy to modify attributes

### Identifiers

  <vrf-id>             VRF
  <static-network-id>  IPv4 address and route prefix in CIDR notation

## nv unset vrf <vrf-id> router bgp address-family ipv4-unicast route-import
### Usage

  nv unset vrf <vrf-id> router bgp address-family ipv4-unicast route-import [options] [<attribute> ...]

### Description

  Route import

### Identifiers

  <vrf-id>    VRF### Atrributes

  from-vrf    Controls for VRF to VRF route leaking for this address-family

## nv unset vrf <vrf-id> router bgp address-family ipv4-unicast route-import from-vrf
### Usage

  nv unset vrf <vrf-id> router bgp address-family ipv4-unicast route-import from-vrf [options] [<attribute> ...]

### Description

  Controls for VRF to VRF route leaking for this address-family

### Identifiers

  <vrf-id>    VRF### Atrributes

  list        List of VRFs the routes can be imported from
  enable      Turn the feature 'on' or 'off'. The default is 'off'.
  route-map   Route-map to control the import of routes into EVPN

## nv unset vrf <vrf-id> router bgp address-family ipv4-unicast route-import from-vrf list <leak-vrf-id>
### Usage

  nv unset vrf <vrf-id> router bgp address-family ipv4-unicast route-import from-vrf list <leak-vrf-id> [options]

### Description

  A VRF

### Identifiers

  <vrf-id>       VRF
  <leak-vrf-id>  VRF

## nv unset vrf <vrf-id> router bgp address-family ipv4-unicast route-import from-vrf enable
### Usage

  nv unset vrf <vrf-id> router bgp address-family ipv4-unicast route-import from-vrf enable [options]

### Description

  Turn the feature 'on' or 'off'.  The default is 'off'.

### Identifiers

  <vrf-id>    VRF## nv unset vrf <vrf-id> router bgp address-family ipv4-unicast route-import from-vrf route-map
### Usage

  nv unset vrf <vrf-id> router bgp address-family ipv4-unicast route-import from-vrf route-map [options]

### Description

  Route-map to control the import of routes into EVPN

### Identifiers

  <vrf-id>    VRF## nv unset vrf <vrf-id> router bgp address-family ipv4-unicast multipaths
### Usage

  nv unset vrf <vrf-id> router bgp address-family ipv4-unicast multipaths [options] [<attribute> ...]

### Description

  Multipaths

### Identifiers

  <vrf-id>              VRF

### Atrributes

  compare-cluster-length
                        If on, if IBGP paths have a CLUSTER_LIST, their
                        lengths must be equal to be selected as multipaths
  ebgp                  EBGP multipath
  ibgp                  IBGP multipath

## nv unset vrf <vrf-id> router bgp address-family ipv4-unicast multipaths ebgp
### Usage

  nv unset vrf <vrf-id> router bgp address-family ipv4-unicast multipaths ebgp [options]

### Description

  EBGP multipath

### Identifiers

  <vrf-id>    VRF## nv unset vrf <vrf-id> router bgp address-family ipv4-unicast multipaths ibgp
### Usage

  nv unset vrf <vrf-id> router bgp address-family ipv4-unicast multipaths ibgp [options]

### Description

  IBGP multipath

### Identifiers

  <vrf-id>    VRF## nv unset vrf <vrf-id> router bgp address-family ipv4-unicast multipaths compare-cluster-length
### Usage

  nv unset vrf <vrf-id> router bgp address-family ipv4-unicast multipaths compare-cluster-length [options]

### Description

  If on, if IBGP paths have a CLUSTER_LIST, their lengths must be equal to be selected as multipaths

### Identifiers

  <vrf-id>    VRF## nv unset vrf <vrf-id> router bgp address-family ipv4-unicast admin-distance

### Usage

  nv unset vrf <vrf-id> router bgp address-family ipv4-unicast admin-distance [options] [<attribute> ...]

### Description

  Admin distances.

### Identifiers

  <vrf-id>    VRF### Atrributes

  external    Distance to apply to routes from EBGP peers when installed into
              the RIB
  internal    Distance to apply to routes from IBGP peers when installed into
              the RIB

## nv unset vrf <vrf-id> router bgp address-family ipv4-unicast admin-distance external
### Usage

  nv unset vrf <vrf-id> router bgp address-family ipv4-unicast admin-distance external [options]

### Description

  Distance to apply to routes from EBGP peers when installed into the RIB

### Identifiers

  <vrf-id>    VRF## nv unset vrf <vrf-id> router bgp address-family ipv4-unicast admin-distance internal

### Usage

  nv unset vrf <vrf-id> router bgp address-family ipv4-unicast admin-distance internal [options]

### Description

  Distance to apply to routes from IBGP peers when installed into the RIB

### Identifiers

  <vrf-id>    VRF## nv unset vrf <vrf-id> router bgp address-family ipv4-unicast route-export
### Usage

  nv unset vrf <vrf-id> router bgp address-family ipv4-unicast route-export [options] [<attribute> ...]

### Description

  Route export

### Identifiers

  <vrf-id>    VRF### Atrributes

  to-evpn     Controls for exporting routes from this VRF for this address-
              family into EVPN (as type-5 routes)

## nv unset vrf <vrf-id> router bgp address-family ipv4-unicast route-export to-evpn
### Usage

  nv unset vrf <vrf-id> router bgp address-family ipv4-unicast route-export to-evpn [options] [<attribute> ...]

### Description

  Controls for exporting routes from this VRF for this address-family into EVPN (as type-5 routes)

### Identifiers

  <vrf-id>              VRF

### Atrributes

  enable                Turn the feature 'on' or 'off'. The default is 'off'.
  default-route-origination
                        Default route origination
  route-map             Route-map to control the export of routes into EVPN

## nv unset vrf <vrf-id> router bgp address-family ipv4-unicast route-export to-evpn enable
### Usage

  nv unset vrf <vrf-id> router bgp address-family ipv4-unicast route-export to-evpn enable [options]

### Description

  Turn the feature 'on' or 'off'.  The default is 'off'.

### Identifiers

  <vrf-id>    VRF## nv unset vrf <vrf-id> router bgp address-family ipv4-unicast route-export to-evpn route-map
### Usage

  nv unset vrf <vrf-id> router bgp address-family ipv4-unicast route-export to-evpn route-map [options]

### Description

  Route-map to control the export of routes into EVPN

### Identifiers

  <vrf-id>    VRF## nv unset vrf <vrf-id> router bgp address-family ipv4-unicast route-export to-evpn default-route-origination
### Usage

  nv unset vrf <vrf-id> router bgp address-family ipv4-unicast route-export to-evpn default-route-origination [options]

### Description

  Default route origination

### Identifiers

  <vrf-id>    VRF## nv unset vrf <vrf-id> router bgp address-family ipv4-unicast rib-filter
### Usage

  nv unset vrf <vrf-id> router bgp address-family ipv4-unicast rib-filter [options]

### Description

  Specifies filtering policies to apply prior to route install into the zebra RIB

### Identifiers

  <vrf-id>    VRF## nv unset vrf <vrf-id> router bgp address-family ipv4-unicast enable
### Usage

  nv unset vrf <vrf-id> router bgp address-family ipv4-unicast enable [options]

### Description

  Turn the feature 'on' or 'off'.  The default is 'on'.

### Identifiers

  <vrf-id>    VRF## nv unset vrf <vrf-id> router bgp address-family l2vpn-evpn
### Usage

  nv unset vrf <vrf-id> router bgp address-family l2vpn-evpn [options] [<attribute> ...]

### Description

  BGP VRF configuration. L2VPN EVPN address family

### Identifiers

  <vrf-id>    VRF### Atrributes

  enable      Turn the feature 'on' or 'off'. The default is 'off'.

## nv unset vrf <vrf-id> router bgp address-family l2vpn-evpn enable

### Usage

  nv unset vrf <vrf-id> router bgp address-family l2vpn-evpn enable [options]

### Description

  Turn the feature 'on' or 'off'.  The default is 'off'.

### Identifiers

  <vrf-id>    VRF## nv unset vrf <vrf-id> router bgp address-family ipv6-unicast

### Usage

  nv unset vrf <vrf-id> router bgp address-family ipv6-unicast [options] [<attribute> ...]

### Description

  IPv6 unicast address family

### Identifiers

  <vrf-id>         VRF

### Atrributes

  aggregate-route  IPv6 aggregate routes
  network          IPv6 static networks.
  route-import     Route import
  multipaths       Multipaths
  admin-distance   Admin distances.
  route-export     Route export
  redistribute     Route redistribute
  rib-filter       Specifies filtering policies to apply prior to route
                   install into the zebra RIB
  enable           Turn the feature 'on' or 'off'. The default is 'off'.

## nv unset vrf <vrf-id> router bgp address-family ipv6-unicast aggregate-route <aggregate-route-id>
### Usage

  nv unset vrf <vrf-id> router bgp address-family ipv6-unicast aggregate-route <aggregate-route-id> [options] [<attribute> ...]

### Description

  An IPv6 aggregate route

### Identifiers

  <vrf-id>              VRF
  <aggregate-route-id>  IPv6 address and route prefix in CIDR notation

### Atrributes

  as-set                If 'on', an AS_SET is generated for the aggregate.
  route-map             Optional policy to modify attributes
  summary-only          If 'on', suppress more-specific routes.

## nv unset vrf <vrf-id> router bgp address-family ipv6-unicast aggregate-route <aggregate-route-id> summary-only
### Usage

  nv unset vrf <vrf-id> router bgp address-family ipv6-unicast aggregate-route <aggregate-route-id> summary-only [options]

### Description

  If 'on', suppress more-specific routes.

### Identifiers

  <vrf-id>              VRF
  <aggregate-route-id>  IPv6 address and route prefix in CIDR notation

## nv unset vrf <vrf-id> router bgp address-family ipv6-unicast aggregate-route <aggregate-route-id> as-set
### Usage

  nv unset vrf <vrf-id> router bgp address-family ipv6-unicast aggregate-route <aggregate-route-id> as-set [options]

### Description

  If 'on', an AS_SET is generated for the aggregate.

### Identifiers

  <vrf-id>              VRF
  <aggregate-route-id>  IPv6 address and route prefix in CIDR notation

## nv unset vrf <vrf-id> router bgp address-family ipv6-unicast aggregate-route <aggregate-route-id> route-map
### Usage

  nv unset vrf <vrf-id> router bgp address-family ipv6-unicast aggregate-route <aggregate-route-id> route-map [options]

### Description

  Optional policy to modify attributes

### Identifiers

  <vrf-id>              VRF
  <aggregate-route-id>  IPv6 address and route prefix in CIDR notation

## nv unset vrf <vrf-id> router bgp address-family ipv6-unicast network <static-network-id>
### Usage

  nv unset vrf <vrf-id> router bgp address-family ipv6-unicast network <static-network-id> [options] [<attribute> ...]

### Description

  An IPv6 static network.

### Identifiers

  <vrf-id>             VRF
  <static-network-id>  IPv6 address and route prefix in CIDR notation

### Atrributes

  route-map            Optional policy to modify attributes

## nv unset vrf <vrf-id> router bgp address-family ipv6-unicast network <static-network-id> route-map
### Usage

  nv unset vrf <vrf-id> router bgp address-family ipv6-unicast network <static-network-id> route-map [options]

### Description

  Optional policy to modify attributes

### Identifiers

  <vrf-id>             VRF
  <static-network-id>  IPv6 address and route prefix in CIDR notation

## nv unset vrf <vrf-id> router bgp address-family ipv6-unicast route-import
### Usage

  nv unset vrf <vrf-id> router bgp address-family ipv6-unicast route-import [options] [<attribute> ...]

### Description

  Route import

### Identifiers

  <vrf-id>    VRF### Atrributes

  from-vrf    Controls for VRF to VRF route leaking for this address-family

## nv unset vrf <vrf-id> router bgp address-family ipv6-unicast route-import from-vrf
### Usage

  nv unset vrf <vrf-id> router bgp address-family ipv6-unicast route-import from-vrf [options] [<attribute> ...]

### Description

  Controls for VRF to VRF route leaking for this address-family

### Identifiers

  <vrf-id>    VRF### Atrributes

  list        List of VRFs the routes can be imported from
  enable      Turn the feature 'on' or 'off'. The default is 'off'.
  route-map   Route-map to control the import of routes into EVPN

## nv unset vrf <vrf-id> router bgp address-family ipv6-unicast route-import from-vrf list
### Usage

  nv unset vrf <vrf-id> router bgp address-family ipv6-unicast route-import from-vrf list [options]

### Description

  Set of VRFs

### Identifiers

  <vrf-id>    VRF## nv unset vrf <vrf-id> router bgp address-family ipv6-unicast route-import from-vrf enable
### Usage

  nv unset vrf <vrf-id> router bgp address-family ipv6-unicast route-import from-vrf enable [options]

### Description

  Turn the feature 'on' or 'off'.  The default is 'off'.

### Identifiers

  <vrf-id>    VRF## nv unset vrf <vrf-id> router bgp address-family ipv6-unicast route-import from-vrf route-map
### Usage

  nv unset vrf <vrf-id> router bgp address-family ipv6-unicast route-import from-vrf route-map [options]

### Description

  Route-map to control the import of routes into EVPN

### Identifiers

  <vrf-id>    VRF## nv unset vrf <vrf-id> router bgp address-family ipv6-unicast multipaths
### Usage

  nv unset vrf <vrf-id> router bgp address-family ipv6-unicast multipaths [options] [<attribute> ...]

### Description

  Multipaths

### Identifiers

  <vrf-id>              VRF

### Atrributes

  compare-cluster-length
                        If on, if IBGP paths have a CLUSTER_LIST, their
                        lengths must be equal to be selected as multipaths
  ebgp                  EBGP multipath
  ibgp                  IBGP multipath

## nv unset vrf <vrf-id> router bgp address-family ipv6-unicast multipaths ebgp
### Usage

  nv unset vrf <vrf-id> router bgp address-family ipv6-unicast multipaths ebgp [options]

### Description

  EBGP multipath

### Identifiers

  <vrf-id>    VRF## nv unset vrf <vrf-id> router bgp address-family ipv6-unicast multipaths ibgp
### Usage

  nv unset vrf <vrf-id> router bgp address-family ipv6-unicast multipaths ibgp [options]

### Description

  IBGP multipath

### Identifiers

  <vrf-id>    VRF## nv unset vrf <vrf-id> router bgp address-family ipv6-unicast multipaths compare-cluster-length
### Usage

  nv unset vrf <vrf-id> router bgp address-family ipv6-unicast multipaths compare-cluster-length [options]

### Description

  If on, if IBGP paths have a CLUSTER_LIST, their lengths must be equal to be selected as multipaths

### Identifiers

  <vrf-id>    VRF## nv unset vrf <vrf-id> router bgp address-family ipv6-unicast admin-distance
### Usage

  nv unset vrf <vrf-id> router bgp address-family ipv6-unicast admin-distance [options] [<attribute> ...]

### Description

  Admin distances.

### Identifiers

  <vrf-id>    VRF### Atrributes

  external    Distance to apply to routes from EBGP peers when installed into
              the RIB
  internal    Distance to apply to routes from IBGP peers when installed into
              the RIB

## nv unset vrf <vrf-id> router bgp address-family ipv6-unicast admin-distance external
### Usage

  nv unset vrf <vrf-id> router bgp address-family ipv6-unicast admin-distance external [options]

### Description

  Distance to apply to routes from EBGP peers when installed into the RIB

### Identifiers

  <vrf-id>    VRF## nv unset vrf <vrf-id> router bgp address-family ipv6-unicast admin-distance internal
### Usage

  nv unset vrf <vrf-id> router bgp address-family ipv6-unicast admin-distance internal [options]

### Description

  Distance to apply to routes from IBGP peers when installed into the RIB

### Identifiers

  <vrf-id>    VRF## nv unset vrf <vrf-id> router bgp address-family ipv6-unicast route-export
### Usage

  nv unset vrf <vrf-id> router bgp address-family ipv6-unicast route-export [options] [<attribute> ...]

### Description

  Route export

### Identifiers

  <vrf-id>    VRF### Atrributes

  to-evpn     Controls for exporting routes from this VRF for this address-
              family into EVPN (as type-5 routes)

## nv unset vrf <vrf-id> router bgp address-family ipv6-unicast route-export to-evpn
### Usage

  nv unset vrf <vrf-id> router bgp address-family ipv6-unicast route-export to-evpn [options] [<attribute> ...]

### Description

  Controls for exporting routes from this VRF for this address-family into EVPN (as type-5 routes)

### Identifiers

  <vrf-id>              VRF

### Atrributes

  enable                Turn the feature 'on' or 'off'. The default is 'off'.
  default-route-origination
                        Default route origination
  route-map             Route-map to control the export of routes into EVPN

## nv unset vrf <vrf-id> router bgp address-family ipv6-unicast route-export to-evpn enable

### Usage

  nv unset vrf <vrf-id> router bgp address-family ipv6-unicast route-export to-evpn enable [options]

### Description

  Turn the feature 'on' or 'off'.  The default is 'off'.

### Identifiers

  <vrf-id>    VRF## nv unset vrf <vrf-id> router bgp address-family ipv6-unicast route-export to-evpn route-map
### Usage

  nv unset vrf <vrf-id> router bgp address-family ipv6-unicast route-export to-evpn route-map [options]

### Description

  Route-map to control the export of routes into EVPN

### Identifiers

  <vrf-id>    VRF## nv unset vrf <vrf-id> router bgp address-family ipv6-unicast route-export to-evpn default-route-origination
### Usage

  nv unset vrf <vrf-id> router bgp address-family ipv6-unicast route-export to-evpn default-route-origination [options]

### Description

  Default route origination

### Identifiers

  <vrf-id>    VRF## nv unset vrf <vrf-id> router bgp address-family ipv6-unicast redistribute
### Usage

  nv unset vrf <vrf-id> router bgp address-family ipv6-unicast redistribute [options] [<attribute> ...]

### Description

  Route redistribute

### Identifiers

  <vrf-id>    VRF### Atrributes

  static      Route redistribution of ipv4 static routes
  connected   Route redistribution of ipv4 connected routes
  kernel      Route redistribution of ipv4 kernel routes
  ospf6       Route redistribution of ipv6 ospf routes

## nv unset vrf <vrf-id> router bgp address-family ipv6-unicast redistribute static
### Usage

  nv unset vrf <vrf-id> router bgp address-family ipv6-unicast redistribute static [options] [<attribute> ...]

### Description

  Source route type.

### Identifiers

  <vrf-id>    VRF### Atrributes

  enable      Turn the feature 'on' or 'off'. The default is 'off'.
  metric      Metric to use for the redistributed route. If "auto", an
              appropriate value will be chosen based on the type of route.
              This is the default.
  route-map   Route map to apply to the redistributed route.

## nv unset vrf <vrf-id> router bgp address-family ipv6-unicast redistribute static enable
### Usage

  nv unset vrf <vrf-id> router bgp address-family ipv6-unicast redistribute static enable [options]

### Description

  Turn the feature 'on' or 'off'.  The default is 'off'.

### Identifiers

  <vrf-id>    VRF## nv unset vrf <vrf-id> router bgp address-family ipv6-unicast redistribute static metric
### Usage

  nv unset vrf <vrf-id> router bgp address-family ipv6-unicast redistribute static metric [options]

### Description

  Metric to use for the redistributed route.  If "auto", an appropriate value will be chosen based on the type of route.  This is the default.

### Identifiers

  <vrf-id>    VRF## nv unset vrf <vrf-id> router bgp address-family ipv6-unicast redistribute static route-map
### Usage

  nv unset vrf <vrf-id> router bgp address-family ipv6-unicast redistribute static route-map [options]

### Description

  Route map to apply to the redistributed route.

### Identifiers

  <vrf-id>    VRF## nv unset vrf <vrf-id> router bgp address-family ipv6-unicast redistribute connected
### Usage

  nv unset vrf <vrf-id> router bgp address-family ipv6-unicast redistribute connected [options] [<attribute> ...]

### Description

  Source route type.

### Identifiers

  <vrf-id>    VRF### Atrributes

  enable      Turn the feature 'on' or 'off'. The default is 'off'.
  metric      Metric to use for the redistributed route. If "auto", an
              appropriate value will be chosen based on the type of route.
              This is the default.
  route-map   Route map to apply to the redistributed route.

## nv unset vrf <vrf-id> router bgp address-family ipv6-unicast redistribute connected enable
### Usage

  nv unset vrf <vrf-id> router bgp address-family ipv6-unicast redistribute connected enable [options]

### Description

  Turn the feature 'on' or 'off'.  The default is 'off'.

### Identifiers

  <vrf-id>    VRF## nv unset vrf <vrf-id> router bgp address-family ipv6-unicast redistribute connected metric
### Usage

  nv unset vrf <vrf-id> router bgp address-family ipv6-unicast redistribute connected metric [options]

### Description

  Metric to use for the redistributed route.  If "auto", an appropriate value will be chosen based on the type of route.  This is the default.

### Identifiers

  <vrf-id>    VRF## nv unset vrf <vrf-id> router bgp address-family ipv6-unicast redistribute connected route-map
### Usage

  nv unset vrf <vrf-id> router bgp address-family ipv6-unicast redistribute connected route-map [options]

### Description

  Route map to apply to the redistributed route.

### Identifiers

  <vrf-id>    VRF## nv unset vrf <vrf-id> router bgp address-family ipv6-unicast redistribute kernel
### Usage

  nv unset vrf <vrf-id> router bgp address-family ipv6-unicast redistribute kernel [options] [<attribute> ...]

### Description

  Source route type.

### Identifiers

  <vrf-id>    VRF### Atrributes

  enable      Turn the feature 'on' or 'off'. The default is 'off'.
  metric      Metric to use for the redistributed route. If "auto", an
              appropriate value will be chosen based on the type of route.
              This is the default.
  route-map   Route map to apply to the redistributed route.

## nv unset vrf <vrf-id> router bgp address-family ipv6-unicast redistribute kernel enable
### Usage

  nv unset vrf <vrf-id> router bgp address-family ipv6-unicast redistribute kernel enable [options]

### Description

  Turn the feature 'on' or 'off'.  The default is 'off'.

### Identifiers

  <vrf-id>    VRF## nv unset vrf <vrf-id> router bgp address-family ipv6-unicast redistribute kernel metric
### Usage

  nv unset vrf <vrf-id> router bgp address-family ipv6-unicast redistribute kernel metric [options]

### Description

  Metric to use for the redistributed route.  If "auto", an appropriate value will be chosen based on the type of route.  This is the default.

### Identifiers

  <vrf-id>    VRF## nv unset vrf <vrf-id> router bgp address-family ipv6-unicast redistribute kernel route-map
### Usage

  nv unset vrf <vrf-id> router bgp address-family ipv6-unicast redistribute kernel route-map [options]

### Description

  Route map to apply to the redistributed route.

### Identifiers

  <vrf-id>    VRF## nv unset vrf <vrf-id> router bgp address-family ipv6-unicast redistribute ospf6
### Usage

  nv unset vrf <vrf-id> router bgp address-family ipv6-unicast redistribute ospf6 [options] [<attribute> ...]

### Description

  Source route type.

### Identifiers

  <vrf-id>    VRF### Atrributes

  enable      Turn the feature 'on' or 'off'. The default is 'off'.
  metric      Metric to use for the redistributed route. If "auto", an
              appropriate value will be chosen based on the type of route.
              This is the default.
  route-map   Route map to apply to the redistributed route.

## nv unset vrf <vrf-id> router bgp address-family ipv6-unicast redistribute ospf6 enable
### Usage

  nv unset vrf <vrf-id> router bgp address-family ipv6-unicast redistribute ospf6 enable [options]

### Description

  Turn the feature 'on' or 'off'.  The default is 'off'.

### Identifiers

  <vrf-id>    VRF## nv unset vrf <vrf-id> router bgp address-family ipv6-unicast redistribute ospf6 metric
### Usage

  nv unset vrf <vrf-id> router bgp address-family ipv6-unicast redistribute ospf6 metric [options]

### Description

  Metric to use for the redistributed route.  If "auto", an appropriate value will be chosen based on the type of route.  This is the default.

### Identifiers

  <vrf-id>    VRF## nv unset vrf <vrf-id> router bgp address-family ipv6-unicast redistribute ospf6 route-map
### Usage

  nv unset vrf <vrf-id> router bgp address-family ipv6-unicast redistribute ospf6 route-map [options]

### Description

  Route map to apply to the redistributed route.

### Identifiers

  <vrf-id>    VRF## nv unset vrf <vrf-id> router bgp address-family ipv6-unicast rib-filter
### Usage

  nv unset vrf <vrf-id> router bgp address-family ipv6-unicast rib-filter [options]

### Description

  Specifies filtering policies to apply prior to route install into the zebra RIB

### Identifiers

  <vrf-id>    VRF## nv unset vrf <vrf-id> router bgp address-family ipv6-unicast enable
### Usage

  nv unset vrf <vrf-id> router bgp address-family ipv6-unicast enable [options]

### Description

  Turn the feature 'on' or 'off'.  The default is 'off'.

### Identifiers

  <vrf-id>    VRF## nv unset vrf <vrf-id> router bgp path-selection
### Usage

  nv unset vrf <vrf-id> router bgp path-selection [options] [<attribute> ...]

### Description

  BGP path-selection configuration.

### Identifiers

  <vrf-id>          VRF

### Atrributes

  aspath            BGP aspath path-selection config, applicable to this BGP
                    instance
  med               BGP med path-selection config, applicable to this BGP
                    instance
  multipath         BGP multipath path-selection config, applicable to this
                    BGP instance
  routerid-compare  Path selection based on Router ID comparison.

## nv unset vrf <vrf-id> router bgp path-selection aspath
### Usage

  nv unset vrf <vrf-id> router bgp path-selection aspath [options] [<attribute> ...]

### Description

  BGP aspath path-selection config, applicable to this BGP instance

### Identifiers

  <vrf-id>         VRF

### Atrributes

  compare-confed   Select AS based on confederations.
  compare-lengths  Select AS based on path length.

## nv unset vrf <vrf-id> router bgp path-selection aspath compare-lengths
### Usage

  nv unset vrf <vrf-id> router bgp path-selection aspath compare-lengths [options]

### Description

  Select AS based on path length.

### Identifiers

  <vrf-id>    VRF## nv unset vrf <vrf-id> router bgp path-selection aspath compare-confed
### Usage

  nv unset vrf <vrf-id> router bgp path-selection aspath compare-confed [options]

### Description

  Select AS based on confederations.

### Identifiers

  <vrf-id>    VRF## nv unset vrf <vrf-id> router bgp path-selection med
### Usage

  nv unset vrf <vrf-id> router bgp path-selection med [options] [<attribute> ...]

### Description

  BGP med path-selection config, applicable to this BGP instance

### Identifiers

  <vrf-id>              VRF

### Atrributes

  compare-always        Always compare the MED on routes, even when they were
                        received from different neighbouring ASes.
  compare-confed        MED configuration for route-selection based on
                        confederations.
  compare-deterministic
                        Carry out route-selection in a way that produces
                        deterministic answers locally.
  missing-as-max        missing-as-max

## nv unset vrf <vrf-id> router bgp path-selection med compare-always
### Usage

  nv unset vrf <vrf-id> router bgp path-selection med compare-always [options]

### Description

  Always compare the MED on routes, even when they were received from different neighbouring ASes.

### Identifiers

  <vrf-id>    VRF## nv unset vrf <vrf-id> router bgp path-selection med compare-deterministic
### Usage

  nv unset vrf <vrf-id> router bgp path-selection med compare-deterministic [options]

### Description

  Carry out route-selection in a way that produces deterministic answers locally.

### Identifiers

  <vrf-id>    VRF## nv unset vrf <vrf-id> router bgp path-selection med compare-confed
### Usage

  nv unset vrf <vrf-id> router bgp path-selection med compare-confed [options]

### Description

  MED configuration for route-selection based on confederations.

### Identifiers

  <vrf-id>    VRF## nv unset vrf <vrf-id> router bgp path-selection med missing-as-max
### Usage

  nv unset vrf <vrf-id> router bgp path-selection med missing-as-max [options]

### Description

  missing-as-max

### Identifiers

  <vrf-id>    VRF## nv unset vrf <vrf-id> router bgp path-selection multipath
### Usage

  nv unset vrf <vrf-id> router bgp path-selection multipath [options] [<attribute> ...]

### Description

  BGP multipath path-selection config, applicable to this BGP instance

### Identifiers

  <vrf-id>        VRF

### Atrributes

  aspath-ignore   Ignore AS path when determining multipath routing.
  bandwidth       Perform multipath route selection based on bandwidth.
  generate-asset  Requires aspath-ignore to be on

## nv unset vrf <vrf-id> router bgp path-selection multipath aspath-ignore
### Usage

  nv unset vrf <vrf-id> router bgp path-selection multipath aspath-ignore [options]

### Description

  Ignore AS path when determining multipath routing.

### Identifiers

  <vrf-id>    VRF## nv unset vrf <vrf-id> router bgp path-selection multipath generate-asset
### Usage

  nv unset vrf <vrf-id> router bgp path-selection multipath generate-asset [options]

### Description

  Requires aspath-ignore to be on

### Identifiers

  <vrf-id>    VRF## nv unset vrf <vrf-id> router bgp path-selection multipath bandwidth
### Usage

  nv unset vrf <vrf-id> router bgp path-selection multipath bandwidth [options]

### Description

  Perform multipath route selection based on bandwidth.

### Identifiers

  <vrf-id>    VRF## nv unset vrf <vrf-id> router bgp path-selection routerid-compare
### Usage

  nv unset vrf <vrf-id> router bgp path-selection routerid-compare [options]

### Description

  Path selection based on Router ID comparison.

### Identifiers

  <vrf-id>    VRF## nv unset vrf <vrf-id> router bgp route-reflection
### Usage

  nv unset vrf <vrf-id> router bgp route-reflection [options] [<attribute> ...]

### Description

  BGP route-reflection configuration.

### Identifiers

  <vrf-id>              VRF

### Atrributes

  enable                Turn the feature 'on' or 'off'. The default is 'off'.
  cluster-id            Cluster ID used during route reflection. Required when
                        route-reflection is enabled.
  outbound-policy       Allows outbound peer policy to modify the attributes
                        for reflected routes. Normally, reflected routes have
                        to retain their original attributes.
  reflect-between-clients
                        Allows routes to be reflected between clients.
                        Normally, routes are reflected only between clients
                        and non-clients, with the clients of a route reflector
                        expected to be fully meshed.

## nv unset vrf <vrf-id> router bgp route-reflection enable
### Usage

  nv unset vrf <vrf-id> router bgp route-reflection enable [options]

### Description

  Turn the feature 'on' or 'off'.  The default is 'off'.

### Identifiers

  <vrf-id>    VRF## nv unset vrf <vrf-id> router bgp route-reflection cluster-id
### Usage

  nv unset vrf <vrf-id> router bgp route-reflection cluster-id [options]

### Description

  Cluster ID used during route reflection. Required when route-reflection is enabled.

### Identifiers

  <vrf-id>    VRF## nv unset vrf <vrf-id> router bgp route-reflection reflect-between-clients
### Usage

  nv unset vrf <vrf-id> router bgp route-reflection reflect-between-clients [options]

### Description

  Allows routes to be reflected between clients. Normally, routes are reflected only between clients and non-clients, with the clients of a route reflector expected to be fully meshed.

### Identifiers

  <vrf-id>    VRF## nv unset vrf <vrf-id> router bgp route-reflection outbound-policy
### Usage

  nv unset vrf <vrf-id> router bgp route-reflection outbound-policy [options]

### Description

  Allows outbound peer policy to modify the attributes for reflected routes. Normally, reflected routes have to retain their original attributes.

### Identifiers

  <vrf-id>    VRF## nv unset vrf <vrf-id> router bgp peer-group <peer-group-id>
### Usage

  nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> [options] [<attribute> ...]

### Description

  BGP global configuration.

### Identifiers

  <vrf-id>              VRF
  <peer-group-id>       Domain

### Atrributes

  bfd                   Specifies whether to track BGP peering sessions using
                        this configuration via BFD.
  ttl-security          RFC 5082
  capabilities          Capabilities
  graceful-restart      Graceful restart
  local-as              Local AS feature
  timers                Peer peer-timerss
  address-family        Address family specific configuration
  description           neighbor description
  enforce-first-as      If on, when BGP updates are received from EBGP peers
                        with this config, check that first AS matches peer's
                        AS
  multihop-ttl          Maximum hops allowed. When 'auto', the type of peer
                        will determine the appropriate value (255 for iBGP and
                        1 for eBGP). This is the default.
  nexthop-connected-check
                        If 'on', it disables the check that a non-multihop
                        EBGP peer should be directly connected and only
                        announce connected next hops
  passive-mode          If enabled, do not initiate the BGP connection but
                        wait for incoming connection
  password              Password
  remote-as             ASN for the BGP neighbor(s) using this configuration.
                        If specified as 'external', it means an EBGP
                        configuration but the actual ASN is immaterial. If
                        specified as 'internal', it means an IBGP
                        configuration.

## nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> bfd
### Usage

  nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> bfd [options] [<attribute> ...]

### Description

  Specifies whether to track BGP peering sessions using this configuration via BFD.

### Identifiers

  <vrf-id>           VRF
  <peer-group-id>    Domain

### Atrributes

  enable             Turn the feature 'on' or 'off'. The default is 'off'.
  detect-multiplier  Detect multiplier
  min-rx-interval    Minimum receive interval
  min-tx-interval    Minimum transmit interval. The actual value used is the
                     smaller of this or what the peer expects.

## nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> bfd enable
### Usage

  nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> bfd enable [options]

### Description

  Turn the feature 'on' or 'off'.  The default is 'off'.

### Identifiers

  <vrf-id>         VRF
  <peer-group-id>  Domain

## nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> bfd detect-multiplier
### Usage

  nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> bfd detect-multiplier [options]

### Description

  Detect multiplier

### Identifiers

  <vrf-id>         VRF
  <peer-group-id>  Domain

## nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> bfd min-rx-interval
### Usage

  nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> bfd min-rx-interval [options]

### Description

  Minimum receive interval

### Identifiers

  <vrf-id>         VRF
  <peer-group-id>  Domain

## nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> bfd min-tx-interval
### Usage

  nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> bfd min-tx-interval [options]

### Description

  Minimum transmit interval.  The actual value used is the smaller of this or what the peer expects.

### Identifiers

  <vrf-id>         VRF
  <peer-group-id>  Domain

## nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> ttl-security
### Usage

  nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> ttl-security [options] [<attribute> ...]

### Description

  RFC 5082

### Identifiers

  <vrf-id>         VRF
  <peer-group-id>  Domain

### Atrributes

  enable           Turn the feature 'on' or 'off'. The default is 'off'.
  hops             Number of hops

## nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> ttl-security enable
### Usage

  nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> ttl-security enable [options]

### Description

  Turn the feature 'on' or 'off'.  The default is 'off'.

### Identifiers

  <vrf-id>         VRF
  <peer-group-id>  Domain

## nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> ttl-security hops
### Usage

  nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> ttl-security hops [options]

### Description

  Number of hops

### Identifiers

  <vrf-id>         VRF
  <peer-group-id>  Domain

## nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> capabilities
### Usage

  nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> capabilities [options] [<attribute> ...]

### Description

  Capabilities

### Identifiers

  <vrf-id>          VRF
  <peer-group-id>   Domain

### Atrributes

  extended-nexthop  If 'on', the extended-nexthop capability defined in RFC
                    5549 is advertised to peer(s) with this config. If 'auto',
                    it will be 'on' for unnumbered peers and 'off' otherwise.
                    This is the default.
  source-address    source IP address of the TCP connection, which is often
                    used as the BGP next hop for Updates

## nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> capabilities extended-nexthop
### Usage

  nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> capabilities extended-nexthop [options]

### Description

  If 'on', the extended-nexthop capability defined in RFC 5549 is advertised to peer(s) with this config.  If 'auto', it will be 'on' for unnumbered peers and 'off' otherwise.  This is the default.

### Identifiers

  <vrf-id>         VRF
  <peer-group-id>  Domain

## nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> capabilities source-address
### Usage

  nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> capabilities source-address [options]

### Description

  source IP address of the TCP connection, which is often used as the BGP next hop for Updates

### Identifiers

  <vrf-id>         VRF
  <peer-group-id>  Domain

## nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> graceful-restart
### Usage

  nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> graceful-restart [options] [<attribute> ...]

### Description

  BGP Graceful restart per neighbor configuration

### Identifiers

  <vrf-id>         VRF
  <peer-group-id>  Domain

### Atrributes

  mode             If 'auto', inherit from global. This is the default. If set
                   to 'off', GR capability is not negotiated with this peer.
                   If set to 'helper-only', only the Helper role is supported
                   for this peer. This means that the GR capability will be
                   negotiated without any address-families with this peer. If
                   set to 'full', both the Helper role and the Restarter role
                   are supported with this peer; the GR capability will be
                   negotiated with the enabled address-families for which GR
                   is also supported.

## nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> graceful-restart mode
### Usage

  nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> graceful-restart mode [options]

### Description

  If 'auto', inherit from global.  This is the default.  If set to 'off', GR capability is not negotiated with this peer.  If set to 'helper-only', only the Helper role is supported for this peer. This means that the GR capability will be negotiated without any address-families with this peer.  If set to 'full', both the Helper role and the Restarter role are supported with this peer; the GR capability will be negotiated with the enabled address-families for which GR is also supported.

### Identifiers

  <vrf-id>         VRF
  <peer-group-id>  Domain

## nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> local-as
### Usage

  nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> local-as [options] [<attribute> ...]

### Description

  Local AS feature

### Identifiers

  <vrf-id>         VRF
  <peer-group-id>  Domain

### Atrributes

  enable           Turn the feature 'on' or 'off'. The default is 'off'.
  asn              ASN to use to establish the peering if different from the
                   ASN of the BGP instance. This configuration finds use
                   during AS renumbering. The local-as configured is also
                   attached to incoming and outgoing updates.
  prepend          When set to 'off', do not prepend the configured local-as
                   to received updates; otherwise, prepend it.
  replace          When set to 'on', attach only the configured local-as to
                   generated updates, effectively "replacing" the AS number
                   configured for the BGP instance with the local-as
                   applicable for the peering; otherwise, attach the AS number
                   of the BGP instance and then prepend it with the configured
                   local-as.

## nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> local-as enable
### Usage

  nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> local-as enable [options]

### Description

  Turn the feature 'on' or 'off'.  The default is 'off'.

### Identifiers

  <vrf-id>         VRF
  <peer-group-id>  Domain

## nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> local-as asn
### Usage

  nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> local-as asn [options]

### Description

  ASN to use to establish the peering if different from the ASN of the BGP instance.  This configuration finds use during AS renumbering.  The local-as configured is also attached to incoming and outgoing updates.

### Identifiers

  <vrf-id>         VRF
  <peer-group-id>  Domain

## nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> local-as prepend
### Usage

  nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> local-as prepend [options]

### Description

  When set to 'off', do not prepend the configured local-as to received updates; otherwise, prepend it.

### Identifiers

  <vrf-id>         VRF
  <peer-group-id>  Domain

## nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> local-as replace
### Usage

  nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> local-as replace [options]

### Description

  When set to 'on', attach only the configured local-as to generated updates, effectively "replacing" the AS number configured for the BGP instance with the local-as applicable for the peering; otherwise, attach the AS number of the BGP instance and then prepend it with the configured local-as.

### Identifiers

  <vrf-id>         VRF
  <peer-group-id>  Domain

## nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> timers
### Usage

  nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> timers [options] [<attribute> ...]

### Description

  Peer peer-timerss

### Identifiers

  <vrf-id>             VRF
  <peer-group-id>      Domain

### Atrributes

  connection-retry     Time interval at which connection attempts are retried
                       upon a failure. If `auto`, the global value is used.
                       This is the default.
  hold                 Hold timer. If `none`, keepalives from the peer are not
                       tracked and the peering session will not experience a
                       hold timeout. If `auto`, the global value is used. This
                       is the default.
  keepalive            Keepalive timer. If `none`, keepalives are not sent. If
                       `auto`, the global value is used. This is the default.
  route-advertisement  Time between route advertisements (BGP Updates). A non-
                       zero value allows route advertisements to be delayed
                       and batched. If `auto`, the global value is used. This
                       is the default.

## nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> timers keepalive
### Usage

  nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> timers keepalive [options]

### Description

  Keepalive timer.  If `none`, keepalives are not sent.  If `auto`, the global value is used.  This is the default.

### Identifiers

  <vrf-id>         VRF
  <peer-group-id>  Domain

## nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> timers hold
### Usage

  nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> timers hold [options]

### Description

  Hold timer.  If `none`, keepalives from the peer are not tracked and the peering session will not experience a hold timeout.  If `auto`, the global value is used.  This is the default.

### Identifiers

  <vrf-id>         VRF
  <peer-group-id>  Domain

## nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> timers connection-retry
### Usage

  nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> timers connection-retry [options]

### Description

  Time interval at which connection attempts are retried upon a failure.  If `auto`, the global value is used.  This is the default.

### Identifiers

  <vrf-id>         VRF
  <peer-group-id>  Domain

## nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> timers route-advertisement
### Usage

  nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> timers route-advertisement [options]

### Description

  Time between route advertisements (BGP Updates).  A non-zero value allows route advertisements to be delayed and batched.  If `auto`, the global value is used.  This is the default.

### Identifiers

  <vrf-id>         VRF
  <peer-group-id>  Domain

## nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family
### Usage

  nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family [options] [<attribute> ...]

### Description

  Address family specific configuration

### Identifiers

  <vrf-id>         VRF
  <peer-group-id>  Domain

### Atrributes

  ipv4-unicast     Peer IPv4 unicast address family. Always on, unless
                   disabled globaly.
  ipv6-unicast     Peer IPv6 unicast address family.
  l2vpn-evpn       Peer l2vpn EVPN address family.

## nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast
### Usage

  nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast [options] [<attribute> ...]

### Description

  Peer IPv4 unicast address family.  Always on, unless disabled globaly.

### Identifiers

  <vrf-id>              VRF
  <peer-group-id>       Domain

### Atrributes

  community-advertise   Community advertise for address family.
  attribute-mod         Attribute mod for address family.
  aspath                Options for handling AS_PATH for prefixes from/to peer
                        for the specified address family
  prefix-limits         Limits on prefix from the peer for this address-family
  default-route-origination
                        Default route origination
  policy                Policies for ipv4 unicast
  conditional-advertise
                        Conditional advertise for address family.
  enable                Turn the feature 'on' or 'off'. The default is 'on'.
  add-path-tx           Used to enable transmission of additional paths; by
                        default, only the best path is announced to peers
  nexthop-setting       Control nexthop value of advertised routes. "auto"
                        follows regular BGP next-hop determination rules. This
                        is the default. "self" sets the next hop to ourselves
                        for route advertisement, except for reflected routes.
                        "force" sets the next hop to ourselves for route
                        advertisement including for reflected routes.
  route-reflector-client
                        Specifies if this peer is a client and we are its
                        route reflector
  route-server-client   Specifies if this peer is a client and we are its
                        route server
  soft-reconfiguration  If 'on', it means that received routes from this peer
                        that are rejected by inbound policy are still stored.
                        This allows policy changes to take effect without any
                        exchange of BGP Updates.
  weight                Weight applied to routes received from peer; this is
                        used in the BGP route selection algorithm

## nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast community-advertise
### Usage

  nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast community-advertise [options] [<attribute> ...]

### Description

  Community advertise for address family.

### Identifiers

  <vrf-id>         VRF
  <peer-group-id>  Domain

### Atrributes

  extended         If 'on', it means we can announce the EXT_COMMUNITIES
                   attribute to this peer, otherwise we cannot.
  large            If 'on', it means we can announce the LARGE_COMMUNITIES
                   attribute to this peer, otherwise we cannot.
  regular          If 'on', it means we can announce the COMMUNITIES attribute
                   to this peer, otherwise we cannot.

## nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast community-advertise regular
### Usage

  nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast community-advertise regular [options]

### Description

  If 'on', it means we can announce the COMMUNITIES attribute to this peer, otherwise we cannot.

### Identifiers

  <vrf-id>         VRF
  <peer-group-id>  Domain

## nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast community-advertise extended
### Usage

  nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast community-advertise extended [options]

### Description

  If 'on', it means we can announce the EXT_COMMUNITIES attribute to this peer, otherwise we cannot.

### Identifiers

  <vrf-id>         VRF
  <peer-group-id>  Domain

## nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast community-advertise large
### Usage

  nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast community-advertise large [options]

### Description

  If 'on', it means we can announce the LARGE_COMMUNITIES attribute to this peer, otherwise we cannot.

### Identifiers

  <vrf-id>         VRF
  <peer-group-id>  Domain

## nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast attribute-mod
### Usage

  nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast attribute-mod [options] [<attribute> ...]

### Description

  Attribute mod for address family.

### Identifiers

  <vrf-id>         VRF
  <peer-group-id>  Domain

### Atrributes

  aspath           If 'on', it means follow normal BGP procedures in the
                   generation of AS_PATH attribute for this peer; if 'off' it
                   means do not change the AS_PATH when sending an Update to
                   this peer.
  med              If 'on', it means follow normal BGP procedures in the
                   generation of MED attribute for this peer; if 'off' it
                   means do not change the MED when sending an Update to this
                   peer.
  nexthop          If 'on', it means follow normal BGP procedures in the
                   generation of NEXT_HOP attribute for this peer; if 'off' it
                   means do not change the NEXT_HOP when sending an Update to
                   this peer.

## nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast attribute-mod aspath
### Usage

  nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast attribute-mod aspath [options]

### Description

  If 'on', it means follow normal BGP procedures in the generation of AS_PATH attribute for this peer; if 'off' it means do not change the AS_PATH when sending an Update to this peer.

### Identifiers

  <vrf-id>         VRF
  <peer-group-id>  Domain

## nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast attribute-mod med
### Usage

  nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast attribute-mod med [options]

### Description

  If 'on', it means follow normal BGP procedures in the generation of MED attribute for this peer; if 'off' it means do not change the MED when sending an Update to this peer.

### Identifiers

  <vrf-id>         VRF
  <peer-group-id>  Domain

## nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast attribute-mod nexthop
### Usage

  nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast attribute-mod nexthop [options]

### Description

  If 'on', it means follow normal BGP procedures in the generation of NEXT_HOP attribute for this peer; if 'off' it means do not change the NEXT_HOP when sending an Update to this peer.

### Identifiers

  <vrf-id>         VRF
  <peer-group-id>  Domain

## nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast aspath
### Usage

  nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast aspath [options] [<attribute> ...]

### Description

  Options for handling AS_PATH for prefixes from/to peer for the specified address family

### Identifiers

  <vrf-id>         VRF
  <peer-group-id>  Domain

### Atrributes

  allow-my-asn     If enabled, it is acceptable for a received AS_PATH to
                   contain the ASN of the local system
  private-as       If 'none', no specific action is taken. This is the
                   default. If set to 'remove', any private ASNs in the Update
                   to the peer are removed. If set to 'replace' any private
                   ASNs in the Update to the peer are replaced with the ASN of
                   the local system.
  replace-peer-as  If on, if the AS_PATH in an outgoing Update contains the
                   peer's ASN, it is replaced with the local system's ASN


## nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast aspath allow-my-asn
### Usage

  nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast aspath allow-my-asn [options] [<attribute> ...]

### Description

  If enabled, it is acceptable for a received AS_PATH to contain the ASN of the local system

### Identifiers

  <vrf-id>         VRF
  <peer-group-id>  Domain

### Atrributes

  enable           Turn the feature 'on' or 'off'. The default is 'off'.
  occurrences      Indicates max number of occurrences of the local system's
                   AS number in the received AS_PATH
  origin           If on, a received AS_PATH containing the ASN of the local
                   system is allowed, but only if it is the originating AS

## nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast aspath allow-my-asn enable
### Usage

  nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast aspath allow-my-asn enable [options]

### Description

  Turn the feature 'on' or 'off'.  The default is 'off'.

### Identifiers

  <vrf-id>         VRF
  <peer-group-id>  Domain

## nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast aspath allow-my-asn origin
### Usage

  nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast aspath allow-my-asn origin [options]

### Description

  If on, a received AS_PATH containing the ASN of the local system is allowed, but only if it is the originating AS

### Identifiers

  <vrf-id>         VRF
  <peer-group-id>  Domain

## nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast aspath allow-my-asn occurrences
### Usage

  nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast aspath allow-my-asn occurrences [options]

### Description

  Indicates max number of occurrences of the local system's AS number in the received AS_PATH

### Identifiers

  <vrf-id>         VRF
  <peer-group-id>  Domain

## nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast aspath replace-peer-as
### Usage

  nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast aspath replace-peer-as [options]

### Description

  If on, if the AS_PATH in an outgoing Update contains the peer's ASN, it is replaced with the local system's ASN

### Identifiers

  <vrf-id>         VRF
  <peer-group-id>  Domain

## nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast aspath private-as
### Usage

  nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast aspath private-as [options]

### Description

  If 'none', no specific action is taken.  This is the default.  If set to 'remove', any private ASNs in the Update to the peer are removed.  If set to 'replace' any private ASNs in the Update to the peer are replaced with the ASN of the local system.

### Identifiers

  <vrf-id>         VRF
  <peer-group-id>  Domain

## nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast prefix-limits
### Usage

  nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast prefix-limits [options] [<attribute> ...]

### Description

  Limits on prefix from the peer for this address-family

### Identifiers

  <vrf-id>         VRF
  <peer-group-id>  Domain

### Atrributes

  inbound          Limits on inbound prefix from the peer for this address-
                   family

## nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast prefix-limits inbound
### Usage

  nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast prefix-limits inbound [options] [<attribute> ...]

### Description

  Limits on inbound prefix from the peer for this address-family

### Identifiers

  <vrf-id>           VRF
  <peer-group-id>    Domain

### Atrributes

  maximum            Limit on number of prefixes of specific address-family
                     that can be received from the peer. By default, there is
                     no limit
  reestablish-wait   Specifes the time in seconds to wait before establishing
                     the BGP session again with the peer. Defaults to 'auto',
                     which will use standard BGP timers and processing. This
                     would typically be 2-3 seconds.
  warning-only       If 'on', it means to only generate a warning syslog if
                     the number of received prefixes exceeds the limit, do not
                     bring down the BGP session.
  warning-threshold  Percentage of the maximum at which a warning syslog is
                     generated.

## nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast prefix-limits inbound maximum
### Usage

  nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast prefix-limits inbound maximum [options]

### Description

  Limit on number of prefixes of specific address-family that can be received from the peer.  By default, there is no limit

### Identifiers

  <vrf-id>         VRF
  <peer-group-id>  Domain

## nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast prefix-limits inbound warning-threshold
### Usage

  nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast prefix-limits inbound warning-threshold [options]

### Description

  Percentage of the maximum at which a warning syslog is generated.

### Identifiers

  <vrf-id>         VRF
  <peer-group-id>  Domain

## nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast prefix-limits inbound warning-only
### Usage

  nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast prefix-limits inbound warning-only [options]

### Description

  If 'on', it means to only generate a warning syslog if the number of received prefixes exceeds the limit, do not bring down the BGP session.

### Identifiers

  <vrf-id>         VRF
  <peer-group-id>  Domain

## nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast prefix-limits inbound reestablish-wait
### Usage

  nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast prefix-limits inbound reestablish-wait [options]

### Description

  Specifes the time in seconds to wait before establishing the BGP session again with the peer. Defaults to 'auto', which will use standard BGP timers and processing.  This would typically be 2-3 seconds.

### Identifiers

  <vrf-id>         VRF
  <peer-group-id>  Domain

## nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast default-route-origination
### Usage

  nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast default-route-origination [options] [<attribute> ...]

### Description

  Default route origination

### Identifiers

  <vrf-id>         VRF
  <peer-group-id>  Domain

### Atrributes

  enable           Turn the feature 'on' or 'off'. The default is 'off'.
  policy           Optional route-map policy to control the conditions under
                   which the default route is originated.

## nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast default-route-origination enable
### Usage

  nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast default-route-origination enable [options]

### Description

  Turn the feature 'on' or 'off'.  The default is 'off'.

### Identifiers

  <vrf-id>         VRF
  <peer-group-id>  Domain

## nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast default-route-origination policy
### Usage

  nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast default-route-origination policy [options]

### Description

  Optional route-map policy to control the conditions under which the default route is originated.

### Identifiers

  <vrf-id>         VRF
  <peer-group-id>  Domain

## nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast policy
### Usage

  nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast policy [options] [<attribute> ...]

### Description

  Policies for ipv4 unicast

### Identifiers

  <vrf-id>         VRF
  <peer-group-id>  Domain

### Atrributes

  inbound          Outbound unicast policy
  outbound         Outbound unicast policy

## nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast policy inbound
### Usage

  nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast policy inbound [options] [<attribute> ...]

### Description

  Outbound unicast policy

### Identifiers

  <vrf-id>         VRF
  <peer-group-id>  Domain

### Atrributes

  route-map        Route map to apply to Updates received from this peer
  aspath-list      AS-Path filter list to apply to Updates received from this
                   peer
  prefix-list      Prefix list to apply to Updates received from this peer

## nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast policy inbound route-map
### Usage

  nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast policy inbound route-map [options]

### Description

  Route map to apply to Updates received from this peer

### Identifiers

  <vrf-id>         VRF
  <peer-group-id>  Domain

## nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast policy inbound prefix-list
### Usage

  nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast policy inbound prefix-list [options]

### Description

  Prefix list to apply to Updates received from this peer

### Identifiers

  <vrf-id>         VRF
  <peer-group-id>  Domain

## nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast policy inbound aspath-list
### Usage

  nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast policy inbound aspath-list [options]

### Description

  AS-Path filter list to apply to Updates received from this peer

### Identifiers

  <vrf-id>         VRF
  <peer-group-id>  Domain

## nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast policy outbound
### Usage

  nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast policy outbound [options] [<attribute> ...]

### Description

  Outbound unicast policy

### Identifiers

  <vrf-id>         VRF
  <peer-group-id>  Domain

### Atrributes

  route-map        Route map to apply to Updates to be sent to this peer
  unsuppress-map   Route map used to unsuppress routes selectively when
                   advertising to this peer; these are routes that have been
                   suppressed due to aggregation configuration.
  aspath-list      AS-Path filter list to apply to Updates sent to this peer
  prefix-list      Prefix list to apply to Updates to be sent to this peer

## nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast policy outbound route-map
### Usage

  nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast policy outbound route-map [options]

### Description

  Route map to apply to Updates to be sent to this peer

### Identifiers

  <vrf-id>         VRF
  <peer-group-id>  Domain

## nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast policy outbound unsuppress-map
### Usage

  nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast policy outbound unsuppress-map [options]

### Description

  Route map used to unsuppress routes selectively when advertising to this peer; these are routes that have been suppressed due to aggregation configuration.

### Identifiers

  <vrf-id>         VRF
  <peer-group-id>  Domain

## nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast policy outbound prefix-list

### Usage

  nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast policy outbound prefix-list [options]

### Description

  Prefix list to apply to Updates to be sent to this peer

### Identifiers

  <vrf-id>         VRF
  <peer-group-id>  Domain

## nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast policy outbound aspath-list
### Usage

  nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast policy outbound aspath-list [options]

### Description

  AS-Path filter list to apply to Updates sent to this peer

### Identifiers

  <vrf-id>         VRF
  <peer-group-id>  Domain

## nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast conditional-advertise
### Usage

  nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast conditional-advertise [options] [<attribute> ...]

### Description

  Conditional advertise for address family.

### Identifiers

  <vrf-id>         VRF
  <peer-group-id>  Domain

### Atrributes

  enable           Turn the feature 'on' or 'off'. The default is 'off'.
  advertise-map    route-map contains prefix-list which has list of
                   routes/prefixes to operate on.
  exist-map        route-map contains the conditional routes/prefixes in
                   prefix-list.
  non-exist-map    route-map contains the negative conditional routes/prefixes
                   in prefix-list.

## nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast conditional-advertise enable
### Usage

  nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast conditional-advertise enable [options]

### Description

  Turn the feature 'on' or 'off'.  The default is 'off'.

### Identifiers

  <vrf-id>         VRF
  <peer-group-id>  Domain

## nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast conditional-advertise advertise-map
### Usage

  nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast conditional-advertise advertise-map [options]

### Description

  route-map contains prefix-list which has list of routes/prefixes to operate on.

### Identifiers

  <vrf-id>         VRF
  <peer-group-id>  Domain

## nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast conditional-advertise exist-map
### Usage

  nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast conditional-advertise exist-map [options]

### Description

  route-map contains the conditional routes/prefixes in prefix-list.

### Identifiers

  <vrf-id>         VRF
  <peer-group-id>  Domain

## nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast conditional-advertise non-exist-map
### Usage

  nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast conditional-advertise non-exist-map [options]

### Description

  route-map contains the negative conditional routes/prefixes in prefix-list.

### Identifiers

  <vrf-id>         VRF
  <peer-group-id>  Domain

## nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast enable
### Usage

  nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast enable [options]

### Description

  Turn the feature 'on' or 'off'.  The default is 'on'.

### Identifiers

  <vrf-id>         VRF
  <peer-group-id>  Domain

## nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast route-reflector-client
### Usage

  nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast route-reflector-client [options]

### Description

  Specifies if this peer is a client and we are its route reflector

### Identifiers

  <vrf-id>         VRF
  <peer-group-id>  Domain

## nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast route-server-client

### Usage

  nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast route-server-client [options]

### Description

  Specifies if this peer is a client and we are its route server

### Identifiers

  <vrf-id>         VRF
  <peer-group-id>  Domain

## nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast soft-reconfiguration
### Usage

  nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast soft-reconfiguration [options]

### Description

  If 'on', it means that received routes from this peer that are rejected by inbound policy are still stored. This allows policy changes to take effect without any exchange of BGP Updates.

### Identifiers

  <vrf-id>         VRF
  <peer-group-id>  Domain

## nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast nexthop-setting
### Usage

  nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast nexthop-setting [options]

### Description

  Control nexthop value of advertised routes.  "auto" follows regular BGP next-hop determination rules.  This is the default.  "self" sets the next hop to ourselves for route advertisement, except for reflected routes.  "force" sets the next hop to ourselves for route advertisement including for reflected routes.

### Identifiers

  <vrf-id>         VRF
  <peer-group-id>  Domain

## nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast add-path-tx
### Usage

  nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast add-path-tx [options]

### Description

  Used to enable transmission of additional paths; by default, only the best path is announced to peers

### Identifiers

  <vrf-id>         VRF
  <peer-group-id>  Domain

## nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast weight
### Usage

  nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast weight [options]

### Description

  Weight applied to routes received from peer; this is used in the BGP route selection algorithm

### Identifiers

  <vrf-id>         VRF
  <peer-group-id>  Domain

## nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast

### Usage

  nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast [options] [<attribute> ...]

### Description

  Peer IPv6 unicast address family.

### Identifiers

  <vrf-id>              VRF
  <peer-group-id>       Domain

### Atrributes

  policy                Policies for ipv4 unicast
  aspath                Options for handling AS_PATH for prefixes from/to peer
                        for the specified address family
  prefix-limits         Limits on prefix from the peer for this address-family
  default-route-origination
                        Default route origination
  community-advertise   Community advertise for address family.
  attribute-mod         Attribute mod for address family.
  conditional-advertise
                        Conditional advertise for address family.
  enable                Turn the feature 'on' or 'off'. The default is 'off'.
  add-path-tx           Used to enable transmission of additional paths; by
                        default, only the best path is announced to peers
  nexthop-setting       Control nexthop value of advertised routes. "auto"
                        follows regular BGP next-hop determination rules. This
                        is the default. "self" sets the next hop to ourselves
                        for route advertisement, except for reflected routes.
                        "force" sets the next hop to ourselves for route
                        advertisement including for reflected routes.
  route-reflector-client
                        Specifies if this peer is a client and we are its
                        route reflector
  route-server-client   Specifies if this peer is a client and we are its
                        route server
  soft-reconfiguration  If 'on', it means that received routes from this peer
                        that are rejected by inbound policy are still stored.
                        This allows policy changes to take effect without any
                        exchange of BGP Updates.
  weight                Weight applied to routes received from peer; this is
                        used in the BGP route selection algorithm

## nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast policy
### Usage

  nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast policy [options] [<attribute> ...]

### Description

  Policies for ipv6 unicast

### Identifiers

  <vrf-id>         VRF
  <peer-group-id>  Domain

### Atrributes

  inbound          Outbound unicast policy
  outbound         Outbound unicast policy

## nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast policy inbound
### Usage

  nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast policy inbound [options] [<attribute> ...]

### Description

  Outbound unicast policy

### Identifiers

  <vrf-id>         VRF
  <peer-group-id>  Domain

### Atrributes

  route-map        Route map to apply to Updates received from this peer
  aspath-list      AS-Path filter list to apply to Updates received from this
                   peer
  prefix-list      Prefix list to apply to Updates received from this peer

## nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast policy inbound route-map
### Usage

  nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast policy inbound route-map [options]

### Description

  Route map to apply to Updates received from this peer

### Identifiers

  <vrf-id>         VRF
  <peer-group-id>  Domain

## nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast policy inbound prefix-list
### Usage

  nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast policy inbound prefix-list [options]

### Description

  Prefix list to apply to Updates received from this peer

### Identifiers

  <vrf-id>         VRF
  <peer-group-id>  Domain

## nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast policy inbound aspath-list
### Usage

  nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast policy inbound aspath-list [options]

### Description

  AS-Path filter list to apply to Updates received from this peer

### Identifiers

  <vrf-id>         VRF
  <peer-group-id>  Domain

## nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast policy outbound
### Usage

  nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast policy outbound [options] [<attribute> ...]

### Description

  Outbound unicast policy

### Identifiers

  <vrf-id>         VRF
  <peer-group-id>  Domain

### Atrributes

  route-map        Route map to apply to Updates to be sent to this peer
  unsuppress-map   Route map used to unsuppress routes selectively when
                   advertising to this peer; these are routes that have been
                   suppressed due to aggregation configuration.
  aspath-list      AS-Path filter list to apply to Updates sent to this peer
  prefix-list      Prefix list to apply to Updates to be sent to this peer

## nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast policy outbound route-map
### Usage

  nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast policy outbound route-map [options]

### Description

  Route map to apply to Updates to be sent to this peer

### Identifiers

  <vrf-id>         VRF
  <peer-group-id>  Domain

## nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast policy outbound unsuppress-map

### Usage

  nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast policy outbound unsuppress-map [options]

### Description

  Route map used to unsuppress routes selectively when advertising to this peer; these are routes that have been suppressed due to aggregation configuration.

### Identifiers

  <vrf-id>         VRF
  <peer-group-id>  Domain

## nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast policy outbound prefix-list
### Usage

  nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast policy outbound prefix-list [options]

### Description

  Prefix list to apply to Updates to be sent to this peer

### Identifiers

  <vrf-id>         VRF
  <peer-group-id>  Domain

## nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast policy outbound aspath-list
### Usage

  nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast policy outbound aspath-list [options]

### Description

  AS-Path filter list to apply to Updates sent to this peer

### Identifiers

  <vrf-id>         VRF
  <peer-group-id>  Domain

## nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast aspath

### Usage

  nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast aspath [options] [<attribute> ...]

### Description

  Options for handling AS_PATH for prefixes from/to peer for the specified address family

### Identifiers

  <vrf-id>         VRF
  <peer-group-id>  Domain

### Atrributes

  allow-my-asn     If enabled, it is acceptable for a received AS_PATH to
                   contain the ASN of the local system
  private-as       If 'none', no specific action is taken. This is the
                   default. If set to 'remove', any private ASNs in the Update
                   to the peer are removed. If set to 'replace' any private
                   ASNs in the Update to the peer are replaced with the ASN of
                   the local system.
  replace-peer-as  If on, if the AS_PATH in an outgoing Update contains the
                   peer's ASN, it is replaced with the local system's ASN

## nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast aspath allow-my-asn

### Usage

  nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast aspath allow-my-asn [options] [<attribute> ...]

### Description

  If enabled, it is acceptable for a received AS_PATH to contain the ASN of the local system

### Identifiers

  <vrf-id>         VRF
  <peer-group-id>  Domain

### Atrributes

  enable           Turn the feature 'on' or 'off'. The default is 'off'.
  occurrences      Indicates max number of occurrences of the local system's
                   AS number in the received AS_PATH
  origin           If on, a received AS_PATH containing the ASN of the local
                   system is allowed, but only if it is the originating AS

## nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast aspath allow-my-asn enable

### Usage

  nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast aspath allow-my-asn enable [options]

### Description

  Turn the feature 'on' or 'off'.  The default is 'off'.

### Identifiers

  <vrf-id>         VRF
  <peer-group-id>  Domain

## nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast aspath allow-my-asn origin

### Usage

  nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast aspath allow-my-asn origin [options]

### Description

  If on, a received AS_PATH containing the ASN of the local system is allowed, but only if it is the originating AS

### Identifiers

  <vrf-id>         VRF
  <peer-group-id>  Domain

## nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast aspath allow-my-asn occurrences

### Usage

  nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast aspath allow-my-asn occurrences [options]

### Description

  Indicates max number of occurrences of the local system's AS number in the received AS_PATH

### Identifiers

  <vrf-id>         VRF
  <peer-group-id>  Domain

## nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast aspath replace-peer-as

### Usage

  nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast aspath replace-peer-as [options]

### Description

  If on, if the AS_PATH in an outgoing Update contains the peer's ASN, it is replaced with the local system's ASN

### Identifiers

  <vrf-id>         VRF
  <peer-group-id>  Domain

## nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast aspath private-as

### Usage

  nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast aspath private-as [options]

### Description

  If 'none', no specific action is taken.  This is the default.  If set to 'remove', any private ASNs in the Update to the peer are removed.  If set to 'replace' any private ASNs in the Update to the peer are replaced with the ASN of the local system.

### Identifiers

  <vrf-id>         VRF
  <peer-group-id>  Domain

## nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast prefix-limits

### Usage

  nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast prefix-limits [options] [<attribute> ...]

### Description

  Limits on prefix from the peer for this address-family

### Identifiers

  <vrf-id>         VRF
  <peer-group-id>  Domain

### Atrributes

  inbound          Limits on inbound prefix from the peer for this address-
                   family

## nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast prefix-limits inbound

### Usage

  nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast prefix-limits inbound [options] [<attribute> ...]

### Description

  Limits on inbound prefix from the peer for this address-family

### Identifiers

  <vrf-id>           VRF
  <peer-group-id>    Domain

### Atrributes

  maximum            Limit on number of prefixes of specific address-family
                     that can be received from the peer. By default, there is
                     no limit
  reestablish-wait   Specifes the time in seconds to wait before establishing
                     the BGP session again with the peer. Defaults to 'auto',
                     which will use standard BGP timers and processing. This
                     would typically be 2-3 seconds.
  warning-only       If 'on', it means to only generate a warning syslog if
                     the number of received prefixes exceeds the limit, do not
                     bring down the BGP session.
  warning-threshold  Percentage of the maximum at which a warning syslog is
                     generated.

## nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast prefix-limits inbound maximum

### Usage

  nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast prefix-limits inbound maximum [options]

### Description

  Limit on number of prefixes of specific address-family that can be received from the peer.  By default, there is no limit

### Identifiers

  <vrf-id>         VRF
  <peer-group-id>  Domain

## nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast prefix-limits inbound warning-threshold

### Usage

  nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast prefix-limits inbound warning-threshold [options]

### Description

  Percentage of the maximum at which a warning syslog is generated.

### Identifiers

  <vrf-id>         VRF
  <peer-group-id>  Domain

## nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast prefix-limits inbound warning-only

### Usage

  nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast prefix-limits inbound warning-only [options]

### Description

  If 'on', it means to only generate a warning syslog if the number of received prefixes exceeds the limit, do not bring down the BGP session.

### Identifiers

  <vrf-id>         VRF
  <peer-group-id>  Domain

## nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast prefix-limits inbound reestablish-wait

### Usage

  nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast prefix-limits inbound reestablish-wait [options]

### Description

  Specifes the time in seconds to wait before establishing the BGP session again with the peer. Defaults to 'auto', which will use standard BGP timers and processing.  This would typically be 2-3 seconds.

### Identifiers

  <vrf-id>         VRF
  <peer-group-id>  Domain

## nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast default-route-origination

### Usage

  nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast default-route-origination [options] [<attribute> ...]

### Description

  Default route origination

### Identifiers

  <vrf-id>         VRF
  <peer-group-id>  Domain

### Atrributes

  enable           Turn the feature 'on' or 'off'. The default is 'off'.
  policy           Optional route-map policy to control the conditions under
                   which the default route is originated.

## nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast default-route-origination enable

### Usage

  nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast default-route-origination enable [options]

### Description

  Turn the feature 'on' or 'off'.  The default is 'off'.

### Identifiers

  <vrf-id>         VRF
  <peer-group-id>  Domain

## nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast default-route-origination policy

### Usage

  nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast default-route-origination policy [options]

### Description

  Optional route-map policy to control the conditions under which the default route is originated.

### Identifiers

  <vrf-id>         VRF
  <peer-group-id>  Domain

## nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast community-advertise

### Usage

  nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast community-advertise [options] [<attribute> ...]

### Description

  Community advertise for address family.

### Identifiers

  <vrf-id>         VRF
  <peer-group-id>  Domain

### Atrributes

  extended         If 'on', it means we can announce the EXT_COMMUNITIES
                   attribute to this peer, otherwise we cannot.
  large            If 'on', it means we can announce the LARGE_COMMUNITIES
                   attribute to this peer, otherwise we cannot.
  regular          If 'on', it means we can announce the COMMUNITIES attribute
                   to this peer, otherwise we cannot.

## nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast community-advertise regular

### Usage

  nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast community-advertise regular [options]

### Description

  If 'on', it means we can announce the COMMUNITIES attribute to this peer, otherwise we cannot.

### Identifiers

  <vrf-id>         VRF
  <peer-group-id>  Domain

## nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast community-advertise extended

### Usage

  nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast community-advertise extended [options]

### Description

  If 'on', it means we can announce the EXT_COMMUNITIES attribute to this peer, otherwise we cannot.

### Identifiers

  <vrf-id>         VRF
  <peer-group-id>  Domain

## nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast community-advertise large

### Usage

  nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast community-advertise large [options]

### Description

  If 'on', it means we can announce the LARGE_COMMUNITIES attribute to this peer, otherwise we cannot.

### Identifiers

  <vrf-id>         VRF
  <peer-group-id>  Domain

## nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast attribute-mod

### Usage

  nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast attribute-mod [options] [<attribute> ...]

### Description

  Attribute mod for address family.

### Identifiers

  <vrf-id>         VRF
  <peer-group-id>  Domain

### Atrributes

  aspath           If 'on', it means follow normal BGP procedures in the
                   generation of AS_PATH attribute for this peer; if 'off' it
                   means do not change the AS_PATH when sending an Update to
                   this peer.
  med              If 'on', it means follow normal BGP procedures in the
                   generation of MED attribute for this peer; if 'off' it
                   means do not change the MED when sending an Update to this
                   peer.
  nexthop          If 'on', it means follow normal BGP procedures in the
                   generation of NEXT_HOP attribute for this peer; if 'off' it
                   means do not change the NEXT_HOP when sending an Update to
                   this peer.

## nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast attribute-mod aspath

### Usage

  nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast attribute-mod aspath [options]

### Description

  If 'on', it means follow normal BGP procedures in the generation of AS_PATH attribute for this peer; if 'off' it means do not change the AS_PATH when sending an Update to this peer.

### Identifiers

  <vrf-id>         VRF
  <peer-group-id>  Domain

## nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast attribute-mod med

### Usage

  nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast attribute-mod med [options]

### Description

  If 'on', it means follow normal BGP procedures in the generation of MED attribute for this peer; if 'off' it means do not change the MED when sending an Update to this peer.

### Identifiers

  <vrf-id>         VRF
  <peer-group-id>  Domain

## nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast attribute-mod nexthop

### Usage

  nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast attribute-mod nexthop [options]

### Description

  If 'on', it means follow normal BGP procedures in the generation of NEXT_HOP attribute for this peer; if 'off' it means do not change the NEXT_HOP when sending an Update to this peer.

### Identifiers

  <vrf-id>         VRF
  <peer-group-id>  Domain

## nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast conditional-advertise

### Usage

  nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast conditional-advertise [options] [<attribute> ...]

### Description

  Conditional advertise for address family.

### Identifiers

  <vrf-id>         VRF
  <peer-group-id>  Domain

### Atrributes

  enable           Turn the feature 'on' or 'off'. The default is 'off'.
  advertise-map    route-map contains prefix-list which has list of
                   routes/prefixes to operate on.
  exist-map        route-map contains the conditional routes/prefixes in
                   prefix-list.
  non-exist-map    route-map contains the negative conditional routes/prefixes
                   in prefix-list.

## nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast conditional-advertise enable

### Usage

  nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast conditional-advertise enable [options]

### Description

  Turn the feature 'on' or 'off'.  The default is 'off'.

### Identifiers

  <vrf-id>         VRF
  <peer-group-id>  Domain

## nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast conditional-advertise advertise-map

### Usage

  nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast conditional-advertise advertise-map [options]

### Description

  route-map contains prefix-list which has list of routes/prefixes to operate on.

### Identifiers

  <vrf-id>         VRF
  <peer-group-id>  Domain

## nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast conditional-advertise exist-map

### Usage

  nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast conditional-advertise exist-map [options]

### Description

  route-map contains the conditional routes/prefixes in prefix-list.

### Identifiers

  <vrf-id>         VRF
  <peer-group-id>  Domain

## nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast conditional-advertise non-exist-map

### Usage

  nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast conditional-advertise non-exist-map [options]

### Description

  route-map contains the negative conditional routes/prefixes in prefix-list.

### Identifiers

  <vrf-id>         VRF
  <peer-group-id>  Domain

## nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast enable

### Usage

  nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast enable [options]

### Description

  Turn the feature 'on' or 'off'.  The default is 'off'.

### Identifiers

  <vrf-id>         VRF
  <peer-group-id>  Domain

## nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast route-reflector-client

### Usage

  nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast route-reflector-client [options]

### Description

  Specifies if this peer is a client and we are its route reflector

### Identifiers

  <vrf-id>         VRF
  <peer-group-id>  Domain

## nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast route-server-client

### Usage

  nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast route-server-client [options]

### Description

  Specifies if this peer is a client and we are its route server

### Identifiers

  <vrf-id>         VRF
  <peer-group-id>  Domain

## nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast soft-reconfiguration

### Usage

  nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast soft-reconfiguration [options]

### Description

  If 'on', it means that received routes from this peer that are rejected by inbound policy are still stored. This allows policy changes to take effect without any exchange of BGP Updates.

### Identifiers

  <vrf-id>         VRF
  <peer-group-id>  Domain

## nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast nexthop-setting

### Usage

  nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast nexthop-setting [options]

### Description

  Control nexthop value of advertised routes.  "auto" follows regular BGP next-hop determination rules.  This is the default.  "self" sets the next hop to ourselves for route advertisement, except for reflected routes.  "force" sets the next hop to ourselves for route advertisement including for reflected routes.

### Identifiers

  <vrf-id>         VRF
  <peer-group-id>  Domain

## nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast add-path-tx

### Usage

  nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast add-path-tx [options]

### Description

  Used to enable transmission of additional paths; by default, only the best path is announced to peers

### Identifiers

  <vrf-id>         VRF
  <peer-group-id>  Domain

## nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast weight

### Usage

  nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast weight [options]

### Description

  Weight applied to routes received from peer; this is used in the BGP route selection algorithm

### Identifiers

  <vrf-id>         VRF
  <peer-group-id>  Domain

## nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family l2vpn-evpn

### Usage

  nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family l2vpn-evpn [options] [<attribute> ...]

### Description

  Peer l2vpn EVPN address family.

### Identifiers

  <vrf-id>              VRF
  <peer-group-id>       Domain

### Atrributes

  attribute-mod         Attribute mod for address family.
  aspath                Options for handling AS_PATH for prefixes from/to peer
                        for the specified address family
  policy                Policies for l2vpn evpn
  enable                Turn the feature 'on' or 'off'. The default is 'off'.
  add-path-tx           Used to enable transmission of additional paths; by
                        default, only the best path is announced to peers
  nexthop-setting       Control nexthop value of advertised routes. "auto"
                        follows regular BGP next-hop determination rules. This
                        is the default. "self" sets the next hop to ourselves
                        for route advertisement, except for reflected routes.
                        "force" sets the next hop to ourselves for route
                        advertisement including for reflected routes.
  route-reflector-client
                        Specifies if this peer is a client and we are its
                        route reflector
  route-server-client   Specifies if this peer is a client and we are its
                        route server
  soft-reconfiguration  If 'on', it means that received routes from this peer
                        that are rejected by inbound policy are still stored.
                        This allows policy changes to take effect without any
                        exchange of BGP Updates.

## nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family l2vpn-evpn attribute-mod

### Usage

  nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family l2vpn-evpn attribute-mod [options] [<attribute> ...]

### Description

  Attribute mod for address family.

### Identifiers

  <vrf-id>         VRF
  <peer-group-id>  Domain

### Atrributes

  aspath           If 'on', it means follow normal BGP procedures in the
                   generation of AS_PATH attribute for this peer; if 'off' it
                   means do not change the AS_PATH when sending an Update to
                   this peer.
  med              If 'on', it means follow normal BGP procedures in the
                   generation of MED attribute for this peer; if 'off' it
                   means do not change the MED when sending an Update to this
                   peer.
  nexthop          If 'on', it means follow normal BGP procedures in the
                   generation of NEXT_HOP attribute for this peer; if 'off' it
                   means do not change the NEXT_HOP when sending an Update to
                   this peer.

## nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family l2vpn-evpn attribute-mod aspath

### Usage

  nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family l2vpn-evpn attribute-mod aspath [options]

### Description

  If 'on', it means follow normal BGP procedures in the generation of AS_PATH attribute for this peer; if 'off' it means do not change the AS_PATH when sending an Update to this peer.

### Identifiers

  <vrf-id>         VRF
  <peer-group-id>  Domain

## nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family l2vpn-evpn attribute-mod med

### Usage

  nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family l2vpn-evpn attribute-mod med [options]

### Description

  If 'on', it means follow normal BGP procedures in the generation of MED attribute for this peer; if 'off' it means do not change the MED when sending an Update to this peer.

### Identifiers

  <vrf-id>         VRF
  <peer-group-id>  Domain

## nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family l2vpn-evpn attribute-mod nexthop

### Usage

  nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family l2vpn-evpn attribute-mod nexthop [options]

### Description

  If 'on', it means follow normal BGP procedures in the generation of NEXT_HOP attribute for this peer; if 'off' it means do not change the NEXT_HOP when sending an Update to this peer.

### Identifiers

  <vrf-id>         VRF
  <peer-group-id>  Domain

## nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family l2vpn-evpn aspath

### Usage

  nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family l2vpn-evpn aspath [options] [<attribute> ...]

### Description

  Options for handling AS_PATH for prefixes from/to peer for the specified address family

### Identifiers

  <vrf-id>         VRF
  <peer-group-id>  Domain

### Atrributes

  allow-my-asn     If enabled, it is acceptable for a received AS_PATH to
                   contain the ASN of the local system
  private-as       If 'none', no specific action is taken. This is the
                   default. If set to 'remove', any private ASNs in the Update
                   to the peer are removed. If set to 'replace' any private
                   ASNs in the Update to the peer are replaced with the ASN of
                   the local system.
  replace-peer-as  If on, if the AS_PATH in an outgoing Update contains the
                   peer's ASN, it is replaced with the local system's ASN

## nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family l2vpn-evpn aspath allow-my-asn

### Usage

  nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family l2vpn-evpn aspath allow-my-asn [options] [<attribute> ...]

### Description

  If enabled, it is acceptable for a received AS_PATH to contain the ASN of the local system

### Identifiers

  <vrf-id>         VRF
  <peer-group-id>  Domain

### Atrributes

  enable           Turn the feature 'on' or 'off'. The default is 'off'.
  occurrences      Indicates max number of occurrences of the local system's
                   AS number in the received AS_PATH
  origin           If on, a received AS_PATH containing the ASN of the local
                   system is allowed, but only if it is the originating AS

## nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family l2vpn-evpn aspath allow-my-asn enable

### Usage

  nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family l2vpn-evpn aspath allow-my-asn enable [options]

### Description

  Turn the feature 'on' or 'off'.  The default is 'off'.

### Identifiers

  <vrf-id>         VRF
  <peer-group-id>  Domain

## nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family l2vpn-evpn aspath allow-my-asn origin

### Usage

  nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family l2vpn-evpn aspath allow-my-asn origin [options]

### Description

  If on, a received AS_PATH containing the ASN of the local system is allowed, but only if it is the originating AS

### Identifiers

  <vrf-id>         VRF
  <peer-group-id>  Domain

## nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family l2vpn-evpn aspath allow-my-asn occurrences

### Usage

  nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family l2vpn-evpn aspath allow-my-asn occurrences [options]

### Description

  Indicates max number of occurrences of the local system's AS number in the received AS_PATH

### Identifiers

  <vrf-id>         VRF
  <peer-group-id>  Domain

## nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family l2vpn-evpn aspath replace-peer-as

### Usage

  nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family l2vpn-evpn aspath replace-peer-as [options]

### Description

  If on, if the AS_PATH in an outgoing Update contains the peer's ASN, it is replaced with the local system's ASN

### Identifiers

  <vrf-id>         VRF
  <peer-group-id>  Domain

## nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family l2vpn-evpn aspath private-as

### Usage

  nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family l2vpn-evpn aspath private-as [options]

### Description

  If 'none', no specific action is taken.  This is the default.  If set to 'remove', any private ASNs in the Update to the peer are removed.  If set to 'replace' any private ASNs in the Update to the peer are replaced with the ASN of the local system.

### Identifiers

  <vrf-id>         VRF
  <peer-group-id>  Domain

## nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family l2vpn-evpn policy

### Usage

  nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family l2vpn-evpn policy [options] [<attribute> ...]

### Description

  Policies for l2vpn evpn

### Identifiers

  <vrf-id>         VRF
  <peer-group-id>  Domain

### Atrributes

  inbound          Inbound l2vpn-evpn policy
  outbound         Outbound l2vpn-evpn policy

## nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family l2vpn-evpn policy inbound

### Usage

  nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family l2vpn-evpn policy inbound [options] [<attribute> ...]

### Description

  Inbound l2vpn-evpn policy

### Identifiers

  <vrf-id>         VRF
  <peer-group-id>  Domain

### Atrributes

  route-map        Route map to apply to Updates received from this peer

## nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family l2vpn-evpn policy inbound route-map

### Usage

  nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family l2vpn-evpn policy inbound route-map [options]

### Description

  Route map to apply to Updates received from this peer

### Identifiers

  <vrf-id>         VRF
  <peer-group-id>  Domain

## nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family l2vpn-evpn policy outbound

### Usage

  nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family l2vpn-evpn policy outbound [options] [<attribute> ...]

### Description

  Outbound l2vpn-evpn policy

### Identifiers

  <vrf-id>         VRF
  <peer-group-id>  Domain

### Atrributes

  route-map        Route map to apply to Updates to be sent to this peer
  unsuppress-map   Route map used to unsuppress routes selectively when
                   advertising to this peer; these are routes that have been
                   suppressed due to aggregation configuration.

## nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family l2vpn-evpn policy outbound route-map

### Usage

  nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family l2vpn-evpn policy outbound route-map [options]

### Description

  Route map to apply to Updates to be sent to this peer

### Identifiers

  <vrf-id>         VRF
  <peer-group-id>  Domain

## nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family l2vpn-evpn policy outbound unsuppress-map

### Usage

  nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family l2vpn-evpn policy outbound unsuppress-map [options]

### Description

  Route map used to unsuppress routes selectively when advertising to this peer; these are routes that have been suppressed due to aggregation configuration.

### Identifiers

  <vrf-id>         VRF
  <peer-group-id>  Domain

## nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family l2vpn-evpn enable

### Usage

  nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family l2vpn-evpn enable [options]

### Description

  Turn the feature 'on' or 'off'.  The default is 'off'.

### Identifiers

  <vrf-id>         VRF
  <peer-group-id>  Domain

## nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family l2vpn-evpn route-reflector-client

### Usage

  nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family l2vpn-evpn route-reflector-client [options]

### Description

  Specifies if this peer is a client and we are its route reflector

### Identifiers

  <vrf-id>         VRF
  <peer-group-id>  Domain

## nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family l2vpn-evpn route-server-client

### Usage

  nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family l2vpn-evpn route-server-client [options]

### Description

  Specifies if this peer is a client and we are its route server

### Identifiers

  <vrf-id>         VRF
  <peer-group-id>  Domain

## nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family l2vpn-evpn soft-reconfiguration

### Usage

  nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family l2vpn-evpn soft-reconfiguration [options]

### Description

  If 'on', it means that received routes from this peer that are rejected by inbound policy are still stored. This allows policy changes to take effect without any exchange of BGP Updates.

### Identifiers

  <vrf-id>         VRF
  <peer-group-id>  Domain

## nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family l2vpn-evpn nexthop-setting

### Usage

  nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family l2vpn-evpn nexthop-setting [options]

### Description

  Control nexthop value of advertised routes.  "auto" follows regular BGP next-hop determination rules.  This is the default.  "self" sets the next hop to ourselves for route advertisement, except for reflected routes.  "force" sets the next hop to ourselves for route advertisement including for reflected routes.

### Identifiers

  <vrf-id>         VRF
  <peer-group-id>  Domain

## nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family l2vpn-evpn add-path-tx

### Usage

  nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> address-family l2vpn-evpn add-path-tx [options]

### Description

  Used to enable transmission of additional paths; by default, only the best path is announced to peers

### Identifiers

  <vrf-id>         VRF
  <peer-group-id>  Domain

## nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> password

### Usage

  nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> password [options]

### Description

  Password

### Identifiers

  <vrf-id>         VRF
  <peer-group-id>  Domain

## nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> enforce-first-as

### Usage

  nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> enforce-first-as [options]

### Description

  If on, when BGP updates are received from EBGP peers with this config, check that first AS matches peer's AS

### Identifiers

  <vrf-id>         VRF
  <peer-group-id>  Domain

## nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> passive-mode

### Usage

  nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> passive-mode [options]

### Description

  If enabled, do not initiate the BGP connection but wait for incoming connection

### Identifiers

  <vrf-id>         VRF
  <peer-group-id>  Domain

## nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> nexthop-connected-check

### Usage

  nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> nexthop-connected-check [options]

### Description

  If 'on', it disables the check that a non-multihop EBGP peer should be directly connected and only announce connected next hops

### Identifiers

  <vrf-id>         VRF
  <peer-group-id>  Domain

## nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> multihop-ttl

### Usage

  nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> multihop-ttl [options]

### Description

  Maximum hops allowed.  When 'auto', the type of peer will determine the appropriate value (255 for iBGP and 1 for eBGP).  This is the default.

### Identifiers

  <vrf-id>         VRF
  <peer-group-id>  Domain

## nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> description

### Usage

  nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> description [options]

### Description

  neighbor description

### Identifiers

  <vrf-id>         VRF
  <peer-group-id>  Domain

## nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> remote-as

### Usage

  nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> remote-as [options]

### Description

  ASN for the BGP neighbor(s) using this configuration.  If specified as 'external', it means an EBGP configuration but the actual ASN is immaterial. If specified as 'internal', it means an IBGP configuration.

### Identifiers

  <vrf-id>         VRF
  <peer-group-id>  Domain

## nv unset vrf <vrf-id> router bgp route-export

### Usage

  nv unset vrf <vrf-id> router bgp route-export [options] [<attribute> ...]

### Description

  Controls for exporting ipv4 and ipv6 routes from this VRF

### Identifiers

  <vrf-id>    VRF### Atrributes

  to-evpn     Controls for exporting routes from this VRF into EVPN



## nv unset vrf <vrf-id> router bgp route-export to-evpn

### Usage

  nv unset vrf <vrf-id> router bgp route-export to-evpn [options] [<attribute> ...]

### Description

  Controls for exporting routes from this VRF into EVPN

### Identifiers

  <vrf-id>      VRF

### Atrributes

  route-target  List the RTs to attach to host or prefix routes when exporting
                them into EVPN or "auto". If "auto", the RT will be derived.
                This is the default.

## nv unset vrf <vrf-id> router bgp route-export to-evpn route-target <rt-id>

### Usage

  nv unset vrf <vrf-id> router bgp route-export to-evpn route-target <rt-id> [options]

### Description

  A route target identifier

### Identifiers

  <vrf-id>    VRF
  <rt-id>     Route targets or "auto"

## nv unset vrf <vrf-id> router bgp route-import

### Usage

  nv unset vrf <vrf-id> router bgp route-import [options] [<attribute> ...]

### Description

  Controls for importing of ipv4 and ipv6 routes from this VRF

### Identifiers

  <vrf-id>    VRF### Atrributes

  from-evpn   Controls for importing EVPN type-2 and type-5 routes into this
              VRF



## nv unset vrf <vrf-id> router bgp route-import from-evpn

### Usage

  nv unset vrf <vrf-id> router bgp route-import from-evpn [options] [<attribute> ...]

### Description

  Controls for importing EVPN type-2 and type-5 routes into this VRF

### Identifiers

  <vrf-id>      VRF

### Atrributes

  route-target  List the RTs to attach to host or prefix routes when importing
                them into VRF or "auto". If "auto", the RT will be derived.
                This is the default.

## nv unset vrf <vrf-id> router bgp route-import from-evpn route-target <rt-id>

### Usage

  nv unset vrf <vrf-id> router bgp route-import from-evpn route-target <rt-id> [options]

### Description

  A route target identifier

### Identifiers

  <vrf-id>    VRF
  <rt-id>     Route targets or "auto"



## nv unset vrf <vrf-id> router bgp timers

### Usage

  nv unset vrf <vrf-id> router bgp timers [options] [<attribute> ...]

### Description

  timer values for all peers in this VRF

### Identifiers

  <vrf-id>              VRF

### Atrributes

  conditional-advertise
                        Time interval at which bgp table is scanned for
                        condition is met.
  connection-retry      Time interval at which connection attempts are retried
                        upon a failure.
  hold                  Hold timer. If `none`, keepalives from the peer are
                        not tracked and the peering session will not
                        experience a hold timeout.
  keepalive             Keepalive timer. If `none`, keepalives are not sent.
  route-advertisement   Time between route advertisements (BGP Updates). If
                        not `none`, route advertisements to be delayed and
                        batched.

## nv unset vrf <vrf-id> router bgp timers keepalive

### Usage

  nv unset vrf <vrf-id> router bgp timers keepalive [options]

### Description

  Keepalive timer.  If `none`, keepalives are not sent.

### Identifiers

  <vrf-id>    VRF## nv unset vrf <vrf-id> router bgp timers hold

### Usage

  nv unset vrf <vrf-id> router bgp timers hold [options]

### Description

  Hold timer.  If `none`, keepalives from the peer are not tracked and the peering session will not experience a hold timeout.

### Identifiers

  <vrf-id>    VRF## nv unset vrf <vrf-id> router bgp timers connection-retry

### Usage

  nv unset vrf <vrf-id> router bgp timers connection-retry [options]

### Description

  Time interval at which connection attempts are retried upon a failure.

### Identifiers

  <vrf-id>    VRF

## nv unset vrf <vrf-id> router bgp timers route-advertisement

### Usage

  nv unset vrf <vrf-id> router bgp timers route-advertisement [options]

### Description

  Time between route advertisements (BGP Updates).  If not `none`, route advertisements to be delayed and batched.

### Identifiers

  <vrf-id>    VRF

## nv unset vrf <vrf-id> router bgp timers conditional-advertise

### Usage

  nv unset vrf <vrf-id> router bgp timers conditional-advertise [options]

### Description

  Time interval at which bgp table is scanned for condition is met.

### Identifiers

  <vrf-id>    VRF

## nv unset vrf <vrf-id> router bgp confederation

### Usage

  nv unset vrf <vrf-id> router bgp confederation [options] [<attribute> ...]

### Description

  BGP Confederation options.

### Identifiers

  <vrf-id>    VRF### Atrributes

  member-as   Confederation ASNs of the peers, maps to BGP confederation peers
  id          Confederation ASN, maps to BGP confederation id



## nv unset vrf <vrf-id> router bgp confederation member-as

### Usage

  nv unset vrf <vrf-id> router bgp confederation member-as [options]

### Description

  Set of autonomous numbers

### Identifiers

  <vrf-id>    VRF

## nv unset vrf <vrf-id> router bgp confederation id

### Usage

  nv unset vrf <vrf-id> router bgp confederation id [options]

### Description

  Confederation ASN, maps to BGP confederation id

### Identifiers

  <vrf-id>    VRF

## nv unset vrf <vrf-id> router bgp neighbor <neighbor-id>

### Usage

  nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> [options] [<attribute> ...]

### Description

  BGP global configuration.

### Identifiers

  <vrf-id>              VRF
  <neighbor-id>         Peer ID

### Atrributes

  bfd                   Specifies whether to track BGP peering sessions using
                        this configuration via BFD.
  capabilities          Capabilities
  local-as              Local AS feature
  graceful-restart      BGP Graceful restart per neighbor configuration
  ttl-security          RFC 5082
  address-family        Address family specific configuration
  timers                Peer peer-timerss
  description           neighbor description
  enforce-first-as      If on, when BGP updates are received from EBGP peers
                        with this config, check that first AS matches peer's
                        AS
  multihop-ttl          Maximum hops allowed. When 'auto', the type of peer
                        will determine the appropriate value (255 for iBGP and
                        1 for eBGP). This is the default.
  nexthop-connected-check
                        If 'on', it disables the check that a non-multihop
                        EBGP peer should be directly connected and only
                        announce connected next hops
  passive-mode          If enabled, do not initiate the BGP connection but
                        wait for incoming connection
  password              Password
  enable                Turn the feature 'on' or 'off'. The default is 'on'.
  peer-group            Optional peer-group to which the peer is attached to
                        inherit the group's configuration.
  remote-as             ASN for the BGP neighbor(s) using this configuration.
                        If specified as 'external', it means an EBGP
                        configuration but the actual ASN is immaterial. If
                        specified as 'internal', it means an IBGP
                        configuration.
  type                  The type of peer

## nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> bfd

### Usage

  nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> bfd [options] [<attribute> ...]

### Description

  Specifies whether to track BGP peering sessions using this configuration via BFD.

### Identifiers

  <vrf-id>           VRF
  <neighbor-id>      Peer ID

### Atrributes

  enable             Turn the feature 'on' or 'off'. The default is 'off'.
  detect-multiplier  Detect multiplier
  min-rx-interval    Minimum receive interval
  min-tx-interval    Minimum transmit interval. The actual value used is the
                     smaller of this or what the peer expects.

## nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> bfd enable

### Usage

  nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> bfd enable [options]

### Description

  Turn the feature 'on' or 'off'.  The default is 'off'.

### Identifiers

  <vrf-id>       VRF
  <neighbor-id>  Peer ID

## nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> bfd detect-multiplier

### Usage

  nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> bfd detect-multiplier [options]

### Description

  Detect multiplier

### Identifiers

  <vrf-id>       VRF
  <neighbor-id>  Peer ID

## nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> bfd min-rx-interval

### Usage

  nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> bfd min-rx-interval [options]

### Description

  Minimum receive interval

### Identifiers

  <vrf-id>       VRF
  <neighbor-id>  Peer ID

## nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> bfd min-tx-interval

### Usage

  nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> bfd min-tx-interval [options]

### Description

  Minimum transmit interval.  The actual value used is the smaller of this or what the peer expects.

### Identifiers

  <vrf-id>       VRF
  <neighbor-id>  Peer ID

## nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> capabilities

### Usage

  nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> capabilities [options] [<attribute> ...]

### Description

  Capabilities

### Identifiers

  <vrf-id>          VRF
  <neighbor-id>     Peer ID

### Atrributes

  extended-nexthop  If 'on', the extended-nexthop capability defined in RFC
                    5549 is advertised to peer(s) with this config. If 'auto',
                    it will be 'on' for unnumbered peers and 'off' otherwise.
                    This is the default.
  source-address    source IP address of the TCP connection, which is often
                    used as the BGP next hop for Updates

## nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> capabilities extended-nexthop

### Usage

  nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> capabilities extended-nexthop [options]

### Description

  If 'on', the extended-nexthop capability defined in RFC 5549 is advertised to peer(s) with this config.  If 'auto', it will be 'on' for unnumbered peers and 'off' otherwise.  This is the default.

### Identifiers

  <vrf-id>       VRF
  <neighbor-id>  Peer ID

## nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> capabilities source-address

### Usage

  nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> capabilities source-address [options]

### Description

  source IP address of the TCP connection, which is often used as the BGP next hop for Updates

### Identifiers

  <vrf-id>       VRF
  <neighbor-id>  Peer ID

## nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> local-as

### Usage

  nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> local-as [options] [<attribute> ...]

### Description

  Local AS feature

### Identifiers

  <vrf-id>       VRF
  <neighbor-id>  Peer ID

### Atrributes

  enable         Turn the feature 'on' or 'off'. The default is 'off'.
  asn            ASN to use to establish the peering if different from the ASN
                 of the BGP instance. This configuration finds use during AS
                 renumbering. The local-as configured is also attached to
                 incoming and outgoing updates.
  prepend        When set to 'off', do not prepend the configured local-as to
                 received updates; otherwise, prepend it.
  replace        When set to 'on', attach only the configured local-as to
                 generated updates, effectively "replacing" the AS number
                 configured for the BGP instance with the local-as applicable
                 for the peering; otherwise, attach the AS number of the BGP
                 instance and then prepend it with the configured local-as.

## nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> local-as enable

### Usage

  nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> local-as enable [options]

### Description

  Turn the feature 'on' or 'off'.  The default is 'off'.

### Identifiers

  <vrf-id>       VRF
  <neighbor-id>  Peer ID

## nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> local-as asn

### Usage

  nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> local-as asn [options]

### Description

  ASN to use to establish the peering if different from the ASN of the BGP instance.  This configuration finds use during AS renumbering.  The local-as configured is also attached to incoming and outgoing updates.

### Identifiers

  <vrf-id>       VRF
  <neighbor-id>  Peer ID

## nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> local-as prepend

### Usage

  nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> local-as prepend [options]

### Description

  When set to 'off', do not prepend the configured local-as to received updates; otherwise, prepend it.

### Identifiers

  <vrf-id>       VRF
  <neighbor-id>  Peer ID

## nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> local-as replace

### Usage

  nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> local-as replace [options]

### Description

  When set to 'on', attach only the configured local-as to generated updates, effectively "replacing" the AS number configured for the BGP instance with the local-as applicable for the peering; otherwise, attach the AS number of the BGP instance and then prepend it with the configured local-as.

### Identifiers

  <vrf-id>       VRF
  <neighbor-id>  Peer ID

## nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> graceful-restart

### Usage

  nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> graceful-restart [options] [<attribute> ...]

### Description

  BGP Graceful restart per neighbor configuration

### Identifiers

  <vrf-id>       VRF
  <neighbor-id>  Peer ID

### Atrributes

  mode           If 'auto', inherit from global. This is the default. If set
                 to 'off', GR capability is not negotiated with this peer. If
                 set to 'helper-only', only the Helper role is supported for
                 this peer. This means that the GR capability will be
                 negotiated without any address-families with this peer. If
                 set to 'full', both the Helper role and the Restarter role
                 are supported with this peer; the GR capability will be
                 negotiated with the enabled address-families for which GR is
                 also supported.

## nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> graceful-restart mode

### Usage

  nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> graceful-restart mode [options]

### Description

  If 'auto', inherit from global.  This is the default.  If set to 'off', GR capability is not negotiated with this peer.  If set to 'helper-only', only the Helper role is supported for this peer. This means that the GR capability will be negotiated without any address-families with this peer.  If set to 'full', both the Helper role and the Restarter role are supported with this peer; the GR capability will be negotiated with the enabled address-families for which GR is also supported.

### Identifiers

  <vrf-id>       VRF
  <neighbor-id>  Peer ID

## nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> ttl-security

### Usage

  nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> ttl-security [options] [<attribute> ...]

### Description

  RFC 5082

### Identifiers

  <vrf-id>       VRF
  <neighbor-id>  Peer ID

### Atrributes

  enable         Turn the feature 'on' or 'off'. The default is 'off'.
  hops           Number of hops

## nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> ttl-security enable

### Usage

  nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> ttl-security enable [options]

### Description

  Turn the feature 'on' or 'off'.  The default is 'off'.

### Identifiers

  <vrf-id>       VRF
  <neighbor-id>  Peer ID

## nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> ttl-security hops

### Usage

  nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> ttl-security hops [options]

### Description

  Number of hops

### Identifiers

  <vrf-id>       VRF
  <neighbor-id>  Peer ID

## nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family

### Usage

  nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family [options] [<attribute> ...]

### Description

  Address family specific configuration

### Identifiers

  <vrf-id>       VRF
  <neighbor-id>  Peer ID

### Atrributes

  ipv4-unicast   Peer IPv4 unicast address family. Always on, unless disabled
                 globaly.
  ipv6-unicast   Peer IPv6 unicast address family.
  l2vpn-evpn     Peer l2vpn EVPN address family.

## nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast

### Usage

  nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast [options] [<attribute> ...]

### Description

  Peer IPv4 unicast address family.  Always on, unless disabled globaly.

### Identifiers

  <vrf-id>              VRF
  <neighbor-id>         Peer ID

### Atrributes

  attribute-mod         Attribute mod for address family.
  aspath                Options for handling AS_PATH for prefixes from/to peer
                        for the specified address family
  policy                Policies for ipv4 unicast
  prefix-limits         Limits on prefix from the peer for this address-family
  default-route-origination
                        Default route origination
  community-advertise   Community advertise for address family.
  conditional-advertise
                        Conditional advertise for address family.
  enable                Turn the feature 'on' or 'off'. The default is 'on'.
  add-path-tx           Used to enable transmission of additional paths; by
                        default, only the best path is announced to peers
  nexthop-setting       Control nexthop value of advertised routes. "auto"
                        follows regular BGP next-hop determination rules. This
                        is the default. "self" sets the next hop to ourselves
                        for route advertisement, except for reflected routes.
                        "force" sets the next hop to ourselves for route
                        advertisement including for reflected routes.
  route-reflector-client
                        Specifies if this peer is a client and we are its
                        route reflector
  route-server-client   Specifies if this peer is a client and we are its
                        route server
  soft-reconfiguration  If 'on', it means that received routes from this peer
                        that are rejected by inbound policy are still stored.
                        This allows policy changes to take effect without any
                        exchange of BGP Updates.
  weight                Weight applied to routes received from peer; this is
                        used in the BGP route selection algorithm

## nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast attribute-mod

### Usage

  nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast attribute-mod [options] [<attribute> ...]

### Description

  Attribute mod for address family.

### Identifiers

  <vrf-id>       VRF
  <neighbor-id>  Peer ID

### Atrributes

  aspath         If 'on', it means follow normal BGP procedures in the
                 generation of AS_PATH attribute for this peer; if 'off' it
                 means do not change the AS_PATH when sending an Update to
                 this peer.
  med            If 'on', it means follow normal BGP procedures in the
                 generation of MED attribute for this peer; if 'off' it means
                 do not change the MED when sending an Update to this peer.
  nexthop        If 'on', it means follow normal BGP procedures in the
                 generation of NEXT_HOP attribute for this peer; if 'off' it
                 means do not change the NEXT_HOP when sending an Update to
                 this peer.

## nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast attribute-mod aspath

### Usage

  nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast attribute-mod aspath [options]

### Description

  If 'on', it means follow normal BGP procedures in the generation of AS_PATH attribute for this peer; if 'off' it means do not change the AS_PATH when sending an Update to this peer.

### Identifiers

  <vrf-id>       VRF
  <neighbor-id>  Peer ID

## nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast attribute-mod med

### Usage

  nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast attribute-mod med [options]

### Description

  If 'on', it means follow normal BGP procedures in the generation of MED attribute for this peer; if 'off' it means do not change the MED when sending an Update to this peer.

### Identifiers

  <vrf-id>       VRF
  <neighbor-id>  Peer ID

## nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast attribute-mod nexthop

### Usage

  nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast attribute-mod nexthop [options]

### Description

  If 'on', it means follow normal BGP procedures in the generation of NEXT_HOP attribute for this peer; if 'off' it means do not change the NEXT_HOP when sending an Update to this peer.

### Identifiers

  <vrf-id>       VRF
  <neighbor-id>  Peer ID

## nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast aspath

### Usage

  nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast aspath [options] [<attribute> ...]

### Description

  Options for handling AS_PATH for prefixes from/to peer for the specified address family

### Identifiers

  <vrf-id>         VRF
  <neighbor-id>    Peer ID

### Atrributes

  allow-my-asn     If enabled, it is acceptable for a received AS_PATH to
                   contain the ASN of the local system
  private-as       If 'none', no specific action is taken. This is the
                   default. If set to 'remove', any private ASNs in the Update
                   to the peer are removed. If set to 'replace' any private
                   ASNs in the Update to the peer are replaced with the ASN of
                   the local system.
  replace-peer-as  If on, if the AS_PATH in an outgoing Update contains the
                   peer's ASN, it is replaced with the local system's ASN

## nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast aspath allow-my-asn

### Usage

  nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast aspath allow-my-asn [options] [<attribute> ...]

### Description

  If enabled, it is acceptable for a received AS_PATH to contain the ASN of the local system

### Identifiers

  <vrf-id>       VRF
  <neighbor-id>  Peer ID

### Atrributes

  enable         Turn the feature 'on' or 'off'. The default is 'off'.
  occurrences    Indicates max number of occurrences of the local system's AS
                 number in the received AS_PATH
  origin         If on, a received AS_PATH containing the ASN of the local
                 system is allowed, but only if it is the originating AS

## nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast aspath allow-my-asn enable

### Usage

  nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast aspath allow-my-asn enable [options]

### Description

  Turn the feature 'on' or 'off'.  The default is 'off'.

### Identifiers

  <vrf-id>       VRF
  <neighbor-id>  Peer ID

## nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast aspath allow-my-asn origin

### Usage

  nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast aspath allow-my-asn origin [options]

### Description

  If on, a received AS_PATH containing the ASN of the local system is allowed, but only if it is the originating AS

### Identifiers

  <vrf-id>       VRF
  <neighbor-id>  Peer ID

## nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast aspath allow-my-asn occurrences

### Usage

  nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast aspath allow-my-asn occurrences [options]

### Description

  Indicates max number of occurrences of the local system's AS number in the received AS_PATH

### Identifiers

  <vrf-id>       VRF
  <neighbor-id>  Peer ID

## nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast aspath replace-peer-as

### Usage

  nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast aspath replace-peer-as [options]

### Description

  If on, if the AS_PATH in an outgoing Update contains the peer's ASN, it is replaced with the local system's ASN

### Identifiers

  <vrf-id>       VRF
  <neighbor-id>  Peer ID

## nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast aspath private-as

### Usage

  nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast aspath private-as [options]

### Description

  If 'none', no specific action is taken.  This is the default.  If set to 'remove', any private ASNs in the Update to the peer are removed.  If set to 'replace' any private ASNs in the Update to the peer are replaced with the ASN of the local system.

### Identifiers

  <vrf-id>       VRF
  <neighbor-id>  Peer ID

## nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast policy

### Usage

  nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast policy [options] [<attribute> ...]

### Description

  Policies for ipv4 unicast

### Identifiers

  <vrf-id>       VRF
  <neighbor-id>  Peer ID

### Atrributes

  inbound        Outbound unicast policy
  outbound       Outbound unicast policy

## nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast policy inbound

### Usage

  nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast policy inbound [options] [<attribute> ...]

### Description

  Outbound unicast policy

### Identifiers

  <vrf-id>       VRF
  <neighbor-id>  Peer ID

### Atrributes

  route-map      Route map to apply to Updates received from this peer
  aspath-list    AS-Path filter list to apply to Updates received from this
                 peer
  prefix-list    Prefix list to apply to Updates received from this peer

## nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast policy inbound route-map

### Usage

  nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast policy inbound route-map [options]

### Description

  Route map to apply to Updates received from this peer

### Identifiers

  <vrf-id>       VRF
  <neighbor-id>  Peer ID

## nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast policy inbound prefix-list

### Usage

  nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast policy inbound prefix-list [options]

### Description

  Prefix list to apply to Updates received from this peer

### Identifiers

  <vrf-id>       VRF
  <neighbor-id>  Peer ID

## nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast policy inbound aspath-list

### Usage

  nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast policy inbound aspath-list [options]

### Description

  AS-Path filter list to apply to Updates received from this peer

### Identifiers

  <vrf-id>       VRF
  <neighbor-id>  Peer ID

## nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast policy outbound

### Usage

  nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast policy outbound [options] [<attribute> ...]

### Description

  Outbound unicast policy

### Identifiers

  <vrf-id>        VRF
  <neighbor-id>   Peer ID

### Atrributes

  route-map       Route map to apply to Updates to be sent to this peer
  unsuppress-map  Route map used to unsuppress routes selectively when
                  advertising to this peer; these are routes that have been
                  suppressed due to aggregation configuration.
  aspath-list     AS-Path filter list to apply to Updates sent to this peer
  prefix-list     Prefix list to apply to Updates to be sent to this peer

## nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast policy outbound route-map

### Usage

  nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast policy outbound route-map [options]

### Description

  Route map to apply to Updates to be sent to this peer

### Identifiers

  <vrf-id>       VRF
  <neighbor-id>  Peer ID

## nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast policy outbound unsuppress-map

### Usage

  nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast policy outbound unsuppress-map [options]

### Description

  Route map used to unsuppress routes selectively when advertising to this peer; these are routes that have been suppressed due to aggregation configuration.

### Identifiers

  <vrf-id>       VRF
  <neighbor-id>  Peer ID

## nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast policy outbound prefix-list

### Usage

  nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast policy outbound prefix-list [options]

### Description

  Prefix list to apply to Updates to be sent to this peer

### Identifiers

  <vrf-id>       VRF
  <neighbor-id>  Peer ID

## nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast policy outbound aspath-list

### Usage

  nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast policy outbound aspath-list [options]

### Description

  AS-Path filter list to apply to Updates sent to this peer

### Identifiers

  <vrf-id>       VRF
  <neighbor-id>  Peer ID

## nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast prefix-limits

### Usage

  nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast prefix-limits [options] [<attribute> ...]

### Description

  Limits on prefix from the peer for this address-family

### Identifiers

  <vrf-id>       VRF
  <neighbor-id>  Peer ID

### Atrributes

  inbound        Limits on inbound prefix from the peer for this address-
                 family

## nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast prefix-limits inbound

### Usage

  nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast prefix-limits inbound [options] [<attribute> ...]

### Description

  Limits on inbound prefix from the peer for this address-family

### Identifiers

  <vrf-id>           VRF
  <neighbor-id>      Peer ID

### Atrributes

  maximum            Limit on number of prefixes of specific address-family
                     that can be received from the peer. By default, there is
                     no limit
  reestablish-wait   Specifes the time in seconds to wait before establishing
                     the BGP session again with the peer. Defaults to 'auto',
                     which will use standard BGP timers and processing. This
                     would typically be 2-3 seconds.
  warning-only       If 'on', it means to only generate a warning syslog if
                     the number of received prefixes exceeds the limit, do not
                     bring down the BGP session.
  warning-threshold  Percentage of the maximum at which a warning syslog is
                     generated.

## nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast prefix-limits inbound maximum

### Usage

  nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast prefix-limits inbound maximum [options]

### Description

  Limit on number of prefixes of specific address-family that can be received from the peer.  By default, there is no limit

### Identifiers

  <vrf-id>       VRF
  <neighbor-id>  Peer ID

## nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast prefix-limits inbound warning-threshold

### Usage

  nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast prefix-limits inbound warning-threshold [options]

### Description

  Percentage of the maximum at which a warning syslog is generated.

### Identifiers

  <vrf-id>       VRF
  <neighbor-id>  Peer ID

## nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast prefix-limits inbound warning-only

### Usage

  nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast prefix-limits inbound warning-only [options]

### Description

  If 'on', it means to only generate a warning syslog if the number of received prefixes exceeds the limit, do not bring down the BGP session.

### Identifiers

  <vrf-id>       VRF
  <neighbor-id>  Peer ID

## nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast prefix-limits inbound reestablish-wait

### Usage

  nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast prefix-limits inbound reestablish-wait [options]

### Description

  Specifes the time in seconds to wait before establishing the BGP session again with the peer. Defaults to 'auto', which will use standard BGP timers and processing.  This would typically be 2-3 seconds.

### Identifiers

  <vrf-id>       VRF
  <neighbor-id>  Peer ID

## nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast default-route-origination

### Usage

  nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast default-route-origination [options] [<attribute> ...]

### Description

  Default route origination

### Identifiers

  <vrf-id>       VRF
  <neighbor-id>  Peer ID

### Atrributes

  enable         Turn the feature 'on' or 'off'. The default is 'off'.
  policy         Optional route-map policy to control the conditions under
                 which the default route is originated.

## nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast default-route-origination enable

### Usage

  nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast default-route-origination enable [options]

### Description

  Turn the feature 'on' or 'off'.  The default is 'off'.

### Identifiers

  <vrf-id>       VRF
  <neighbor-id>  Peer ID

## nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast default-route-origination policy

### Usage

  nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast default-route-origination policy [options]

### Description

  Optional route-map policy to control the conditions under which the default route is originated.

### Identifiers

  <vrf-id>       VRF
  <neighbor-id>  Peer ID

## nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast community-advertise

### Usage

  nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast community-advertise [options] [<attribute> ...]

### Description

  Community advertise for address family.

### Identifiers

  <vrf-id>       VRF
  <neighbor-id>  Peer ID

### Atrributes

  extended       If 'on', it means we can announce the EXT_COMMUNITIES
                 attribute to this peer, otherwise we cannot.
  large          If 'on', it means we can announce the LARGE_COMMUNITIES
                 attribute to this peer, otherwise we cannot.
  regular        If 'on', it means we can announce the COMMUNITIES attribute
                 to this peer, otherwise we cannot.

## nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast community-advertise regular

### Usage

  nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast community-advertise regular [options]

### Description

  If 'on', it means we can announce the COMMUNITIES attribute to this peer, otherwise we cannot.

### Identifiers

  <vrf-id>       VRF
  <neighbor-id>  Peer ID

## nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast community-advertise extended

### Usage

  nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast community-advertise extended [options]

### Description

  If 'on', it means we can announce the EXT_COMMUNITIES attribute to this peer, otherwise we cannot.

### Identifiers

  <vrf-id>       VRF
  <neighbor-id>  Peer ID

## nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast community-advertise large

### Usage

  nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast community-advertise large [options]

### Description

  If 'on', it means we can announce the LARGE_COMMUNITIES attribute to this peer, otherwise we cannot.

### Identifiers

  <vrf-id>       VRF
  <neighbor-id>  Peer ID

## nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast conditional-advertise

### Usage

  nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast conditional-advertise [options] [<attribute> ...]

### Description

  Conditional advertise for address family.

### Identifiers

  <vrf-id>       VRF
  <neighbor-id>  Peer ID

### Atrributes

  enable         Turn the feature 'on' or 'off'. The default is 'off'.
  advertise-map  route-map contains prefix-list which has list of
                 routes/prefixes to operate on.
  exist-map      route-map contains the conditional routes/prefixes in prefix-
                 list.
  non-exist-map  route-map contains the negative conditional routes/prefixes
                 in prefix-list.

## nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast conditional-advertise enable

### Usage

  nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast conditional-advertise enable [options]

### Description

  Turn the feature 'on' or 'off'.  The default is 'off'.

### Identifiers

  <vrf-id>       VRF
  <neighbor-id>  Peer ID

## nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast conditional-advertise advertise-map

### Usage

  nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast conditional-advertise advertise-map [options]

### Description

  route-map contains prefix-list which has list of routes/prefixes to operate on.

### Identifiers

  <vrf-id>       VRF
  <neighbor-id>  Peer ID

## nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast conditional-advertise exist-map

### Usage

  nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast conditional-advertise exist-map [options]

### Description

  route-map contains the conditional routes/prefixes in prefix-list.

### Identifiers

  <vrf-id>       VRF
  <neighbor-id>  Peer ID

## nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast conditional-advertise non-exist-map

### Usage

  nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast conditional-advertise non-exist-map [options]

### Description

  route-map contains the negative conditional routes/prefixes in prefix-list.

### Identifiers

  <vrf-id>       VRF
  <neighbor-id>  Peer ID

## nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast enable

### Usage

  nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast enable [options]

### Description

  Turn the feature 'on' or 'off'.  The default is 'on'.

### Identifiers

  <vrf-id>       VRF
  <neighbor-id>  Peer ID

## nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast route-reflector-client

### Usage

  nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast route-reflector-client [options]

### Description

  Specifies if this peer is a client and we are its route reflector

### Identifiers

  <vrf-id>       VRF
  <neighbor-id>  Peer ID

## nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast route-server-client

### Usage

  nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast route-server-client [options]

### Description

  Specifies if this peer is a client and we are its route server

### Identifiers

  <vrf-id>       VRF
  <neighbor-id>  Peer ID

## nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast soft-reconfiguration

### Usage

  nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast soft-reconfiguration [options]

### Description

  If 'on', it means that received routes from this peer that are rejected by inbound policy are still stored. This allows policy changes to take effect without any exchange of BGP Updates.

### Identifiers

  <vrf-id>       VRF
  <neighbor-id>  Peer ID

## nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast nexthop-setting

### Usage

  nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast nexthop-setting [options]

### Description

  Control nexthop value of advertised routes.  "auto" follows regular BGP next-hop determination rules.  This is the default.  "self" sets the next hop to ourselves for route advertisement, except for reflected routes.  "force" sets the next hop to ourselves for route advertisement including for reflected routes.

### Identifiers

  <vrf-id>       VRF
  <neighbor-id>  Peer ID

## nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast add-path-tx

### Usage

  nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast add-path-tx [options]

### Description

  Used to enable transmission of additional paths; by default, only the best path is announced to peers

### Identifiers

  <vrf-id>       VRF
  <neighbor-id>  Peer ID

## nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast weight

### Usage

  nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast weight [options]

### Description

  Weight applied to routes received from peer; this is used in the BGP route selection algorithm

### Identifiers

  <vrf-id>       VRF
  <neighbor-id>  Peer ID

## nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast

### Usage

  nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast [options] [<attribute> ...]

### Description

  Peer IPv6 unicast address family.

### Identifiers

  <vrf-id>              VRF
  <neighbor-id>         Peer ID

### Atrributes

  attribute-mod         Attribute mod for address family.
  aspath                Options for handling AS_PATH for prefixes from/to peer
                        for the specified address family
  prefix-limits         Limits on prefix from the peer for this address-family
  default-route-origination
                        Default route origination
  policy                Policies for ipv4 unicast
  community-advertise   Community advertise for address family.
  conditional-advertise
                        Conditional advertise for address family.
  enable                Turn the feature 'on' or 'off'. The default is 'off'.
  add-path-tx           Used to enable transmission of additional paths; by
                        default, only the best path is announced to peers
  nexthop-setting       Control nexthop value of advertised routes. "auto"
                        follows regular BGP next-hop determination rules. This
                        is the default. "self" sets the next hop to ourselves
                        for route advertisement, except for reflected routes.
                        "force" sets the next hop to ourselves for route
                        advertisement including for reflected routes.
  route-reflector-client
                        Specifies if this peer is a client and we are its
                        route reflector
  route-server-client   Specifies if this peer is a client and we are its
                        route server
  soft-reconfiguration  If 'on', it means that received routes from this peer
                        that are rejected by inbound policy are still stored.
                        This allows policy changes to take effect without any
                        exchange of BGP Updates.
  weight                Weight applied to routes received from peer; this is
                        used in the BGP route selection algorithm

## nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast attribute-mod

### Usage

  nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast attribute-mod [options] [<attribute> ...]

### Description

  Attribute mod for address family.

### Identifiers

  <vrf-id>       VRF
  <neighbor-id>  Peer ID

### Atrributes

  aspath         If 'on', it means follow normal BGP procedures in the
                 generation of AS_PATH attribute for this peer; if 'off' it
                 means do not change the AS_PATH when sending an Update to
                 this peer.
  med            If 'on', it means follow normal BGP procedures in the
                 generation of MED attribute for this peer; if 'off' it means
                 do not change the MED when sending an Update to this peer.
  nexthop        If 'on', it means follow normal BGP procedures in the
                 generation of NEXT_HOP attribute for this peer; if 'off' it
                 means do not change the NEXT_HOP when sending an Update to
                 this peer.

## nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast attribute-mod aspath

### Usage

  nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast attribute-mod aspath [options]

### Description

  If 'on', it means follow normal BGP procedures in the generation of AS_PATH attribute for this peer; if 'off' it means do not change the AS_PATH when sending an Update to this peer.

### Identifiers

  <vrf-id>       VRF
  <neighbor-id>  Peer ID

## nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast attribute-mod med

### Usage

  nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast attribute-mod med [options]

### Description

  If 'on', it means follow normal BGP procedures in the generation of MED attribute for this peer; if 'off' it means do not change the MED when sending an Update to this peer.

### Identifiers

  <vrf-id>       VRF
  <neighbor-id>  Peer ID

## nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast attribute-mod nexthop

### Usage

  nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast attribute-mod nexthop [options]

### Description

  If 'on', it means follow normal BGP procedures in the generation of NEXT_HOP attribute for this peer; if 'off' it means do not change the NEXT_HOP when sending an Update to this peer.

### Identifiers

  <vrf-id>       VRF
  <neighbor-id>  Peer ID

## nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast aspath

### Usage

  nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast aspath [options] [<attribute> ...]

### Description

  Options for handling AS_PATH for prefixes from/to peer for the specified address family

### Identifiers

  <vrf-id>         VRF
  <neighbor-id>    Peer ID

### Atrributes

  allow-my-asn     If enabled, it is acceptable for a received AS_PATH to
                   contain the ASN of the local system
  private-as       If 'none', no specific action is taken. This is the
                   default. If set to 'remove', any private ASNs in the Update
                   to the peer are removed. If set to 'replace' any private
                   ASNs in the Update to the peer are replaced with the ASN of
                   the local system.
  replace-peer-as  If on, if the AS_PATH in an outgoing Update contains the
                   peer's ASN, it is replaced with the local system's ASN

## nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast aspath allow-my-asn

### Usage

  nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast aspath allow-my-asn [options] [<attribute> ...]

### Description

  If enabled, it is acceptable for a received AS_PATH to contain the ASN of the local system

### Identifiers

  <vrf-id>       VRF
  <neighbor-id>  Peer ID

### Atrributes

  enable         Turn the feature 'on' or 'off'. The default is 'off'.
  occurrences    Indicates max number of occurrences of the local system's AS
                 number in the received AS_PATH
  origin         If on, a received AS_PATH containing the ASN of the local
                 system is allowed, but only if it is the originating AS

## nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast aspath allow-my-asn enable

### Usage

  nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast aspath allow-my-asn enable [options]

### Description

  Turn the feature 'on' or 'off'.  The default is 'off'.

### Identifiers

  <vrf-id>       VRF
  <neighbor-id>  Peer ID

## nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast aspath allow-my-asn origin

### Usage

  nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast aspath allow-my-asn origin [options]

### Description

  If on, a received AS_PATH containing the ASN of the local system is allowed, but only if it is the originating AS

### Identifiers

  <vrf-id>       VRF
  <neighbor-id>  Peer ID

## nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast aspath allow-my-asn occurrences

### Usage

  nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast aspath allow-my-asn occurrences [options]

### Description

  Indicates max number of occurrences of the local system's AS number in the received AS_PATH

### Identifiers

  <vrf-id>       VRF
  <neighbor-id>  Peer ID

## nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast aspath replace-peer-as

### Usage

  nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast aspath replace-peer-as [options]

### Description

  If on, if the AS_PATH in an outgoing Update contains the peer's ASN, it is replaced with the local system's ASN

### Identifiers

  <vrf-id>       VRF
  <neighbor-id>  Peer ID

## nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast aspath private-as

### Usage

  nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast aspath private-as [options]

### Description

  If 'none', no specific action is taken.  This is the default.  If set to 'remove', any private ASNs in the Update to the peer are removed.  If set to 'replace' any private ASNs in the Update to the peer are replaced with the ASN of the local system.

### Identifiers

  <vrf-id>       VRF
  <neighbor-id>  Peer ID

## nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast prefix-limits

### Usage

  nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast prefix-limits [options] [<attribute> ...]

### Description

  Limits on prefix from the peer for this address-family

### Identifiers

  <vrf-id>       VRF
  <neighbor-id>  Peer ID

### Atrributes

  inbound        Limits on inbound prefix from the peer for this address-
                 family

## nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast prefix-limits inbound

### Usage

  nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast prefix-limits inbound [options] [<attribute> ...]

### Description

  Limits on inbound prefix from the peer for this address-family

### Identifiers

  <vrf-id>           VRF
  <neighbor-id>      Peer ID

### Atrributes

  maximum            Limit on number of prefixes of specific address-family
                     that can be received from the peer. By default, there is
                     no limit
  reestablish-wait   Specifes the time in seconds to wait before establishing
                     the BGP session again with the peer. Defaults to 'auto',
                     which will use standard BGP timers and processing. This
                     would typically be 2-3 seconds.
  warning-only       If 'on', it means to only generate a warning syslog if
                     the number of received prefixes exceeds the limit, do not
                     bring down the BGP session.
  warning-threshold  Percentage of the maximum at which a warning syslog is
                     generated.

## nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast prefix-limits inbound maximum

### Usage

  nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast prefix-limits inbound maximum [options]

### Description

  Limit on number of prefixes of specific address-family that can be received from the peer.  By default, there is no limit

### Identifiers

  <vrf-id>       VRF
  <neighbor-id>  Peer ID

## nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast prefix-limits inbound warning-threshold

### Usage

  nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast prefix-limits inbound warning-threshold [options]

### Description

  Percentage of the maximum at which a warning syslog is generated.

### Identifiers

  <vrf-id>       VRF
  <neighbor-id>  Peer ID

## nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast prefix-limits inbound warning-only

### Usage

  nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast prefix-limits inbound warning-only [options]

### Description

  If 'on', it means to only generate a warning syslog if the number of received prefixes exceeds the limit, do not bring down the BGP session.

### Identifiers

  <vrf-id>       VRF
  <neighbor-id>  Peer ID

## nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast prefix-limits inbound reestablish-wait

### Usage

  nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast prefix-limits inbound reestablish-wait [options]

### Description

  Specifes the time in seconds to wait before establishing the BGP session again with the peer. Defaults to 'auto', which will use standard BGP timers and processing.  This would typically be 2-3 seconds.

### Identifiers

  <vrf-id>       VRF
  <neighbor-id>  Peer ID

## nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast default-route-origination

### Usage

  nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast default-route-origination [options] [<attribute> ...]

### Description

  Default route origination

### Identifiers

  <vrf-id>       VRF
  <neighbor-id>  Peer ID

### Atrributes

  enable         Turn the feature 'on' or 'off'. The default is 'off'.
  policy         Optional route-map policy to control the conditions under
                 which the default route is originated.

## nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast default-route-origination enable

### Usage

  nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast default-route-origination enable [options]

### Description

  Turn the feature 'on' or 'off'.  The default is 'off'.

### Identifiers

  <vrf-id>       VRF
  <neighbor-id>  Peer ID

## nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast default-route-origination policy

### Usage

  nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast default-route-origination policy [options]

### Description

  Optional route-map policy to control the conditions under which the default route is originated.

### Identifiers

  <vrf-id>       VRF
  <neighbor-id>  Peer ID

## nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast policy

### Usage

  nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast policy [options] [<attribute> ...]

### Description

  Policies for ipv6 unicast

### Identifiers

  <vrf-id>       VRF
  <neighbor-id>  Peer ID

### Atrributes

  inbound        Outbound unicast policy
  outbound       Outbound unicast policy

## nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast policy inbound

### Usage

  nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast policy inbound [options] [<attribute> ...]

### Description

  Outbound unicast policy

### Identifiers

  <vrf-id>       VRF
  <neighbor-id>  Peer ID

### Atrributes

  route-map      Route map to apply to Updates received from this peer
  aspath-list    AS-Path filter list to apply to Updates received from this
                 peer
  prefix-list    Prefix list to apply to Updates received from this peer

## nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast policy inbound route-map

### Usage

  nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast policy inbound route-map [options]

### Description

  Route map to apply to Updates received from this peer

### Identifiers

  <vrf-id>       VRF
  <neighbor-id>  Peer ID

## nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast policy inbound prefix-list

### Usage

  nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast policy inbound prefix-list [options]

### Description

  Prefix list to apply to Updates received from this peer

### Identifiers

  <vrf-id>       VRF
  <neighbor-id>  Peer ID

## nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast policy inbound aspath-list

### Usage

  nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast policy inbound aspath-list [options]

### Description

  AS-Path filter list to apply to Updates received from this peer

### Identifiers

  <vrf-id>       VRF
  <neighbor-id>  Peer ID

## nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast policy outbound

### Usage

  nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast policy outbound [options] [<attribute> ...]

### Description

  Outbound unicast policy

### Identifiers

  <vrf-id>        VRF
  <neighbor-id>   Peer ID

### Atrributes

  route-map       Route map to apply to Updates to be sent to this peer
  unsuppress-map  Route map used to unsuppress routes selectively when
                  advertising to this peer; these are routes that have been
                  suppressed due to aggregation configuration.
  aspath-list     AS-Path filter list to apply to Updates sent to this peer
  prefix-list     Prefix list to apply to Updates to be sent to this peer

## nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast policy outbound route-map

### Usage

  nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast policy outbound route-map [options]

### Description

  Route map to apply to Updates to be sent to this peer

### Identifiers

  <vrf-id>       VRF
  <neighbor-id>  Peer ID

## nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast policy outbound unsuppress-map

### Usage

  nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast policy outbound unsuppress-map [options]

### Description

  Route map used to unsuppress routes selectively when advertising to this peer; these are routes that have been suppressed due to aggregation configuration.

### Identifiers

  <vrf-id>       VRF
  <neighbor-id>  Peer ID

## nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast policy outbound prefix-list

### Usage

  nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast policy outbound prefix-list [options]

### Description

  Prefix list to apply to Updates to be sent to this peer

### Identifiers

  <vrf-id>       VRF
  <neighbor-id>  Peer ID

## nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast policy outbound aspath-list

### Usage

  nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast policy outbound aspath-list [options]

### Description

  AS-Path filter list to apply to Updates sent to this peer

### Identifiers

  <vrf-id>       VRF
  <neighbor-id>  Peer ID

## nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast community-advertise

### Usage

  nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast community-advertise [options] [<attribute> ...]

### Description

  Community advertise for address family.

### Identifiers

  <vrf-id>       VRF
  <neighbor-id>  Peer ID

### Atrributes

  extended       If 'on', it means we can announce the EXT_COMMUNITIES
                 attribute to this peer, otherwise we cannot.
  large          If 'on', it means we can announce the LARGE_COMMUNITIES
                 attribute to this peer, otherwise we cannot.
  regular        If 'on', it means we can announce the COMMUNITIES attribute
                 to this peer, otherwise we cannot.

## nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast community-advertise regular

### Usage

  nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast community-advertise regular [options]

### Description

  If 'on', it means we can announce the COMMUNITIES attribute to this peer, otherwise we cannot.

### Identifiers

  <vrf-id>       VRF
  <neighbor-id>  Peer ID

## nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast community-advertise extended

### Usage

  nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast community-advertise extended [options]

### Description

  If 'on', it means we can announce the EXT_COMMUNITIES attribute to this peer, otherwise we cannot.

### Identifiers

  <vrf-id>       VRF
  <neighbor-id>  Peer ID

## nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast community-advertise large

### Usage

  nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast community-advertise large [options]

### Description

  If 'on', it means we can announce the LARGE_COMMUNITIES attribute to this peer, otherwise we cannot.

### Identifiers

  <vrf-id>       VRF
  <neighbor-id>  Peer ID

## nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast conditional-advertise

### Usage

  nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast conditional-advertise [options] [<attribute> ...]

### Description

  Conditional advertise for address family.

### Identifiers

  <vrf-id>       VRF
  <neighbor-id>  Peer ID

### Atrributes

  enable         Turn the feature 'on' or 'off'. The default is 'off'.
  advertise-map  route-map contains prefix-list which has list of
                 routes/prefixes to operate on.
  exist-map      route-map contains the conditional routes/prefixes in prefix-
                 list.
  non-exist-map  route-map contains the negative conditional routes/prefixes
                 in prefix-list.

## nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast conditional-advertise enable

### Usage

  nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast conditional-advertise enable [options]

### Description

  Turn the feature 'on' or 'off'.  The default is 'off'.

### Identifiers

  <vrf-id>       VRF
  <neighbor-id>  Peer ID

## nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast conditional-advertise advertise-map

### Usage

  nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast conditional-advertise advertise-map [options]

### Description

  route-map contains prefix-list which has list of routes/prefixes to operate on.

### Identifiers

  <vrf-id>       VRF
  <neighbor-id>  Peer ID

## nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast conditional-advertise exist-map

### Usage

  nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast conditional-advertise exist-map [options]

### Description

  route-map contains the conditional routes/prefixes in prefix-list.

### Identifiers

  <vrf-id>       VRF
  <neighbor-id>  Peer ID

## nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast conditional-advertise non-exist-map

### Usage

  nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast conditional-advertise non-exist-map [options]

### Description

  route-map contains the negative conditional routes/prefixes in prefix-list.

### Identifiers

  <vrf-id>       VRF
  <neighbor-id>  Peer ID

## nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast enable

### Usage

  nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast enable [options]

### Description

  Turn the feature 'on' or 'off'.  The default is 'off'.

### Identifiers

  <vrf-id>       VRF
  <neighbor-id>  Peer ID

## nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast route-reflector-client

### Usage

  nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast route-reflector-client [options]

### Description

  Specifies if this peer is a client and we are its route reflector

### Identifiers

  <vrf-id>       VRF
  <neighbor-id>  Peer ID

## nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast route-server-client

### Usage

  nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast route-server-client [options]

### Description

  Specifies if this peer is a client and we are its route server

### Identifiers

  <vrf-id>       VRF
  <neighbor-id>  Peer ID

## nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast soft-reconfiguration

### Usage

  nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast soft-reconfiguration [options]

### Description

  If 'on', it means that received routes from this peer that are rejected by inbound policy are still stored. This allows policy changes to take effect without any exchange of BGP Updates.

### Identifiers

  <vrf-id>       VRF
  <neighbor-id>  Peer ID

## nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast nexthop-setting

### Usage

  nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast nexthop-setting [options]

### Description

  Control nexthop value of advertised routes.  "auto" follows regular BGP next-hop determination rules.  This is the default.  "self" sets the next hop to ourselves for route advertisement, except for reflected routes.  "force" sets the next hop to ourselves for route advertisement including for reflected routes.

### Identifiers

  <vrf-id>       VRF
  <neighbor-id>  Peer ID

## nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast add-path-tx

### Usage

  nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast add-path-tx [options]

### Description

  Used to enable transmission of additional paths; by default, only the best path is announced to peers

### Identifiers

  <vrf-id>       VRF
  <neighbor-id>  Peer ID

## nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast weight

### Usage

  nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast weight [options]

### Description

  Weight applied to routes received from peer; this is used in the BGP route selection algorithm

### Identifiers

  <vrf-id>       VRF
  <neighbor-id>  Peer ID

## nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family l2vpn-evpn

### Usage

  nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family l2vpn-evpn [options] [<attribute> ...]

### Description

  Peer l2vpn EVPN address family.

### Identifiers

  <vrf-id>              VRF
  <neighbor-id>         Peer ID

### Atrributes

  attribute-mod         Attribute mod for address family.
  aspath                Options for handling AS_PATH for prefixes from/to peer
                        for the specified address family
  policy                Policies for l2vpn evpn
  enable                Turn the feature 'on' or 'off'. The default is 'off'.
  add-path-tx           Used to enable transmission of additional paths; by
                        default, only the best path is announced to peers
  nexthop-setting       Control nexthop value of advertised routes. "auto"
                        follows regular BGP next-hop determination rules. This
                        is the default. "self" sets the next hop to ourselves
                        for route advertisement, except for reflected routes.
                        "force" sets the next hop to ourselves for route
                        advertisement including for reflected routes.
  route-reflector-client
                        Specifies if this peer is a client and we are its
                        route reflector
  route-server-client   Specifies if this peer is a client and we are its
                        route server
  soft-reconfiguration  If 'on', it means that received routes from this peer
                        that are rejected by inbound policy are still stored.
                        This allows policy changes to take effect without any
                        exchange of BGP Updates.

## nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family l2vpn-evpn attribute-mod

### Usage

  nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family l2vpn-evpn attribute-mod [options] [<attribute> ...]

### Description

  Attribute mod for address family.

### Identifiers

  <vrf-id>       VRF
  <neighbor-id>  Peer ID

### Atrributes

  aspath         If 'on', it means follow normal BGP procedures in the
                 generation of AS_PATH attribute for this peer; if 'off' it
                 means do not change the AS_PATH when sending an Update to
                 this peer.
  med            If 'on', it means follow normal BGP procedures in the
                 generation of MED attribute for this peer; if 'off' it means
                 do not change the MED when sending an Update to this peer.
  nexthop        If 'on', it means follow normal BGP procedures in the
                 generation of NEXT_HOP attribute for this peer; if 'off' it
                 means do not change the NEXT_HOP when sending an Update to
                 this peer.

## nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family l2vpn-evpn attribute-mod aspath

### Usage

  nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family l2vpn-evpn attribute-mod aspath [options]

### Description

  If 'on', it means follow normal BGP procedures in the generation of AS_PATH attribute for this peer; if 'off' it means do not change the AS_PATH when sending an Update to this peer.

### Identifiers

  <vrf-id>       VRF
  <neighbor-id>  Peer ID

## nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family l2vpn-evpn attribute-mod med

### Usage

  nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family l2vpn-evpn attribute-mod med [options]

### Description

  If 'on', it means follow normal BGP procedures in the generation of MED attribute for this peer; if 'off' it means do not change the MED when sending an Update to this peer.

### Identifiers

  <vrf-id>       VRF
  <neighbor-id>  Peer ID

## nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family l2vpn-evpn attribute-mod nexthop

### Usage

  nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family l2vpn-evpn attribute-mod nexthop [options]

### Description

  If 'on', it means follow normal BGP procedures in the generation of NEXT_HOP attribute for this peer; if 'off' it means do not change the NEXT_HOP when sending an Update to this peer.

### Identifiers

  <vrf-id>       VRF
  <neighbor-id>  Peer ID

## nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family l2vpn-evpn aspath

### Usage

  nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family l2vpn-evpn aspath [options] [<attribute> ...]

### Description

  Options for handling AS_PATH for prefixes from/to peer for the specified address family

### Identifiers

  <vrf-id>         VRF
  <neighbor-id>    Peer ID

### Atrributes

  allow-my-asn     If enabled, it is acceptable for a received AS_PATH to
                   contain the ASN of the local system
  private-as       If 'none', no specific action is taken. This is the
                   default. If set to 'remove', any private ASNs in the Update
                   to the peer are removed. If set to 'replace' any private
                   ASNs in the Update to the peer are replaced with the ASN of
                   the local system.
  replace-peer-as  If on, if the AS_PATH in an outgoing Update contains the
                   peer's ASN, it is replaced with the local system's ASN

## nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family l2vpn-evpn aspath allow-my-asn

### Usage

  nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family l2vpn-evpn aspath allow-my-asn [options] [<attribute> ...]

### Description

  If enabled, it is acceptable for a received AS_PATH to contain the ASN of the local system

### Identifiers

  <vrf-id>       VRF
  <neighbor-id>  Peer ID

### Atrributes

  enable         Turn the feature 'on' or 'off'. The default is 'off'.
  occurrences    Indicates max number of occurrences of the local system's AS
                 number in the received AS_PATH
  origin         If on, a received AS_PATH containing the ASN of the local
                 system is allowed, but only if it is the originating AS

## nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family l2vpn-evpn aspath allow-my-asn enable

### Usage

  nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family l2vpn-evpn aspath allow-my-asn enable [options]

### Description

  Turn the feature 'on' or 'off'.  The default is 'off'.

### Identifiers

  <vrf-id>       VRF
  <neighbor-id>  Peer ID

## nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family l2vpn-evpn aspath allow-my-asn origin

### Usage

  nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family l2vpn-evpn aspath allow-my-asn origin [options]

### Description

  If on, a received AS_PATH containing the ASN of the local system is allowed, but only if it is the originating AS

### Identifiers

  <vrf-id>       VRF
  <neighbor-id>  Peer ID

## nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family l2vpn-evpn aspath allow-my-asn occurrences

### Usage

  nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family l2vpn-evpn aspath allow-my-asn occurrences [options]

### Description

  Indicates max number of occurrences of the local system's AS number in the received AS_PATH

### Identifiers

  <vrf-id>       VRF
  <neighbor-id>  Peer ID

## nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family l2vpn-evpn aspath replace-peer-as

### Usage

  nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family l2vpn-evpn aspath replace-peer-as [options]

### Description

  If on, if the AS_PATH in an outgoing Update contains the peer's ASN, it is replaced with the local system's ASN

### Identifiers

  <vrf-id>       VRF
  <neighbor-id>  Peer ID

## nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family l2vpn-evpn aspath private-as

### Usage

  nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family l2vpn-evpn aspath private-as [options]

### Description

  If 'none', no specific action is taken.  This is the default.  If set to 'remove', any private ASNs in the Update to the peer are removed.  If set to 'replace' any private ASNs in the Update to the peer are replaced with the ASN of the local system.

### Identifiers

  <vrf-id>       VRF
  <neighbor-id>  Peer ID

## nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family l2vpn-evpn policy

### Usage

  nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family l2vpn-evpn policy [options] [<attribute> ...]

### Description

  Policies for l2vpn evpn

### Identifiers

  <vrf-id>       VRF
  <neighbor-id>  Peer ID

### Atrributes

  inbound        Inbound l2vpn-evpn policy
  outbound       Outbound l2vpn-evpn policy

## nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family l2vpn-evpn policy inbound

### Usage

  nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family l2vpn-evpn policy inbound [options] [<attribute> ...]

### Description

  Inbound l2vpn-evpn policy

### Identifiers

  <vrf-id>       VRF
  <neighbor-id>  Peer ID

### Atrributes

  route-map      Route map to apply to Updates received from this peer

## nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family l2vpn-evpn policy inbound route-map

### Usage

  nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family l2vpn-evpn policy inbound route-map [options]

### Description

  Route map to apply to Updates received from this peer

### Identifiers

  <vrf-id>       VRF
  <neighbor-id>  Peer ID

## nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family l2vpn-evpn policy outbound

### Usage

  nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family l2vpn-evpn policy outbound [options] [<attribute> ...]

### Description

  Outbound l2vpn-evpn policy

### Identifiers

  <vrf-id>        VRF
  <neighbor-id>   Peer ID

### Atrributes

  route-map       Route map to apply to Updates to be sent to this peer
  unsuppress-map  Route map used to unsuppress routes selectively when
                  advertising to this peer; these are routes that have been
                  suppressed due to aggregation configuration.

## nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family l2vpn-evpn policy outbound route-map

### Usage

  nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family l2vpn-evpn policy outbound route-map [options]

### Description

  Route map to apply to Updates to be sent to this peer

### Identifiers

  <vrf-id>       VRF
  <neighbor-id>  Peer ID

## nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family l2vpn-evpn policy outbound unsuppress-map

### Usage

  nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family l2vpn-evpn policy outbound unsuppress-map [options]

### Description

  Route map used to unsuppress routes selectively when advertising to this peer; these are routes that have been suppressed due to aggregation configuration.

### Identifiers

  <vrf-id>       VRF
  <neighbor-id>  Peer ID

## nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family l2vpn-evpn enable

### Usage

  nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family l2vpn-evpn enable [options]

### Description

  Turn the feature 'on' or 'off'.  The default is 'off'.

### Identifiers

  <vrf-id>       VRF
  <neighbor-id>  Peer ID

## nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family l2vpn-evpn route-reflector-client

### Usage

  nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family l2vpn-evpn route-reflector-client [options]

### Description

  Specifies if this peer is a client and we are its route reflector

### Identifiers

  <vrf-id>       VRF
  <neighbor-id>  Peer ID

## nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family l2vpn-evpn route-server-client

### Usage

  nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family l2vpn-evpn route-server-client [options]

### Description

  Specifies if this peer is a client and we are its route server

### Identifiers

  <vrf-id>       VRF
  <neighbor-id>  Peer ID

## nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family l2vpn-evpn soft-reconfiguration

### Usage

  nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family l2vpn-evpn soft-reconfiguration [options]

### Description

  If 'on', it means that received routes from this peer that are rejected by inbound policy are still stored. This allows policy changes to take effect without any exchange of BGP Updates.

### Identifiers

  <vrf-id>       VRF
  <neighbor-id>  Peer ID

## nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family l2vpn-evpn nexthop-setting

### Usage

  nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family l2vpn-evpn nexthop-setting [options]

### Description

  Control nexthop value of advertised routes.  "auto" follows regular BGP next-hop determination rules.  This is the default.  "self" sets the next hop to ourselves for route advertisement, except for reflected routes.  "force" sets the next hop to ourselves for route advertisement including for reflected routes.

### Identifiers

  <vrf-id>       VRF
  <neighbor-id>  Peer ID

## nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family l2vpn-evpn add-path-tx

### Usage

  nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> address-family l2vpn-evpn add-path-tx [options]

### Description

  Used to enable transmission of additional paths; by default, only the best path is announced to peers

### Identifiers

  <vrf-id>       VRF
  <neighbor-id>  Peer ID

## nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> timers

### Usage

  nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> timers [options] [<attribute> ...]

### Description

  Peer peer-timerss

### Identifiers

  <vrf-id>             VRF
  <neighbor-id>        Peer ID

### Atrributes

  connection-retry     Time interval at which connection attempts are retried
                       upon a failure. If `auto`, the global value is used.
                       This is the default.
  hold                 Hold timer. If `none`, keepalives from the peer are not
                       tracked and the peering session will not experience a
                       hold timeout. If `auto`, the global value is used. This
                       is the default.
  keepalive            Keepalive timer. If `none`, keepalives are not sent. If
                       `auto`, the global value is used. This is the default.
  route-advertisement  Time between route advertisements (BGP Updates). A non-
                       zero value allows route advertisements to be delayed
                       and batched. If `auto`, the global value is used. This
                       is the default.

## nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> timers keepalive

### Usage

  nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> timers keepalive [options]

### Description

  Keepalive timer.  If `none`, keepalives are not sent.  If `auto`, the global value is used.  This is the default.

### Identifiers

  <vrf-id>       VRF
  <neighbor-id>  Peer ID

## nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> timers hold

### Usage

  nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> timers hold [options]

### Description

  Hold timer.  If `none`, keepalives from the peer are not tracked and the peering session will not experience a hold timeout.  If `auto`, the global value is used.  This is the default.

### Identifiers

  <vrf-id>       VRF
  <neighbor-id>  Peer ID

## nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> timers connection-retry

### Usage

  nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> timers connection-retry [options]

### Description

  Time interval at which connection attempts are retried upon a failure.  If `auto`, the global value is used.  This is the default.

### Identifiers

  <vrf-id>       VRF
  <neighbor-id>  Peer ID

## nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> timers route-advertisement

### Usage

  nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> timers route-advertisement [options]

### Description

  Time between route advertisements (BGP Updates).  A non-zero value allows route advertisements to be delayed and batched.  If `auto`, the global value is used.  This is the default.

### Identifiers

  <vrf-id>       VRF
  <neighbor-id>  Peer ID

## nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> password

### Usage

  nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> password [options]

### Description

  Password

### Identifiers

  <vrf-id>       VRF
  <neighbor-id>  Peer ID

## nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> enforce-first-as

### Usage

  nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> enforce-first-as [options]

### Description

  If on, when BGP updates are received from EBGP peers with this config, check that first AS matches peer's AS

### Identifiers

  <vrf-id>       VRF
  <neighbor-id>  Peer ID

## nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> passive-mode

### Usage

  nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> passive-mode [options]

### Description

  If enabled, do not initiate the BGP connection but wait for incoming connection

### Identifiers

  <vrf-id>       VRF
  <neighbor-id>  Peer ID

## nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> nexthop-connected-check

### Usage

  nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> nexthop-connected-check [options]

### Description

  If 'on', it disables the check that a non-multihop EBGP peer should be directly connected and only announce connected next hops

### Identifiers

  <vrf-id>       VRF
  <neighbor-id>  Peer ID

## nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> multihop-ttl

### Usage

  nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> multihop-ttl [options]

### Description

  Maximum hops allowed.  When 'auto', the type of peer will determine the appropriate value (255 for iBGP and 1 for eBGP).  This is the default.

### Identifiers

  <vrf-id>       VRF
  <neighbor-id>  Peer ID

## nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> description

### Usage

  nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> description [options]

### Description

  neighbor description

### Identifiers

  <vrf-id>       VRF
  <neighbor-id>  Peer ID

## nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> enable

### Usage

  nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> enable [options]

### Description

  Turn the feature 'on' or 'off'.  The default is 'on'.

### Identifiers

  <vrf-id>       VRF
  <neighbor-id>  Peer ID

## nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> type

### Usage

  nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> type [options]

### Description

  The type of peer

### Identifiers

  <vrf-id>       VRF
  <neighbor-id>  Peer ID

## nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> peer-group

### Usage

  nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> peer-group [options]

### Description

  Optional peer-group to which the peer is attached to inherit the group's configuration.

### Identifiers

  <vrf-id>       VRF
  <neighbor-id>  Peer ID

## nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> remote-as

### Usage

  nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> remote-as [options]

### Description

  ASN for the BGP neighbor(s) using this configuration.  If specified as 'external', it means an EBGP configuration but the actual ASN is immaterial. If specified as 'internal', it means an IBGP configuration.

### Identifiers

  <vrf-id>       VRF
  <neighbor-id>  Peer ID

## nv unset vrf <vrf-id> router bgp enable

### Usage

  nv unset vrf <vrf-id> router bgp enable [options]

### Description

  Turn the feature 'on' or 'off'.  The default is 'off'.

### Identifiers

  <vrf-id>    VRF

## nv unset vrf <vrf-id> router bgp autonomous-system

### Usage

  nv unset vrf <vrf-id> router bgp autonomous-system [options]

### Description

  ASN for this VRF.  If "auto", inherit from the global config.  This is the default.

### Identifiers

  <vrf-id>    VRF## nv unset vrf <vrf-id> router bgp router-id

### Usage

  nv unset vrf <vrf-id> router bgp router-id [options]

### Description

  BGP router-id for this VRF.  If "auto", inherit from the global config.  This is the default.

### Identifiers

  <vrf-id>    VRF

## nv unset vrf <vrf-id> router bgp rd

### Usage

  nv unset vrf <vrf-id> router bgp rd [options]

### Description

  BGP Route Distinguisher to use when this VRF routes have to be exported.

### Identifiers

  <vrf-id>    VRF## nv unset vrf <vrf-id> router bgp dynamic-peer-limit

### Usage

  nv unset vrf <vrf-id> router bgp dynamic-peer-limit [options]

### Description

  Maximum number of dynamic neighbors from whom we can accept a connection. Applicable only if 'dynamic-peering' subnet ranges are configured

### Identifiers

  <vrf-id>    VRF## nv unset vrf <vrf-id> router static <route-id>

### Usage

  nv unset vrf <vrf-id> router static <route-id> [options] [<attribute> ...]

### Description

  A route

### Identifiers

  <vrf-id>        VRF
  <route-id>      IP prefix

### Atrributes

  distance        Paths
  via             Nexthops
  tag             Path tag
  address-family  Route address family

## nv unset vrf <vrf-id> router static <route-id> distance <distance-id>

### Usage

  nv unset vrf <vrf-id> router static <route-id> distance <distance-id> [options] [<attribute> ...]

### Description

  A path

### Identifiers

  <vrf-id>       VRF
  <route-id>     IP prefix
  <distance-id>  A path distance

### Atrributes

  via            Nexthops
  tag            Path tag

## nv unset vrf <vrf-id> router static <route-id> distance <distance-id> via <via-id>

### Usage

  nv unset vrf <vrf-id> router static <route-id> distance <distance-id> via <via-id> [options] [<attribute> ...]

### Description

  A via

### Identifiers

  <vrf-id>       VRF
  <route-id>     IP prefix
  <distance-id>  A path distance
  <via-id>       IP address, interface, or "blackhole".

### Atrributes

  flag           Nexthop flags
  interface      The interface to use for egress. If not specified, it will
                 automatically be determined. Only valid when the via's type
                 is ipv4-address or ipv6-address.
  vrf            The VRF to use for egress. If not specified, the route's VRF
                 will be used. Only valid when the via's type is ipv4-address
                 or ipv6-address.
  type           The type of via

## nv unset vrf <vrf-id> router static <route-id> distance <distance-id> via <via-id> flag

### Usage

  nv unset vrf <vrf-id> router static <route-id> distance <distance-id> via <via-id> flag [options]

### Description

  Nexthop flags

### Identifiers

  <vrf-id>       VRF
  <route-id>     IP prefix
  <distance-id>  A path distance
  <via-id>       IP address, interface, or "blackhole".

## nv unset vrf <vrf-id> router static <route-id> distance <distance-id> via <via-id> interface

### Usage

  nv unset vrf <vrf-id> router static <route-id> distance <distance-id> via <via-id> interface [options]

### Description

  The interface to use for egress.  If not specified, it will automatically be determined.  Only valid when the via's type is ipv4-address or ipv6-address.

### Identifiers

  <vrf-id>       VRF
  <route-id>     IP prefix
  <distance-id>  A path distance
  <via-id>       IP address, interface, or "blackhole".

## nv unset vrf <vrf-id> router static <route-id> distance <distance-id> via <via-id> vrf

### Usage

  nv unset vrf <vrf-id> router static <route-id> distance <distance-id> via <via-id> vrf [options]

### Description

  The VRF to use for egress.  If not specified, the route's VRF will be used.  Only valid when the via's type is ipv4-address or ipv6-address.

### Identifiers

  <vrf-id>       VRF
  <route-id>     IP prefix
  <distance-id>  A path distance
  <via-id>       IP address, interface, or "blackhole".

## nv unset vrf <vrf-id> router static <route-id> distance <distance-id> via <via-id> type

### Usage

  nv unset vrf <vrf-id> router static <route-id> distance <distance-id> via <via-id> type [options]

### Description

  The type of via

### Identifiers

  <vrf-id>       VRF
  <route-id>     IP prefix
  <distance-id>  A path distance
  <via-id>       IP address, interface, or "blackhole".

## nv unset vrf <vrf-id> router static <route-id> distance <distance-id> tag

### Usage

  nv unset vrf <vrf-id> router static <route-id> distance <distance-id> tag [options]

### Description

  Path tag

### Identifiers

  <vrf-id>       VRF
  <route-id>     IP prefix
  <distance-id>  A path distance

## nv unset vrf <vrf-id> router static <route-id> via <via-id>

### Usage

  nv unset vrf <vrf-id> router static <route-id> via <via-id> [options] [<attribute> ...]

### Description

  A via

### Identifiers

  <vrf-id>    VRF
  <route-id>  IP prefix
  <via-id>    IP address, interface, or "blackhole".

### Atrributes

  flag        Nexthop flags
  interface   The interface to use for egress. If not specified, it will
              automatically be determined. Only valid when the via's type is
              ipv4-address or ipv6-address.
  vrf         The VRF to use for egress. If not specified, the route's VRF
              will be used. Only valid when the via's type is ipv4-address or
              ipv6-address.
  type        The type of via



## nv unset vrf <vrf-id> router static <route-id> via <via-id> flag

### Usage

  nv unset vrf <vrf-id> router static <route-id> via <via-id> flag [options]

### Description

  Nexthop flags

### Identifiers

  <vrf-id>    VRF
  <route-id>  IP prefix
  <via-id>    IP address, interface, or "blackhole".



## nv unset vrf <vrf-id> router static <route-id> via <via-id> interface

### Usage

  nv unset vrf <vrf-id> router static <route-id> via <via-id> interface [options]

### Description

  The interface to use for egress.  If not specified, it will automatically be determined.  Only valid when the via's type is ipv4-address or ipv6-address.

### Identifiers

  <vrf-id>    VRF
  <route-id>  IP prefix
  <via-id>    IP address, interface, or "blackhole".



## nv unset vrf <vrf-id> router static <route-id> via <via-id> vrf

### Usage

  nv unset vrf <vrf-id> router static <route-id> via <via-id> vrf [options]

### Description

  The VRF to use for egress.  If not specified, the route's VRF will be used.  Only valid when the via's type is ipv4-address or ipv6-address.

### Identifiers

  <vrf-id>    VRF
  <route-id>  IP prefix
  <via-id>    IP address, interface, or "blackhole".



## nv unset vrf <vrf-id> router static <route-id> via <via-id> type

### Usage

  nv unset vrf <vrf-id> router static <route-id> via <via-id> type [options]

### Description

  The type of via

### Identifiers

  <vrf-id>    VRF
  <route-id>  IP prefix
  <via-id>    IP address, interface, or "blackhole".



## nv unset vrf <vrf-id> router static <route-id> tag

### Usage

  nv unset vrf <vrf-id> router static <route-id> tag [options]

### Description

  Path tag

### Identifiers

  <vrf-id>    VRF
  <route-id>  IP prefix



## nv unset vrf <vrf-id> router static <route-id> address-family

### Usage

  nv unset vrf <vrf-id> router static <route-id> address-family [options]

### Description

  Route address family

### Identifiers

  <vrf-id>    VRF
  <route-id>  IP prefix



## nv unset vrf <vrf-id> router pim

### Usage

  nv unset vrf <vrf-id> router pim [options] [<attribute> ...]

### Description

  PIM VRF configuration.

### Identifiers

  <vrf-id>         VRF

### Atrributes

  timers           Timers
  ecmp             Choose all available ECMP paths for a particular RPF. If
                   'off', the first nexthop found will be used. This is the
                   default.
  msdp-mesh-group  To connect multiple PIM-SM multicast domains using RPs.
  address-family   Address family specific configuration
  enable           Turn the feature 'on' or 'off'. The default is 'off'.

## nv unset vrf <vrf-id> router pim timers

### Usage

  nv unset vrf <vrf-id> router pim timers [options] [<attribute> ...]

### Description

  Timers

### Identifiers

  <vrf-id>       VRF

### Atrributes

  keep-alive     Timeout value for S,G stream, in seconds
  rp-keep-alive  RP's timeout value, in seconds

## nv unset vrf <vrf-id> router pim timers keep-alive

### Usage

  nv unset vrf <vrf-id> router pim timers keep-alive [options]

### Description

  Timeout value for S,G stream, in seconds

### Identifiers

  <vrf-id>    VRF

## nv unset vrf <vrf-id> router pim timers rp-keep-alive

### Usage

  nv unset vrf <vrf-id> router pim timers rp-keep-alive [options]

### Description

  RP's timeout value, in seconds

### Identifiers

  <vrf-id>    VRF

## nv unset vrf <vrf-id> router pim ecmp

### Usage

  nv unset vrf <vrf-id> router pim ecmp [options] [<attribute> ...]

### Description

  Choose all available ECMP paths for a particular RPF.  If 'off', the first nexthop found will be used.  This is the default.

### Identifiers

  <vrf-id>    VRF### Atrributes

  enable      Turn the feature 'on' or 'off'. The default is 'off'.
  rebalance   Recalculate all multicast streams in the event of path going
              down. If 'off', only the impacted streams by path going down
              recalculated. This is the default.



## nv unset vrf <vrf-id> router pim ecmp enable

### Usage

  nv unset vrf <vrf-id> router pim ecmp enable [options]

### Description

  Turn the feature 'on' or 'off'.  The default is 'off'.

### Identifiers

  <vrf-id>    VRF

## nv unset vrf <vrf-id> router pim ecmp rebalance

### Usage

  nv unset vrf <vrf-id> router pim ecmp rebalance [options]

### Description

  Recalculate all multicast streams in the event of path going down. If 'off', only the impacted streams by path going down recalculated.  This is the default.

### Identifiers

  <vrf-id>    VRF

## nv unset vrf <vrf-id> router pim msdp-mesh-group <msdp-mesh-group-id>

### Usage

  nv unset vrf <vrf-id> router pim msdp-mesh-group <msdp-mesh-group-id> [options] [<attribute> ...]

### Description

  MSDP mesh-group

### Identifiers

  <vrf-id>              VRF
  <msdp-mesh-group-id>  MSDP mesh group name

### Atrributes

  member-address        Set of member-address
  source-address        MSDP mesh-group source IP address

## nv unset vrf <vrf-id> router pim msdp-mesh-group <msdp-mesh-group-id> member-address <mesh-member-id>

### Usage

  nv unset vrf <vrf-id> router pim msdp-mesh-group <msdp-mesh-group-id> member-address <mesh-member-id> [options]

### Description

  A MSDP mesh member

### Identifiers

  <vrf-id>              VRF
  <msdp-mesh-group-id>  MSDP mesh group name
  <mesh-member-id>      MSDP mesh-group member IP address

## nv unset vrf <vrf-id> router pim msdp-mesh-group <msdp-mesh-group-id> source-address

### Usage

  nv unset vrf <vrf-id> router pim msdp-mesh-group <msdp-mesh-group-id> source-address [options]

### Description

  MSDP mesh-group source IP address

### Identifiers

  <vrf-id>              VRF
  <msdp-mesh-group-id>  MSDP mesh group name

## nv unset vrf <vrf-id> router pim address-family

### Usage

  nv unset vrf <vrf-id> router pim address-family [options] [<attribute> ...]

### Description

  Address family specific configuration

### Identifiers

  <vrf-id>      VRF

### Atrributes

  ipv4-unicast  IPv4 unicast address family

## nv unset vrf <vrf-id> router pim address-family ipv4-unicast

### Usage

  nv unset vrf <vrf-id> router pim address-family ipv4-unicast [options] [<attribute> ...]

### Description

  IPv4 unicast address family

### Identifiers

  <vrf-id>              VRF

### Atrributes

  spt-switchover        Build shortest path tree towards source.
  rp                    RP address and associated group range.
  register-accept-list  Prefix-list to specifiy source list to accept register
                        message.
  send-v6-secondary     Use IPv6 secondary address to transmit PIM Hello
                        packets. It allows to use IPv6 nexthop in RPF lookup.
  ssm-prefix-list       Prefix-list to specificy Source Specific Multicast
                        Group range.

## nv unset vrf <vrf-id> router pim address-family ipv4-unicast spt-switchover

### Usage

  nv unset vrf <vrf-id> router pim address-family ipv4-unicast spt-switchover [options] [<attribute> ...]

### Description

  Build shortest path tree towards source.

### Identifiers

  <vrf-id>     VRF

### Atrributes

  action       PIM shortest path switchover (SPT) action.
  prefix-list  Prefix-list to specify multicast group range.

## nv unset vrf <vrf-id> router pim address-family ipv4-unicast spt-switchover action

### Usage

  nv unset vrf <vrf-id> router pim address-family ipv4-unicast spt-switchover action [options]

### Description

  PIM shortest path switchover (SPT) action.

### Identifiers

  <vrf-id>    VRF

## nv unset vrf <vrf-id> router pim address-family ipv4-unicast spt-switchover prefix-list

### Usage

  nv unset vrf <vrf-id> router pim address-family ipv4-unicast spt-switchover prefix-list [options]

### Description

  Prefix-list to specify multicast group range.

### Identifiers

  <vrf-id>    VRF

## nv unset vrf <vrf-id> router pim address-family ipv4-unicast rp <rp-id>

### Usage

  nv unset vrf <vrf-id> router pim address-family ipv4-unicast rp <rp-id> [options] [<attribute> ...]

### Description

  RP

### Identifiers

  <vrf-id>     VRF
  <rp-id>      RP IP address

### Atrributes

  group-range  Set of group range assocaited to RP.
  prefix-list  Prefix-list to specify multicast group range.

## nv unset vrf <vrf-id> router pim address-family ipv4-unicast rp <rp-id> group-range <group-range-id>

### Usage

  nv unset vrf <vrf-id> router pim address-family ipv4-unicast rp <rp-id> group-range <group-range-id> [options]

### Description

  A group range

### Identifiers

  <vrf-id>          VRF
  <rp-id>           RP IP address
  <group-range-id>  Group range associated to RP.

## nv unset vrf <vrf-id> router pim address-family ipv4-unicast rp <rp-id> prefix-list

### Usage

  nv unset vrf <vrf-id> router pim address-family ipv4-unicast rp <rp-id> prefix-list [options]

### Description

  Prefix-list to specify multicast group range.

### Identifiers

  <vrf-id>    VRF
  <rp-id>     RP IP address



## nv unset vrf <vrf-id> router pim address-family ipv4-unicast ssm-prefix-list

### Usage

  nv unset vrf <vrf-id> router pim address-family ipv4-unicast ssm-prefix-list [options]

### Description

  Prefix-list to specificy Source Specific Multicast Group range.

### Identifiers

  <vrf-id>    VRF

## nv unset vrf <vrf-id> router pim address-family ipv4-unicast register-accept-list

### Usage

  nv unset vrf <vrf-id> router pim address-family ipv4-unicast register-accept-list [options]

### Description

  Prefix-list to specifiy source list to accept register message.

### Identifiers

  <vrf-id>    VRF

## nv unset vrf <vrf-id> router pim address-family ipv4-unicast send-v6-secondary

### Usage

  nv unset vrf <vrf-id> router pim address-family ipv4-unicast send-v6-secondary [options]

### Description

  Use IPv6 secondary address to transmit PIM Hello packets. It allows to use IPv6 nexthop in RPF lookup.

### Identifiers

  <vrf-id>    VRF

## nv unset vrf <vrf-id> router pim enable

### Usage

  nv unset vrf <vrf-id> router pim enable [options]

### Description

  Turn the feature 'on' or 'off'.  The default is 'off'.

### Identifiers

  <vrf-id>    VRF

## nv unset vrf <vrf-id> router ospf

### Usage

  nv unset vrf <vrf-id> router ospf [options] [<attribute> ...]

### Description

  OSPF VRF configuration.

### Identifiers

  <vrf-id>             VRF

### Atrributes

  area                 OSPF areas
  default-originate    Advertise a default route as external lsa
  distance             Administrative distance for installation into the rib
  max-metric           Set maximum metric value in router lsa to make stub
                       router
  log                  Log configuration
  redistribute         Route redistribute
  timers               Timers
  enable               Turn the feature 'on' or 'off'. The default is 'off'.
  reference-bandwidth  Used to determine link cost/metric value relative to
                       defined reference.
  rfc1583-compatible   RFC1583 compatible
  router-id            BGP router-id for this VRF. If "auto", inherit from the
                       global config. This is the default.

## nv unset vrf <vrf-id> router ospf area <area-id>

### Usage

  nv unset vrf <vrf-id> router ospf area <area-id> [options] [<attribute> ...]

### Description

  An OSPF area

### Identifiers

  <vrf-id>          VRF
  <area-id>         Area

### Atrributes

  filter-list       Filters networks between OSPF areas
  range             Area ranges
  network           Area networks
  default-lsa-cost  Default LSA cost. Only applies when type is non-normal.
  type              The type of area

## nv unset vrf <vrf-id> router ospf area <area-id> filter-list

### Usage

  nv unset vrf <vrf-id> router ospf area <area-id> filter-list [options] [<attribute> ...]

### Description

  Filters networks between OSPF areas

### Identifiers

  <vrf-id>    VRF
  <area-id>   Area

### Atrributes

  in          prefix-list to use as an inbound filter.
  out         prefix-list to use as an inbound filter.



## nv unset vrf <vrf-id> router ospf area <area-id> filter-list in

### Usage

  nv unset vrf <vrf-id> router ospf area <area-id> filter-list in [options]

### Description

  prefix-list to use as an inbound filter.

### Identifiers

  <vrf-id>    VRF
  <area-id>   Area



## nv unset vrf <vrf-id> router ospf area <area-id> filter-list out

### Usage

  nv unset vrf <vrf-id> router ospf area <area-id> filter-list out [options]

### Description

  prefix-list to use as an inbound filter.

### Identifiers

  <vrf-id>    VRF
  <area-id>   Area



## nv unset vrf <vrf-id> router ospf area <area-id> range <range-id>

### Usage

  nv unset vrf <vrf-id> router ospf area <area-id> range <range-id> [options] [<attribute> ...]

### Description

  Filters out components of the prefix

### Identifiers

  <vrf-id>    VRF
  <area-id>   Area
  <range-id>  Range

### Atrributes

  cost        User specified metric advertised for this summary lsa. If
              'auto', operational default value is derived from components.
              This is the default.
  suppress    If on, filters out components but does not advertise prefix



## nv unset vrf <vrf-id> router ospf area <area-id> range <range-id> suppress

### Usage

  nv unset vrf <vrf-id> router ospf area <area-id> range <range-id> suppress [options]

### Description

  If on, filters out components but does not advertise prefix

### Identifiers

  <vrf-id>    VRF
  <area-id>   Area
  <range-id>  Range



## nv unset vrf <vrf-id> router ospf area <area-id> range <range-id> cost

### Usage

  nv unset vrf <vrf-id> router ospf area <area-id> range <range-id> cost [options]

### Description

  User specified metric advertised for this summary lsa. If 'auto', operational default value is derived from components. This is the default.

### Identifiers

  <vrf-id>    VRF
  <area-id>   Area
  <range-id>  Range



## nv unset vrf <vrf-id> router ospf area <area-id> network <network-id>

### Usage

  nv unset vrf <vrf-id> router ospf area <area-id> network <network-id> [options]

### Description

  Filters out components of the prefix

### Identifiers

  <vrf-id>      VRF
  <area-id>     Area
  <network-id>  Network

## nv unset vrf <vrf-id> router ospf area <area-id> type

### Usage

  nv unset vrf <vrf-id> router ospf area <area-id> type [options]

### Description

  The type of area

### Identifiers

  <vrf-id>    VRF
  <area-id>   Area



## nv unset vrf <vrf-id> router ospf area <area-id> default-lsa-cost

### Usage

  nv unset vrf <vrf-id> router ospf area <area-id> default-lsa-cost [options]

### Description

  Default LSA cost.  Only applies when type is non-normal.

### Identifiers

  <vrf-id>    VRF
  <area-id>   Area



## nv unset vrf <vrf-id> router ospf default-originate

### Usage

  nv unset vrf <vrf-id> router ospf default-originate [options] [<attribute> ...]

### Description

  Advertise a default route as external lsa

### Identifiers

  <vrf-id>     VRF

### Atrributes

  enable       Turn the feature 'on' or 'off'. The default is 'off'.
  metric       Metric value for destination routing protocol
  metric-type  Set OSPF External Type 1/2 metrics
  route-map    Optional policy to apply to this advertisement
  always       When 'off', only advertise default route if one exists in the
               rib. This is the default.

## nv unset vrf <vrf-id> router ospf default-originate enable

### Usage

  nv unset vrf <vrf-id> router ospf default-originate enable [options]

### Description

  Turn the feature 'on' or 'off'.  The default is 'off'.

### Identifiers

  <vrf-id>    VRF

## nv unset vrf <vrf-id> router ospf default-originate metric

### Usage

  nv unset vrf <vrf-id> router ospf default-originate metric [options]

### Description

  Metric value for destination routing protocol

### Identifiers

  <vrf-id>    VRF

## nv unset vrf <vrf-id> router ospf default-originate metric-type

### Usage

  nv unset vrf <vrf-id> router ospf default-originate metric-type [options]

### Description

  Set OSPF External Type 1/2 metrics

### Identifiers

  <vrf-id>    VRF

## nv unset vrf <vrf-id> router ospf default-originate route-map

### Usage

  nv unset vrf <vrf-id> router ospf default-originate route-map [options]

### Description

  Optional policy to apply to this advertisement

### Identifiers

  <vrf-id>    VRF

## nv unset vrf <vrf-id> router ospf default-originate always

### Usage

  nv unset vrf <vrf-id> router ospf default-originate always [options]

### Description

  When 'off', only advertise default route if one exists in the rib. This is the default.

### Identifiers

  <vrf-id>    VRF

## nv unset vrf <vrf-id> router ospf distance

### Usage

  nv unset vrf <vrf-id> router ospf distance [options] [<attribute> ...]

### Description

  Administrative distance for installation into the rib

### Identifiers

  <vrf-id>    VRF### Atrributes

  external    External
  inter-area  Inter-area
  intra-area  Intra-area



## nv unset vrf <vrf-id> router ospf distance external

### Usage

  nv unset vrf <vrf-id> router ospf distance external [options]

### Description

  External

### Identifiers

  <vrf-id>    VRF

## nv unset vrf <vrf-id> router ospf distance inter-area

### Usage

  nv unset vrf <vrf-id> router ospf distance inter-area [options]

### Description

  Inter-area

### Identifiers

  <vrf-id>    VRF

## nv unset vrf <vrf-id> router ospf distance intra-area

### Usage

  nv unset vrf <vrf-id> router ospf distance intra-area [options]

### Description

  Intra-area

### Identifiers

  <vrf-id>    VRF

## nv unset vrf <vrf-id> router ospf max-metric

### Usage

  nv unset vrf <vrf-id> router ospf max-metric [options] [<attribute> ...]

### Description

  Set maximum metric value in router lsa to make stub router

### Identifiers

  <vrf-id>        VRF

### Atrributes

  administrative  Administratively applied, for an indefinite period
  on-shutdown     Advertise stub-router prior to full shutdown of OSPF
  on-startup      Automatically advertise stub Router-LSA on startup of OSPF

## nv unset vrf <vrf-id> router ospf max-metric administrative

### Usage

  nv unset vrf <vrf-id> router ospf max-metric administrative [options]

### Description

  Administratively applied, for an indefinite period

### Identifiers

  <vrf-id>    VRF

## nv unset vrf <vrf-id> router ospf max-metric on-shutdown

### Usage

  nv unset vrf <vrf-id> router ospf max-metric on-shutdown [options]

### Description

  Advertise stub-router prior to full shutdown of OSPF

### Identifiers

  <vrf-id>    VRF

## nv unset vrf <vrf-id> router ospf max-metric on-startup

### Usage

  nv unset vrf <vrf-id> router ospf max-metric on-startup [options]

### Description

  Automatically advertise stub Router-LSA on startup of OSPF

### Identifiers

  <vrf-id>    VRF

## nv unset vrf <vrf-id> router ospf log

### Usage

  nv unset vrf <vrf-id> router ospf log [options] [<attribute> ...]

### Description

  Log configuration

### Identifiers

  <vrf-id>           VRF

### Atrributes

  adjacency-changes  Log adjacency changes

## nv unset vrf <vrf-id> router ospf log adjacency-changes

### Usage

  nv unset vrf <vrf-id> router ospf log adjacency-changes [options]

### Description

  Log adjacency changes

### Identifiers

  <vrf-id>    VRF## nv unset vrf <vrf-id> router ospf redistribute

### Usage

  nv unset vrf <vrf-id> router ospf redistribute [options] [<attribute> ...]

### Description

  Route redistribute

### Identifiers

  <vrf-id>    VRF### Atrributes

  static      Route redistribute of static routes
  connected   Route redistribute of connected routes
  kernel      Route redistribute of kernel routes
  bgp         Route redistribute of bgp routes

## nv unset vrf <vrf-id> router ospf redistribute static

### Usage

  nv unset vrf <vrf-id> router ospf redistribute static [options] [<attribute> ...]

### Description

  Source route type.

### Identifiers

  <vrf-id>     VRF

### Atrributes

  enable       Turn the feature 'on' or 'off'. The default is 'off'.
  metric       Metric value for destination routing protocol
  metric-type  Set OSPF External Type 1/2 metrics
  route-map    Optional policy to apply to this advertisement

## nv unset vrf <vrf-id> router ospf redistribute static enable

### Usage

  nv unset vrf <vrf-id> router ospf redistribute static enable [options]

### Description

  Turn the feature 'on' or 'off'.  The default is 'off'.

### Identifiers

  <vrf-id>    VRF

## nv unset vrf <vrf-id> router ospf redistribute static metric

### Usage

  nv unset vrf <vrf-id> router ospf redistribute static metric [options]

### Description

  Metric value for destination routing protocol

### Identifiers

  <vrf-id>    VRF

## nv unset vrf <vrf-id> router ospf redistribute static metric-type

### Usage

  nv unset vrf <vrf-id> router ospf redistribute static metric-type [options]

### Description

  Set OSPF External Type 1/2 metrics

### Identifiers

  <vrf-id>    VRF## nv unset vrf <vrf-id> router ospf redistribute static route-map

### Usage

  nv unset vrf <vrf-id> router ospf redistribute static route-map [options]

### Description

  Optional policy to apply to this advertisement

### Identifiers

  <vrf-id>    VRF## nv unset vrf <vrf-id> router ospf redistribute connected

### Usage

  nv unset vrf <vrf-id> router ospf redistribute connected [options] [<attribute> ...]

### Description

  Source route type.

### Identifiers

  <vrf-id>     VRF

### Atrributes

  enable       Turn the feature 'on' or 'off'. The default is 'off'.
  metric       Metric value for destination routing protocol
  metric-type  Set OSPF External Type 1/2 metrics
  route-map    Optional policy to apply to this advertisement

## nv unset vrf <vrf-id> router ospf redistribute connected enable

### Usage

  nv unset vrf <vrf-id> router ospf redistribute connected enable [options]

### Description

  Turn the feature 'on' or 'off'.  The default is 'off'.

### Identifiers

  <vrf-id>    VRF## nv unset vrf <vrf-id> router ospf redistribute connected metric

### Usage

  nv unset vrf <vrf-id> router ospf redistribute connected metric [options]

### Description

  Metric value for destination routing protocol

### Identifiers

  <vrf-id>    VRF## nv unset vrf <vrf-id> router ospf redistribute connected metric-type

### Usage

  nv unset vrf <vrf-id> router ospf redistribute connected metric-type [options]

### Description

  Set OSPF External Type 1/2 metrics

### Identifiers

  <vrf-id>    VRF## nv unset vrf <vrf-id> router ospf redistribute connected route-map

### Usage

  nv unset vrf <vrf-id> router ospf redistribute connected route-map [options]

### Description

  Optional policy to apply to this advertisement

### Identifiers

  <vrf-id>    VRF

## nv unset vrf <vrf-id> router ospf redistribute kernel

### Usage

  nv unset vrf <vrf-id> router ospf redistribute kernel [options] [<attribute> ...]

### Description

  Source route type.

### Identifiers

  <vrf-id>     VRF

### Atrributes

  enable       Turn the feature 'on' or 'off'. The default is 'off'.
  metric       Metric value for destination routing protocol
  metric-type  Set OSPF External Type 1/2 metrics
  route-map    Optional policy to apply to this advertisement

## nv unset vrf <vrf-id> router ospf redistribute kernel enable

### Usage

  nv unset vrf <vrf-id> router ospf redistribute kernel enable [options]

### Description

  Turn the feature 'on' or 'off'.  The default is 'off'.

### Identifiers

  <vrf-id>    VRF

## nv unset vrf <vrf-id> router ospf redistribute kernel metric

### Usage

  nv unset vrf <vrf-id> router ospf redistribute kernel metric [options]

### Description

  Metric value for destination routing protocol

### Identifiers

  <vrf-id>    VRF## nv unset vrf <vrf-id> router ospf redistribute kernel metric-type

### Usage

  nv unset vrf <vrf-id> router ospf redistribute kernel metric-type [options]

### Description

  Set OSPF External Type 1/2 metrics

### Identifiers

  <vrf-id>    VRF
## nv unset vrf <vrf-id> router ospf redistribute kernel route-map

### Usage

  nv unset vrf <vrf-id> router ospf redistribute kernel route-map [options]

### Description

  Optional policy to apply to this advertisement

### Identifiers

  <vrf-id>    VRF## nv unset vrf <vrf-id> router ospf redistribute bgp

### Usage

  nv unset vrf <vrf-id> router ospf redistribute bgp [options] [<attribute> ...]

### Description

  Source route type.

### Identifiers

  <vrf-id>     VRF

### Atrributes

  enable       Turn the feature 'on' or 'off'. The default is 'off'.
  metric       Metric value for destination routing protocol
  metric-type  Set OSPF External Type 1/2 metrics
  route-map    Optional policy to apply to this advertisement

## nv unset vrf <vrf-id> router ospf redistribute bgp enable

### Usage

  nv unset vrf <vrf-id> router ospf redistribute bgp enable [options]

### Description

  Turn the feature 'on' or 'off'.  The default is 'off'.

### Identifiers

  <vrf-id>    VRF## nv unset vrf <vrf-id> router ospf redistribute bgp metric

### Usage

  nv unset vrf <vrf-id> router ospf redistribute bgp metric [options]

### Description

  Metric value for destination routing protocol

### Identifiers

  <vrf-id>    VRF## nv unset vrf <vrf-id> router ospf redistribute bgp metric-type

### Usage

  nv unset vrf <vrf-id> router ospf redistribute bgp metric-type [options]

### Description

  Set OSPF External Type 1/2 metrics

### Identifiers

  <vrf-id>    VRF

## nv unset vrf <vrf-id> router ospf redistribute bgp route-map

### Usage

  nv unset vrf <vrf-id> router ospf redistribute bgp route-map [options]

### Description

  Optional policy to apply to this advertisement

### Identifiers

  <vrf-id>    VRF

## nv unset vrf <vrf-id> router ospf timers

### Usage

  nv unset vrf <vrf-id> router ospf timers [options] [<attribute> ...]

### Description

  Timers

### Identifiers

  <vrf-id>    VRF### Atrributes

  lsa         LSA timers
  spf         SPF timers
  refresh     defines interval (sec) to re-send lsas to keep from aging out.
              If 'auto', inherited from global. This is the default.

## nv unset vrf <vrf-id> router ospf timers lsa

### Usage

  nv unset vrf <vrf-id> router ospf timers lsa [options] [<attribute> ...]

### Description

  LSA timers

### Identifiers

  <vrf-id>     VRF

### Atrributes

  min-arrival  Minimum delay in receiving new version of a LSA. If 'auto',
               inherited from global. This is the default.
  throttle     Delay (msec) between sending LSAs. If 'auto', inherited from
               global. This is the default.

## nv unset vrf <vrf-id> router ospf timers lsa min-arrival

### Usage

  nv unset vrf <vrf-id> router ospf timers lsa min-arrival [options]

### Description

  Minimum delay in receiving new version of a LSA.  If 'auto', inherited from global.  This is the default.

### Identifiers

  <vrf-id>    VRF

## nv unset vrf <vrf-id> router ospf timers lsa throttle

### Usage

  nv unset vrf <vrf-id> router ospf timers lsa throttle [options]

### Description

  Delay (msec) between sending LSAs.  If 'auto', inherited from global.  This is the default.

### Identifiers

  <vrf-id>    VRF

## nv unset vrf <vrf-id> router ospf timers spf

### Usage

  nv unset vrf <vrf-id> router ospf timers spf [options] [<attribute> ...]

### Description

  SPF timers

### Identifiers

  <vrf-id>      VRF

### Atrributes

  delay         Delay (msec) from first change received till SPF calculation.
                If 'auto', inherited from global. This is the default.
  holdtime      Initial hold time (msec) between consecutive SPF calculations.
                If 'auto', inherited from global. This is the default.
  max-holdtime  Maximum hold time (msec) between consecutive SPF calculations.
                If 'auto', inherited from global. This is the default.

## nv unset vrf <vrf-id> router ospf timers spf delay

### Usage

  nv unset vrf <vrf-id> router ospf timers spf delay [options]

### Description

  Delay (msec) from first change received till SPF calculation. If 'auto', inherited from global.  This is the default.

### Identifiers

  <vrf-id>    VRF

## nv unset vrf <vrf-id> router ospf timers spf holdtime

### Usage

  nv unset vrf <vrf-id> router ospf timers spf holdtime [options]

### Description

  Initial hold time (msec) between consecutive SPF calculations. If 'auto', inherited from global.  This is the default.

### Identifiers

  <vrf-id>    VRF

## nv unset vrf <vrf-id> router ospf timers spf max-holdtime

### Usage

  nv unset vrf <vrf-id> router ospf timers spf max-holdtime [options]

### Description

  Maximum hold time (msec) between consecutive SPF calculations. If 'auto', inherited from global.  This is the default.

### Identifiers

  <vrf-id>    VRF

## nv unset vrf <vrf-id> router ospf timers refresh

### Usage

  nv unset vrf <vrf-id> router ospf timers refresh [options]

### Description

  defines interval (sec) to re-send lsas to keep from aging out. If 'auto', inherited from global.  This is the default.

### Identifiers

  <vrf-id>    VRF

## nv unset vrf <vrf-id> router ospf enable

### Usage

  nv unset vrf <vrf-id> router ospf enable [options]

### Description

  Turn the feature 'on' or 'off'.  The default is 'off'.

### Identifiers

  <vrf-id>    VRF

## nv unset vrf <vrf-id> router ospf reference-bandwidth

### Usage

  nv unset vrf <vrf-id> router ospf reference-bandwidth [options]

### Description

  Used to determine link cost/metric value relative to defined reference.

### Identifiers

  <vrf-id>    VRF

## nv unset vrf <vrf-id> router ospf rfc1583-compatible

### Usage

  nv unset vrf <vrf-id> router ospf rfc1583-compatible [options]

### Description

  RFC1583 compatible

### Identifiers

  <vrf-id>    VRF

## nv unset vrf <vrf-id> router ospf router-id

### Usage

  nv unset vrf <vrf-id> router ospf router-id [options]

### Description

  BGP router-id for this VRF.  If "auto", inherit from the global config.  This is the default.

### Identifiers

  <vrf-id>    VRF

## nv unset vrf <vrf-id> ptp

### Usage

  nv unset vrf <vrf-id> ptp [options] [<attribute> ...]

### Description

  VRF PTP configuration.  Inherited by interfaces in this VRF.

### Identifiers

  <vrf-id>    VRF### Atrributes

  enable      Turn the feature 'on' or 'off'. The default is 'on'.

## nv unset vrf <vrf-id> ptp enable

### Usage

  nv unset vrf <vrf-id> ptp enable [options]

### Description

  Turn the feature 'on' or 'off'.  The default is 'on'.

### Identifiers

  <vrf-id>    VRF

## nv unset vrf <vrf-id> table

### Usage

  nv unset vrf <vrf-id> table [options]

### Description

  The routing table number, between 1001-1255, used by the named VRF. If auto, the default, it will be auto generated.

### Identifiers

  <vrf-id>    VRF

## nv unset nve

### Usage

  nv unset nve [options] [<attribute> ...]

### Description

  Network Virtualization configuration and operational info

### Atrributes

  vxlan       Global VxLAN configuration and operational properties.

## nv unset nve vxlan

### Usage

  nv unset nve vxlan [options] [<attribute> ...]

### Description

  VxLAN

### Atrributes

  mlag             VxLAN specific MLAG address
  source           Source address
  flooding         Configuration to specify how BUM traffic in the overlay is
                   handled. This applies to all overlays (VNIs), but can be
                   overridden by VNI-specific configuration.
  enable           Turn the feature 'on' or 'off'. The default is 'off'.
  arp-nd-suppress  Controls dynamic MAC learning over VXLAN tunnels based on
                   received packets. This applies to all overlays (VNIs).
  mac-learning     Controls dynamic MAC learning over VXLAN tunnels based on
                   received packets. This applies to all overlays (VNIs), but
                   can be overridden by VNI-specific configuration.
  mtu              interface mtu
  port             UDP port for VXLAN frames

## nv unset nve vxlan mlag

### Usage

  nv unset nve vxlan mlag [options] [<attribute> ...]

### Description

  VxLAN specfic MLAG configuration

### Atrributes

  shared-address  shared anycast address for MLAG peers

## nv unset nve vxlan mlag shared-address

### Usage

  nv unset nve vxlan mlag shared-address [options]

### Description

  shared anycast address for MLAG peers

## nv unset nve vxlan source

### Usage

  nv unset nve vxlan source [options] [<attribute> ...]

### Description

  Source address

### Atrributes

  address     IP addresses of this node's VTEP or 'auto'. If 'auto', use the
              primary IP loopback (not 127.0.0.1). This is the default.

## nv unset nve vxlan source address

### Usage

  nv unset nve vxlan source address [options]

### Description

  IP addresses of this node's VTEP or 'auto'.  If 'auto', use the primary IP loopback (not 127.0.0.1).  This is the default.



## nv unset nve vxlan flooding

### Usage

  nv unset nve vxlan flooding [options] [<attribute> ...]

### Description

  Handling of BUM traffic

### Atrributes

  head-end-replication  BUM traffic is replicated and individual copies sent
                        to remote destinations.
  enable                Turn the feature 'on' or 'off'. The default is 'off'.
  multicast-group       BUM traffic is sent to the specified multicast group
                        and will be received by receivers who are interested
                        in that group. This usually requires PIM-SM to be used
                        in the network.

## nv unset nve vxlan flooding head-end-replication

### Usage

  nv unset nve vxlan flooding head-end-replication [options] [<hrep-id> ...]

### Description

  Set of IPv4 unicast addresses or "evpn".

### Identifiers

  <hrep-id>   IPv4 unicast addresses or "evpn"

## nv unset nve vxlan flooding head-end-replication <hrep-id>

### Usage

  nv unset nve vxlan flooding head-end-replication <hrep-id> [options]

### Description

  Set of IPv4 unicast addresses or "evpn".

### Identifiers

  <hrep-id>   IPv4 unicast addresses or "evpn"

## nv unset nve vxlan flooding enable

### Usage

  nv unset nve vxlan flooding enable [options]

### Description

  Turn the feature 'on' or 'off'.  The default is 'off'.

## nv unset nve vxlan flooding multicast-group

### Usage

  nv unset nve vxlan flooding multicast-group [options]

### Description

  BUM traffic is sent to the specified multicast group and will be received by receivers who are interested in that group. This usually requires PIM-SM to be used in the network.

## nv unset nve vxlan enable

### Usage

  nv unset nve vxlan enable [options]

### Description

  Turn the feature 'on' or 'off'.  The default is 'off'.

## nv unset nve vxlan mac-learning

### Usage

  nv unset nve vxlan mac-learning [options]

### Description

  Controls dynamic MAC learning over VXLAN tunnels based on received packets. This applies to all overlays (VNIs), but can be overridden by VNI-specific configuration.

## nv unset nve vxlan port

### Usage

  nv unset nve vxlan port [options]

### Description

  UDP port for VXLAN frames

## nv unset nve vxlan arp-nd-suppress

### Usage

  nv unset nve vxlan arp-nd-suppress [options]

### Description

  Controls dynamic MAC learning over VXLAN tunnels based on received packets. This applies to all overlays (VNIs).

## nv unset nve vxlan mtu

### Usage

  nv unset nve vxlan mtu [options]

### Description

  interface mtu

## nv unset acl

### Usage

  nv unset acl [options] [<acl-id> ...]

### Description

  ACL rules

### Identifiers

  <acl-id>    ACL ID

## nv unset acl <acl-id>

### Usage

  nv unset acl <acl-id> [options] [<attribute> ...]

### Description

  An ACL is used for matching packets and take actions

### Identifiers

  <acl-id>    ACL ID

### Atrributes

  rule        acl rule
  type        acl type

## nv unset acl <acl-id> rule <rule-id>

### Usage

  nv unset acl <acl-id> rule <rule-id> [options] [<attribute> ...]

### Description

  ACL Matching criteria and action rule

### Identifiers

  <acl-id>    ACL ID
  <rule-id>   ACL rule number

### Atrributes

  match       ACL match criteria
  action      ACL action

## nv unset acl <acl-id> rule <rule-id> match

### Usage

  nv unset acl <acl-id> rule <rule-id> match [options] [<attribute> ...]

### Description

  An ACL match

### Identifiers

  <acl-id>    ACL ID
  <rule-id>   ACL rule number

### Atrributes

  ip          IPv4 and IPv6 match
  mac         MAC match

## nv unset acl <acl-id> rule <rule-id> match ip

### Usage

  nv unset acl <acl-id> rule <rule-id> match ip [options] [<attribute> ...]

### Description

  An ACL IPv4/IPv6 match

### Identifiers

  <acl-id>     ACL ID
  <rule-id>    ACL rule number

### Atrributes

  source-port  source port
  dest-port    destination port
  fragment     Fragment packets
  ecn          ECN protocol packet match
  tcp          TCP protocol packet match
  dest-ip      Destination IP address
  dscp         DSCP
  icmp-type    ICMP message type
  icmpv6-type  ICMPv6 message type
  protocol     IP protocol
  source-ip    Source IP address

## nv unset acl <acl-id> rule <rule-id> match ip source-port <ip-port-id>

### Usage

  nv unset acl <acl-id> rule <rule-id> match ip source-port <ip-port-id> [options]

### Description

  L4 port

### Identifiers

  <acl-id>      ACL ID
  <rule-id>     ACL rule number
  <ip-port-id>  IP port ID

## nv unset acl <acl-id> rule <rule-id> match ip dest-port <ip-port-id>

### Usage

  nv unset acl <acl-id> rule <rule-id> match ip dest-port <ip-port-id> [options]

### Description

  L4 port

### Identifiers

  <acl-id>      ACL ID
  <rule-id>     ACL rule number
  <ip-port-id>  IP port ID

## nv unset acl <acl-id> rule <rule-id> match ip fragment

### Usage

  nv unset acl <acl-id> rule <rule-id> match ip fragment [options]

### Description

  State details

### Identifiers

  <acl-id>    ACL ID
  <rule-id>   ACL rule number

## nv unset acl <acl-id> rule <rule-id> match ip ecn

### Usage

  nv unset acl <acl-id> rule <rule-id> match ip ecn [options] [<attribute> ...]

### Description

  ECN

### Identifiers

  <acl-id>    ACL ID
  <rule-id>   ACL rule number

### Atrributes

  flags       ECN protocol flags
  ip-ect      IP ECT

## nv unset acl <acl-id> rule <rule-id> match ip ecn flags

### Usage

  nv unset acl <acl-id> rule <rule-id> match ip ecn flags [options]

### Description

  ECN flags

### Identifiers

  <acl-id>    ACL ID
  <rule-id>   ACL rule number

## nv unset acl <acl-id> rule <rule-id> match ip ecn ip-ect

### Usage

  nv unset acl <acl-id> rule <rule-id> match ip ecn ip-ect [options]

### Description

  IP ECT

### Identifiers

  <acl-id>    ACL ID
  <rule-id>   ACL rule number

## nv unset acl <acl-id> rule <rule-id> match ip tcp

### Usage

  nv unset acl <acl-id> rule <rule-id> match ip tcp [options] [<attribute> ...]

### Description

  L4 port

### Identifiers

  <acl-id>    ACL ID
  <rule-id>   ACL rule number

### Atrributes

  flags       TCP protocol flags
  mask        TCP protocol flag mask
  state       TCP state

## nv unset acl <acl-id> rule <rule-id> match ip tcp flags

### Usage

  nv unset acl <acl-id> rule <rule-id> match ip tcp flags [options]

### Description

  TCP flags

### Identifiers

  <acl-id>    ACL ID
  <rule-id>   ACL rule number

## nv unset acl <acl-id> rule <rule-id> match ip tcp mask

### Usage

  nv unset acl <acl-id> rule <rule-id> match ip tcp mask [options]

### Description

  TCP flags

### Identifiers

  <acl-id>    ACL ID
  <rule-id>   ACL rule number

## nv unset acl <acl-id> rule <rule-id> match ip tcp state

### Usage

  nv unset acl <acl-id> rule <rule-id> match ip tcp state [options]

### Description

  TCP state

### Identifiers

  <acl-id>    ACL ID
  <rule-id>   ACL rule number

## nv unset acl <acl-id> rule <rule-id> match ip source-ip

### Usage

  nv unset acl <acl-id> rule <rule-id> match ip source-ip [options]

### Description

  Source IP address

### Identifiers

  <acl-id>    ACL ID
  <rule-id>   ACL rule number

## nv unset acl <acl-id> rule <rule-id> match ip dest-ip

### Usage

  nv unset acl <acl-id> rule <rule-id> match ip dest-ip [options]

### Description

  Destination IP address

### Identifiers

  <acl-id>    ACL ID
  <rule-id>   ACL rule number

## nv unset acl <acl-id> rule <rule-id> match ip protocol

### Usage

  nv unset acl <acl-id> rule <rule-id> match ip protocol [options]

### Description

  IP protocol

### Identifiers

  <acl-id>    ACL ID
  <rule-id>   ACL rule number

## nv unset acl <acl-id> rule <rule-id> match ip dscp

### Usage

  nv unset acl <acl-id> rule <rule-id> match ip dscp [options]

### Description

  DSCP

### Identifiers

  <acl-id>    ACL ID
  <rule-id>   ACL rule number

## nv unset acl <acl-id> rule <rule-id> match ip icmp-type

### Usage

  nv unset acl <acl-id> rule <rule-id> match ip icmp-type [options]

### Description

  ICMP message type

### Identifiers

  <acl-id>    ACL ID
  <rule-id>   ACL rule number

## nv unset acl <acl-id> rule <rule-id> match ip icmpv6-type

### Usage

  nv unset acl <acl-id> rule <rule-id> match ip icmpv6-type [options]

### Description

  ICMPv6 message type

### Identifiers

  <acl-id>    ACL ID
  <rule-id>   ACL rule number

## nv unset acl <acl-id> rule <rule-id> match mac

### Usage

  nv unset acl <acl-id> rule <rule-id> match mac [options] [<attribute> ...]

### Description

  An ACL MAC match

### Identifiers

  <acl-id>         ACL ID
  <rule-id>        ACL rule number

### Atrributes

  dest-mac         Destination MAC address
  dest-mac-mask    Destination MAC address mask
  protocol         MAC protocol
  source-mac       Source MAC address
  source-mac-mask  Source MAC address mask
  vlan             VLAN ID

## nv unset acl <acl-id> rule <rule-id> match mac source-mac

### Usage

  nv unset acl <acl-id> rule <rule-id> match mac source-mac [options]

### Description

  Source MAC address

### Identifiers

  <acl-id>    ACL ID
  <rule-id>   ACL rule number

## nv unset acl <acl-id> rule <rule-id> match mac source-mac-mask

### Usage

  nv unset acl <acl-id> rule <rule-id> match mac source-mac-mask [options]

### Description

  Source MAC address mask

### Identifiers

  <acl-id>    ACL ID
  <rule-id>   ACL rule number

## nv unset acl <acl-id> rule <rule-id> match mac dest-mac

### Usage

  nv unset acl <acl-id> rule <rule-id> match mac dest-mac [options]

### Description

  Destination MAC address

### Identifiers

  <acl-id>    ACL ID
  <rule-id>   ACL rule number

## nv unset acl <acl-id> rule <rule-id> match mac dest-mac-mask

### Usage

  nv unset acl <acl-id> rule <rule-id> match mac dest-mac-mask [options]

### Description

  Destination MAC address mask

### Identifiers

  <acl-id>    ACL ID
  <rule-id>   ACL rule number

## nv unset acl <acl-id> rule <rule-id> match mac protocol

### Usage

  nv unset acl <acl-id> rule <rule-id> match mac protocol [options]

### Description

  MAC protocol

### Identifiers

  <acl-id>    ACL ID
  <rule-id>   ACL rule number

## nv unset acl <acl-id> rule <rule-id> match mac vlan

### Usage

  nv unset acl <acl-id> rule <rule-id> match mac vlan [options]

### Description

  VLAN ID

### Identifiers

  <acl-id>    ACL ID
  <rule-id>   ACL rule number

## nv unset acl <acl-id> rule <rule-id> action

### Usage

  nv unset acl <acl-id> rule <rule-id> action [options] [<attribute> ...]

### Description

  ACL rule action

### Identifiers

  <acl-id>    ACL ID
  <rule-id>   ACL rule number

### Atrributes

  permit      Permit action
  deny        Deny action
  log         Provides ACL logging facility
  set         Modify the packet with appropriate values
  erspan      ERSPAN session
  police      policing of packets/bytes
  span        SPAN session

## nv unset acl <acl-id> rule <rule-id> action permit

### Usage

  nv unset acl <acl-id> rule <rule-id> action permit [options]

### Description

  Permit packets

### Identifiers

  <acl-id>    ACL ID
  <rule-id>   ACL rule number

## nv unset acl <acl-id> rule <rule-id> action deny

### Usage

  nv unset acl <acl-id> rule <rule-id> action deny [options]

### Description

  deny packets

### Identifiers

  <acl-id>    ACL ID
  <rule-id>   ACL rule number

## nv unset acl <acl-id> rule <rule-id> action log

### Usage

  nv unset acl <acl-id> rule <rule-id> action log [options]

### Description

  log packets

### Identifiers

  <acl-id>    ACL ID
  <rule-id>   ACL rule number

## nv unset acl <acl-id> rule <rule-id> action set

### Usage

  nv unset acl <acl-id> rule <rule-id> action set [options] [<attribute> ...]

### Description

  Set action for packets

### Identifiers

  <acl-id>    ACL ID
  <rule-id>   ACL rule number

### Atrributes

  class       Sets the class value for classification of the packet
  cos         Set the CoS value
  dscp        Sets/Modifies the DSCP value in the packet

## nv unset acl <acl-id> rule <rule-id> action set dscp

### Usage

  nv unset acl <acl-id> rule <rule-id> action set dscp [options]

### Description

  Sets/Modifies the DSCP value in the packet

### Identifiers

  <acl-id>    ACL ID
  <rule-id>   ACL rule number

## nv unset acl <acl-id> rule <rule-id> action set class

### Usage

  nv unset acl <acl-id> rule <rule-id> action set class [options]

### Description

  Sets the class value for classification of the packet

### Identifiers

  <acl-id>    ACL ID
  <rule-id>   ACL rule number

## nv unset acl <acl-id> rule <rule-id> action set cos

### Usage

  nv unset acl <acl-id> rule <rule-id> action set cos [options]

### Description

  Set the CoS value

### Identifiers

  <acl-id>    ACL ID
  <rule-id>   ACL rule number

## nv unset acl <acl-id> rule <rule-id> action erspan

### Usage

  nv unset acl <acl-id> rule <rule-id> action erspan [options] [<attribute> ...]

### Description

  ERSPAN session

### Identifiers

  <acl-id>    ACL ID
  <rule-id>   ACL rule number

### Atrributes

  dest-ip     Destination IP address
  source-ip   Source IP address
  ttl         Time to Live

## nv unset acl <acl-id> rule <rule-id> action erspan source-ip

### Usage

  nv unset acl <acl-id> rule <rule-id> action erspan source-ip [options]

### Description

  Source IP address

### Identifiers

  <acl-id>    ACL ID
  <rule-id>   ACL rule number

## nv unset acl <acl-id> rule <rule-id> action erspan dest-ip

### Usage

  nv unset acl <acl-id> rule <rule-id> action erspan dest-ip [options]

### Description

  Destination IP address

### Identifiers

  <acl-id>    ACL ID
  <rule-id>   ACL rule number

## nv unset acl <acl-id> rule <rule-id> action erspan ttl

### Usage

  nv unset acl <acl-id> rule <rule-id> action erspan ttl [options]

### Description

  Time to Live

### Identifiers

  <acl-id>    ACL ID
  <rule-id>   ACL rule number

## nv unset acl <acl-id> rule <rule-id> action police

### Usage

  nv unset acl <acl-id> rule <rule-id> action police [options] [<attribute> ...]

### Description

  Policing of matched packets/bytes

### Identifiers

  <acl-id>    ACL ID
  <rule-id>   ACL rule number

### Atrributes

  burst       Policing burst value
  mode        Policing mode
  rate        Policing rate value

## nv unset acl <acl-id> rule <rule-id> action police mode

### Usage

  nv unset acl <acl-id> rule <rule-id> action police mode [options]

### Description

  Policing mode

### Identifiers

  <acl-id>    ACL ID
  <rule-id>   ACL rule number

## nv unset acl <acl-id> rule <rule-id> action police burst

### Usage

  nv unset acl <acl-id> rule <rule-id> action police burst [options]

### Description

  Policing burst value

### Identifiers

  <acl-id>    ACL ID
  <rule-id>   ACL rule number

## nv unset acl <acl-id> rule <rule-id> action police rate

### Usage

  nv unset acl <acl-id> rule <rule-id> action police rate [options]

### Description

  Policing rate value

### Identifiers

  <acl-id>    ACL ID
  <rule-id>   ACL rule number

## nv unset acl <acl-id> rule <rule-id> action span

### Usage

  nv unset acl <acl-id> rule <rule-id> action span [options]

### Description

  SPAN session

### Identifiers

  <acl-id>    ACL ID
  <rule-id>   ACL rule number

## nv unset acl <acl-id> type

### Usage

  nv unset acl <acl-id> type [options]

### Description

  acl type

### Identifiers

  <acl-id>    ACL ID
