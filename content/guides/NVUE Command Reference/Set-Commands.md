---
title: Set Commands
author: Cumulus Networks
weight: 30
product: Cumulus Linux
---
## nv set router

### Usage

  nv set router [options] [<attribute> ...]

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

## nv set router nexthop-group <nexthop-group-id>

### Usage

  nv set router nexthop-group <nexthop-group-id> [options] [<attribute> ...]

### Description

  A nexthop-group

### Identifiers

  <nexthop-group-id>  Nexthop group ID

### Atrributes

  via                 Nexthops  
  
## nv set router nexthop-group <nexthop-group-id> via <via-id>

### Usage

  nv set router nexthop-group <nexthop-group-id> via <via-id> [options] [<attribute> ...]

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

## nv set router pbr

### Usage

  nv set router pbr [options] [<attribute> ...]

### Description

  PBR global configuration.

### Atrributes

  map         Collection of PBR Maps
  enable      Turn the feature 'on' or 'off'. The default is 'off'.

## nv set router pbr map <pbr-map-id>

### Usage

  nv set router pbr map <pbr-map-id> [options] [<attribute> ...]

### Description

  A pbr map is used for policy configuration.

### Identifiers

  <pbr-map-id>  Route Map ID

### Atrributes

  rule          PBR Map rule
  
## nv set router pbr map <pbr-map-id> rule <rule-id>

### Usage

  nv set router pbr map <pbr-map-id> rule <rule-id> [options] [<attribute> ...]

### Description

  Route Map Matching/setting criteria and action rule

### Identifiers

  <pbr-map-id>  Route Map ID
  <rule-id>     PBR rule number

### Atrributes

  match         PBR match
  action        PBR set  
  
## nv set router pbr map <pbr-map-id> rule <rule-id> match

### Usage

  nv set router pbr map <pbr-map-id> rule <rule-id> match [options] [<attribute> ...]

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

## nv set router pbr map <pbr-map-id> rule <rule-id> match dscp 0-63

### Usage

  nv set router pbr map <pbr-map-id> rule <rule-id> match dscp [options] 0-63

### Description

  DSCP

### Identifiers

  <pbr-map-id>  Route Map ID
  <rule-id>     PBR rule number
  
## nv set router pbr map <pbr-map-id> rule <rule-id> match ecn 0-3

### Usage

  nv set router pbr map <pbr-map-id> rule <rule-id> match ecn [options] 0-3

### Description

  ECN

### Identifiers

  <pbr-map-id>  Route Map ID
  <rule-id>     PBR rule number

## nv set router pbr map <pbr-map-id> rule <rule-id> action

### Usage

  nv set router pbr map <pbr-map-id> rule <rule-id> action [options] [<attribute> ...]

### Description

  PBR map rule action

### Identifiers

  <pbr-map-id>   Route Map ID
  <rule-id>      PBR rule number

### Atrributes

  nexthop-group  Route with nexthop-group
  vrf            Route through VRF

## nv set router pbr map <pbr-map-id> rule <rule-id> action nexthop-group <nexthop-group-id>

### Usage

  nv set router pbr map <pbr-map-id> rule <rule-id> action nexthop-group <nexthop-group-id> [options]

### Description

  A nexthop-group

### Identifiers

  <pbr-map-id>        Route Map ID
  <rule-id>           PBR rule number
  <nexthop-group-id>  Nexthop group ID
  
## nv set router pbr map <pbr-map-id> rule <rule-id> action vrf <vrf-name>

### Usage

  nv set router pbr map <pbr-map-id> rule <rule-id> action vrf [options] <vrf-name>

### Description

  Route through VRF

### Identifiers

  <pbr-map-id>  Route Map ID
  <rule-id>     PBR rule number
  
## nv set router policy

### Usage

  nv set router policy [options] [<attribute> ...]

### Description

  A router

### Atrributes

  community-list        Community lists
  as-path-list          AS Path lists
  ext-community-list    Extended Community lists
  large-community-list  Large Community lists
  prefix-list           Prefix list rules
  route-map             Collection of Route Maps

## nv set router policy community-list <list-id>

### Usage

  nv set router policy community-list <list-id> [options] [<attribute> ...]

### Description

  A community list is used for matching BGP community policies.

### Identifiers

  <list-id>   Community List ID

### Atrributes

  rule        Community List rule## nv set router policy community-list <list-id> rule <rule-id>

### Usage

  nv set router policy community-list <list-id> rule <rule-id> [options] [<attribute> ...]

### Description

  Community list Matching criteria and action rule

### Identifiers

  <list-id>   Community List ID
  <rule-id>   Prefix List rule number

### Atrributes

  community   Community expression
  action      Action to be taken for community list match## nv set router policy community-list <list-id> rule <rule-id> community <community-id>

### Usage

  nv set router policy community-list <list-id> rule <rule-id> community <community-id> [options]

### Description

  A community name

### Identifiers

  <list-id>       Community List ID
  <rule-id>       Prefix List rule number
  <community-id>  Community number in AA:NN format or well known name

## nv set router policy as-path-list <list-id>

### Usage

  nv set router policy as-path-list <list-id> [options] [<attribute> ...]

### Description

  An AS Path list is used for matching BGP AS Path

### Identifiers

  <list-id>   AS Path List ID

### Atrributes

  rule        AS Path List rule
  
## nv set router policy as-path-list <list-id> rule <rule-id>

### Usage

  nv set router policy as-path-list <list-id> rule <rule-id> [options] [<attribute> ...]

### Description

  AS Path list Matching criteria and action rule

### Identifiers

  <list-id>   AS Path List ID
  <rule-id>   Prefix List rule number

### Atrributes

  action      Action to be taken for AS path list match
  aspath-exp  Regular expression to match BGP AS Paths
  
## nv set router policy as-path-list <list-id> rule <rule-id> aspath-exp <bgp-regex>

### Usage

  nv set router policy as-path-list <list-id> rule <rule-id> aspath-exp [options] <bgp-regex>

### Description

  Regular expression to match BGP AS Paths

### Identifiers

  <list-id>   AS Path List ID
  <rule-id>   Prefix List rule number
  
## nv set router policy ext-community-list <list-id>

### Usage

  nv set router policy ext-community-list <list-id> [options] [<attribute> ...]

### Description

  A Extended Community list used for matching BGP communities

### Identifiers

  <list-id>   Community List ID

### Atrributes

  rule        Extended Community List rule
  
## nv set router policy ext-community-list <list-id> rule <rule-id>

### Usage

  nv set router policy ext-community-list <list-id> rule <rule-id> [options] [<attribute> ...]

### Description

  Extended Community list Matching criteria and action rule

### Identifiers

  <list-id>      Community List ID
  <rule-id>      Prefix List rule number

### Atrributes

  ext-community  Extended Community expression
  action         Action to be taken for extended community list match
  
## nv set router policy ext-community-list <list-id> rule <rule-id> ext-community

### Usage

  nv set router policy ext-community-list <list-id> rule <rule-id> ext-community [options] [<attribute> ...]

### Description

  A Extended community name

### Identifiers

  <list-id>   Community List ID
  <rule-id>   Prefix List rule number

### Atrributes

  rt          Route Target Extended Community
  soo         Site of Origin Extended Community
  
## nv set router policy ext-community-list <list-id> rule <rule-id> ext-community rt <ext-community-id>

### Usage

  nv set router policy ext-community-list <list-id> rule <rule-id> ext-community rt <ext-community-id> [options]

### Description

  A extended community name

### Identifiers

  <list-id>           Community List ID
  <rule-id>           Prefix List rule number
  <ext-community-id>  Community number in AA:NN or IP:NN format
  
## nv set router policy ext-community-list <list-id> rule <rule-id> ext-community soo <ext-community-id>

### Usage

  nv set router policy ext-community-list <list-id> rule <rule-id> ext-community soo <ext-community-id> [options]

### Description

  A extended community name

### Identifiers

  <list-id>           Community List ID
  <rule-id>           Prefix List rule number
  <ext-community-id>  Community number in AA:NN or IP:NN format

## nv set router policy large-community-list <list-id>

### Usage

  nv set router policy large-community-list <list-id> [options] [<attribute> ...]

### Description

  A Large Community list used for matching community based BGP policies

### Identifiers

  <list-id>   Community List ID

### Atrributes

  rule        Large Community List rules
  
## nv set router policy large-community-list <list-id> rule <rule-id>

### Usage

  nv set router policy large-community-list <list-id> rule <rule-id> [options] [<attribute> ...]

### Description

  Large Community list Matching criteria and action rule

### Identifiers

  <list-id>        Community List ID
  <rule-id>        Prefix List rule number

### Atrributes

  large-community  Large Community expression
  action           Action to be taken for community list match
  
## nv set router policy large-community-list <list-id> rule <rule-id> large-community <large-community-id>

### Usage

  nv set router policy large-community-list <list-id> rule <rule-id> large-community <large-community-id> [options]

### Description

  Set of community names for large community list

### Identifiers

  <list-id>             Community List ID
  <rule-id>             Prefix List rule number
  <large-community-id>  Community number in AA:BB:CC format

## nv set router policy prefix-list <prefix-list-id>

### Usage

  nv set router policy prefix-list <prefix-list-id> [options] [<attribute> ...]

### Description

  A prefix list is used for matching IPv4 and IPv6 address prefixes.

### Identifiers

  <prefix-list-id>  Prefix List ID

### Atrributes

  rule              Prefix List rule
  type              prefix list type

## nv set router policy prefix-list <prefix-list-id> rule <rule-id>

### Usage

  nv set router policy prefix-list <prefix-list-id> rule <rule-id> [options] [<attribute> ...]

### Description

  Prefix list Matching criteria and action rule

### Identifiers

  <prefix-list-id>  Prefix List ID
  <rule-id>         Prefix List rule number

### Atrributes

  match             Prefix List rule
  action            Action to be taken for prefix list match

## nv set router policy prefix-list <prefix-list-id> rule <rule-id> match <match-id>
### Usage

  nv set router policy prefix-list <prefix-list-id> rule <rule-id> match <match-id> [options] [<attribute> ...]

### Description

  A prefix match

### Identifiers

  <prefix-list-id>  Prefix List ID
  <rule-id>         Prefix List rule number
  <match-id>        ip v4/v6 prefix, or any

### Atrributes

  max-prefix-len    Maximum prefix length to be matched
  min-prefix-len    Minimum prefix length to be matched

## nv set router policy prefix-list <prefix-list-id> rule <rule-id> match <match-id> min-prefix-len 0-128
### Usage

  nv set router policy prefix-list <prefix-list-id> rule <rule-id> match <match-id> min-prefix-len [options] 0-128

### Description

  Minimum prefix length to be matched

### Identifiers

  <prefix-list-id>  Prefix List ID
  <rule-id>         Prefix List rule number
  <match-id>        ip v4/v6 prefix, or any

## nv set router policy prefix-list <prefix-list-id> rule <rule-id> match <match-id> max-prefix-len 0-128

### Usage

  nv set router policy prefix-list <prefix-list-id> rule <rule-id> match <match-id> max-prefix-len [options] 0-128

### Description

  Maximum prefix length to be matched

### Identifiers

  <prefix-list-id>  Prefix List ID
  <rule-id>         Prefix List rule number
  <match-id>        ip v4/v6 prefix, or any

## nv set router policy route-map <route-map-id>

### Usage

  nv set router policy route-map <route-map-id> [options] [<attribute> ...]

### Description

  A route map is used for policy configuration.

### Identifiers

  <route-map-id>  Route Map ID

### Atrributes

  rule            Route Map rule

## nv set router policy route-map <route-map-id> rule <rule-id>

### Usage

  nv set router policy route-map <route-map-id> rule <rule-id> [options] [<attribute> ...]

### Description

  Route Map Matching/setting criteria and action rule

### Identifiers

  <route-map-id>  Route Map ID
  <rule-id>       Sequence to insert or delete from the route-map

### Atrributes

  match           Route Map match
  set             Route Map set
  action          Route Map set

## nv set router policy route-map <route-map-id> rule <rule-id> match

### Usage

  nv set router policy route-map <route-map-id> rule <rule-id> match [options] [<attribute> ...]

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

## nv set router policy route-map <route-map-id> rule <rule-id> match ip-prefix-list <instance-name>

### Usage

  nv set router policy route-map <route-map-id> rule <rule-id> match ip-prefix-list [options] <instance-name>

### Description

  IP prefix list

### Identifiers

  <route-map-id>  Route Map ID
  <rule-id>       Sequence to insert or delete from the route-map

## nv set router policy route-map <route-map-id> rule <rule-id> match ip-prefix-len 0-128

### Usage

  nv set router policy route-map <route-map-id> rule <rule-id> match ip-prefix-len [options] 0-128

### Description

  IP address prefix length

### Identifiers

  <route-map-id>  Route Map ID
  <rule-id>       Sequence to insert or delete from the route-map

## nv set router policy route-map <route-map-id> rule <rule-id> match ip-nexthop-list <instance-name>

### Usage

  nv set router policy route-map <route-map-id> rule <rule-id> match ip-nexthop-list [options] <instance-name>

### Description

  IP prefix list

### Identifiers

  <route-map-id>  Route Map ID
  <rule-id>       Sequence to insert or delete from the route-map

## nv set router policy route-map <route-map-id> rule <rule-id> match ip-nexthop-len 0-32

### Usage

  nv set router policy route-map <route-map-id> rule <rule-id> match ip-nexthop-len [options] 0-32

### Description

  IP nexthop prefix length

### Identifiers

  <route-map-id>  Route Map ID
  <rule-id>       Sequence to insert or delete from the route-map

## nv set router policy route-map <route-map-id> rule <rule-id> match ip-nexthop-type blackhole

### Usage

  nv set router policy route-map <route-map-id> rule <rule-id> match ip-nexthop-type [options] blackhole

### Description

  IP nexthop type

### Identifiers

  <route-map-id>  Route Map ID
  <rule-id>       Sequence to insert or delete from the route-map

## nv set router policy route-map <route-map-id> rule <rule-id> match as-path-list <instance-name>
### Usage

  nv set router policy route-map <route-map-id> rule <rule-id> match as-path-list [options] <instance-name>

### Description

  BGP AS path list

### Identifiers

  <route-map-id>  Route Map ID
  <rule-id>       Sequence to insert or delete from the route-map

## nv set router policy route-map <route-map-id> rule <rule-id> match community-list <instance-name>

### Usage

  nv set router policy route-map <route-map-id> rule <rule-id> match community-list [options] <instance-name>

### Description

  BGP community list

### Identifiers

  <route-map-id>  Route Map ID
  <rule-id>       Sequence to insert or delete from the route-map

## nv set router policy route-map <route-map-id> rule <rule-id> match large-community-list <instance-name>

### Usage

  nv set router policy route-map <route-map-id> rule <rule-id> match large-community-list [options] <instance-name>

### Description

  BGP large community list

### Identifiers

  <route-map-id>  Route Map ID
  <rule-id>       Sequence to insert or delete from the route-map

## nv set router policy route-map <route-map-id> rule <rule-id> match metric <value>

### Usage

  nv set router policy route-map <route-map-id> rule <rule-id> match metric [options] <value>

### Description

  Metric of route

### Identifiers

  <route-map-id>  Route Map ID
  <rule-id>       Sequence to insert or delete from the route-map

## nv set router policy route-map <route-map-id> rule <rule-id> match tag 1-4294967295

### Usage

  nv set router policy route-map <route-map-id> rule <rule-id> match tag [options] 1-4294967295

### Description

  Tag

### Identifiers

  <route-map-id>  Route Map ID
  <rule-id>       Sequence to insert or delete from the route-map

## nv set router policy route-map <route-map-id> rule <rule-id> match local-preference 0-4294967295

### Usage

  nv set router policy route-map <route-map-id> rule <rule-id> match local-preference [options] 0-4294967295

### Description

  Local preference of route

### Identifiers

  <route-map-id>  Route Map ID
  <rule-id>       Sequence to insert or delete from the route-map

## nv set router policy route-map <route-map-id> rule <rule-id> match evpn-vni <value>

### Usage

  nv set router policy route-map <route-map-id> rule <rule-id> match evpn-vni [options] <value>

### Description

  VNI ID

### Identifiers

  <route-map-id>  Route Map ID
  <rule-id>       Sequence to insert or delete from the route-map

## nv set router policy route-map <route-map-id> rule <rule-id> match source-vrf <vrf-name>

### Usage

  nv set router policy route-map <route-map-id> rule <rule-id> match source-vrf [options] <vrf-name>

### Description

  Source VRF

### Identifiers

  <route-map-id>  Route Map ID
  <rule-id>       Sequence to insert or delete from the route-map

## nv set router policy route-map <route-map-id> rule <rule-id> set

### Usage

  nv set router policy route-map <route-map-id> rule <rule-id> set [options] [<attribute> ...]

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

## nv set router policy route-map <route-map-id> rule <rule-id> set as-path-prepend

### Usage

  nv set router policy route-map <route-map-id> rule <rule-id> set as-path-prepend [options] [<attribute> ...]

### Description

  AS Path prepend

### Identifiers

  <route-map-id>  Route Map ID
  <rule-id>       Sequence to insert or delete from the route-map

### Atrributes

  as              AS number
  last-as         Number of times to insert peer's AS number

## nv set router policy route-map <route-map-id> rule <rule-id> set as-path-prepend as 1-4294967295

### Usage

  nv set router policy route-map <route-map-id> rule <rule-id> set as-path-prepend as [options] 1-4294967295

### Description

  AS number

### Identifiers

  <route-map-id>  Route Map ID
  <rule-id>       Sequence to insert or delete from the route-map

## nv set router policy route-map <route-map-id> rule <rule-id> set as-path-prepend last-as 1-10

### Usage

  nv set router policy route-map <route-map-id> rule <rule-id> set as-path-prepend last-as [options] 1-10

### Description

  Number of times to insert peer's AS number

### Identifiers

  <route-map-id>  Route Map ID
  <rule-id>       Sequence to insert or delete from the route-map

## nv set router policy route-map <route-map-id> rule <rule-id> set community <community-id>

### Usage

  nv set router policy route-map <route-map-id> rule <rule-id> set community <community-id> [options]

### Description

  BGP Community

### Identifiers

  <route-map-id>  Route Map ID
  <rule-id>       Sequence to insert or delete from the route-map
  <community-id>  Community number

## nv set router policy route-map <route-map-id> rule <rule-id> set large-community <large-community-id>

### Usage

  nv set router policy route-map <route-map-id> rule <rule-id> set large-community <large-community-id> [options]

### Description

  Large BGP Community

### Identifiers

  <route-map-id>        Route Map ID
  <rule-id>             Sequence to insert or delete from the route-map
  <large-community-id>  Large Community number

## nv set router policy route-map <route-map-id> rule <rule-id> set aggregator-as <asn-id>

### Usage

  nv set router policy route-map <route-map-id> rule <rule-id> set aggregator-as <asn-id> [options] [<attribute> ...]

### Description

  Aggregator AS Number

### Identifiers

  <route-map-id>  Route Map ID
  <rule-id>       Sequence to insert or delete from the route-map
  <asn-id>        Autonomous number

### Atrributes

  address         Set of IPv4 addresses

## nv set router policy route-map <route-map-id> rule <rule-id> set aggregator-as <asn-id> address <ipv4-address-id>

### Usage

  nv set router policy route-map <route-map-id> rule <rule-id> set aggregator-as <asn-id> address <ipv4-address-id> [options]

### Description

  An IPv4 address

### Identifiers

  <route-map-id>     Route Map ID
  <rule-id>          Sequence to insert or delete from the route-map
  <asn-id>           Autonomous number
  <ipv4-address-id>  IPv4 address
  
## nv set router policy route-map <route-map-id> rule <rule-id> set as-path-exclude 1-4294967295

### Usage

  nv set router policy route-map <route-map-id> rule <rule-id> set as-path-exclude [options] 1-4294967295

### Description

  Exclude from AS path

### Identifiers

  <route-map-id>  Route Map ID
  <rule-id>       Sequence to insert or delete from the route-map

## nv set router policy route-map <route-map-id> rule <rule-id> set ext-community-rt <route-distinguisher>

### Usage

  nv set router policy route-map <route-map-id> rule <rule-id> set ext-community-rt [options] <route-distinguisher>

### Description

  Route target extended community

### Identifiers

  <route-map-id>  Route Map ID
  <rule-id>       Sequence to insert or delete from the route-map

## nv set router policy route-map <route-map-id> rule <rule-id> set ext-community-soo <route-distinguisher>

### Usage

  nv set router policy route-map <route-map-id> rule <rule-id> set ext-community-soo [options] <route-distinguisher>

### Description

  Site of origin extended community

### Identifiers

  <route-map-id>  Route Map ID
  <rule-id>       Sequence to insert or delete from the route-map

## nv set router policy route-map <route-map-id> rule <rule-id> set local-preference 0-4294967295

### Usage

  nv set router policy route-map <route-map-id> rule <rule-id> set local-preference [options] 0-4294967295

### Description

  Local preference

### Identifiers

  <route-map-id>  Route Map ID
  <rule-id>       Sequence to insert or delete from the route-map

## nv set router policy route-map <route-map-id> rule <rule-id> set weight 0-4294967295

### Usage

  nv set router policy route-map <route-map-id> rule <rule-id> set weight [options] 0-4294967295

### Description

  BGP weight

### Identifiers

  <route-map-id>  Route Map ID
  <rule-id>       Sequence to insert or delete from the route-map

## nv set router policy route-map <route-map-id> rule <rule-id> set tag 1-4294967295

### Usage

  nv set router policy route-map <route-map-id> rule <rule-id> set tag [options] 1-4294967295

### Description

  Tag value for routing protocol

### Identifiers

  <route-map-id>  Route Map ID
  <rule-id>       Sequence to insert or delete from the route-map

## nv set router policy route-map <route-map-id> rule <rule-id> set ipv6-nexthop-global <ipv6>

### Usage

  nv set router policy route-map <route-map-id> rule <rule-id> set ipv6-nexthop-global [options] <ipv6>

### Description

  IPv6 nexthop global address

### Identifiers

  <route-map-id>  Route Map ID
  <rule-id>       Sequence to insert or delete from the route-map

## nv set router policy route-map <route-map-id> rule <rule-id> set ipv6-nexthop-local <ipv6>

### Usage

  nv set router policy route-map <route-map-id> rule <rule-id> set ipv6-nexthop-local [options] <ipv6>

### Description

  IPv6 nexthop local address

### Identifiers

  <route-map-id>  Route Map ID
  <rule-id>       Sequence to insert or delete from the route-map

## nv set router policy route-map <route-map-id> rule <rule-id> action

### Usage

  nv set router policy route-map <route-map-id> rule <rule-id> action [options] [<attribute> ...]

### Description

  Route map rule action

### Identifiers

  <route-map-id>  Route Map ID
  <rule-id>       Sequence to insert or delete from the route-map

### Atrributes

  deny            Deny action
  permit          Permit action

## nv set router policy route-map <route-map-id> rule <rule-id> action deny

### Usage

  nv set router policy route-map <route-map-id> rule <rule-id> action deny [options]

### Description

  State details

### Identifiers

  <route-map-id>  Route Map ID
  <rule-id>       Sequence to insert or delete from the route-map

## nv set router policy route-map <route-map-id> rule <rule-id> action permit

### Usage

  nv set router policy route-map <route-map-id> rule <rule-id> action permit [options] [<attribute> ...]

### Description

  permit action

### Identifiers

  <route-map-id>  Route Map ID
  <rule-id>       Sequence to insert or delete from the route-map

### Atrributes

  exit-policy     Permit action exit policy

## nv set router policy route-map <route-map-id> rule <rule-id> action permit exit-policy

### Usage

  nv set router policy route-map <route-map-id> rule <rule-id> action permit exit-policy [options] [<attribute> ...]

### Description

  Permit action exit policy

### Identifiers

  <route-map-id>  Route Map ID
  <rule-id>       Sequence to insert or delete from the route-map

### Atrributes

  rule            jump to specific rule

## nv set router policy route-map <route-map-id> rule <rule-id> action permit exit-policy rule <value>

### Usage

  nv set router policy route-map <route-map-id> rule <rule-id> action permit exit-policy rule [options] <value>

### Description

  jump to specific rule

### Identifiers

  <route-map-id>  Route Map ID
  <rule-id>       Sequence to insert or delete from the route-map

## nv set router bgp

### Usage

  nv set router bgp [options] [<attribute> ...]

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
                       
## nv set router bgp graceful-restart

### Usage

  nv set router bgp graceful-restart [options] [<attribute> ...]

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

## nv set router bgp graceful-restart restart-time 1-3600

### Usage

  nv set router bgp graceful-restart restart-time [options] 1-3600

### Description

  Amount of time taken to restart by router. It is advertised to the peer
  
## nv set router bgp graceful-restart path-selection-deferral-time 0-3600

### Usage

  nv set router bgp graceful-restart path-selection-deferral-time [options] 0-3600

### Description

  Used by the restarter as an upper-bounds for waiting for peering establishment and end-of-RIB from peers post restart before it starts path-selection.
  
## nv set router bgp graceful-restart stale-routes-time 1-3600

### Usage

  nv set router bgp graceful-restart stale-routes-time [options] 1-3600

### Description

  Specifies an upper-bounds on how long we retain routes from a restarting peer before flusing them.
  
## nv set router bgp convergence-wait

### Usage

  nv set router bgp convergence-wait [options] [<attribute> ...]

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
                       
## nv set router bgp convergence-wait time 0-3600

### Usage

  nv set router bgp convergence-wait time [options] 0-3600

### Description

  Time to wait for peers to send end-of-RIB before router performs path selection, install and advertisement. This is used during startup or when all peerings are flapped. 0 value means wait time is not configured
  
## nv set router bgp convergence-wait establish-wait-time 0-3600

### Usage

  nv set router bgp convergence-wait establish-wait-time [options] 0-3600

### Description

  Maximum time to wait to establish BGP sessions. Any peers which do not come up in this time are not tracked for the convergence-wait purposes. 0 value means there is no max time and peers are tracked for convergence time.
  
## nv set router bgp policy-update-timer 0-600

### Usage

  nv set router bgp policy-update-timer [options] 0-600

### Description

  Wait time in seconds before processing updates to policies to ensure that a series of changes are processed together.
  
## nv set router ospf

### Usage

  nv set router ospf [options] [<attribute> ...]

### Description

  OSPF global configuration.

### Atrributes

  timers      Timers
  enable      Turn the feature 'on' or 'off'. The default is 'off'.
  router-id   OSPF router-id for all VRFs, if a common one is used. If "none",
              then router-id must be set for every VRF. This is the default.
              
## nv set router ospf timers

### Usage

  nv set router ospf timers [options] [<attribute> ...]

### Description

  Timers

### Atrributes

  lsa         LSA timers
  spf         SPF timers
  refresh     defines interval (sec) to re-send lsas to keep from aging out.
  
## nv set router ospf timers lsa

### Usage

  nv set router ospf timers lsa [options] [<attribute> ...]

### Description

  LSA timers

### Atrributes

  min-arrival  Minimum delay in receiving new version of a LSA.
  throttle     Delay (msec) between sending LSAs.
  
## nv set router ospf timers lsa min-arrival 0-600000

### Usage

  nv set router ospf timers lsa min-arrival [options] 0-600000

### Description

  Minimum delay in receiving new version of a LSA.
  
## nv set router ospf timers lsa throttle 0-5000

### Usage

  nv set router ospf timers lsa throttle [options] 0-5000

### Description

  Delay (msec) between sending LSAs.

## nv set router ospf timers spf

### Usage

  nv set router ospf timers spf [options] [<attribute> ...]

### Description

  SPF timers

### Atrributes

  delay         Delay (msec) from first change received till SPF calculation.
  holdtime      Initial hold time (msec) between consecutive SPF calculations.
  max-holdtime  Maximum hold time (msec) between consecutive SPF calculations.
  
## nv set router ospf timers spf delay 0-600000

### Usage

  nv set router ospf timers spf delay [options] 0-600000

### Description

  Delay (msec) from first change received till SPF calculation.
  
## nv set router ospf timers spf holdtime 0-600000

### Usage

  nv set router ospf timers spf holdtime [options] 0-600000

### Description

  Initial hold time (msec) between consecutive SPF calculations.
  
## nv set router ospf timers spf max-holdtime 0-600000

### Usage

  nv set router ospf timers spf max-holdtime [options] 0-600000

### Description

  Maximum hold time (msec) between consecutive SPF calculations.

## nv set router ospf timers refresh 10-1800

### Usage

  nv set router ospf timers refresh [options] 10-1800

### Description

  defines interval (sec) to re-send lsas to keep from aging out.
  
## nv set router pim

### Usage

  nv set router pim [options] [<attribute> ...]

### Description

  PIM global configuration.

### Atrributes

  timers      Timers
  enable      Turn the feature 'on' or 'off'. The default is 'off'.
  packets     Number of incoming packet processing from neighbor.
  
## nv set router pim timers

### Usage

  nv set router pim timers [options] [<attribute> ...]

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
  
## nv set router pim timers hello-interval 1-180

### Usage

  nv set router pim timers hello-interval [options] 1-180

### Description

  PIM Hello packets periodic interval. Holdtime is 3.5 times the hello-interval, the amount of time neighbor must kept in reachable state.
  
## nv set router pim timers register-suppress 5-60000

### Usage

  nv set router pim timers register-suppress [options] 5-60000

### Description

  FHR supresses the register msg transmit to RP, in seconds
  
## nv set router pim timers join-prune-interval 60-600

### Usage

  nv set router pim timers join-prune-interval [options] 60-600

### Description

  Periodic multicast Join/Prune msg, in seconds
  
## nv set router pim timers keep-alive 31-60000

### Usage

  nv set router pim timers keep-alive [options] 31-60000

### Description

  Timeout value for S,G stream, in seconds
  
## nv set router pim timers rp-keep-alive 31-60000

### Usage

  nv set router pim timers rp-keep-alive [options] 31-60000

### Description

  RP's timeout value, in seconds
  
## nv set router pim packets 1-100

### Usage

  nv set router pim packets [options] 1-100

### Description

  Number of incoming packet processing from neighbor.
  
## nv set router igmp

### Usage

  nv set router igmp [options] [<attribute> ...]

### Description

  IGMP global configuration.

### Atrributes

  enable      Turn the feature 'on' or 'off'. The default is 'off'.
  
## nv set router vrrp

### Usage

  nv set router vrrp [options] [<attribute> ...]

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

## nv set router vrrp priority 1-254

### Usage

  nv set router vrrp priority [options] 1-254

### Description

  Specifies the sending VRRP interface's priority for the virtual router. Higher values equal higher priority

## nv set router vrrp advertisement-interval 10-40950

### Usage

  nv set router vrrp advertisement-interval [options] 10-40950

### Description

  Sets the interval between successive VRRP advertisements -- RFC 5798 defines this as a 12-bit value expressed as 0.1 seconds, with default 1000 milliseconds, i.e., 1 second. Represented in units of milliseconds
  
## nv set router vrr

### Usage

  nv set router vrr [options] [<attribute> ...]

### Description

  VRR global configuration.

### Atrributes

  enable      Turn the feature 'on' or 'off'. The default is 'off'.
  
## nv set router adaptive-routing

### Usage

  nv set router adaptive-routing [options] [<attribute> ...]

### Description

  Adaptive routing global configuration.

### Atrributes

  enable      Turn the feature 'on' or 'off'. The default is 'off'.

## nv set platform

### Usage

  nv set platform [options] [<attribute> ...]

### Description

  Top-level container for the components in the system. This node represents a system component inventory, which includes hardware and software elements.

### Atrributes

  hardware    The platform's hardware

## nv set platform hardware

### Usage

  nv set platform hardware [options] [<attribute> ...]

### Description

  Set of components making up the platform.

### Atrributes

  component   A component in the platform.

## nv set platform hardware component <component-id>

### Usage

  nv set platform hardware component <component-id> [options] [<attribute> ...]

### Description

  A component in the platform.

### Identifiers

  <component-id>  Component identifier

### Atrributes

  linecard        Properties of a linecard component
  admin-state     The component's admin state
  type            The type of this component

## nv set platform hardware component <component-id> linecard

### Usage

  nv set platform hardware component <component-id> linecard [options] [<attribute> ...]

### Description

  Properties of a linecard component

### Identifiers

  <component-id>  Component identifier

### Atrributes

  provision       Provision linecard types

## nv set bridge

### Usage

  nv set bridge [options] [<attribute> ...]

### Description

  Properties associated with an instance of a bridge.

### Atrributes

  domain      Bridge domains

## nv set bridge domain <domain-id>

### Usage

  nv set bridge domain <domain-id> [options] [<attribute> ...]

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

## nv set bridge domain <domain-id> stp

### Usage

  nv set bridge domain <domain-id> stp [options] [<attribute> ...]

### Description

  attributes related to global stp

### Identifiers

  <domain-id>  Domain

### Atrributes

  state        The state of STP on the bridge
  priority     stp priority. The priority value must be a number between 4096
               and 32768 and a multiple of 4096.

## nv set bridge domain <domain-id> stp priority 4096-61440

### Usage

  nv set bridge domain <domain-id> stp priority [options] 4096-61440

### Description

  stp priority. The priority value must be a number between 4096 and 32768 and a multiple of 4096.

### Identifiers

  <domain-id>  Domain.

## nv set bridge domain <domain-id> multicast

### Usage

  nv set bridge domain <domain-id> multicast [options] [<attribute> ...]

### Description

  Configure multicast on the bridge

### Identifiers

  <domain-id>  Domain

### Atrributes

  snooping     IGMP/MLD snooping configuration

## nv set bridge domain <domain-id> multicast snooping

### Usage

  nv set bridge domain <domain-id> multicast snooping [options] [<attribute> ...]

### Description

  IGMP/MLD snooping configuration

### Identifiers

  <domain-id>  Domain

### Atrributes

  querier      IGMP/MLD querier configuration
  enable       Turn the feature 'on' or 'off'. The default is 'off'.
  
## nv set bridge domain <domain-id> multicast snooping querier

### Usage

  nv set bridge domain <domain-id> multicast snooping querier [options] [<attribute> ...]

### Description

  IGMP/MLD querier configuration

### Identifiers

  <domain-id>  Domain

### Atrributes

  enable       Turn the feature 'on' or 'off'. The default is 'off'.

## nv set bridge domain <domain-id> vlan <vid>

### Usage

  nv set bridge domain <domain-id> vlan <vid> [options] [<attribute> ...]

### Description

  A VLAN tag identifier

### Identifiers

  <domain-id>  Domain
  <vid>        VLAN ID

### Atrributes

  vni          L2 VNI
  ptp          VLAN PTP configuration. Inherited by interfaces in this VLAN.
  multicast    Configure multicast on the vlan

## nv set bridge domain <domain-id> vlan <vid> vni <vni-id>

### Usage

  nv set bridge domain <domain-id> vlan <vid> vni <vni-id> [options] [<attribute> ...]

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

## nv set bridge domain <domain-id> vlan <vid> vni <vni-id> flooding

### Usage

  nv set bridge domain <domain-id> vlan <vid> vni <vni-id> flooding [options] [<attribute> ...]

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

## nv set bridge domain <domain-id> vlan <vid> vni <vni-id> flooding head-end-replication <hrep-id>

### Usage

  nv set bridge domain <domain-id> vlan <vid> vni <vni-id> flooding head-end-replication <hrep-id> [options]

### Description

  Set of IPv4 unicast addresses or "evpn".

### Identifiers

  <domain-id>  Domain
  <vid>        VLAN ID
  <vni-id>     VxLAN ID
  <hrep-id>    IPv4 unicast addresses or "evpn"

## nv set bridge domain <domain-id> vlan <vid> vni <vni-id> flooding multicast-group <ipv4-multicast>

### Usage

  nv set bridge domain <domain-id> vlan <vid> vni <vni-id> flooding multicast-group [options] <ipv4-multicast>

### Description

  BUM traffic is sent to the specified multicast group and will be received by receivers who are interested in that group. This usually requires PIM-SM to be used in the network.

### Identifiers

  <domain-id>  Domain
  <vid>        VLAN ID
  <vni-id>     VxLAN ID

## nv set bridge domain <domain-id> vlan <vid> ptp

### Usage

  nv set bridge domain <domain-id> vlan <vid> ptp [options] [<attribute> ...]

### Description

  VLAN PTP configuration.  Inherited by interfaces in this VLAN.

### Identifiers

  <domain-id>  Domain
  <vid>        VLAN ID

### Atrributes

  enable       Turn the feature 'on' or 'off'. The default is 'off'.

## nv set bridge domain <domain-id> vlan <vid> multicast

### Usage

  nv set bridge domain <domain-id> vlan <vid> multicast [options] [<attribute> ...]

### Description

  Configure multicast on the vlan

### Identifiers

  <domain-id>  Domain
  <vid>        VLAN ID

### Atrributes

  snooping     IGMP/MLD snooping configuration

## nv set bridge domain <domain-id> vlan <vid> multicast snooping

### Usage

  nv set bridge domain <domain-id> vlan <vid> multicast snooping [options] [<attribute> ...]

### Description

  IGMP/MLD snooping configuration

### Identifiers

  <domain-id>  Domain
  <vid>        VLAN ID

### Atrributes

  querier      IGMP/MLD querier configuration## nv set bridge domain <domain-id> vlan <vid> multicast snooping querier

### Usage

  nv set bridge domain <domain-id> vlan <vid> multicast snooping querier [options] [<attribute> ...]

### Description

  IGMP/MLD querier configuration

### Identifiers

  <domain-id>  Domain
  <vid>        VLAN ID

### Atrributes

  source-ip    Source IP to use when sending IGMP/MLD queries.
  
## nv set bridge domain <domain-id> vlan <vid> multicast snooping querier source-ip <ipv4>

### Usage

  nv set bridge domain <domain-id> vlan <vid> multicast snooping querier source-ip [options] <ipv4>

### Description

  Source IP to use when sending IGMP/MLD queries.

### Identifiers

  <domain-id>  Domain
  <vid>        VLAN ID
  
## nv set bridge domain <domain-id> type vlan-aware

### Usage

  nv set bridge domain <domain-id> type [options] vlan-aware

### Description

  Type of bridge domain.

### Identifiers

  <domain-id>  Domai
  
## nv set bridge domain <domain-id> encap 802.1Q

### Usage

  nv set bridge domain <domain-id> encap [options] 802.1Q

### Description

  Interfaces added to this domain will, by default, use this encapsulation.

### Identifiers

  <domain-id>  Domain
  
## nv set bridge domain <domain-id> vlan-vni-offset 0-16773120

### Usage

  nv set bridge domain <domain-id> vlan-vni-offset [options] 0-16773120

### Description

  A VNI offset while (automatically) mapping VLANs to VNIs

### Identifiers

  <domain-id>  Domain
  
## nv set mlag

### Usage

  nv set mlag [options] [<attribute> ...]

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

## nv set mlag lacp-conflict

### Usage

  nv set mlag lacp-conflict [options]

### Description

  Configure the mlag lacp-conflict parameters
  
## nv set mlag backup <backup-ip>

### Usage

  nv set mlag backup <backup-ip> [options] [<attribute> ...]

### Description

  alternative ip address or interface for peer to reach us

### Identifiers

  <backup-ip>  Backup IP of MLAG peer

### Atrributes

  vrf          The backup IP's VRF.
  
## nv set mlag backup <backup-ip> vrf <vrf-name>

### Usage

  nv set mlag backup <backup-ip> vrf [options] <vrf-name>

### Description

  The backup IP's VRF.

### Identifiers

  <backup-ip>  Backup IP of MLAG peer
  
## nv set mlag priority 0-65535

### Usage

  nv set mlag priority [options] 0-65535

### Description

  Mlag Priority
  
## nv set mlag init-delay 0-900

### Usage

  nv set mlag init-delay [options] 0-900

### Description

  The delay, in seconds, before bonds are brought up.## nv set evpn

### Usage

  nv set evpn [options] [<attribute> ...]

### Description

  Enables the EVPN control plane.  When enabled, it also means that the EVPN service offered is vlan-based service and an EVI is auto-created for each extended VLAN.

### Atrributes

  route-advertise  Route advertising
  dad              Advertise
  evi              EVI
  multihoming      Multihoming global configuration parameters
  enable           Turn the feature 'on' or 'off'. The default is 'off'.
  
## nv set evpn route-advertise

### Usage

  nv set evpn route-advertise [options] [<attribute> ...]

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

## nv set evpn dad

### Usage

  nv set evpn dad [options] [<attribute> ...]

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
  
## nv set evpn dad duplicate-action

### Usage

  nv set evpn dad duplicate-action [options] [<attribute> ...]

### Description

  Handling of BUM traffic

### Atrributes

  freeze      Further move events for the MAC will not be acted upon.
  
## nv set evpn dad duplicate-action freeze

### Usage

  nv set evpn dad duplicate-action freeze [options] [<attribute> ...]

### Description

  Advertise

### Atrributes

  duration    Freeze the MAC for the specified duration or, if 'permanent'
              until the operator intervenes.
              
## nv set evpn dad mac-move-threshold 2-1000

### Usage

  nv set evpn dad mac-move-threshold [options] 2-1000

### Description

  Number of MAC moves within a time window before the MAC is flagged as a possible duplicate.
  
## nv set evpn dad move-window 2-1800

### Usage

  nv set evpn dad move-window [options] 2-1800

### Description

  Time window during which the move threshold applies
  
## nv set evpn evi <evi-id>

### Usage

  nv set evpn evi <evi-id> [options] [<attribute> ...]

### Description

  Enables the EVPN control plane.  When enabled, it also means that the EVPN service offered is vlan-based service and an EVI is auto-created for each extended VLAN.

### Identifiers

  <evi-id>         VRF

### Atrributes

  route-advertise  Route advertise
  route-target     Route targets
  rd               BGP Route Distinguisher to use for EVPN type-5 routes
                   originated for this VRF.
                   
## nv set evpn evi <evi-id> route-advertise

### Usage

  nv set evpn evi <evi-id> route-advertise [options] [<attribute> ...]

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
                   
## nv set evpn evi <evi-id> route-target

### Usage

  nv set evpn evi <evi-id> route-target [options] [<attribute> ...]

### Description

  EVPN control plane config and info for VRF

### Identifiers

  <evi-id>    VRF

### Atrributes

  export      Route targets to export
  import      Route targets to import
  both        Route targets to import and export
  
## nv set evpn evi <evi-id> route-target export <rt-id>

### Usage

  nv set evpn evi <evi-id> route-target export <rt-id> [options]

### Description

  A route target identifier

### Identifiers

  <evi-id>    VRF
  <rt-id>     Route target ID
  
## nv set evpn evi <evi-id> route-target import <rt-id>

### Usage

  nv set evpn evi <evi-id> route-target import <rt-id> [options]

### Description

  A route target identifier

### Identifiers

  <evi-id>    VRF
  <rt-id>     Route target ID
  
## nv set evpn evi <evi-id> route-target both <rt-id>

### Usage

  nv set evpn evi <evi-id> route-target both <rt-id> [options]

### Description

  A route target identifier

### Identifiers

  <evi-id>    VRF
  <rt-id>     Route target ID
  
## nv set evpn multihoming

### Usage

  nv set evpn multihoming [options] [<attribute> ...]

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
                     
## nv set evpn multihoming ead-evi-route

### Usage

  nv set evpn multihoming ead-evi-route [options] [<attribute> ...]

### Description

  Ethernet Auto-discovery per EVPN instance routes

### Atrributes

  rx          Disable EAD-per-EVI at receiving end.
  tx          Suppress advertisement of EAD-per-EVI routes.
  
## nv set evpn multihoming segment

### Usage

  nv set evpn multihoming segment [options] [<attribute> ...]

### Description

  Multihoming interface segment

### Atrributes

  df-preference  Designated forwarder preference value.
  mac-address    MAC address per ethernet segment. Required.
  
## nv set evpn multihoming segment mac-address <mac>

### Usage

  nv set evpn multihoming segment mac-address [options] <mac>

### Description

  MAC address per ethernet segment.  Required.
  
## nv set evpn multihoming segment df-preference 1-65535

### Usage

  nv set evpn multihoming segment df-preference [options] 1-65535

### Description

  Designated forwarder preference value.
  
## nv set evpn multihoming mac-holdtime 0-86400

### Usage

  nv set evpn multihoming mac-holdtime [options] 0-86400

### Description

  During this interval, the switch attempts to independently establish reachability of the MAC on the local ethernet segment. If 'none', there is no holdtime.
  
## nv set evpn multihoming neighbor-holdtime 0-86400

### Usage

  nv set evpn multihoming neighbor-holdtime [options] 0-86400

### Description

  During this interval, the switch attempts to independently establish reachability of the host on the local ethernet segment.
  
## nv set evpn multihoming startup-delay 0-3600

### Usage

  nv set evpn multihoming startup-delay [options] 0-3600

### Description

  The duration for which a switch holds the Ethernet segment-bond in a protodown state after a reboot or process restart.
  
## nv set qos

### Usage

  nv set qos [options] [<attribute> ...]

### Description

  QOS

### Atrributes

  roce        Properties associated with the RDMA over Converged Ethernet
              (RoCE) feature.
              
## nv set qos roce

### Usage

  nv set qos roce [options] [<attribute> ...]

### Description

  Properties associated with the RDMA over Converged Ethernet (RoCE) feature.

### Atrributes

  enable        Turn the feature 'on' or 'off'. The default is 'off'.
  mode          Roce Mode
  cable-length  Cable Length(in meters) for Roce Lossless Config
  
## nv set qos roce cable-length 1-100000

### Usage

  nv set qos roce cable-length [options] 1-100000

### Description

  Cable Length(in meters) for Roce Lossless Config
  
## nv set interface <interface-id>

### Usage

  nv set interface <interface-id> [options] [<attribute> ...]

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

## nv set interface <interface-id> router

### Usage

  nv set interface <interface-id> router [options] [<attribute> ...]

### Description

  interface router

### Identifiers

  <interface-id>    Interface

### Atrributes

  pbr               PBR interface configuration.
  ospf              OSPF interface configuration.
  pim               PIM interface configuration.
  adaptive-routing  Adaptive routing interface configuration.

## nv set interface <interface-id> router pbr

### Usage

  nv set interface <interface-id> router pbr [options] [<attribute> ...]

### Description

  PBR interface configuration.

### Identifiers

  <interface-id>  Interface

### Atrributes

  map             PBR map to use on this interface

## nv set interface <interface-id> router pbr map <pbr-map-id>

### Usage

  nv set interface <interface-id> router pbr map <pbr-map-id> [options]

### Description

  Interface Pbr map

### Identifiers

  <interface-id>  Interface
  <pbr-map-id>    Route Map ID

## nv set interface <interface-id> router ospf

### Usage

  nv set interface <interface-id> router ospf [options] [<attribute> ...]

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

## nv set interface <interface-id> router ospf timers

### Usage

  nv set interface <interface-id> router ospf timers [options] [<attribute> ...]

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
  
## nv set interface <interface-id> router ospf timers hello-multiplier 1-10

### Usage

  nv set interface <interface-id> router ospf timers hello-multiplier [options] 1-10

### Description

  Required and only valid if `dead-interval` is `minimal`.

### Identifiers

  <interface-id>  Interface

## nv set interface <interface-id> router ospf timers hello-interval 1-65535

### Usage

  nv set interface <interface-id> router ospf timers hello-interval [options] 1-65535

### Description

  How often to transmit a hello packet, in seconds.  Only valid if `dead-interval` is not `minimal`.

### Identifiers

  <interface-id>  Interface

## nv set interface <interface-id> router ospf timers retransmit-interval 1-65535

### Usage

  nv set interface <interface-id> router ospf timers retransmit-interval [options] 1-65535

### Description

  How often to retransmit a packet not acknowledged, in seconds

### Identifiers

  <interface-id>  Interface

## nv set interface <interface-id> router ospf timers transmit-delay 1-65535

### Usage

  nv set interface <interface-id> router ospf timers transmit-delay [options] 1-65535

### Description

  Delay before sending a new lsa, in seconds

### Identifiers

  <interface-id>  Interface

## nv set interface <interface-id> router ospf authentication

### Usage

  nv set interface <interface-id> router ospf authentication [options] [<attribute> ...]

### Description

  md5 authentication configuration

### Identifiers

  <interface-id>      Interface

### Atrributes

  enable              Turn the feature 'on' or 'off'. The default is 'off'.
  md5-key             md5 key
  message-digest-key  Message digest key

## nv set interface <interface-id> router ospf authentication message-digest-key 1-255

### Usage

  nv set interface <interface-id> router ospf authentication message-digest-key [options] 1-255

### Description

  Message digest key

### Identifiers

  <interface-id>  Interface

## nv set interface <interface-id> router ospf authentication md5-key <value>

### Usage

  nv set interface <interface-id> router ospf authentication md5-key [options] <value>

### Description

  md5 key

### Identifiers

  <interface-id>  Interface

## nv set interface <interface-id> router ospf bfd

### Usage

  nv set interface <interface-id> router ospf bfd [options] [<attribute> ...]

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

## nv set interface <interface-id> router ospf bfd detect-multiplier 2-255

### Usage

  nv set interface <interface-id> router ospf bfd detect-multiplier [options] 2-255

### Description

  Detect multiplier value

### Identifiers

  <interface-id>  Interface

## nv set interface <interface-id> router ospf bfd min-receive-interval 50-60000

### Usage

  nv set interface <interface-id> router ospf bfd min-receive-interval [options] 50-60000

### Description

  Minimum receive interval in milliseconds

### Identifiers

  <interface-id>  Interface

## nv set interface <interface-id> router ospf bfd min-transmit-interval 50-60000

### Usage

  nv set interface <interface-id> router ospf bfd min-transmit-interval [options] 50-60000

### Description

  Minimum transmit interval in milliseconds

### Identifiers

  <interface-id>  Interface

## nv set interface <interface-id> router ospf priority 0-255

### Usage

  nv set interface <interface-id> router ospf priority [options] 0-255

### Description

  Eligibility of this router to become DR on multi-access network

### Identifiers

  <interface-id>  Interface

## nv set interface <interface-id> router pim

### Usage

  nv set interface <interface-id> router pim [options] [<attribute> ...]

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

## nv set interface <interface-id> router pim timers

### Usage

  nv set interface <interface-id> router pim timers [options] [<attribute> ...]

### Description

  Timers

### Identifiers

  <interface-id>  Interface

### Atrributes

  hello-interval  PIM Hello packets periodic interval. If "auto", inherit from
                  the VRF. This is the default. Holdtime is 3.5 times the
                  hello-interval, the amount of time neighbor must kept in
                  reachable state.

## nv set interface <interface-id> router pim bfd

### Usage

  nv set interface <interface-id> router pim bfd [options] [<attribute> ...]

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

## nv set interface <interface-id> router pim bfd detect-multiplier 2-255

### Usage

  nv set interface <interface-id> router pim bfd detect-multiplier [options] 2-255

### Description

  Detect multiplier value

### Identifiers

  <interface-id>  Interface

## nv set interface <interface-id> router pim bfd min-receive-interval 50-60000

### Usage

  nv set interface <interface-id> router pim bfd min-receive-interval [options] 50-60000

### Description

  Minimum receive interval in milliseconds

### Identifiers

  <interface-id>  Interface

## nv set interface <interface-id> router pim bfd min-transmit-interval 50-60000

### Usage

  nv set interface <interface-id> router pim bfd min-transmit-interval [options] 50-60000

### Description

  Minimum transmit interval in milliseconds

### Identifiers

  <interface-id>  Interface

## nv set interface <interface-id> router pim address-family

### Usage

  nv set interface <interface-id> router pim address-family [options] [<attribute> ...]

### Description

  Address family specific configuration

### Identifiers

  <interface-id>  Interface

### Atrributes

  ipv4-unicast    IPv4 unicast address family

## nv set interface <interface-id> router pim address-family ipv4-unicast

### Usage

  nv set interface <interface-id> router pim address-family ipv4-unicast [options] [<attribute> ...]

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

## nv set interface <interface-id> router pim address-family ipv4-unicast allow-rp

### Usage

  nv set interface <interface-id> router pim address-family ipv4-unicast allow-rp [options] [<attribute> ...]

### Description

  Allow RP feature, which allows RP address to be accepts for the received

### Identifiers

  <interface-id>  Interface

### Atrributes

  enable          Turn the feature 'on' or 'off'. The default is 'off'.
  rp-list         The prefix-list provides the list of group addresses to
                  accept downstream (*,G) joins and propogate towards the
                  allowed-rp.

## nv set interface <interface-id> router pim dr-priority 1-4294967295

### Usage

  nv set interface <interface-id> router pim dr-priority [options] 1-4294967295

### Description

  Designated Router Election priority.

### Identifiers

  <interface-id>  Interface

## nv set interface <interface-id> router adaptive-routing

### Usage

  nv set interface <interface-id> router adaptive-routing [options] [<attribute> ...]

### Description

  Adaptive routing interface configuration.

### Identifiers

  <interface-id>        Interface

### Atrributes

  enable                Turn the feature 'on' or 'off'. The default is 'off'.
  link-utilization-threshold
                        Link utilization threshold percentage

## nv set interface <interface-id> router adaptive-routing link-utilization-threshold 1-100

### Usage

  nv set interface <interface-id> router adaptive-routing link-utilization-threshold [options] 1-100

### Description

  Link utilization threshold percentage

### Identifiers

  <interface-id>  Interface

## nv set interface <interface-id> bond

### Usage

  nv set interface <interface-id> bond [options] [<attribute> ...]

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

## nv set interface <interface-id> bond member <member-id>

### Usage

  nv set interface <interface-id> bond member <member-id> [options]

### Description

  A bond member

### Identifiers

  <interface-id>  Interface
  <member-id>     Bond memer interface

## nv set interface <interface-id> bond mlag

### Usage

  nv set interface <interface-id> bond mlag [options] [<attribute> ...]

### Description

  MLAG configuration on the bond interface

### Identifiers

  <interface-id>  Interface

### Atrributes

  lacp-conflict   Configure the mlag lacp-conflict parameters
  enable          Turn the feature 'on' or 'off'. The default is 'off'.
  id              MLAG id

## nv set interface <interface-id> bond mlag lacp-conflict

### Usage

  nv set interface <interface-id> bond mlag lacp-conflict [options]

### Description

  Configure the mlag lacp-conflict parameters

### Identifiers

  <interface-id>  Interface

## nv set interface <interface-id> bond down-delay 0-65535

### Usage

  nv set interface <interface-id> bond down-delay [options] 0-65535

### Description

  bond down delay

### Identifiers

  <interface-id>  Interface

## nv set interface <interface-id> bond up-delay 0-65535

### Usage

  nv set interface <interface-id> bond up-delay [options] 0-65535

### Description

  bond up delay

### Identifiers

  <interface-id>  Interface

## nv set interface <interface-id> bridge

### Usage

  nv set interface <interface-id> bridge [options] [<attribute> ...]

### Description

  attributed related to a bridged interface

### Identifiers

  <interface-id>  Interface

### Atrributes

  domain          Bridge domains on this interface

## nv set interface <interface-id> bridge domain <domain-id>

### Usage

  nv set interface <interface-id> bridge domain <domain-id> [options] [<attribute> ...]

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

## nv set interface <interface-id> bridge domain <domain-id> stp

### Usage

  nv set interface <interface-id> bridge domain <domain-id> stp [options] [<attribute> ...]

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

## nv set interface <interface-id> bridge domain <domain-id> vlan <vid>

### Usage

  nv set interface <interface-id> bridge domain <domain-id> vlan <vid> [options]

### Description

  A VLAN tag identifier

### Identifiers

  <interface-id>  Interface
  <domain-id>     Domain
  <vid>           VLAN ID, or all

## nv set interface <interface-id> ip

### Usage

  nv set interface <interface-id> ip [options] [<attribute> ...]

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
  
## nv set interface <interface-id> ip address <ip-prefix-id>

### Usage

  nv set interface <interface-id> ip address <ip-prefix-id> [options]

### Description

  An IP address with prefix

### Identifiers

  <interface-id>  Interface
  <ip-prefix-id>  IPv4 or IPv6 address and route prefix in CIDR notation

## nv set interface <interface-id> ip vrr

### Usage

  nv set interface <interface-id> ip vrr [options] [<attribute> ...]

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

## nv set interface <interface-id> ip vrr address <ip-prefix-id>

### Usage

  nv set interface <interface-id> ip vrr address <ip-prefix-id> [options]

### Description

  An IP address with prefix

### Identifiers

  <interface-id>  Interface
  <ip-prefix-id>  IPv4 or IPv6 address and route prefix in CIDR notation

## nv set interface <interface-id> ip gateway <ip-address-id>

### Usage

  nv set interface <interface-id> ip gateway <ip-address-id> [options]

### Description

  An IP address

### Identifiers

  <interface-id>   Interface
  <ip-address-id>  IPv4 or IPv6 address
  
## nv set interface <interface-id> ip ipv4

### Usage

  nv set interface <interface-id> ip ipv4 [options] [<attribute> ...]

### Description

  IPv4 configuration for an interface

### Identifiers

  <interface-id>  Interface

### Atrributes

  forward         Enable or disable forwarding.

## nv set interface <interface-id> ip ipv6

### Usage

  nv set interface <interface-id> ip ipv6 [options] [<attribute> ...]

### Description

  IPv6 configuration for an interface

### Identifiers

  <interface-id>  Interface

### Atrributes

  enable          Turn the feature 'on' or 'off'. The default is 'on'.
  forward         Enable or disable forwarding.

## nv set interface <interface-id> ip igmp

### Usage

  nv set interface <interface-id> ip igmp [options] [<attribute> ...]

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

## nv set interface <interface-id> ip igmp static-group <static-group-id>

### Usage

  nv set interface <interface-id> ip igmp static-group <static-group-id> [options] [<attribute> ...]

### Description

  IGMP static multicast mroute

### Identifiers

  <interface-id>     Interface
  <static-group-id>  IGMP static multicast mroute destination

### Atrributes

  source-address     IGMP static multicast mroute source.
  
## nv set interface <interface-id> ip igmp static-group <static-group-id> source-address <ipv4-unicast>

### Usage

  nv set interface <interface-id> ip igmp static-group <static-group-id> source-address [options] <ipv4-unicast>

### Description

  IGMP static multicast mroute source.

### Identifiers

  <interface-id>     Interface
  <static-group-id>  IGMP static multicast mroute destination
  
## nv set interface <interface-id> ip igmp query-interval 1-1800

### Usage

  nv set interface <interface-id> ip igmp query-interval [options] 1-1800

### Description

  Query interval, in seconds.

### Identifiers

  <interface-id>  Interface

## nv set interface <interface-id> ip igmp query-max-response-time 10-250

### Usage

  nv set interface <interface-id> ip igmp query-max-response-time [options] 10-250

### Description

  Max query response time, in seconds.

### Identifiers

  <interface-id>  Interface

## nv set interface <interface-id> ip igmp last-member-query-interval 1-255

### Usage

  nv set interface <interface-id> ip igmp last-member-query-interval [options] 1-255

### Description

  Last member query interval.

### Identifiers

  <interface-id>  Interface

## nv set interface <interface-id> ip vrrp

### Usage

  nv set interface <interface-id> ip vrrp [options] [<attribute> ...]

### Description

  Configuration for VRRP

### Identifiers

  <interface-id>  Interface

### Atrributes

  virtual-router  Group of virtual gateways implemented with VRRP
  enable          Turn the feature 'on' or 'off'. The default is 'off'.

## nv set interface <interface-id> ip vrrp virtual-router <virtual-router-id>

### Usage

  nv set interface <interface-id> ip vrrp virtual-router <virtual-router-id> [options] [<attribute> ...]

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

## nv set interface <interface-id> ip vrrp virtual-router <virtual-router-id> address <ip-address-id>

### Usage

  nv set interface <interface-id> ip vrrp virtual-router <virtual-router-id> address <ip-address-id> [options]

### Description

  An IP address

### Identifiers

  <interface-id>       Interface
  <virtual-router-id>  Virtual Router IDentifier (VRID)
  <ip-address-id>      IPv4 or IPv6 address

## nv set interface <interface-id> ip neighbor-discovery

### Usage

  nv set interface <interface-id> ip neighbor-discovery [options] [<attribute> ...]

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

## nv set interface <interface-id> ip neighbor-discovery rdnss <ipv6-address-id>

### Usage

  nv set interface <interface-id> ip neighbor-discovery rdnss <ipv6-address-id> [options] [<attribute> ...]

### Description

  A recursive DNS server

### Identifiers

  <interface-id>     Interface
  <ipv6-address-id>  IPv6 address

### Atrributes

  lifetime           Maximum time in seconds for which the server may be used
                     for domain name resolution
                     
## nv set interface <interface-id> ip neighbor-discovery prefix <ipv6-prefix-id>

### Usage

  nv set interface <interface-id> ip neighbor-discovery prefix <ipv6-prefix-id> [options] [<attribute> ...]

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
                      
## nv set interface <interface-id> ip neighbor-discovery prefix <ipv6-prefix-id> valid-lifetime 0-4294967295

### Usage

  nv set interface <interface-id> ip neighbor-discovery prefix <ipv6-prefix-id> valid-lifetime [options] 0-4294967295

### Description

  Time in seconds the prefix is valid for on-link determination

### Identifiers

  <interface-id>    Interface
  <ipv6-prefix-id>  IPv6 address and route prefix in CIDR notation

## nv set interface <interface-id> ip neighbor-discovery prefix <ipv6-prefix-id> preferred-lifetime 0-4294967295

### Usage

  nv set interface <interface-id> ip neighbor-discovery prefix <ipv6-prefix-id> preferred-lifetime [options] 0-4294967295

### Description

  Time in seconds that addresses generated from a prefix remain preferred

### Identifiers

  <interface-id>    Interface
  <ipv6-prefix-id>  IPv6 address and route prefix in CIDR notation

## nv set interface <interface-id> ip neighbor-discovery dnssl <domain-name-id>

### Usage

  nv set interface <interface-id> ip neighbor-discovery dnssl <domain-name-id> [options] [<attribute> ...]

### Description

  A DNS search list

### Identifiers

  <interface-id>    Interface
  <domain-name-id>  The domain portion of a hostname (RFC 1123) or an
                    internationalized hostname (RFC 5890).

### Atrributes

  lifetime          Maximum time in seconds for which the domain suffix may be
                    used for domain name resolution

## nv set interface <interface-id> ip neighbor-discovery router-advertisement

### Usage

  nv set interface <interface-id> ip neighbor-discovery router-advertisement [options] [<attribute> ...]

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
                     
## nv set interface <interface-id> ip neighbor-discovery router-advertisement interval 70-1800000

### Usage

  nv set interface <interface-id> ip neighbor-discovery router-advertisement interval [options] 70-1800000

### Description

  Maximum time in milliseconds allowed between sending unsolicited multicast RA from the interface

### Identifiers

  <interface-id>  Interface

## nv set interface <interface-id> ip neighbor-discovery router-advertisement lifetime 0-9000

### Usage

  nv set interface <interface-id> ip neighbor-discovery router-advertisement lifetime [options] 0-9000

### Description

  Maximum time in seconds that the router can be treated as default gateway

### Identifiers

  <interface-id>  Interface

## nv set interface <interface-id> ip neighbor-discovery router-advertisement reachable-time 0-3600000

### Usage

  nv set interface <interface-id> ip neighbor-discovery router-advertisement reachable-time [options] 0-3600000

### Description

  Time in milliseconds that a IPv6 node is considered reachable

### Identifiers

  <interface-id>  Interface

## nv set interface <interface-id> ip neighbor-discovery router-advertisement retransmit-time 0-4294967295

### Usage

  nv set interface <interface-id> ip neighbor-discovery router-advertisement retransmit-time [options] 0-4294967295

### Description

  Time in milliseconds between retransmission of neighbor solicitation messages

### Identifiers

  <interface-id>  Interface

## nv set interface <interface-id> ip neighbor-discovery router-advertisement hop-limit 0-255

### Usage

  nv set interface <interface-id> ip neighbor-discovery router-advertisement hop-limit [options] 0-255

### Description

  Value in hop count field in IP header of the outgoing router advertisement packet

### Identifiers

  <interface-id>  Interface

## nv set interface <interface-id> ip neighbor-discovery home-agent

### Usage

  nv set interface <interface-id> ip neighbor-discovery home-agent [options] [<attribute> ...]

### Description

  Indicates to neighbors that this router acts as a Home Agent and includes a Home Agent Option. Not defined by default

### Identifiers

  <interface-id>  Interface

### Atrributes

  lifetime        Lifetime of a home agent in seconds
  preference      Home agent's preference value that is used to order the
                  addresses returned in the home agent address discovery
                  reply.

## nv set interface <interface-id> ip neighbor-discovery home-agent lifetime 0-65520

### Usage

  nv set interface <interface-id> ip neighbor-discovery home-agent lifetime [options] 0-65520

### Description

  Lifetime of a home agent in seconds

### Identifiers

  <interface-id>  Interface

## nv set interface <interface-id> ip neighbor-discovery home-agent preference 0-65535

### Usage

  nv set interface <interface-id> ip neighbor-discovery home-agent preference [options] 0-65535

### Description

  Home agent's preference value that is used to order the addresses returned in the home agent address discovery reply.

### Identifiers

  <interface-id>  Interface

## nv set interface <interface-id> ip neighbor-discovery mtu 1-65535

### Usage

  nv set interface <interface-id> ip neighbor-discovery mtu [options] 1-65535

### Description

  MTU option for neighbor discovery messages

### Identifiers

  <interface-id>  Interface

## nv set interface <interface-id> ip vrf <vrf-name>

### Usage

  nv set interface <interface-id> ip vrf [options] <vrf-name>

### Description

  Virtual routing and forwarding

### Identifiers

  <interface-id>  Interface

## nv set interface <interface-id> lldp

### Usage

  nv set interface <interface-id> lldp [options] [<attribute> ...]

### Description

  LLDP on for an interface

### Identifiers

  <interface-id>       Interface

### Atrributes

  dcbx-ets-config-tlv  DCBX ETS config TLV flag
  dcbx-ets-recomm-tlv  DCBX ETS recommendation TLV flag
  dcbx-pfc-tlv         DCBX PFC TLV flag

## nv set interface <interface-id> link

### Usage

  nv set interface <interface-id> link [options] [<attribute> ...]

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

## nv set interface <interface-id> link dot1x

### Usage

  nv set interface <interface-id> link dot1x [options] [<attribute> ...]

### Description

  An physical interface

### Identifiers

  <interface-id>  Interface

### Atrributes

  mab             bypass MAC authentication
  parking-vlan    VLAN for unauthorized MAC addresses

## nv set interface <interface-id> link mtu 552-9216

### Usage

  nv set interface <interface-id> link mtu [options] 552-9216

### Description

  interface mtu

### Identifiers

  <interface-id>  Interface

## nv set interface <interface-id> evpn

### Usage

  nv set interface <interface-id> evpn [options] [<attribute> ...]

### Description

  EVPN control plane config and info for VRF

### Identifiers

  <interface-id>  Interface

### Atrributes

  multihoming     Multihoming interface configuration parameters

## nv set interface <interface-id> evpn multihoming

### Usage

  nv set interface <interface-id> evpn multihoming [options] [<attribute> ...]

### Description

  Multihoming interface configuration parameters

### Identifiers

  <interface-id>  Interface

### Atrributes

  segment         Multihoming interface segment
  uplink          Enable evpn multihoming tracking to prevent traffic loss due
                  to NVE connectivity loss, uplink's operational state is
                  tracked when enabled.

## nv set interface <interface-id> evpn multihoming segment

### Usage

  nv set interface <interface-id> evpn multihoming segment [options] [<attribute> ...]

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

## nv set interface <interface-id> evpn multihoming segment local-id 1-16777215

### Usage

  nv set interface <interface-id> evpn multihoming segment local-id [options] 1-16777215

### Description

  Ethernet segment local-id.  If provided, it will be combined with the global multihoming `mac-address` to create the ethernet segment identifier, which must be unique for each segment and match other bonds in the segment.

### Identifiers

  <interface-id>  Interface

## nv set interface <interface-id> evpn multihoming segment identifier <es-identifier>

### Usage

  nv set interface <interface-id> evpn multihoming segment identifier [options] <es-identifier>

### Description

  Ethernet segment identifier.  This must be unique for each segment and match other bonds in the segment.

### Identifiers

  <interface-id>  Interface

## nv set interface <interface-id> acl <acl-id>

### Usage

  nv set interface <interface-id> acl <acl-id> [options] [<attribute> ...]

### Description

  An ACL is used for matching packets and take actions

### Identifiers

  <interface-id>  Interface
  <acl-id>        ACL ID

### Atrributes

  inbound         ACL applied for inbound direction
  outbound        ACL applied for outbound direction

## nv set interface <interface-id> acl <acl-id> inbound

### Usage

  nv set interface <interface-id> acl <acl-id> inbound [options] [<attribute> ...]

### Description

  inbound direction

### Identifiers

  <interface-id>  Interface
  <acl-id>        ACL ID

### Atrributes

  control-plane   ACL applied for control plane

## nv set interface <interface-id> acl <acl-id> inbound control-plane

### Usage

  nv set interface <interface-id> acl <acl-id> inbound control-plane [options]

### Description

  State details

### Identifiers

  <interface-id>  Interface
  <acl-id>        ACL ID

## nv set interface <interface-id> acl <acl-id> outbound

### Usage

  nv set interface <interface-id> acl <acl-id> outbound [options] [<attribute> ...]

### Description

  State details

### Identifiers

  <interface-id>  Interface
  <acl-id>        ACL ID

### Atrributes

  control-plane

## nv set interface <interface-id> acl <acl-id> outbound control-plane

### Usage

  nv set interface <interface-id> acl <acl-id> outbound control-plane [options]

### Description

  State details

### Identifiers

  <interface-id>  Interface
  <acl-id>        ACL ID

## nv set interface <interface-id> ptp

### Usage

  nv set interface <interface-id> ptp [options] [<attribute> ...]

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
                     
## nv set interface <interface-id> ptp timers

### Usage

  nv set interface <interface-id> ptp timers [options] [<attribute> ...]

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

## nv set interface <interface-id> ptp timers announce-interval -3-4

### Usage

  nv set interface <interface-id> ptp timers announce-interval [options] -3-4

### Description

  Mean time interval between successive Announce messages.  It's specified as a power of two in seconds.

### Identifiers

  <interface-id>  Interface

## nv set interface <interface-id> ptp timers sync-interval -7-1

### Usage

  nv set interface <interface-id> ptp timers sync-interval [options] -7-1

### Description

  The mean SyncInterval for multicast messages.  It's specified as a power of two in seconds.

### Identifiers

  <interface-id>  Interface

## nv set interface <interface-id> ptp timers delay-req-interval -7-6

### Usage

  nv set interface <interface-id> ptp timers delay-req-interval [options] -7-6

### Description

  The minimum permitted mean time interval between successive Delay Req messages.  It's specified as a power of two in seconds.

### Identifiers

  <interface-id>  Interface

## nv set interface <interface-id> ptp timers announce-timeout 2-10

### Usage

  nv set interface <interface-id> ptp timers announce-timeout [options] 2-10

### Description

  The number of announceIntervals that have to pass without receipt of an Announce message before the occurrence of the timeout event

### Identifiers

  <interface-id>  Interface

## nv set interface <interface-id> ptp instance <value>

### Usage

  nv set interface <interface-id> ptp instance [options] <value>

### Description

  PTP instance number.

### Identifiers

  <interface-id>  Interface

## nv set interface <interface-id> ptp delay-mechanism end-to-end

### Usage

  nv set interface <interface-id> ptp delay-mechanism [options] end-to-end

### Description

  Mode in which PTP message is transmitted.

### Identifiers

  <interface-id>  Interface

## nv set interface <interface-id> ptp ttl 1-255

### Usage

  nv set interface <interface-id> ptp ttl [options] 1-255

### Description

  Maximum number of hops the PTP messages can make before it gets dropped.

### Identifiers

  <interface-id>  Interface

## nv set interface <interface-id> tunnel

### Usage

  nv set interface <interface-id> tunnel [options] [<attribute> ...]

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

## nv set interface <interface-id> tunnel source-ip <ipv4>

### Usage

  nv set interface <interface-id> tunnel source-ip [options] <ipv4>

### Description

  Source underlay IP address

### Identifiers

  <interface-id>  Interface

## nv set interface <interface-id> tunnel dest-ip <ipv4>

### Usage

  nv set interface <interface-id> tunnel dest-ip [options] <ipv4>

### Description

  Destination underlay IP address

### Identifiers

  <interface-id>  Interface

## nv set interface <interface-id> tunnel ttl 1-255

### Usage

  nv set interface <interface-id> tunnel ttl [options] 1-255

### Description

  time to live

### Identifiers

  <interface-id>  Interface

## nv set interface <interface-id> tunnel mode gre

### Usage

  nv set interface <interface-id> tunnel mode [options] gre

### Description

  tunnel mode

### Identifiers

  <interface-id>  Interface

## nv set interface <interface-id> tunnel interface <interface-name>

### Usage

  nv set interface <interface-id> tunnel interface [options] <interface-name>

### Description

  Physical underlay interface to used for Tunnel packets

### Identifiers

  <interface-id>  Interface

## nv set interface <interface-id> description <value>

### Usage

  nv set interface <interface-id> description [options] <value>

### Description

  Details about the interface

### Identifiers

  <interface-id>  Interface

## nv set interface <interface-id> vlan 1-4094

### Usage

  nv set interface <interface-id> vlan [options] 1-4094

### Description

  VLAN ID

### Identifiers

  <interface-id>  Interface

## nv set service

### Usage

  nv set service [options] [<attribute> ...]

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

## nv set service dns <vrf-id>

### Usage

  nv set service dns <vrf-id> [options] [<attribute> ...]

### Description

  Domain Name Service

### Identifiers

  <vrf-id>    VRF

### Atrributes

  server      Remote DNS servers## nv set service dns <vrf-id> server <dns-server-id>

### Usage

  nv set service dns <vrf-id> server <dns-server-id> [options]

### Description

  A remote DNS server

### Identifiers

  <vrf-id>         VRF
  <dns-server-id>  IPv4 or IPv6 address of a DNS server
  
## nv set service syslog <vrf-id>

### Usage

  nv set service syslog <vrf-id> [options] [<attribute> ...]

### Description

  Domain Name Service

### Identifiers

  <vrf-id>    VRF

### Atrributes

  server      Remote DNS servers
  
## nv set service syslog <vrf-id> server <server-id>

### Usage

  nv set service syslog <vrf-id> server <server-id> [options] [<attribute> ...]

### Description

  A remote DNS server

### Identifiers

  <vrf-id>     VRF
  <server-id>  Hostname or IP address of a syslog server

### Atrributes

  port         Port number of the remote syslog server
  protocol     Protocol, udp or tcp, of the remote syslog server
  
## nv set service syslog <vrf-id> server <server-id> port 1-32767

### Usage

  nv set service syslog <vrf-id> server <server-id> port [options] 1-32767

### Description

  Port number of the remote syslog server

### Identifiers

  <vrf-id>     VRF
  <server-id>  Hostname or IP address of a syslog server
  
## nv set service ntp <vrf-id>

### Usage

  nv set service ntp <vrf-id> [options] [<attribute> ...]

### Description

  Network Time Protocol

### Identifiers

  <vrf-id>    VRF

### Atrributes

  server      Remote NTP Servers
  pool        Remote NTP Servers
  listen      NTP interface to listen on.
  
## nv set service ntp <vrf-id> server <server-id>

### Usage

  nv set service ntp <vrf-id> server <server-id> [options] [<attribute> ...]

### Description

  A remote NTP Server

### Identifiers

  <vrf-id>     VRF
  <server-id>  Hostname or IP address of the NTP server

### Atrributes

  iburst       When the server is unreachable, send a burst of eight packets
               instead of the usual one.
               
## nv set service ntp <vrf-id> pool <server-id>

### Usage

  nv set service ntp <vrf-id> pool <server-id> [options] [<attribute> ...]

### Description

  A remote NTP Server

### Identifiers

  <vrf-id>     VRF
  <server-id>  Hostname or IP address of the NTP server

### Atrributes

  iburst       When the server is unreachable, send a burst of eight packets
               instead of the usual one.
               
## nv set service ntp <vrf-id> listen <interface-name>

### Usage

  nv set service ntp <vrf-id> listen [options] <interface-name>

### Description

  NTP interface to listen on.

### Identifiers

  <vrf-id>    VRF
  
## nv set service dhcp-relay <vrf-id>

### Usage

  nv set service dhcp-relay <vrf-id> [options] [<attribute> ...]

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
                       
## nv set service dhcp-relay <vrf-id> server <server-id>

### Usage

  nv set service dhcp-relay <vrf-id> server <server-id> [options]

### Description

  A DHCP server

### Identifiers

  <vrf-id>     VRF
  <server-id>  DHCP server
  
## nv set service dhcp-relay <vrf-id> interface <interface-id>

### Usage

  nv set service dhcp-relay <vrf-id> interface <interface-id> [options]

### Description

  An interface on which DHCP relay is configured.

### Identifiers

  <vrf-id>        VRF
  <interface-id>  DHCP relay interface

## nv set service dhcp-relay <vrf-id> giaddress-interface <interface-id>

### Usage

  nv set service dhcp-relay <vrf-id> giaddress-interface <interface-id> [options] [<attribute> ...]

### Description

  An interface on which DHCP relay giaddress is configured.

### Identifiers

  <vrf-id>        VRF
  <interface-id>  DHCP relay giaddress interface

### Atrributes

  address         ipv4 address on giaddress interface

## nv set service dhcp-relay6 <vrf-id>

### Usage

  nv set service dhcp-relay6 <vrf-id> [options] [<attribute> ...]

### Description

  DHCP relay

### Identifiers

  <vrf-id>    VRF

### Atrributes

  interface   DHCP relay interfaces
  
## nv set service dhcp-relay6 <vrf-id> interface

### Usage

  nv set service dhcp-relay6 <vrf-id> interface [options] [<attribute> ...]

### Description

  DHCP relay interfaces

### Identifiers

  <vrf-id>    VRF

### Atrributes

  upstream    Configures DHCP relay on the interfaes.
  downstream  Configures DHCP relay on the interfaes.
  
## nv set service dhcp-relay6 <vrf-id> interface upstream <interface-id>

### Usage

  nv set service dhcp-relay6 <vrf-id> interface upstream <interface-id> [options] [<attribute> ...]

### Description

  An interface on which DPCH relay is configured.

### Identifiers

  <vrf-id>        VRF
  <interface-id>  DHCP relay interface

### Atrributes

  address         ipv6 address on interface

## nv set service dhcp-relay6 <vrf-id> interface upstream <interface-id> address <ipv6>

### Usage

  nv set service dhcp-relay6 <vrf-id> interface upstream <interface-id> address [options] <ipv6>

### Description

  ipv6 address on interface

### Identifiers

  <vrf-id>        VRF
  <interface-id>  DHCP relay interface

## nv set service dhcp-relay6 <vrf-id> interface downstream <interface-id>

### Usage

  nv set service dhcp-relay6 <vrf-id> interface downstream <interface-id> [options] [<attribute> ...]

### Description

  An interface on which DPCH relay is configured.

### Identifiers

  <vrf-id>        VRF
  <interface-id>  DHCP relay interface

### Atrributes

  address         ipv6 address on interface

## nv set service dhcp-relay6 <vrf-id> interface downstream <interface-id> address <ipv6>

### Usage

  nv set service dhcp-relay6 <vrf-id> interface downstream <interface-id> address [options] <ipv6>

### Description

  ipv6 address on interface

### Identifiers

  <vrf-id>        VRF
  <interface-id>  DHCP relay interface

## nv set service ptp <instance-id>

### Usage

  nv set service ptp <instance-id> [options] [<attribute> ...]

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
  
## nv set service ptp <instance-id> acceptable-master <clock-id>

### Usage

  nv set service ptp <instance-id> acceptable-master <clock-id> [options] [<attribute> ...]

### Description

  List of clocks that the local clock can accept as master clock

### Identifiers

  <instance-id>  PTP instance number. It is used for management purpose.
  <clock-id>     Clock ID

### Atrributes

  alt-priority   Alternate priority
  
## nv set service ptp <instance-id> acceptable-master <clock-id> alt-priority <value>

### Usage

  nv set service ptp <instance-id> acceptable-master <clock-id> alt-priority [options] <value>

### Description

  Alternate priority

### Identifiers

  <instance-id>  PTP instance number. It is used for management purpose.
  <clock-id>     Clock ID

## nv set service ptp <instance-id> monitor

### Usage

  nv set service ptp <instance-id> monitor [options] [<attribute> ...]

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

## nv set service ptp <instance-id> monitor min-offset-threshold <value>

### Usage

  nv set service ptp <instance-id> monitor min-offset-threshold [options] <value>

### Description

  Minimum offset threshold in nano seconds

### Identifiers

  <instance-id>  PTP instance number. It is used for management purpose.

## nv set service ptp <instance-id> monitor max-offset-threshold <value>

### Usage

  nv set service ptp <instance-id> monitor max-offset-threshold [options] <value>

### Description

  Maximum offset threshold in nano seconds

### Identifiers

  <instance-id>  PTP instance number. It is used for management purpose.

## nv set service ptp <instance-id> monitor path-delay-threshold <value>

### Usage

  nv set service ptp <instance-id> monitor path-delay-threshold [options] <value>

### Description

  Path delay threshold in nano seconds

### Identifiers

  <instance-id>  PTP instance number. It is used for management purpose.

## nv set service ptp <instance-id> monitor max-timestamp-entries 400-1000

### Usage

  nv set service ptp <instance-id> monitor max-timestamp-entries [options] 400-1000

### Description

  Maximum timestamp entries allowed

### Identifiers

  <instance-id>  PTP instance number. It is used for management purpose.

## nv set service ptp <instance-id> monitor max-violation-log-sets 8-128

### Usage

  nv set service ptp <instance-id> monitor max-violation-log-sets [options] 8-128

### Description

  Maximum violation logs sets allowed

### Identifiers

  <instance-id>  PTP instance number. It is used for management purpose.

## nv set service ptp <instance-id> monitor max-violation-log-entries 8-128

### Usage

  nv set service ptp <instance-id> monitor max-violation-log-entries [options] 8-128

### Description

  Maximum violation log entries per set

### Identifiers

  <instance-id>  PTP instance number. It is used for management purpose.

## nv set service ptp <instance-id> monitor violation-log-interval 0-259200

### Usage

  nv set service ptp <instance-id> monitor violation-log-interval [options] 0-259200

### Description

  violation log intervals in seconds

### Identifiers

  <instance-id>  PTP instance number. It is used for management purpose.

## nv set service ptp <instance-id> priority1 <value>

### Usage

  nv set service ptp <instance-id> priority1 [options] <value>

### Description

  Priority1 attribute of the local clock

### Identifiers

  <instance-id>  PTP instance number. It is used for management purpose.
  
## nv set service ptp <instance-id> priority2 <value>

### Usage

  nv set service ptp <instance-id> priority2 [options] <value>

### Description

  Priority2 attribute of the local clock

### Identifiers

  <instance-id>  PTP instance number. It is used for management purpose.
  
## nv set service ptp <instance-id> domain 0-127

### Usage

  nv set service ptp <instance-id> domain [options] 0-127

### Description

  Domain number of the current syntonization

### Identifiers

  <instance-id>  PTP instance number. It is used for management purpose.

## nv set service ptp <instance-id> ip-dscp 0-63

### Usage

  nv set service ptp <instance-id> ip-dscp [options] 0-63

### Description

  Sets the Diffserv code point for all PTP packets originated locally.

### Identifiers

  <instance-id>  PTP instance number. It is used for management purpose.
  
## nv set service dhcp-server <vrf-id>

### Usage

  nv set service dhcp-server <vrf-id> [options] [<attribute> ...]

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

## nv set service dhcp-server <vrf-id> interface <interface-id>

### Usage

  nv set service dhcp-server <vrf-id> interface <interface-id> [options]

### Description

  An interface on which DPCH clients are attached.

### Identifiers

  <vrf-id>        VRF
  <interface-id>  DHCP client interface

## nv set service dhcp-server <vrf-id> pool <pool-id>

### Usage

  nv set service dhcp-server <vrf-id> pool <pool-id> [options] [<attribute> ...]

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

## nv set service dhcp-server <vrf-id> pool <pool-id> domain-name-server <server-id>

### Usage

  nv set service dhcp-server <vrf-id> pool <pool-id> domain-name-server <server-id> [options]

### Description

  A remote DNS server

### Identifiers

  <vrf-id>     VRF
  <pool-id>    DHCP pool subnet.
  <server-id>  DNS server
  
## nv set service dhcp-server <vrf-id> pool <pool-id> domain-name <domain-name-id>

### Usage

  nv set service dhcp-server <vrf-id> pool <pool-id> domain-name <domain-name-id> [options] [<attribute> ...]

### Description

  TBD

### Identifiers

  <vrf-id>          VRF
  <pool-id>         DHCP pool subnet.
  <domain-name-id>  DHCP domain name

### Atrributes

  domain-name       DHCP domain name

## nv set service dhcp-server <vrf-id> pool <pool-id> domain-name <domain-name-id> domain-name <idn-hostname>

### Usage

  nv set service dhcp-server <vrf-id> pool <pool-id> domain-name <domain-name-id> domain-name [options] <idn-hostname>

### Description

  DHCP domain name

### Identifiers

  <vrf-id>          VRF
  <pool-id>         DHCP pool subnet.
  <domain-name-id>  DHCP domain name

## nv set service dhcp-server <vrf-id> pool <pool-id> gateway <gateway-id>

### Usage

  nv set service dhcp-server <vrf-id> pool <pool-id> gateway <gateway-id> [options]

### Description

  A remote DNS server

### Identifiers

  <vrf-id>      VRF
  <pool-id>     DHCP pool subnet.
  <gateway-id>  Gateway
  
## nv set service dhcp-server <vrf-id> pool <pool-id> range <range-id>

### Usage

  nv set service dhcp-server <vrf-id> pool <pool-id> range <range-id> [options] [<attribute> ...]

### Description

  DHCP Pool range

### Identifiers

  <vrf-id>    VRF
  <pool-id>   DHCP pool subnet.
  <range-id>  DHCP client interface

### Atrributes

  to          End of the range.
  
## nv set service dhcp-server <vrf-id> pool <pool-id> range <range-id> to <ipv4>

### Usage

  nv set service dhcp-server <vrf-id> pool <pool-id> range <range-id> to [options] <ipv4>

### Description

  End of the range.

### Identifiers

  <vrf-id>    VRF
  <pool-id>   DHCP pool subnet.
  <range-id>  DHCP client interface
  
## nv set service dhcp-server <vrf-id> pool <pool-id> pool-name <value>

### Usage

  nv set service dhcp-server <vrf-id> pool <pool-id> pool-name [options] <value>

### Description

  Name

### Identifiers

  <vrf-id>    VRF
  <pool-id>   DHCP pool subnet.
  
## nv set service dhcp-server <vrf-id> pool <pool-id> lease-time 180-31536000

### Usage

  nv set service dhcp-server <vrf-id> pool <pool-id> lease-time [options] 180-31536000

### Description

  Network address lease time in seconds assigned to DHCP clients.

### Identifiers

  <vrf-id>    VRF
  <pool-id>   DHCP pool subnet.
  
## nv set service dhcp-server <vrf-id> pool <pool-id> default-url <value>

### Usage

  nv set service dhcp-server <vrf-id> pool <pool-id> default-url [options] <value>

### Description

  TBD

### Identifiers

  <vrf-id>    VRF
  <pool-id>   DHCP pool subnet.
  
## nv set service dhcp-server <vrf-id> pool <pool-id> cumulus-provision-url <value>

### Usage

  nv set service dhcp-server <vrf-id> pool <pool-id> cumulus-provision-url [options] <value>

### Description

  Cumulus specific URL for provisioning script

### Identifiers

  <vrf-id>    VRF
  <pool-id>   DHCP pool subnet.
  
## nv set service dhcp-server <vrf-id> domain-name <domain-name-id>

### Usage

  nv set service dhcp-server <vrf-id> domain-name <domain-name-id> [options] [<attribute> ...]

### Description

  TBD

### Identifiers

  <vrf-id>          VRF
  <domain-name-id>  DHCP domain name

### Atrributes

  domain-name       DHCP domain name

## nv set service dhcp-server <vrf-id> domain-name <domain-name-id> domain-name <idn-hostname>

### Usage

  nv set service dhcp-server <vrf-id> domain-name <domain-name-id> domain-name [options] <idn-hostname>

### Description

  DHCP domain name

### Identifiers

  <vrf-id>          VRF
  <domain-name-id>  DHCP domain name

## nv set service dhcp-server <vrf-id> domain-name-server <server-id>

### Usage

  nv set service dhcp-server <vrf-id> domain-name-server <server-id> [options]

### Description

  A remote DNS server

### Identifiers

  <vrf-id>     VRF
  <server-id>  DNS server
  
## nv set service dhcp-server <vrf-id> static <static-id>

### Usage

  nv set service dhcp-server <vrf-id> static <static-id> [options] [<attribute> ...]

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

## nv set service dhcp-server <vrf-id> static <static-id> mac-address <mac>

### Usage

  nv set service dhcp-server <vrf-id> static <static-id> mac-address [options] <mac>

### Description

  MAC (hardware) address

### Identifiers

  <vrf-id>     VRF
  <static-id>  static mapping nane
  
## nv set service dhcp-server <vrf-id> static <static-id> ip-address <ipv4>

### Usage

  nv set service dhcp-server <vrf-id> static <static-id> ip-address [options] <ipv4>

### Description

  IP address

### Identifiers

  <vrf-id>     VRF
  <static-id>  static mapping nane
  
## nv set service dhcp-server <vrf-id> static <static-id> cumulus-provision-url <value>

### Usage

  nv set service dhcp-server <vrf-id> static <static-id> cumulus-provision-url [options] <value>

### Description

  Cumulus specific URL for provisioning script

### Identifiers

  <vrf-id>     VRF
  <static-id>  static mapping nane
  
## nv set service dhcp-server6 <vrf-id>

### Usage

  nv set service dhcp-server6 <vrf-id> [options] [<attribute> ...]

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
  
## nv set service dhcp-server6 <vrf-id> interface <interface-id>

### Usage

  nv set service dhcp-server6 <vrf-id> interface <interface-id> [options]

### Description

  An interface on which DPCH clients are attached.

### Identifiers

  <vrf-id>        VRF
  <interface-id>  DHCP client interface

## nv set service dhcp-server6 <vrf-id> pool <pool-id>

### Usage

  nv set service dhcp-server6 <vrf-id> pool <pool-id> [options] [<attribute> ...]

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

## nv set service dhcp-server6 <vrf-id> pool <pool-id> domain-name-server <server-id>

### Usage

  nv set service dhcp-server6 <vrf-id> pool <pool-id> domain-name-server <server-id> [options]

### Description

  A remote DNS server

### Identifiers

  <vrf-id>     VRF
  <pool-id>    DHCP6 pool subnet.
  <server-id>  DNS server
  
## nv set service dhcp-server6 <vrf-id> pool <pool-id> domain-name <domain-name-id>

### Usage

  nv set service dhcp-server6 <vrf-id> pool <pool-id> domain-name <domain-name-id> [options] [<attribute> ...]

### Description

  TBD

### Identifiers

  <vrf-id>          VRF
  <pool-id>         DHCP6 pool subnet.
  <domain-name-id>  DHCP domain name

### Atrributes

  domain-name       DHCP domain name

## nv set service dhcp-server6 <vrf-id> pool <pool-id> domain-name <domain-name-id> domain-name <idn-hostname>

### Usage

  nv set service dhcp-server6 <vrf-id> pool <pool-id> domain-name <domain-name-id> domain-name [options] <idn-hostname>

### Description

  DHCP domain name

### Identifiers

  <vrf-id>          VRF
  <pool-id>         DHCP6 pool subnet.
  <domain-name-id>  DHCP domain name

## nv set service dhcp-server6 <vrf-id> pool <pool-id> range <range-id>

### Usage

  nv set service dhcp-server6 <vrf-id> pool <pool-id> range <range-id> [options] [<attribute> ...]

### Description

  DHCP Pool range

### Identifiers

  <vrf-id>    VRF
  <pool-id>   DHCP6 pool subnet.
  <range-id>  DHCP client interface

### Atrributes

  to          End of the range.
  
## nv set service dhcp-server6 <vrf-id> pool <pool-id> range <range-id> to <ipv6>

### Usage

  nv set service dhcp-server6 <vrf-id> pool <pool-id> range <range-id> to [options] <ipv6>

### Description

  End of the range.

### Identifiers

  <vrf-id>    VRF
  <pool-id>   DHCP6 pool subnet.
  <range-id>  DHCP client interface
  
## nv set service dhcp-server6 <vrf-id> pool <pool-id> pool-name <value>

### Usage

  nv set service dhcp-server6 <vrf-id> pool <pool-id> pool-name [options] <value>

### Description

  Name

### Identifiers

  <vrf-id>    VRF
  <pool-id>   DHCP6 pool subnet.
  
## nv set service dhcp-server6 <vrf-id> pool <pool-id> lease-time 180-31536000

### Usage

  nv set service dhcp-server6 <vrf-id> pool <pool-id> lease-time [options] 180-31536000

### Description

  Network address lease time in seconds assigned to DHCP clients.

### Identifiers

  <vrf-id>    VRF
  <pool-id>   DHCP6 pool subnet.
  
## nv set service dhcp-server6 <vrf-id> pool <pool-id> default-url <value>

### Usage

  nv set service dhcp-server6 <vrf-id> pool <pool-id> default-url [options] <value>

### Description

  TBD

### Identifiers

  <vrf-id>    VRF
  <pool-id>   DHCP6 pool subnet.
  
## nv set service dhcp-server6 <vrf-id> pool <pool-id> cumulus-provision-url <value>

### Usage

  nv set service dhcp-server6 <vrf-id> pool <pool-id> cumulus-provision-url [options] <value>

### Description

  Cumulus specific URL for provisioning script

### Identifiers

  <vrf-id>    VRF
  <pool-id>   DHCP6 pool subnet.
  
## nv set service dhcp-server6 <vrf-id> domain-name <domain-name-id>

### Usage

  nv set service dhcp-server6 <vrf-id> domain-name <domain-name-id> [options] [<attribute> ...]

### Description

  TBD

### Identifiers

  <vrf-id>          VRF
  <domain-name-id>  DHCP domain name

### Atrributes

  domain-name       DHCP domain name

## nv set service dhcp-server6 <vrf-id> domain-name <domain-name-id> domain-name <idn-hostname>

### Usage

  nv set service dhcp-server6 <vrf-id> domain-name <domain-name-id> domain-name [options] <idn-hostname>

### Description

  DHCP domain name

### Identifiers

  <vrf-id>          VRF
  <domain-name-id>  DHCP domain name

## nv set service dhcp-server6 <vrf-id> domain-name-server <server-id>

### Usage

  nv set service dhcp-server6 <vrf-id> domain-name-server <server-id> [options]

### Description

  A remote DNS server

### Identifiers

  <vrf-id>     VRF
  <server-id>  DNS server
  
## nv set service dhcp-server6 <vrf-id> static <static-id>

### Usage

  nv set service dhcp-server6 <vrf-id> static <static-id> [options] [<attribute> ...]

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

## nv set service dhcp-server6 <vrf-id> static <static-id> mac-address <mac>

### Usage

  nv set service dhcp-server6 <vrf-id> static <static-id> mac-address [options] <mac>

### Description

  MAC (hardware) address

### Identifiers

  <vrf-id>     VRF
  <static-id>  static mapping nane
  
## nv set service dhcp-server6 <vrf-id> static <static-id> ip-address <ipv6>

### Usage

  nv set service dhcp-server6 <vrf-id> static <static-id> ip-address [options] <ipv6>

### Description

  IP address

### Identifiers

  <vrf-id>     VRF
  <static-id>  static mapping nane
  
## nv set service dhcp-server6 <vrf-id> static <static-id> cumulus-provision-url <value>

### Usage

  nv set service dhcp-server6 <vrf-id> static <static-id> cumulus-provision-url [options] <value>

### Description

  Cumulus specific URL for provisioning script

### Identifiers

  <vrf-id>     VRF
  <static-id>  static mapping nane
  
## nv set service lldp

### Usage

  nv set service lldp [options] [<attribute> ...]

### Description

  Global LLDP

### Atrributes

  dot1-tlv            Enable dot1 TLV advertisements on enabled ports
  tx-hold-multiplier  < TTL of transmitted packets is calculated by
                      multiplying the tx-interval by the given factor
  tx-interval         change transmit delay
  
## nv set service lldp tx-interval 10-300

### Usage

  nv set service lldp tx-interval [options] 10-300

### Description

  change transmit delay
  
## nv set service lldp tx-hold-multiplier 1-10

### Usage

  nv set service lldp tx-hold-multiplier [options] 1-10

### Description

  < TTL of transmitted packets is calculated by multiplying the tx-interval by the given factor
  
## nv set system

### Usage

  nv set system [options] [<attribute> ...]

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

## nv set system control-plane

### Usage

  nv set system control-plane [options] [<attribute> ...]

### Description

  Control Plane specific configurations

### Atrributes

  trap        Traps
  policer     Policers
  
## nv set system control-plane trap <trap-id>

### Usage

  nv set system control-plane trap <trap-id> [options] [<attribute> ...]

### Description

  Trap

### Identifiers

  <trap-id>   TRAP ID

### Atrributes

  state       trap state
  
## nv set system control-plane policer <policer-id>

### Usage

  nv set system control-plane policer <policer-id> [options] [<attribute> ...]

### Description

  Policer

### Identifiers

  <policer-id>  Policer ID

### Atrributes

  burst         policer burst value
  rate          policer rate value
  state         policer state
  
## nv set system control-plane policer <policer-id> burst 10-10000

### Usage

  nv set system control-plane policer <policer-id> burst [options] 10-10000

### Description

  policer burst value

### Identifiers

  <policer-id>  Policer ID

## nv set system control-plane policer <policer-id> rate 10-10000

### Usage

  nv set system control-plane policer <policer-id> rate [options] 10-10000

### Description

  policer rate value

### Identifiers

  <policer-id>  Policer ID
  
## nv set system message

### Usage

  nv set system message [options] [<attribute> ...]

### Description

  System pre-login and post-login messages

### Atrributes

  post-login  configure post-login message of the day
  pre-login   configure pre-login banner
  
## nv set system message pre-login <value>

### Usage

  nv set system message pre-login [options] <value>

### Description

  configure pre-login banner
  
## nv set system message post-login <value>

### Usage

  nv set system message post-login [options] <value>

### Description

  configure post-login message of the day
  
## nv set system global

### Usage

  nv set system global [options] [<attribute> ...]

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
  
## nv set system global reserved

### Usage

  nv set system global reserved [options] [<attribute> ...]

### Description

  reserved ranges

### Atrributes

  routing-table  reserved routing table ranges
  vlan           reserved vlan ranges

## nv set system global reserved routing-table

### Usage

  nv set system global reserved routing-table [options] [<attribute> ...]

### Description

  reserved routing table ranges

### Atrributes

  pbr         reserved routing table ranges for PBR
  
## nv set system global reserved routing-table pbr

### Usage

  nv set system global reserved routing-table pbr [options] [<attribute> ...]

### Description

  reserved routing table ranges for PBR

### Atrributes

  begin       Beginning of reserved routing table range for PBR
  end         End of reserved routing table range for PBR
  
## nv set system global reserved routing-table pbr begin 10000-4294966272

### Usage

  nv set system global reserved routing-table pbr begin [options] 10000-4294966272

### Description

  Beginning of reserved routing table range for PBR
  
## nv set system global reserved routing-table pbr end 10000-4294966272

### Usage

  nv set system global reserved routing-table pbr end [options] 10000-4294966272

### Description

  End of reserved routing table range for PBR
  
## nv set system global reserved vlan

### Usage

  nv set system global reserved vlan [options] [<attribute> ...]

### Description

  reserved vlan ranges

### Atrributes

  l3-vni-vlan  Reserved vlans to be used with l3vni
  
## nv set system global reserved vlan l3-vni-vlan

### Usage

  nv set system global reserved vlan l3-vni-vlan [options] [<attribute> ...]

### Description

  Reserved vlans to be used with l3vni

### Atrributes

  begin       Beginning of reserved vlan range for L3 VNI
  end         End of reserved vlan range for L3 VNI
  
## nv set system global reserved vlan l3-vni-vlan begin 1-4093

### Usage

  nv set system global reserved vlan l3-vni-vlan begin [options] 1-4093

### Description

  Beginning of reserved vlan range for L3 VNI
  
## nv set system global reserved vlan l3-vni-vlan end 2-4093

### Usage

  nv set system global reserved vlan l3-vni-vlan end [options] 2-4093

### Description

  End of reserved vlan range for L3 VNI
  
## nv set system global fabric-id 1-255

### Usage

  nv set system global fabric-id [options] 1-255

### Description

  An integer (1-255) to select first hop router MAC adress in range 00:00:5E:00:01:01 to 00:00:5E:00:01:ff
  
## nv set system port-mirror

### Usage

  nv set system port-mirror [options] [<attribute> ...]

### Description

  Port mirror

### Atrributes

  session     sessions
  
## nv set system port-mirror session <session-id>

### Usage

  nv set system port-mirror session <session-id> [options] [<attribute> ...]

### Description

  port mirror session number

### Identifiers

  <session-id>  port mirror session number

### Atrributes

  span          Switched Port Analyzer
  erspan        Encapsulated Remote Switched Port Analyzer.

## nv set system port-mirror session <session-id> span

### Usage

  nv set system port-mirror session <session-id> span [options] [<attribute> ...]

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
  
## nv set system port-mirror session <session-id> span source-port <port-id>

### Usage

  nv set system port-mirror session <session-id> span source-port <port-id> [options]

### Description

  A port-mirror source port (swps or bonds only)

### Identifiers

  <session-id>  port mirror session number
  <port-id>     Port interface
  
## nv set system port-mirror session <session-id> span destination <port-id>

### Usage

  nv set system port-mirror session <session-id> span destination <port-id> [options]

### Description

  The SPAN destination port.

### Identifiers

  <session-id>  port mirror session number
  <port-id>     Port interface
  
## nv set system port-mirror session <session-id> span truncate

### Usage

  nv set system port-mirror session <session-id> span truncate [options] [<attribute> ...]

### Description

  TBD

### Identifiers

  <session-id>  port mirror session number

### Atrributes

  enable        Turn the feature 'on' or 'off'. The default is 'off'.
  size          Truncates the mirrored frames at specified number of bytes.
                Truncate size must be between 4 and 4088 bytes and a multiple
                of 4 
                
## nv set system port-mirror session <session-id> erspan

### Usage

  nv set system port-mirror session <session-id> erspan [options] [<attribute> ...]

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
  
## nv set system port-mirror session <session-id> erspan source-port <port-id>

### Usage

  nv set system port-mirror session <session-id> erspan source-port <port-id> [options]

### Description

  A port-mirror source port (swps or bonds only)

### Identifiers

  <session-id>  port mirror session number
  <port-id>     Port interface
  
## nv set system port-mirror session <session-id> erspan destination

### Usage

  nv set system port-mirror session <session-id> erspan destination [options] [<attribute> ...]

### Description

  erspan destination

### Identifiers

  <session-id>  port mirror session number

### Atrributes

  source-ip     TBD
  dest-ip       TBD
  
## nv set system port-mirror session <session-id> erspan destination source-ip <source-ip>

### Usage

  nv set system port-mirror session <session-id> erspan destination source-ip <source-ip> [options]

### Description

  An IPv4 address

### Identifiers

  <session-id>  port mirror session number
  
## nv set system port-mirror session <session-id> erspan destination dest-ip <dest-ip>

### Usage

  nv set system port-mirror session <session-id> erspan destination dest-ip <dest-ip> [options]

### Description

  An IPv4 address

### Identifiers

  <session-id>  port mirror session number
  
## nv set system port-mirror session <session-id> erspan truncate

### Usage

  nv set system port-mirror session <session-id> erspan truncate [options] [<attribute> ...]

### Description

  TBD

### Identifiers

  <session-id>  port mirror session number

### Atrributes

  enable        Turn the feature 'on' or 'off'. The default is 'off'.
  size          Truncates the mirrored frames at specified number of bytes.
                Truncate size must be between 4 and 4088 bytes and a multiple
                of 4
                
## nv set system config

### Usage

  nv set system config [options] [<attribute> ...]

### Description

  Affect how config operations are performed.

### Atrributes

  apply       Affect how config apply operations are performed.
  
## nv set system config apply

### Usage

  nv set system config apply [options] [<attribute> ...]

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
              
## nv set system config apply ignore <ignore-id>

### Usage

  nv set system config apply ignore <ignore-id> [options]

### Description

  File to ignore during config apply operations.

### Identifiers

  <ignore-id>  Ignored file
  
## nv set system hostname <idn-hostname>

### Usage

  nv set system hostname [options] <idn-hostname>

### Description

  Static hostname for the switch
  
## nv set vrf <vrf-id>

### Usage

  nv set vrf <vrf-id> [options] [<attribute> ...]

### Description

  A VRF

### Identifiers

  <vrf-id>    VRF

### Atrributes

  loopback    The loopback IP interface associated with this VRF.
  evpn        EVPN control plane config and info for VRF
  router      A VRF
  ptp         VRF PTP configuration. Inherited by interfaces in this VRF.
  table       The routing table number, between 1001-1255, used by the named
              VRF. If auto, the default, it will be auto generated.
              
## nv set vrf <vrf-id> loopback

### Usage

  nv set vrf <vrf-id> loopback [options] [<attribute> ...]

### Description

  The loopback IP interface associated with this VRF.

### Identifiers

  <vrf-id>    VRF

### Atrributes

  ip          Properties associated with the loopback IP address on this VRF.
  
## nv set vrf <vrf-id> loopback ip

### Usage

  nv set vrf <vrf-id> loopback ip [options] [<attribute> ...]

### Description

  IP addresses associated with the VRF's loopback interface.

### Identifiers

  <vrf-id>    VRF

### Atrributes

  address     static IPv4 or IPv6 address
  
## nv set vrf <vrf-id> loopback ip address <ip-prefix-id>

### Usage

  nv set vrf <vrf-id> loopback ip address <ip-prefix-id> [options]

### Description

  An IP address with prefix

### Identifiers

  <vrf-id>        VRF
  <ip-prefix-id>  IPv4 or IPv6 address and route prefix in CIDR notation

## nv set vrf <vrf-id> evpn

### Usage

  nv set vrf <vrf-id> evpn [options] [<attribute> ...]

### Description

  EVPN control plane config and info for VRF

### Identifiers

  <vrf-id>    VRF

### Atrributes

  vni         L3 VNI
  enable      Turn the feature 'on' or 'off'. The default is 'off'.
  vlan        VLAN ID
  
## nv set vrf <vrf-id> evpn vni <vni-id>

### Usage

  nv set vrf <vrf-id> evpn vni <vni-id> [options] [<attribute> ...]

### Description

  VNI

### Identifiers

  <vrf-id>            VRF
  <vni-id>            VxLAN ID

### Atrributes

  prefix-routes-only  Associated L3 VNI and corresponding route targets only
                      with EVPN type-5 routes, not with EVPN type-2 routes.

## nv set vrf <vrf-id> router

### Usage

  nv set vrf <vrf-id> router [options] [<attribute> ...]

### Description

  A VRF

### Identifiers

  <vrf-id>    VRF

### Atrributes

  rib         RIB Routes
  bgp         BGP VRF configuration.
  static      Routes
  pim         PIM VRF configuration.
  ospf        OSPF VRF configuration.
  
## nv set vrf <vrf-id> router rib <afi>

### Usage

  nv set vrf <vrf-id> router rib <afi> [options] [<attribute> ...]

### Description

  Vrf aware Routing-table per address-family

### Identifiers

  <vrf-id>    VRF
  <afi>       Route address family.

### Atrributes

  protocol    Import protocols from RIB to FIB
  
## nv set vrf <vrf-id> router rib <afi> protocol <import-protocol-id>

### Usage

  nv set vrf <vrf-id> router rib <afi> protocol <import-protocol-id> [options] [<attribute> ...]

### Description

  Import Protocols from where routes are known

### Identifiers

  <vrf-id>              VRF
  <afi>                 Route address family.
  <import-protocol-id>  Import protocol list.

### Atrributes

  fib-filter            Route map to apply on the import prootcol's routes.

## nv set vrf <vrf-id> router bgp

### Usage

  nv set vrf <vrf-id> router bgp [options] [<attribute> ...]

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
                      
## nv set vrf <vrf-id> router bgp address-family

### Usage

  nv set vrf <vrf-id> router bgp address-family [options] [<attribute> ...]

### Description

  Address family specific configuration

### Identifiers

  <vrf-id>      VRF

### Atrributes

  ipv4-unicast  IPv4 unicast address family
  l2vpn-evpn    BGP VRF configuration. L2VPN EVPN address family
  ipv6-unicast  IPv6 unicast address family

## nv set vrf <vrf-id> router bgp address-family ipv4-unicast

### Usage

  nv set vrf <vrf-id> router bgp address-family ipv4-unicast [options] [<attribute> ...]

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

## nv set vrf <vrf-id> router bgp address-family ipv4-unicast redistribute

### Usage

  nv set vrf <vrf-id> router bgp address-family ipv4-unicast redistribute [options] [<attribute> ...]

### Description

  Route redistribute

### Identifiers

  <vrf-id>    VRF

### Atrributes

  static      Route redistribution of ipv4 static routes
  connected   Route redistribution of ipv4 connected routes
  kernel      Route redistribution of ipv4 kernel routes
  ospf        Route redistribution of ipv4 ospf routes
  
## nv set vrf <vrf-id> router bgp address-family ipv4-unicast redistribute static

### Usage

  nv set vrf <vrf-id> router bgp address-family ipv4-unicast redistribute static [options] [<attribute> ...]

### Description

  Source route type.

### Identifiers

  <vrf-id>    VRF

### Atrributes

  enable      Turn the feature 'on' or 'off'. The default is 'off'.
  metric      Metric to use for the redistributed route. If "auto", an
              appropriate value will be chosen based on the type of route.
              This is the default.
  route-map   Route map to apply to the redistributed route.
  
## nv set vrf <vrf-id> router bgp address-family ipv4-unicast redistribute connected

### Usage

  nv set vrf <vrf-id> router bgp address-family ipv4-unicast redistribute connected [options] [<attribute> ...]

### Description

  Source route type.

### Identifiers

  <vrf-id>    VRF

### Atrributes

  enable      Turn the feature 'on' or 'off'. The default is 'off'.
  metric      Metric to use for the redistributed route. If "auto", an
              appropriate value will be chosen based on the type of route.
              This is the default.
  route-map   Route map to apply to the redistributed route.
  
## nv set vrf <vrf-id> router bgp address-family ipv4-unicast redistribute kernel

### Usage

  nv set vrf <vrf-id> router bgp address-family ipv4-unicast redistribute kernel [options] [<attribute> ...]

### Description

  Source route type.

### Identifiers

  <vrf-id>    VRF

### Atrributes

  enable      Turn the feature 'on' or 'off'. The default is 'off'.
  metric      Metric to use for the redistributed route. If "auto", an
              appropriate value will be chosen based on the type of route.
              This is the default.
  route-map   Route map to apply to the redistributed route.
  
## nv set vrf <vrf-id> router bgp address-family ipv4-unicast redistribute ospf

### Usage

  nv set vrf <vrf-id> router bgp address-family ipv4-unicast redistribute ospf [options] [<attribute> ...]

### Description

  Source route type.

### Identifiers

  <vrf-id>    VRF

### Atrributes

  enable      Turn the feature 'on' or 'off'. The default is 'off'.
  metric      Metric to use for the redistributed route. If "auto", an
              appropriate value will be chosen based on the type of route.
              This is the default.
  route-map   Route map to apply to the redistributed route.
  
## nv set vrf <vrf-id> router bgp address-family ipv4-unicast aggregate-route <aggregate-route-id>

### Usage

  nv set vrf <vrf-id> router bgp address-family ipv4-unicast aggregate-route <aggregate-route-id> [options] [<attribute> ...]

### Description

  An IPv4 aggregate route

### Identifiers

  <vrf-id>              VRF
  <aggregate-route-id>  IPv4 address and route prefix in CIDR notation

### Atrributes

  as-set                If 'on', an AS_SET is generated for the aggregate.
  route-map             Optional policy to modify attributes
  summary-only          If 'on', suppress more-specific routes.

## nv set vrf <vrf-id> router bgp address-family ipv4-unicast network <static-network-id>

### Usage

  nv set vrf <vrf-id> router bgp address-family ipv4-unicast network <static-network-id> [options] [<attribute> ...]

### Description

  An IPv4 static network.

### Identifiers

  <vrf-id>             VRF
  <static-network-id>  IPv4 address and route prefix in CIDR notation

### Atrributes

  route-map            Optional policy to modify attributes
  
## nv set vrf <vrf-id> router bgp address-family ipv4-unicast route-import

### Usage

  nv set vrf <vrf-id> router bgp address-family ipv4-unicast route-import [options] [<attribute> ...]

### Description

  Route import

### Identifiers

  <vrf-id>    VRF

### Atrributes

  from-vrf    Controls for VRF to VRF route leaking for this address-family
  
## nv set vrf <vrf-id> router bgp address-family ipv4-unicast route-import from-vrf

### Usage

  nv set vrf <vrf-id> router bgp address-family ipv4-unicast route-import from-vrf [options] [<attribute> ...]

### Description

  Controls for VRF to VRF route leaking for this address-family

### Identifiers

  <vrf-id>    VRF

### Atrributes

  list        List of VRFs the routes can be imported from
  enable      Turn the feature 'on' or 'off'. The default is 'off'.
  route-map   Route-map to control the import of routes into EVPN

## nv set vrf <vrf-id> router bgp address-family ipv4-unicast route-import from-vrf list <leak-vrf-id>

### Usage

  nv set vrf <vrf-id> router bgp address-family ipv4-unicast route-import from-vrf list <leak-vrf-id> [options]

### Description

  A VRF

### Identifiers

  <vrf-id>       VRF
  <leak-vrf-id>  VRF

## nv set vrf <vrf-id> router bgp address-family ipv4-unicast route-import from-vrf route-map <instance-name>

### Usage

  nv set vrf <vrf-id> router bgp address-family ipv4-unicast route-import from-vrf route-map [options] <instance-name>

### Description

  Route-map to control the import of routes into EVPN

### Identifiers

  <vrf-id>    VRF

## nv set vrf <vrf-id> router bgp address-family ipv4-unicast multipaths

### Usage

  nv set vrf <vrf-id> router bgp address-family ipv4-unicast multipaths [options] [<attribute> ...]

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

## nv set vrf <vrf-id> router bgp address-family ipv4-unicast multipaths ebgp 1-128

### Usage

  nv set vrf <vrf-id> router bgp address-family ipv4-unicast multipaths ebgp [options] 1-128

### Description

  EBGP multipath

### Identifiers

  <vrf-id>    VRF
  
## nv set vrf <vrf-id> router bgp address-family ipv4-unicast multipaths ibgp 1-128

### Usage

  nv set vrf <vrf-id> router bgp address-family ipv4-unicast multipaths ibgp [options] 1-128

### Description

  IBGP multipath

### Identifiers

  <vrf-id>    VRF
  
## nv set vrf <vrf-id> router bgp address-family ipv4-unicast admin-distance

### Usage

  nv set vrf <vrf-id> router bgp address-family ipv4-unicast admin-distance [options] [<attribute> ...]

### Description

  Admin distances.

### Identifiers

  <vrf-id>    VRF

### Atrributes

  external    Distance to apply to routes from EBGP peers when installed into
              the RIB
  internal    Distance to apply to routes from IBGP peers when installed into
              the RIB
## nv set vrf <vrf-id> router bgp address-family ipv4-unicast admin-distance external 1-255

### Usage

  nv set vrf <vrf-id> router bgp address-family ipv4-unicast admin-distance external [options] 1-255

### Description

  Distance to apply to routes from EBGP peers when installed into the RIB

### Identifiers

  <vrf-id>    VRF
  
## nv set vrf <vrf-id> router bgp address-family ipv4-unicast admin-distance internal 1-255

### Usage

  nv set vrf <vrf-id> router bgp address-family ipv4-unicast admin-distance internal [options] 1-255

### Description

  Distance to apply to routes from IBGP peers when installed into the RIB

### Identifiers

  <vrf-id>    VRF
  
## nv set vrf <vrf-id> router bgp address-family ipv4-unicast route-export

### Usage

  nv set vrf <vrf-id> router bgp address-family ipv4-unicast route-export [options] [<attribute> ...]

### Description

  Route export

### Identifiers

  <vrf-id>    VRF

### Atrributes

  to-evpn     Controls for exporting routes from this VRF for this address-
              family into EVPN (as type-5 routes)
              
## nv set vrf <vrf-id> router bgp address-family ipv4-unicast route-export to-evpn

### Usage

  nv set vrf <vrf-id> router bgp address-family ipv4-unicast route-export to-evpn [options] [<attribute> ...]

### Description

  Controls for exporting routes from this VRF for this address-family into EVPN (as type-5 routes)

### Identifiers

  <vrf-id>              VRF

### Atrributes

  enable                Turn the feature 'on' or 'off'. The default is 'off'.
  default-route-origination
                        Default route origination
  route-map             Route-map to control the export of routes into EVPN

## nv set vrf <vrf-id> router bgp address-family l2vpn-evpn

### Usage

  nv set vrf <vrf-id> router bgp address-family l2vpn-evpn [options] [<attribute> ...]

### Description

  BGP VRF configuration. L2VPN EVPN address family

### Identifiers

  <vrf-id>    VRF

### Atrributes

  enable      Turn the feature 'on' or 'off'. The default is 'off'.
  
## nv set vrf <vrf-id> router bgp address-family ipv6-unicast

### Usage

  nv set vrf <vrf-id> router bgp address-family ipv6-unicast [options] [<attribute> ...]

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
  
## nv set vrf <vrf-id> router bgp address-family ipv6-unicast aggregate-route <aggregate-route-id>

### Usage

  nv set vrf <vrf-id> router bgp address-family ipv6-unicast aggregate-route <aggregate-route-id> [options] [<attribute> ...]

### Description

  An IPv6 aggregate route

### Identifiers

  <vrf-id>              VRF
  <aggregate-route-id>  IPv6 address and route prefix in CIDR notation

### Atrributes

  as-set                If 'on', an AS_SET is generated for the aggregate.
  route-map             Optional policy to modify attributes
  summary-only          If 'on', suppress more-specific routes.

## nv set vrf <vrf-id> router bgp address-family ipv6-unicast network <static-network-id>

### Usage

  nv set vrf <vrf-id> router bgp address-family ipv6-unicast network <static-network-id> [options] [<attribute> ...]

### Description

  An IPv6 static network.

### Identifiers

  <vrf-id>             VRF
  <static-network-id>  IPv6 address and route prefix in CIDR notation

### Atrributes

  route-map            Optional policy to modify attributes
  
## nv set vrf <vrf-id> router bgp address-family ipv6-unicast route-import

### Usage

  nv set vrf <vrf-id> router bgp address-family ipv6-unicast route-import [options] [<attribute> ...]

### Description

  Route import

### Identifiers

  <vrf-id>    VRF

### Atrributes

  from-vrf    Controls for VRF to VRF route leaking for this address-family
  
## nv set vrf <vrf-id> router bgp address-family ipv6-unicast route-import from-vrf

### Usage

  nv set vrf <vrf-id> router bgp address-family ipv6-unicast route-import from-vrf [options] [<attribute> ...]

### Description

  Controls for VRF to VRF route leaking for this address-family

### Identifiers

  <vrf-id>    VRF

### Atrributes

  list        List of VRFs the routes can be imported from
  enable      Turn the feature 'on' or 'off'. The default is 'off'.
  route-map   Route-map to control the import of routes into EVPN
  
## nv set vrf <vrf-id> router bgp address-family ipv6-unicast route-import from-vrf list

### Usage

  nv set vrf <vrf-id> router bgp address-family ipv6-unicast route-import from-vrf list [options]

### Description

  Set of VRFs

### Identifiers

  <vrf-id>    VRF
  
## nv set vrf <vrf-id> router bgp address-family ipv6-unicast route-import from-vrf route-map <instance-name>

### Usage

  nv set vrf <vrf-id> router bgp address-family ipv6-unicast route-import from-vrf route-map [options] <instance-name>

### Description

  Route-map to control the import of routes into EVPN

### Identifiers

  <vrf-id>    VRF
  
## nv set vrf <vrf-id> router bgp address-family ipv6-unicast multipaths

### Usage

  nv set vrf <vrf-id> router bgp address-family ipv6-unicast multipaths [options] [<attribute> ...]

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

## nv set vrf <vrf-id> router bgp address-family ipv6-unicast multipaths ebgp 1-128

### Usage

  nv set vrf <vrf-id> router bgp address-family ipv6-unicast multipaths ebgp [options] 1-128

### Description

  EBGP multipath

### Identifiers

  <vrf-id>    VRF
  
## nv set vrf <vrf-id> router bgp address-family ipv6-unicast multipaths ibgp 1-128

### Usage

  nv set vrf <vrf-id> router bgp address-family ipv6-unicast multipaths ibgp [options] 1-128

### Description

  IBGP multipath

### Identifiers

  <vrf-id>    VRF
  
## nv set vrf <vrf-id> router bgp address-family ipv6-unicast admin-distance

### Usage

  nv set vrf <vrf-id> router bgp address-family ipv6-unicast admin-distance [options] [<attribute> ...]

### Description

  Admin distances.

### Identifiers

  <vrf-id>    VRF

### Atrributes

  external    Distance to apply to routes from EBGP peers when installed into
              the RIB
  internal    Distance to apply to routes from IBGP peers when installed into
              the RIB
              
## nv set vrf <vrf-id> router bgp address-family ipv6-unicast admin-distance external 1-255

### Usage

  nv set vrf <vrf-id> router bgp address-family ipv6-unicast admin-distance external [options] 1-255

### Description

  Distance to apply to routes from EBGP peers when installed into the RIB

### Identifiers

  <vrf-id>    VRF
  
## nv set vrf <vrf-id> router bgp address-family ipv6-unicast admin-distance internal 1-255

### Usage

  nv set vrf <vrf-id> router bgp address-family ipv6-unicast admin-distance internal [options] 1-255

### Description

  Distance to apply to routes from IBGP peers when installed into the RIB

### Identifiers

  <vrf-id>    VRF
  
## nv set vrf <vrf-id> router bgp address-family ipv6-unicast route-export

### Usage

  nv set vrf <vrf-id> router bgp address-family ipv6-unicast route-export [options] [<attribute> ...]

### Description

  Route export

### Identifiers

  <vrf-id>    VRF

### Atrributes

  to-evpn     Controls for exporting routes from this VRF for this address-
              family into EVPN (as type-5 routes)
              
## nv set vrf <vrf-id> router bgp address-family ipv6-unicast route-export to-evpn

### Usage

  nv set vrf <vrf-id> router bgp address-family ipv6-unicast route-export to-evpn [options] [<attribute> ...]

### Description

  Controls for exporting routes from this VRF for this address-family into EVPN (as type-5 routes)

### Identifiers

  <vrf-id>              VRF

### Atrributes

  enable                Turn the feature 'on' or 'off'. The default is 'off'.
  default-route-origination
                        Default route origination
  route-map             Route-map to control the export of routes into EVPN

## nv set vrf <vrf-id> router bgp address-family ipv6-unicast redistribute

### Usage

  nv set vrf <vrf-id> router bgp address-family ipv6-unicast redistribute [options] [<attribute> ...]

### Description

  Route redistribute

### Identifiers

  <vrf-id>    VRF

### Atrributes

  static      Route redistribution of ipv4 static routes
  connected   Route redistribution of ipv4 connected routes
  kernel      Route redistribution of ipv4 kernel routes
  ospf6       Route redistribution of ipv6 ospf routes
  
## nv set vrf <vrf-id> router bgp address-family ipv6-unicast redistribute static

### Usage

  nv set vrf <vrf-id> router bgp address-family ipv6-unicast redistribute static [options] [<attribute> ...]

### Description

  Source route type.

### Identifiers

  <vrf-id>    VRF

### Atrributes

  enable      Turn the feature 'on' or 'off'. The default is 'off'.
  metric      Metric to use for the redistributed route. If "auto", an
              appropriate value will be chosen based on the type of route.
              This is the default.
  route-map   Route map to apply to the redistributed route.
  
## nv set vrf <vrf-id> router bgp address-family ipv6-unicast redistribute connected

### Usage

  nv set vrf <vrf-id> router bgp address-family ipv6-unicast redistribute connected [options] [<attribute> ...]

### Description

  Source route type.

### Identifiers

  <vrf-id>    VRF

### Atrributes

  enable      Turn the feature 'on' or 'off'. The default is 'off'.
  metric      Metric to use for the redistributed route. If "auto", an
              appropriate value will be chosen based on the type of route.
              This is the default.
  route-map   Route map to apply to the redistributed route.
  
## nv set vrf <vrf-id> router bgp address-family ipv6-unicast redistribute kernel

### Usage

  nv set vrf <vrf-id> router bgp address-family ipv6-unicast redistribute kernel [options] [<attribute> ...]

### Description

  Source route type.

### Identifiers

  <vrf-id>    VRF

### Atrributes

  enable      Turn the feature 'on' or 'off'. The default is 'off'.
  metric      Metric to use for the redistributed route. If "auto", an
              appropriate value will be chosen based on the type of route.
              This is the default.
  route-map   Route map to apply to the redistributed route.
  
## nv set vrf <vrf-id> router bgp address-family ipv6-unicast redistribute ospf6

### Usage

  nv set vrf <vrf-id> router bgp address-family ipv6-unicast redistribute ospf6 [options] [<attribute> ...]

### Description

  Source route type.

### Identifiers

  <vrf-id>    VRF

### Atrributes

  enable      Turn the feature 'on' or 'off'. The default is 'off'.
  metric      Metric to use for the redistributed route. If "auto", an
              appropriate value will be chosen based on the type of route.
              This is the default.
  route-map   Route map to apply to the redistributed route.
  
## nv set vrf <vrf-id> router bgp path-selection

### Usage

  nv set vrf <vrf-id> router bgp path-selection [options] [<attribute> ...]

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

## nv set vrf <vrf-id> router bgp path-selection aspath

### Usage

  nv set vrf <vrf-id> router bgp path-selection aspath [options] [<attribute> ...]

### Description

  BGP aspath path-selection config, applicable to this BGP instance

### Identifiers

  <vrf-id>         VRF

### Atrributes

  compare-confed   Select AS based on confederations.
  compare-lengths  Select AS based on path length.
  
## nv set vrf <vrf-id> router bgp path-selection med

### Usage

  nv set vrf <vrf-id> router bgp path-selection med [options] [<attribute> ...]

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

## nv set vrf <vrf-id> router bgp path-selection multipath

### Usage

  nv set vrf <vrf-id> router bgp path-selection multipath [options] [<attribute> ...]

### Description

  BGP multipath path-selection config, applicable to this BGP instance

### Identifiers

  <vrf-id>        VRF

### Atrributes

  aspath-ignore   Ignore AS path when determining multipath routing.
  bandwidth       Perform multipath route selection based on bandwidth.
  generate-asset  Requires aspath-ignore to be on

## nv set vrf <vrf-id> router bgp route-reflection

### Usage

  nv set vrf <vrf-id> router bgp route-reflection [options] [<attribute> ...]

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

## nv set vrf <vrf-id> router bgp peer-group <peer-group-id>

### Usage

  nv set vrf <vrf-id> router bgp peer-group <peer-group-id> [options] [<attribute> ...]

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

## nv set vrf <vrf-id> router bgp peer-group <peer-group-id> bfd

### Usage

  nv set vrf <vrf-id> router bgp peer-group <peer-group-id> bfd [options] [<attribute> ...]

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
                     
## nv set vrf <vrf-id> router bgp peer-group <peer-group-id> bfd detect-multiplier 2-255

### Usage

  nv set vrf <vrf-id> router bgp peer-group <peer-group-id> bfd detect-multiplier [options] 2-255

### Description

  Detect multiplier

### Identifiers

  <vrf-id>         VRF
  <peer-group-id>  Domain
  
## nv set vrf <vrf-id> router bgp peer-group <peer-group-id> bfd min-rx-interval 50-60000

### Usage

  nv set vrf <vrf-id> router bgp peer-group <peer-group-id> bfd min-rx-interval [options] 50-60000

### Description

  Minimum receive interval

### Identifiers

  <vrf-id>         VRF
  <peer-group-id>  Domain
  
## nv set vrf <vrf-id> router bgp peer-group <peer-group-id> bfd min-tx-interval 50-60000

### Usage

  nv set vrf <vrf-id> router bgp peer-group <peer-group-id> bfd min-tx-interval [options] 50-60000

### Description

  Minimum transmit interval.  The actual value used is the smaller of this or what the peer expects.

### Identifiers

  <vrf-id>         VRF
  <peer-group-id>  Domain

## nv set vrf <vrf-id> router bgp peer-group <peer-group-id> ttl-security

### Usage

  nv set vrf <vrf-id> router bgp peer-group <peer-group-id> ttl-security [options] [<attribute> ...]

### Description

  RFC 5082

### Identifiers

  <vrf-id>         VRF
  <peer-group-id>  Domain

### Atrributes

  enable           Turn the feature 'on' or 'off'. The default is 'off'.
  hops             Number of hops

## nv set vrf <vrf-id> router bgp peer-group <peer-group-id> ttl-security hops 1-254

### Usage

  nv set vrf <vrf-id> router bgp peer-group <peer-group-id> ttl-security hops [options] 1-254

### Description

  Number of hops

### Identifiers

  <vrf-id>         VRF
  <peer-group-id>  Domain
  
## nv set vrf <vrf-id> router bgp peer-group <peer-group-id> capabilities

### Usage

  nv set vrf <vrf-id> router bgp peer-group <peer-group-id> capabilities [options] [<attribute> ...]

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

## nv set vrf <vrf-id> router bgp peer-group <peer-group-id> graceful-restart

### Usage

  nv set vrf <vrf-id> router bgp peer-group <peer-group-id> graceful-restart [options] [<attribute> ...]

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
                   
## nv set vrf <vrf-id> router bgp peer-group <peer-group-id> local-as

### Usage

  nv set vrf <vrf-id> router bgp peer-group <peer-group-id> local-as [options] [<attribute> ...]

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
                   
## nv set vrf <vrf-id> router bgp peer-group <peer-group-id> local-as asn 1-4294967295

### Usage

  nv set vrf <vrf-id> router bgp peer-group <peer-group-id> local-as asn [options] 1-4294967295

### Description

  ASN to use to establish the peering if different from the ASN of the BGP instance.  This configuration finds use during AS renumbering.  The local-as configured is also attached to incoming and outgoing updates.

### Identifiers

  <vrf-id>         VRF
  <peer-group-id>  Domain
  
## nv set vrf <vrf-id> router bgp peer-group <peer-group-id> timers

### Usage

  nv set vrf <vrf-id> router bgp peer-group <peer-group-id> timers [options] [<attribute> ...]

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
                       
## nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family

### Usage

  nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family [options] [<attribute> ...]

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
  
## nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast

### Usage

  nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast [options] [<attribute> ...]

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

## nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast community-advertise

### Usage

  nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast community-advertise [options] [<attribute> ...]

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
                   
## nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast attribute-mod

### Usage

  nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast attribute-mod [options] [<attribute> ...]

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
                   
## nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast aspath

### Usage

  nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast aspath [options] [<attribute> ...]

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
                   
## nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast aspath allow-my-asn

### Usage

  nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast aspath allow-my-asn [options] [<attribute> ...]

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
                   
## nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast aspath allow-my-asn occurrences 1-10

### Usage

  nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast aspath allow-my-asn occurrences [options] 1-10

### Description

  Indicates max number of occurrences of the local system's AS number in the received AS_PATH

### Identifiers

  <vrf-id>         VRF
  <peer-group-id>  Domain

## nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast prefix-limits

### Usage

  nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast prefix-limits [options] [<attribute> ...]

### Description

  Limits on prefix from the peer for this address-family

### Identifiers

  <vrf-id>         VRF
  <peer-group-id>  Domain

### Atrributes

  inbound          Limits on inbound prefix from the peer for this address-
                   family
                   
## nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast prefix-limits inbound

### Usage

  nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast prefix-limits inbound [options] [<attribute> ...]

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
                     
## nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast prefix-limits inbound warning-threshold 1-100

### Usage

  nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast prefix-limits inbound warning-threshold [options] 1-100

### Description

  Percentage of the maximum at which a warning syslog is generated.

### Identifiers

  <vrf-id>         VRF
  <peer-group-id>  Domain
  
## nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast prefix-limits inbound reestablish-wait 1-4294967295

### Usage

  nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast prefix-limits inbound reestablish-wait [options] 1-4294967295

### Description

  Specifes the time in seconds to wait before establishing the BGP session again with the peer. Defaults to 'auto', which will use standard BGP timers and processing.  This would typically be 2-3 seconds.

### Identifiers

  <vrf-id>         VRF
  <peer-group-id>  Domai
  
## nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast default-route-origination

### Usage

  nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast default-route-origination [options] [<attribute> ...]

### Description

  Default route origination

### Identifiers

  <vrf-id>         VRF
  <peer-group-id>  Domain

### Atrributes

  enable           Turn the feature 'on' or 'off'. The default is 'off'.
  policy           Optional route-map policy to control the conditions under
                   which the default route is originated.
                   
## nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast policy

### Usage

  nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast policy [options] [<attribute> ...]

### Description

  Policies for ipv4 unicast

### Identifiers

  <vrf-id>         VRF
  <peer-group-id>  Domain

### Atrributes

  inbound          Outbound unicast policy
  outbound         Outbound unicast policy

## nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast policy inbound

### Usage

  nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast policy inbound [options] [<attribute> ...]

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
  
## nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast policy inbound aspath-list none

### Usage

  nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast policy inbound aspath-list [options] none

### Description

  AS-Path filter list to apply to Updates received from this peer

### Identifiers

  <vrf-id>         VRF
  <peer-group-id>  Domain
  
## nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast policy outbound

### Usage

  nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast policy outbound [options] [<attribute> ...]

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
  
## nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast policy outbound aspath-list none

### Usage

  nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast policy outbound aspath-list [options] none

### Description

  AS-Path filter list to apply to Updates sent to this peer

### Identifiers

  <vrf-id>         VRF
  <peer-group-id>  Domain
  
## nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast conditional-advertise

### Usage

  nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast conditional-advertise [options] [<attribute> ...]

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
                   
## nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast conditional-advertise advertise-map <instance-name>

### Usage

  nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast conditional-advertise advertise-map [options] <instance-name>

### Description

  route-map contains prefix-list which has list of routes/prefixes to operate on.

### Identifiers

  <vrf-id>         VRF
  <peer-group-id>  Domain
  
## nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast conditional-advertise exist-map <instance-name>

### Usage

  nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast conditional-advertise exist-map [options] <instance-name>

### Description

  route-map contains the conditional routes/prefixes in prefix-list.

### Identifiers

  <vrf-id>         VRF
  <peer-group-id>  Domain
  
## nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast conditional-advertise non-exist-map <instance-name>

### Usage

  nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast conditional-advertise non-exist-map [options] <instance-name>

### Description

  route-map contains the negative conditional routes/prefixes in prefix-list.

### Identifiers

  <vrf-id>         VRF
  <peer-group-id>  Domain

## nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast weight 0-65535

### Usage

  nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast weight [options] 0-65535

### Description

  Weight applied to routes received from peer; this is used in the BGP route selection algorithm

### Identifiers

  <vrf-id>         VRF
  <peer-group-id>  Domain
  
## nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast

### Usage

  nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast [options] [<attribute> ...]

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

## nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast policy

### Usage

  nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast policy [options] [<attribute> ...]

### Description

  Policies for ipv6 unicast

### Identifiers

  <vrf-id>         VRF
  <peer-group-id>  Domain

### Atrributes

  inbound          Outbound unicast policy
  outbound         Outbound unicast policy
  
## nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast policy inbound

### Usage

  nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast policy inbound [options] [<attribute> ...]

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
  
## nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast policy inbound aspath-list none

### Usage

  nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast policy inbound aspath-list [options] none

### Description

  AS-Path filter list to apply to Updates received from this peer

### Identifiers

  <vrf-id>         VRF
  <peer-group-id>  Domain 
  
## nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast policy outbound

### Usage

  nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast policy outbound [options] [<attribute> ...]

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
  
## nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast policy outbound aspath-list none

### Usage

  nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast policy outbound aspath-list [options] none

### Description

  AS-Path filter list to apply to Updates sent to this peer

### Identifiers

  <vrf-id>         VRF
  <peer-group-id>  Domain
  
## nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast aspath

### Usage

  nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast aspath [options] [<attribute> ...]

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
                   
## nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast aspath allow-my-asn

### Usage

  nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast aspath allow-my-asn [options] [<attribute> ...]

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
                   
## nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast aspath allow-my-asn occurrences 1-10

### Usage

  nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast aspath allow-my-asn occurrences [options] 1-10

### Description

  Indicates max number of occurrences of the local system's AS number in the received AS_PATH

### Identifiers

  <vrf-id>         VRF
  <peer-group-id>  Domain
  
## nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast prefix-limits

### Usage

  nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast prefix-limits [options] [<attribute> ...]

### Description

  Limits on prefix from the peer for this address-family

### Identifiers

  <vrf-id>         VRF
  <peer-group-id>  Domain

### Atrributes

  inbound          Limits on inbound prefix from the peer for this address-
                   family
                   
## nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast prefix-limits inbound

### Usage

  nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast prefix-limits inbound [options] [<attribute> ...]

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
                     
## nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast prefix-limits inbound warning-threshold 1-100

### Usage

  nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast prefix-limits inbound warning-threshold [options] 1-100

### Description

  Percentage of the maximum at which a warning syslog is generated.

### Identifiers

  <vrf-id>         VRF
  <peer-group-id>  Domain

## nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast prefix-limits inbound reestablish-wait 1-4294967295

### Usage

  nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast prefix-limits inbound reestablish-wait [options] 1-4294967295

### Description

  Specifes the time in seconds to wait before establishing the BGP session again with the peer. Defaults to 'auto', which will use standard BGP timers and processing.  This would typically be 2-3 seconds.

### Identifiers

  <vrf-id>         VRF
  <peer-group-id>  Domain
  
## nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast default-route-origination

### Usage

  nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast default-route-origination [options] [<attribute> ...]

### Description

  Default route origination

### Identifiers

  <vrf-id>         VRF
  <peer-group-id>  Domain

### Atrributes

  enable           Turn the feature 'on' or 'off'. The default is 'off'.
  policy           Optional route-map policy to control the conditions under
                   which the default route is originated.
                   
## nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast community-advertise

### Usage

  nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast community-advertise [options] [<attribute> ...]

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
                   
## nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast attribute-mod

### Usage

  nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast attribute-mod [options] [<attribute> ...]

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
                   
## nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast conditional-advertise

### Usage

  nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast conditional-advertise [options] [<attribute> ...]

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
                   
## nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast conditional-advertise advertise-map <instance-name>

### Usage

  nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast conditional-advertise advertise-map [options] <instance-name>

### Description

  route-map contains prefix-list which has list of routes/prefixes to operate on.

### Identifiers

  <vrf-id>         VRF
  <peer-group-id>  Domain
  
## nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast conditional-advertise exist-map <instance-name>

### Usage

  nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast conditional-advertise exist-map [options] <instance-name>

### Description

  route-map contains the conditional routes/prefixes in prefix-list.

### Identifiers

  <vrf-id>         VRF
  <peer-group-id>  Domain
  
## nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast conditional-advertise non-exist-map <instance-name>

### Usage

  nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast conditional-advertise non-exist-map [options] <instance-name>

### Description

  route-map contains the negative conditional routes/prefixes in prefix-list.

### Identifiers

  <vrf-id>         VRF
  <peer-group-id>  Domain

## nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast weight 0-65535

### Usage

  nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast weight [options] 0-65535

### Description

  Weight applied to routes received from peer; this is used in the BGP route selection algorithm

### Identifiers

  <vrf-id>         VRF
  <peer-group-id>  Domain
  
## nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family l2vpn-evpn

### Usage

  nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family l2vpn-evpn [options] [<attribute> ...]

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

## nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family l2vpn-evpn attribute-mod

### Usage

  nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family l2vpn-evpn attribute-mod [options] [<attribute> ...]

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
                   
## nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family l2vpn-evpn aspath

### Usage

  nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family l2vpn-evpn aspath [options] [<attribute> ...]

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
                   
## nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family l2vpn-evpn aspath allow-my-asn

### Usage

  nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family l2vpn-evpn aspath allow-my-asn [options] [<attribute> ...]

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
                   
## nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family l2vpn-evpn aspath allow-my-asn occurrences 1-10

### Usage

  nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family l2vpn-evpn aspath allow-my-asn occurrences [options] 1-10

### Description

  Indicates max number of occurrences of the local system's AS number in the received AS_PATH

### Identifiers

  <vrf-id>         VRF
  <peer-group-id>  Domain
  
## nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family l2vpn-evpn policy

### Usage

  nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family l2vpn-evpn policy [options] [<attribute> ...]

### Description

  Policies for l2vpn evpn

### Identifiers

  <vrf-id>         VRF
  <peer-group-id>  Domain

### Atrributes

  inbound          Inbound l2vpn-evpn policy
  outbound         Outbound l2vpn-evpn policy

## nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family l2vpn-evpn policy inbound

### Usage

  nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family l2vpn-evpn policy inbound [options] [<attribute> ...]

### Description

  Inbound l2vpn-evpn policy

### Identifiers

  <vrf-id>         VRF
  <peer-group-id>  Domain

### Atrributes

  route-map        Route map to apply to Updates received from this peer

## nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family l2vpn-evpn policy outbound

### Usage

  nv set vrf <vrf-id> router bgp peer-group <peer-group-id> address-family l2vpn-evpn policy outbound [options] [<attribute> ...]

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

## nv set vrf <vrf-id> router bgp peer-group <peer-group-id> password none

### Usage

  nv set vrf <vrf-id> router bgp peer-group <peer-group-id> password [options] none

### Description

  Password

### Identifiers

  <vrf-id>         VRF
  <peer-group-id>  Domain

## nv set vrf <vrf-id> router bgp peer-group <peer-group-id> description none

### Usage

  nv set vrf <vrf-id> router bgp peer-group <peer-group-id> description [options] none

### Description

  neighbor description

### Identifiers

  <vrf-id>         VRF
  <peer-group-id>  Domain
  
## nv set vrf <vrf-id> router bgp route-export

### Usage

  nv set vrf <vrf-id> router bgp route-export [options] [<attribute> ...]

### Description

  Controls for exporting ipv4 and ipv6 routes from this VRF

### Identifiers

  <vrf-id>    VRF

### Atrributes

  to-evpn     Controls for exporting routes from this VRF into EVPN
  
## nv set vrf <vrf-id> router bgp route-export to-evpn

### Usage

  nv set vrf <vrf-id> router bgp route-export to-evpn [options] [<attribute> ...]

### Description

  Controls for exporting routes from this VRF into EVPN

### Identifiers

  <vrf-id>      VRF

### Atrributes

  route-target  List the RTs to attach to host or prefix routes when exporting
                them into EVPN or "auto". If "auto", the RT will be derived.
                This is the default.
                
## nv set vrf <vrf-id> router bgp route-export to-evpn route-target <rt-id>

### Usage

  nv set vrf <vrf-id> router bgp route-export to-evpn route-target <rt-id> [options]

### Description

  A route target identifier

### Identifiers

  <vrf-id>    VRF
  <rt-id>     Route targets or "auto"
  
## nv set vrf <vrf-id> router bgp route-import

### Usage

  nv set vrf <vrf-id> router bgp route-import [options] [<attribute> ...]

### Description

  Controls for importing of ipv4 and ipv6 routes from this VRF

### Identifiers

  <vrf-id>    VRF

### Atrributes

  from-evpn   Controls for importing EVPN type-2 and type-5 routes into this
              VRF
              
## nv set vrf <vrf-id> router bgp route-import from-evpn

### Usage

  nv set vrf <vrf-id> router bgp route-import from-evpn [options] [<attribute> ...]

### Description

  Controls for importing EVPN type-2 and type-5 routes into this VRF

### Identifiers

  <vrf-id>      VRF

### Atrributes

  route-target  List the RTs to attach to host or prefix routes when importing
                them into VRF or "auto". If "auto", the RT will be derived.
                This is the default. 
                
## nv set vrf <vrf-id> router bgp route-import from-evpn route-target <rt-id>

### Usage

  nv set vrf <vrf-id> router bgp route-import from-evpn route-target <rt-id> [options]

### Description

  A route target identifier

### Identifiers

  <vrf-id>    VRF
  <rt-id>     Route targets or "auto"
  
## nv set vrf <vrf-id> router bgp timers

### Usage

  nv set vrf <vrf-id> router bgp timers [options] [<attribute> ...]

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

## nv set vrf <vrf-id> router bgp timers connection-retry 1-65535

### Usage

  nv set vrf <vrf-id> router bgp timers connection-retry [options] 1-65535

### Description

  Time interval at which connection attempts are retried upon a failure.

### Identifiers

  <vrf-id>    VRF
  
## nv set vrf <vrf-id> router bgp confederation

### Usage

  nv set vrf <vrf-id> router bgp confederation [options] [<attribute> ...]

### Description

  BGP Confederation options.

### Identifiers

  <vrf-id>    VRF

### Atrributes

  member-as   Confederation ASNs of the peers, maps to BGP confederation peers
  id          Confederation ASN, maps to BGP confederation id
  
## nv set vrf <vrf-id> router bgp confederation member-as

### Usage

  nv set vrf <vrf-id> router bgp confederation member-as [options]

### Description

  Set of autonomous numbers

### Identifiers

  <vrf-id>    VRF
  
## nv set vrf <vrf-id> router bgp neighbor <neighbor-id>

### Usage

  nv set vrf <vrf-id> router bgp neighbor <neighbor-id> [options] [<attribute> ...]

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

## nv set vrf <vrf-id> router bgp neighbor <neighbor-id> bfd

### Usage

  nv set vrf <vrf-id> router bgp neighbor <neighbor-id> bfd [options] [<attribute> ...]

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
                     
## nv set vrf <vrf-id> router bgp neighbor <neighbor-id> bfd detect-multiplier 2-255

### Usage

  nv set vrf <vrf-id> router bgp neighbor <neighbor-id> bfd detect-multiplier [options] 2-255

### Description

  Detect multiplier

### Identifiers

  <vrf-id>       VRF
  <neighbor-id>  Peer ID
  
## nv set vrf <vrf-id> router bgp neighbor <neighbor-id> bfd min-rx-interval 50-60000

### Usage

  nv set vrf <vrf-id> router bgp neighbor <neighbor-id> bfd min-rx-interval [options] 50-60000

### Description

  Minimum receive interval

### Identifiers

  <vrf-id>       VRF
  <neighbor-id>  Peer ID
  
## nv set vrf <vrf-id> router bgp neighbor <neighbor-id> bfd min-tx-interval 50-60000

### Usage

  nv set vrf <vrf-id> router bgp neighbor <neighbor-id> bfd min-tx-interval [options] 50-60000

### Description

  Minimum transmit interval.  The actual value used is the smaller of this or what the peer expects.

### Identifiers

  <vrf-id>       VRF
  <neighbor-id>  Peer ID
  
## nv set vrf <vrf-id> router bgp neighbor <neighbor-id> capabilities

### Usage

  nv set vrf <vrf-id> router bgp neighbor <neighbor-id> capabilities [options] [<attribute> ...]

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

## nv set vrf <vrf-id> router bgp neighbor <neighbor-id> local-as

### Usage

  nv set vrf <vrf-id> router bgp neighbor <neighbor-id> local-as [options] [<attribute> ...]

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
                 
## nv set vrf <vrf-id> router bgp neighbor <neighbor-id> local-as asn 1-4294967295

### Usage

  nv set vrf <vrf-id> router bgp neighbor <neighbor-id> local-as asn [options] 1-4294967295

### Description

  ASN to use to establish the peering if different from the ASN of the BGP instance.  This configuration finds use during AS renumbering.  The local-as configured is also attached to incoming and outgoing updates.

### Identifiers

  <vrf-id>       VRF
  <neighbor-id>  Peer ID
  
## nv set vrf <vrf-id> router bgp neighbor <neighbor-id> graceful-restart

### Usage

  nv set vrf <vrf-id> router bgp neighbor <neighbor-id> graceful-restart [options] [<attribute> ...]

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
                 
## nv set vrf <vrf-id> router bgp neighbor <neighbor-id> ttl-security

### Usage

  nv set vrf <vrf-id> router bgp neighbor <neighbor-id> ttl-security [options] [<attribute> ...]

### Description

  RFC 5082

### Identifiers

  <vrf-id>       VRF
  <neighbor-id>  Peer ID

### Atrributes

  enable         Turn the feature 'on' or 'off'. The default is 'off'.
  hops           Number of hops
  
## nv set vrf <vrf-id> router bgp neighbor <neighbor-id> ttl-security hops 1-254

### Usage

  nv set vrf <vrf-id> router bgp neighbor <neighbor-id> ttl-security hops [options] 1-254

### Description

  Number of hops

### Identifiers

  <vrf-id>       VRF
  <neighbor-id>  Peer ID
  
## nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family

### Usage

  nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family [options] [<attribute> ...]

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
  
## nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast

### Usage

  nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast [options] [<attribute> ...]

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

## nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast attribute-mod

### Usage

  nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast attribute-mod [options] [<attribute> ...]

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
                 
## nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast aspath

### Usage

  nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast aspath [options] [<attribute> ...]

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
                   
## nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast aspath allow-my-asn

### Usage

  nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast aspath allow-my-asn [options] [<attribute> ...]

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
                 
## nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast aspath allow-my-asn occurrences 1-10

### Usage

  nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast aspath allow-my-asn occurrences [options] 1-10

### Description

  Indicates max number of occurrences of the local system's AS number in the received AS_PATH

### Identifiers

  <vrf-id>       VRF
  <neighbor-id>  Peer ID
  
## nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast policy

### Usage

  nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast policy [options] [<attribute> ...]

### Description

  Policies for ipv4 unicast

### Identifiers

  <vrf-id>       VRF
  <neighbor-id>  Peer ID

### Atrributes

  inbound        Outbound unicast policy
  outbound       Outbound unicast policy

## nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast policy inbound

### Usage

  nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast policy inbound [options] [<attribute> ...]

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
  
## nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast policy inbound aspath-list none

### Usage

  nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast policy inbound aspath-list [options] none

### Description

  AS-Path filter list to apply to Updates received from this peer

### Identifiers

  <vrf-id>       VRF
  <neighbor-id>  Peer ID
  
## nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast policy outbound

### Usage

  nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast policy outbound [options] [<attribute> ...]

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

## nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast policy outbound aspath-list none

### Usage

  nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast policy outbound aspath-list [options] none

### Description

  AS-Path filter list to apply to Updates sent to this peer

### Identifiers

  <vrf-id>       VRF
  <neighbor-id>  Peer ID
  
## nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast prefix-limits

### Usage

  nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast prefix-limits [options] [<attribute> ...]

### Description

  Limits on prefix from the peer for this address-family

### Identifiers

  <vrf-id>       VRF
  <neighbor-id>  Peer ID

### Atrributes

  inbound        Limits on inbound prefix from the peer for this address-
                 family
                 
## nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast prefix-limits inbound

### Usage

  nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast prefix-limits inbound [options] [<attribute> ...]

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
                     generated
                     
## nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast prefix-limits inbound warning-threshold 1-100

### Usage

  nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast prefix-limits inbound warning-threshold [options] 1-100

### Description

  Percentage of the maximum at which a warning syslog is generated.

### Identifiers

  <vrf-id>       VRF
  <neighbor-id>  Peer ID
  
## nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast prefix-limits inbound reestablish-wait 1-4294967295

### Usage

  nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast prefix-limits inbound reestablish-wait [options] 1-4294967295

### Description

  Specifes the time in seconds to wait before establishing the BGP session again with the peer. Defaults to 'auto', which will use standard BGP timers and processing.  This would typically be 2-3 seconds.

### Identifiers

  <vrf-id>       VRF
  <neighbor-id>  Peer ID 
  
## nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast default-route-origination

### Usage

  nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast default-route-origination [options] [<attribute> ...]

### Description

  Default route origination

### Identifiers

  <vrf-id>       VRF
  <neighbor-id>  Peer ID

### Atrributes

  enable         Turn the feature 'on' or 'off'. The default is 'off'.
  policy         Optional route-map policy to control the conditions under
                 which the default route is originated.
                 
## nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast community-advertise

### Usage

  nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast community-advertise [options] [<attribute> ...]

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
                 
## nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast conditional-advertise

### Usage

  nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast conditional-advertise [options] [<attribute> ...]

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
                 
## nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast conditional-advertise advertise-map <instance-name>

### Usage

  nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast conditional-advertise advertise-map [options] <instance-name>

### Description

  route-map contains prefix-list which has list of routes/prefixes to operate on.

### Identifiers

  <vrf-id>       VRF
  <neighbor-id>  Peer ID
  
## nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast conditional-advertise exist-map <instance-name>

### Usage

  nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast conditional-advertise exist-map [options] <instance-name>

### Description

  route-map contains the conditional routes/prefixes in prefix-list.

### Identifiers

  <vrf-id>       VRF
  <neighbor-id>  Peer ID
  
## nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast conditional-advertise non-exist-map <instance-name>

### Usage

  nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast conditional-advertise non-exist-map [options] <instance-name>

### Description

  route-map contains the negative conditional routes/prefixes in prefix-list.

### Identifiers

  <vrf-id>       VRF
  <neighbor-id>  Peer ID

## nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast weight 0-65535

### Usage

  nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast weight [options] 0-65535

### Description

  Weight applied to routes received from peer; this is used in the BGP route selection algorithm

### Identifiers

  <vrf-id>       VRF
  <neighbor-id>  Peer 

## nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast

### Usage

  nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast [options] [<attribute> ...]

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

## nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast attribute-mod

### Usage

  nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast attribute-mod [options] [<attribute> ...]

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
                 
## nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast aspath

### Usage

  nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast aspath [options] [<attribute> ...]

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

## nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast aspath allow-my-asn

### Usage

  nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast aspath allow-my-asn [options] [<attribute> ...]

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
                 
## nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast aspath allow-my-asn occurrences 1-10

### Usage

  nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast aspath allow-my-asn occurrences [options] 1-10

### Description

  Indicates max number of occurrences of the local system's AS number in the received AS_PATH

### Identifiers

  <vrf-id>       VRF
  <neighbor-id>  Peer ID
  
## nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast prefix-limits

### Usage

  nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast prefix-limits [options] [<attribute> ...]

### Description

  Limits on prefix from the peer for this address-family

### Identifiers

  <vrf-id>       VRF
  <neighbor-id>  Peer ID

### Atrributes

  inbound        Limits on inbound prefix from the peer for this address-
                 family
                 
## nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast prefix-limits inbound

### Usage

  nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast prefix-limits inbound [options] [<attribute> ...]

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
                     generated
                     
## nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast prefix-limits inbound warning-threshold 1-100

### Usage

  nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast prefix-limits inbound warning-threshold [options] 1-100

### Description

  Percentage of the maximum at which a warning syslog is generated.

### Identifiers

  <vrf-id>       VRF
  <neighbor-id>  Peer ID 

## nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast prefix-limits inbound reestablish-wait 1-4294967295

### Usage

  nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast prefix-limits inbound reestablish-wait [options] 1-4294967295

### Description

  Specifes the time in seconds to wait before establishing the BGP session again with the peer. Defaults to 'auto', which will use standard BGP timers and processing.  This would typically be 2-3 seconds.

### Identifiers

  <vrf-id>       VRF
  <neighbor-id>  Peer ID
  
## nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast default-route-origination

### Usage

  nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast default-route-origination [options] [<attribute> ...]

### Description

  Default route origination

### Identifiers

  <vrf-id>       VRF
  <neighbor-id>  Peer ID

### Atrributes

  enable         Turn the feature 'on' or 'off'. The default is 'off'.
  policy         Optional route-map policy to control the conditions under
                 which the default route is originated.
                 
## nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast policy

### Usage

  nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast policy [options] [<attribute> ...]

### Description

  Policies for ipv6 unicast

### Identifiers

  <vrf-id>       VRF
  <neighbor-id>  Peer ID

### Atrributes

  inbound        Outbound unicast policy
  outbound       Outbound unicast policy
  
## nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast policy inbound

### Usage

  nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast policy inbound [options] [<attribute> ...]

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
  
## nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast policy inbound aspath-list none

### Usage

  nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast policy inbound aspath-list [options] none

### Description

  AS-Path filter list to apply to Updates received from this peer

### Identifiers

  <vrf-id>       VRF
  <neighbor-id>  Peer ID
  
## nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast policy outbound

### Usage

  nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast policy outbound [options] [<attribute> ...]

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

## nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast policy outbound aspath-list none

### Usage

  nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast policy outbound aspath-list [options] none

### Description

  AS-Path filter list to apply to Updates sent to this peer

### Identifiers

  <vrf-id>       VRF
  <neighbor-id>  Peer ID
  
## nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast community-advertise

### Usage

  nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast community-advertise [options] [<attribute> ...]

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
                 
## nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast conditional-advertise

### Usage

  nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast conditional-advertise [options] [<attribute> ...]

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
                 
## nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast conditional-advertise advertise-map <instance-name>

### Usage

  nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast conditional-advertise advertise-map [options] <instance-name>

### Description

  route-map contains prefix-list which has list of routes/prefixes to operate on.

### Identifiers

  <vrf-id>       VRF
  <neighbor-id>  Peer ID
  
## nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast conditional-advertise exist-map <instance-name>

### Usage

  nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast conditional-advertise exist-map [options] <instance-name>

### Description

  route-map contains the conditional routes/prefixes in prefix-list.

### Identifiers

  <vrf-id>       VRF
  <neighbor-id>  Peer ID

## nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast conditional-advertise non-exist-map <instance-name>

### Usage

  nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast conditional-advertise non-exist-map [options] <instance-name>

### Description

  route-map contains the negative conditional routes/prefixes in prefix-list.

### Identifiers

  <vrf-id>       VRF
  <neighbor-id>  Peer ID

## nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast weight 0-65535

### Usage

  nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast weight [options] 0-65535

### Description

  Weight applied to routes received from peer; this is used in the BGP route selection algorithm

### Identifiers

  <vrf-id>       VRF
  <neighbor-id>  Peer ID
  
## nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family l2vpn-evpn

### Usage

  nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family l2vpn-evpn [options] [<attribute> ...]

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

## nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family l2vpn-evpn attribute-mod

### Usage

  nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family l2vpn-evpn attribute-mod [options] [<attribute> ...]

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
                 
## nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family l2vpn-evpn aspath

### Usage

  nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family l2vpn-evpn aspath [options] [<attribute> ...]

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
                  
## nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family l2vpn-evpn aspath allow-my-asn

### Usage

  nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family l2vpn-evpn aspath allow-my-asn [options] [<attribute> ...]

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
                 
## nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family l2vpn-evpn aspath allow-my-asn occurrences 1-10

### Usage

  nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family l2vpn-evpn aspath allow-my-asn occurrences [options] 1-10

### Description

  Indicates max number of occurrences of the local system's AS number in the received AS_PATH

### Identifiers

  <vrf-id>       VRF
  <neighbor-id>  Peer ID
  
## nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family l2vpn-evpn policy

### Usage

  nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family l2vpn-evpn policy [options] [<attribute> ...]

### Description

  Policies for l2vpn evpn

### Identifiers

  <vrf-id>       VRF
  <neighbor-id>  Peer ID

### Atrributes

  inbound        Inbound l2vpn-evpn policy
  outbound       Outbound l2vpn-evpn policy
  
## nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family l2vpn-evpn policy inbound

### Usage

  nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family l2vpn-evpn policy inbound [options] [<attribute> ...]

### Description

  Inbound l2vpn-evpn policy

### Identifiers

  <vrf-id>       VRF
  <neighbor-id>  Peer ID

### Atrributes

  route-map      Route map to apply to Updates received from this peer
  
## nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family l2vpn-evpn policy outbound

### Usage

  nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family l2vpn-evpn policy outbound [options] [<attribute> ...]

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

## nv set vrf <vrf-id> router bgp neighbor <neighbor-id> timers

### Usage

  nv set vrf <vrf-id> router bgp neighbor <neighbor-id> timers [options] [<attribute> ...]

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
                       
## nv set vrf <vrf-id> router bgp neighbor <neighbor-id> password none

### Usage

  nv set vrf <vrf-id> router bgp neighbor <neighbor-id> password [options] none

### Description

  Password

### Identifiers

  <vrf-id>       VRF
  <neighbor-id>  Peer ID
  
## nv set vrf <vrf-id> router bgp neighbor <neighbor-id> description none

### Usage

  nv set vrf <vrf-id> router bgp neighbor <neighbor-id> description [options] none

### Description

  neighbor description

### Identifiers

  <vrf-id>       VRF
  <neighbor-id>  Peer ID

## nv set vrf <vrf-id> router bgp dynamic-peer-limit 1-5000

### Usage

  nv set vrf <vrf-id> router bgp dynamic-peer-limit [options] 1-5000

### Description

  Maximum number of dynamic neighbors from whom we can accept a connection. Applicable only if 'dynamic-peering' subnet ranges are configured

### Identifiers

  <vrf-id>    VRF
  
## nv set vrf <vrf-id> router static <route-id>

### Usage

  nv set vrf <vrf-id> router static <route-id> [options] [<attribute> ...]

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

## nv set vrf <vrf-id> router static <route-id> distance <distance-id>

### Usage

  nv set vrf <vrf-id> router static <route-id> distance <distance-id> [options] [<attribute> ...]

### Description

  A path

### Identifiers

  <vrf-id>       VRF
  <route-id>     IP prefix
  <distance-id>  A path distance

### Atrributes

  via            Nexthops
  tag            Path tag

## nv set vrf <vrf-id> router static <route-id> distance <distance-id> via <via-id>

### Usage

  nv set vrf <vrf-id> router static <route-id> distance <distance-id> via <via-id> [options] [<attribute> ...]

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
  
## nv set vrf <vrf-id> router static <route-id> distance <distance-id> via <via-id> flag onlink

### Usage

  nv set vrf <vrf-id> router static <route-id> distance <distance-id> via <via-id> flag [options] onlink

### Description

  Nexthop flags

### Identifiers

  <vrf-id>       VRF
  <route-id>     IP prefix
  <distance-id>  A path distance
  <via-id>       IP address, interface, or "blackhole".
  
## nv set vrf <vrf-id> router static <route-id> via <via-id>

### Usage

  nv set vrf <vrf-id> router static <route-id> via <via-id> [options] [<attribute> ...]

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
  
## nv set vrf <vrf-id> router static <route-id> via <via-id> flag onlink

### Usage

  nv set vrf <vrf-id> router static <route-id> via <via-id> flag [options] onlink

### Description

  Nexthop flags

### Identifiers

  <vrf-id>    VRF
  <route-id>  IP prefix
  <via-id>    IP address, interface, or "blackhole".
  
## nv set vrf <vrf-id> router pim

### Usage

  nv set vrf <vrf-id> router pim [options] [<attribute> ...]

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
  
## nv set vrf <vrf-id> router pim timers

### Usage

  nv set vrf <vrf-id> router pim timers [options] [<attribute> ...]

### Description

  Timers

### Identifiers

  <vrf-id>       VRF

### Atrributes

  keep-alive     Timeout value for S,G stream, in seconds
  rp-keep-alive  RP's timeout value, in seconds
  
## nv set vrf <vrf-id> router pim ecmp

### Usage

  nv set vrf <vrf-id> router pim ecmp [options] [<attribute> ...]

### Description

  Choose all available ECMP paths for a particular RPF.  If 'off', the first nexthop found will be used.  This is the default.

### Identifiers

  <vrf-id>    VRF

### Atrributes

  enable      Turn the feature 'on' or 'off'. The default is 'off'.
  rebalance   Recalculate all multicast streams in the event of path going
              down. If 'off', only the impacted streams by path going down
              recalculated. This is the default.
              
## nv set vrf <vrf-id> router pim msdp-mesh-group <msdp-mesh-group-id>

### Usage

  nv set vrf <vrf-id> router pim msdp-mesh-group <msdp-mesh-group-id> [options] [<attribute> ...]

### Description

  MSDP mesh-group

### Identifiers

  <vrf-id>              VRF
  <msdp-mesh-group-id>  MSDP mesh group name

### Atrributes

  member-address        Set of member-address
  source-address        MSDP mesh-group source IP address

## nv set vrf <vrf-id> router pim msdp-mesh-group <msdp-mesh-group-id> member-address <mesh-member-id>

### Usage

  nv set vrf <vrf-id> router pim msdp-mesh-group <msdp-mesh-group-id> member-address <mesh-member-id> [options]

### Description

  A MSDP mesh member

### Identifiers

  <vrf-id>              VRF
  <msdp-mesh-group-id>  MSDP mesh group name
  <mesh-member-id>      MSDP mesh-group member IP address

## nv set vrf <vrf-id> router pim msdp-mesh-group <msdp-mesh-group-id> source-address <ipv4>

### Usage

  nv set vrf <vrf-id> router pim msdp-mesh-group <msdp-mesh-group-id> source-address [options] <ipv4>

### Description

  MSDP mesh-group source IP address

### Identifiers

  <vrf-id>              VRF
  <msdp-mesh-group-id>  MSDP mesh group name

## nv set vrf <vrf-id> router pim address-family

### Usage

  nv set vrf <vrf-id> router pim address-family [options] [<attribute> ...]

### Description

  Address family specific configuration

### Identifiers

  <vrf-id>      VRF

### Atrributes

  ipv4-unicast  IPv4 unicast address family
  
## nv set vrf <vrf-id> router pim address-family ipv4-unicast

### Usage

  nv set vrf <vrf-id> router pim address-family ipv4-unicast [options] [<attribute> ...]

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

## nv set vrf <vrf-id> router pim address-family ipv4-unicast spt-switchover

### Usage

  nv set vrf <vrf-id> router pim address-family ipv4-unicast spt-switchover [options] [<attribute> ...]

### Description

  Build shortest path tree towards source.

### Identifiers

  <vrf-id>     VRF

### Atrributes

  action       PIM shortest path switchover (SPT) action.
  prefix-list  Prefix-list to specify multicast group range.
  
## nv set vrf <vrf-id> router pim address-family ipv4-unicast spt-switchover prefix-list <instance-name>

### Usage

  nv set vrf <vrf-id> router pim address-family ipv4-unicast spt-switchover prefix-list [options] <instance-name>

### Description

  Prefix-list to specify multicast group range.

### Identifiers

  <vrf-id>    VRF
  
## nv set vrf <vrf-id> router pim address-family ipv4-unicast rp <rp-id>

### Usage

  nv set vrf <vrf-id> router pim address-family ipv4-unicast rp <rp-id> [options] [<attribute> ...]

### Description

  RP

### Identifiers

  <vrf-id>     VRF
  <rp-id>      RP IP address

### Atrributes

  group-range  Set of group range assocaited to RP.
  prefix-list  Prefix-list to specify multicast group range.
  
## nv set vrf <vrf-id> router pim address-family ipv4-unicast rp <rp-id> group-range <group-range-id>

### Usage

  nv set vrf <vrf-id> router pim address-family ipv4-unicast rp <rp-id> group-range <group-range-id> [options]

### Description

  A group range

### Identifiers

  <vrf-id>          VRF
  <rp-id>           RP IP address
  <group-range-id>  Group range associated to RP.

## nv set vrf <vrf-id> router pim address-family ipv4-unicast rp <rp-id> prefix-list <instance-name>

### Usage

  nv set vrf <vrf-id> router pim address-family ipv4-unicast rp <rp-id> prefix-list [options] <instance-name>

### Description

  Prefix-list to specify multicast group range.

### Identifiers

  <vrf-id>    VRF
  <rp-id>     RP IP address
  
## nv set vrf <vrf-id> router ospf

### Usage

  nv set vrf <vrf-id> router ospf [options] [<attribute> ...]

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
                       
## nv set vrf <vrf-id> router ospf area <area-id>

### Usage

  nv set vrf <vrf-id> router ospf area <area-id> [options] [<attribute> ...]

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

## nv set vrf <vrf-id> router ospf area <area-id> filter-list

### Usage

  nv set vrf <vrf-id> router ospf area <area-id> filter-list [options] [<attribute> ...]

### Description

  Filters networks between OSPF areas

### Identifiers

  <vrf-id>    VRF
  <area-id>   Area

### Atrributes

  in          prefix-list to use as an inbound filter.
  out         prefix-list to use as an inbound filter.
  
## nv set vrf <vrf-id> router ospf area <area-id> range <range-id>

### Usage

  nv set vrf <vrf-id> router ospf area <area-id> range <range-id> [options] [<attribute> ...]

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
  
## nv set vrf <vrf-id> router ospf area <area-id> network <network-id>

### Usage

  nv set vrf <vrf-id> router ospf area <area-id> network <network-id> [options]

### Description

  Filters out components of the prefix

### Identifiers

  <vrf-id>      VRF
  <area-id>     Area
  <network-id>  Network
  
## nv set vrf <vrf-id> router ospf area <area-id> default-lsa-cost 0-16777215

### Usage

  nv set vrf <vrf-id> router ospf area <area-id> default-lsa-cost [options] 0-16777215

### Description

  Default LSA cost.  Only applies when type is non-normal.

### Identifiers

  <vrf-id>    VRF
  <area-id>   Area
  
## nv set vrf <vrf-id> router ospf default-originate

### Usage

  nv set vrf <vrf-id> router ospf default-originate [options] [<attribute> ...]

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
               
## nv set vrf <vrf-id> router ospf default-originate metric-type 1-2

### Usage

  nv set vrf <vrf-id> router ospf default-originate metric-type [options] 1-2

### Description

  Set OSPF External Type 1/2 metrics

### Identifiers

  <vrf-id>    VRF
  
## nv set vrf <vrf-id> router ospf distance

### Usage

  nv set vrf <vrf-id> router ospf distance [options] [<attribute> ...]

### Description

  Administrative distance for installation into the rib

### Identifiers

  <vrf-id>    VRF

### Atrributes

  external    External
  inter-area  Inter-area
  intra-area  Intra-area
  
## nv set vrf <vrf-id> router ospf max-metric

### Usage

  nv set vrf <vrf-id> router ospf max-metric [options] [<attribute> ...]

### Description

  Set maximum metric value in router lsa to make stub router

### Identifiers

  <vrf-id>        VRF

### Atrributes

  administrative  Administratively applied, for an indefinite period
  on-shutdown     Advertise stub-router prior to full shutdown of OSPF
  on-startup      Automatically advertise stub Router-LSA on startup of OSPF

## nv set vrf <vrf-id> router ospf log

### Usage

  nv set vrf <vrf-id> router ospf log [options] [<attribute> ...]

### Description

  Log configuration

### Identifiers

  <vrf-id>           VRF

### Atrributes

  adjacency-changes  Log adjacency changes
  
## nv set vrf <vrf-id> router ospf redistribute

### Usage

  nv set vrf <vrf-id> router ospf redistribute [options] [<attribute> ...]

### Description

  Route redistribute

### Identifiers

  <vrf-id>    VRF

### Atrributes

  static      Route redistribute of static routes
  connected   Route redistribute of connected routes
  kernel      Route redistribute of kernel routes
  bgp         Route redistribute of bgp routes
  
## nv set vrf <vrf-id> router ospf redistribute static

### Usage

  nv set vrf <vrf-id> router ospf redistribute static [options] [<attribute> ...]

### Description

  Source route type.

### Identifiers

  <vrf-id>     VRF

### Atrributes

  enable       Turn the feature 'on' or 'off'. The default is 'off'.
  metric       Metric value for destination routing protocol
  metric-type  Set OSPF External Type 1/2 metrics
  route-map    Optional policy to apply to this advertisement
  
## nv set vrf <vrf-id> router ospf redistribute static metric-type 1-2

### Usage

  nv set vrf <vrf-id> router ospf redistribute static metric-type [options] 1-2

### Description

  Set OSPF External Type 1/2 metrics

### Identifiers

  <vrf-id>    VRF
  
## nv set vrf <vrf-id> router ospf redistribute connected

### Usage

  nv set vrf <vrf-id> router ospf redistribute connected [options] [<attribute> ...]

### Description

  Source route type.

### Identifiers

  <vrf-id>     VRF

### Atrributes

  enable       Turn the feature 'on' or 'off'. The default is 'off'.
  metric       Metric value for destination routing protocol
  metric-type  Set OSPF External Type 1/2 metrics
  route-map    Optional policy to apply to this advertisement
  
## nv set vrf <vrf-id> router ospf redistribute connected metric-type 1-2

### Usage

  nv set vrf <vrf-id> router ospf redistribute connected metric-type [options] 1-2

### Description

  Set OSPF External Type 1/2 metrics

### Identifiers

  <vrf-id>    VRF
  
## nv set vrf <vrf-id> router ospf redistribute kernel

### Usage

  nv set vrf <vrf-id> router ospf redistribute kernel [options] [<attribute> ...]

### Description

  Source route type.

### Identifiers

  <vrf-id>     VRF

### Atrributes

  enable       Turn the feature 'on' or 'off'. The default is 'off'.
  metric       Metric value for destination routing protocol
  metric-type  Set OSPF External Type 1/2 metrics
  route-map    Optional policy to apply to this advertisement
  
## nv set vrf <vrf-id> router ospf redistribute kernel metric-type 1-2

### Usage

  nv set vrf <vrf-id> router ospf redistribute kernel metric-type [options] 1-2

### Description

  Set OSPF External Type 1/2 metrics

### Identifiers

  <vrf-id>    VRF
  
## nv set vrf <vrf-id> router ospf redistribute bgp

### Usage

  nv set vrf <vrf-id> router ospf redistribute bgp [options] [<attribute> ...]

### Description

  Source route type.

### Identifiers

  <vrf-id>     VRF

### Atrributes

  enable       Turn the feature 'on' or 'off'. The default is 'off'.
  metric       Metric value for destination routing protocol
  metric-type  Set OSPF External Type 1/2 metrics
  route-map    Optional policy to apply to this advertisement
  
## nv set vrf <vrf-id> router ospf redistribute bgp metric-type 1-2

### Usage

  nv set vrf <vrf-id> router ospf redistribute bgp metric-type [options] 1-2

### Description

  Set OSPF External Type 1/2 metrics

### Identifiers

  <vrf-id>    VRF
  
## nv set vrf <vrf-id> router ospf timers

### Usage

  nv set vrf <vrf-id> router ospf timers [options] [<attribute> ...]

### Description

  Timers

### Identifiers

  <vrf-id>    VRF

### Atrributes

  lsa         LSA timers
  spf         SPF timers
  refresh     defines interval (sec) to re-send lsas to keep from aging out.
              If 'auto', inherited from global. This is the default.
              
## nv set vrf <vrf-id> router ospf timers lsa

### Usage

  nv set vrf <vrf-id> router ospf timers lsa [options] [<attribute> ...]

### Description

  LSA timers

### Identifiers

  <vrf-id>     VRF

### Atrributes

  min-arrival  Minimum delay in receiving new version of a LSA. If 'auto',
               inherited from global. This is the default.
  throttle     Delay (msec) between sending LSAs. If 'auto', inherited from
               global. This is the default.
               
## nv set vrf <vrf-id> router ospf timers spf

### Usage

  nv set vrf <vrf-id> router ospf timers spf [options] [<attribute> ...]

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
                
## nv set vrf <vrf-id> router ospf reference-bandwidth 1-4294967

### Usage

  nv set vrf <vrf-id> router ospf reference-bandwidth [options] 1-4294967

### Description

  Used to determine link cost/metric value relative to defined reference.

### Identifiers

  <vrf-id>    VRF
  
  
## nv set vrf <vrf-id> ptp

### Usage

  nv set vrf <vrf-id> ptp [options] [<attribute> ...]

### Description

  VRF PTP configuration.  Inherited by interfaces in this VRF.

### Identifiers

  <vrf-id>    VRF

### Atrributes

  enable      Turn the feature 'on' or 'off'. The default is 'on'.
  
## nv set vrf <vrf-id> table auto

### Usage

  nv set vrf <vrf-id> table [options] auto

### Description

  The routing table number, between 1001-1255, used by the named VRF. If auto, the default, it will be auto generated.

### Identifiers

  <vrf-id>    VRF
  
## nv set nve

### Usage

  nv set nve [options] [<attribute> ...]

### Description

  Network Virtualization configuration and operational info

### Atrributes

  vxlan       Global VxLAN configuration and operational properties.
  
## nv set nve vxlan

### Usage

  nv set nve vxlan [options] [<attribute> ...]

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
  
## nv set nve vxlan mlag

### Usage

  nv set nve vxlan mlag [options] [<attribute> ...]

### Description

  VxLAN specfic MLAG configuration

### Atrributes

  shared-address  shared anycast address for MLAG peers

## nv set nve vxlan source

### Usage

  nv set nve vxlan source [options] [<attribute> ...]

### Description

  Source address

### Atrributes

  address     IP addresses of this node's VTEP or 'auto'. If 'auto', use the
              primary IP loopback (not 127.0.0.1). This is the default.
              
## nv set nve vxlan flooding

### Usage

  nv set nve vxlan flooding [options] [<attribute> ...]

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

## nv set nve vxlan flooding head-end-replication <hrep-id>

### Usage

  nv set nve vxlan flooding head-end-replication <hrep-id> [options]

### Description

  Set of IPv4 unicast addresses or "evpn".

### Identifiers

  <hrep-id>   IPv4 unicast addresses or "evpn"
  
## nv set nve vxlan flooding multicast-group <ipv4-multicast>

### Usage

  nv set nve vxlan flooding multicast-group [options] <ipv4-multicast>

### Description

  BUM traffic is sent to the specified multicast group and will be received by receivers who are interested in that group. This usually requires PIM-SM to be used in the network.
  
## nv set nve vxlan port 1024-65535

### Usage

  nv set nve vxlan port [options] 1024-65535

### Description

  UDP port for VXLAN frames
  
## nv set nve vxlan mtu 552-9216

### Usage

  nv set nve vxlan mtu [options] 552-9216

### Description

  interface mtu
  
## nv set acl <acl-id>

### Usage

  nv set acl <acl-id> [options] [<attribute> ...]

### Description

  An ACL is used for matching packets and take actions

### Identifiers

  <acl-id>    ACL ID

### Atrributes

  rule        acl rule
  type        acl type
  
## nv set acl <acl-id> rule <rule-id>

### Usage

  nv set acl <acl-id> rule <rule-id> [options] [<attribute> ...]

### Description

  ACL Matching criteria and action rule

### Identifiers

  <acl-id>    ACL ID
  <rule-id>   ACL rule number

### Atrributes

  match       ACL match criteria
  action      ACL action
  
## nv set acl <acl-id> rule <rule-id> match

### Usage

  nv set acl <acl-id> rule <rule-id> match [options] [<attribute> ...]

### Description

  An ACL match

### Identifiers

  <acl-id>    ACL ID
  <rule-id>   ACL rule number

### Atrributes

  ip          IPv4 and IPv6 match
  mac         MAC match
  
## nv set acl <acl-id> rule <rule-id> match ip

### Usage

  nv set acl <acl-id> rule <rule-id> match ip [options] [<attribute> ...]

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
  
## nv set acl <acl-id> rule <rule-id> match ip source-port <ip-port-id>

### Usage

  nv set acl <acl-id> rule <rule-id> match ip source-port <ip-port-id> [options]

### Description

  L4 port

### Identifiers

  <acl-id>      ACL ID
  <rule-id>     ACL rule number
  <ip-port-id>  IP port ID
  
## nv set acl <acl-id> rule <rule-id> match ip dest-port <ip-port-id>

### Usage

  nv set acl <acl-id> rule <rule-id> match ip dest-port <ip-port-id> [options]

### Description

  L4 port

### Identifiers

  <acl-id>      ACL ID
  <rule-id>     ACL rule number
  <ip-port-id>  IP port ID

## nv set acl <acl-id> rule <rule-id> match ip fragment

### Usage

  nv set acl <acl-id> rule <rule-id> match ip fragment [options]

### Description

  State details

### Identifiers

  <acl-id>    ACL ID
  <rule-id>   ACL rule number
  
## nv set acl <acl-id> rule <rule-id> match ip ecn

### Usage

  nv set acl <acl-id> rule <rule-id> match ip ecn [options] [<attribute> ...]

### Description

  ECN

### Identifiers

  <acl-id>    ACL ID
  <rule-id>   ACL rule number

### Atrributes

  flags       ECN protocol flags
  ip-ect      IP ECT
  
## nv set acl <acl-id> rule <rule-id> match ip ecn ip-ect 0-3

### Usage

  nv set acl <acl-id> rule <rule-id> match ip ecn ip-ect [options] 0-3

### Description

  IP ECT

### Identifiers

  <acl-id>    ACL ID
  <rule-id>   ACL rule number
  
## nv set acl <acl-id> rule <rule-id> match ip tcp

### Usage

  nv set acl <acl-id> rule <rule-id> match ip tcp [options] [<attribute> ...]

### Description

  L4 port

### Identifiers

  <acl-id>    ACL ID
  <rule-id>   ACL rule number

### Atrributes

  flags       TCP protocol flags
  mask        TCP protocol flag mask
  state       TCP state
  
## nv set acl <acl-id> rule <rule-id> match ip tcp state established

### Usage

  nv set acl <acl-id> rule <rule-id> match ip tcp state [options] established

### Description

  TCP state

### Identifiers

  <acl-id>    ACL ID
  <rule-id>   ACL rule number
  
## nv set acl <acl-id> rule <rule-id> match mac

### Usage

  nv set acl <acl-id> rule <rule-id> match mac [options] [<attribute> ...]

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
  vlan             VLAN ID  -h, --help

## nv set acl <acl-id> rule <rule-id> match mac source-mac-mask <mac>

### Usage

  nv set acl <acl-id> rule <rule-id> match mac source-mac-mask [options] <mac>

### Description

  Source MAC address mask

### Identifiers

  <acl-id>    ACL ID
  <rule-id>   ACL rule number
  
## nv set acl <acl-id> rule <rule-id> match mac dest-mac-mask <mac>

### Usage

  nv set acl <acl-id> rule <rule-id> match mac dest-mac-mask [options] <mac>

### Description

  Destination MAC address mask

### Identifiers

  <acl-id>    ACL ID
  <rule-id>   ACL rule number
  
## nv set acl <acl-id> rule <rule-id> match mac vlan 1-4094

### Usage

  nv set acl <acl-id> rule <rule-id> match mac vlan [options] 1-4094

### Description

  VLAN ID

### Identifiers

  <acl-id>    ACL ID
  <rule-id>   ACL rule number
  
## nv set acl <acl-id> rule <rule-id> action

### Usage

  nv set acl <acl-id> rule <rule-id> action [options] [<attribute> ...]

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
  
## nv set acl <acl-id> rule <rule-id> action permit

### Usage

  nv set acl <acl-id> rule <rule-id> action permit [options]

### Description

  Permit packets

### Identifiers

  <acl-id>    ACL ID
  <rule-id>   ACL rule number
  
## nv set acl <acl-id> rule <rule-id> action deny

### Usage

  nv set acl <acl-id> rule <rule-id> action deny [options]

### Description

  deny packets

### Identifiers

  <acl-id>    ACL ID
  <rule-id>   ACL rule number
  
## nv set acl <acl-id> rule <rule-id> action log

### Usage

  nv set acl <acl-id> rule <rule-id> action log [options]

### Description

  log packets

### Identifiers

  <acl-id>    ACL ID
  <rule-id>   ACL rule number
  
## nv set acl <acl-id> rule <rule-id> action set

### Usage

  nv set acl <acl-id> rule <rule-id> action set [options] [<attribute> ...]

### Description

  Set action for packets

### Identifiers

  <acl-id>    ACL ID
  <rule-id>   ACL rule number

### Atrributes

  class       Sets the class value for classification of the packet
  cos         Set the CoS value
  dscp        Sets/Modifies the DSCP value in the packet
  
## nv set acl <acl-id> rule <rule-id> action set class 0-7

### Usage

  nv set acl <acl-id> rule <rule-id> action set class [options] 0-7

### Description

  Sets the class value for classification of the packet

### Identifiers

  <acl-id>    ACL ID
  <rule-id>   ACL rule number
  
## nv set acl <acl-id> rule <rule-id> action set cos 0-7

### Usage

  nv set acl <acl-id> rule <rule-id> action set cos [options] 0-7

### Description

  Set the CoS value

### Identifiers

  <acl-id>    ACL ID
  <rule-id>   ACL rule number
  
## nv set acl <acl-id> rule <rule-id> action erspan

### Usage

  nv set acl <acl-id> rule <rule-id> action erspan [options] [<attribute> ...]

### Description

  ERSPAN session

### Identifiers

  <acl-id>    ACL ID
  <rule-id>   ACL rule number

### Atrributes

  dest-ip     Destination IP address
  source-ip   Source IP address
  ttl         Time to Live
  
## nv set acl <acl-id> rule <rule-id> action erspan ttl 1-255

### Usage

  nv set acl <acl-id> rule <rule-id> action erspan ttl [options] 1-255

### Description

  Time to Live

### Identifiers

  <acl-id>    ACL ID
  <rule-id>   ACL rule number
  
## nv set acl <acl-id> rule <rule-id> action police

### Usage

  nv set acl <acl-id> rule <rule-id> action police [options] [<attribute> ...]

### Description

  Policing of matched packets/bytes

### Identifiers

  <acl-id>    ACL ID
  <rule-id>   ACL rule number

### Atrributes

  burst       Policing burst value
  mode        Policing mode
  rate        Policing rate value
  
## nv set acl <acl-id> rule <rule-id> action police burst 1-2147483647

### Usage

  nv set acl <acl-id> rule <rule-id> action police burst [options] 1-2147483647

### Description

  Policing burst value

### Identifiers

  <acl-id>    ACL ID
  <rule-id>   ACL rule number
  
## nv set acl <acl-id> rule <rule-id> action police rate 1-2147483647

### Usage

  nv set acl <acl-id> rule <rule-id> action police rate [options] 1-2147483647

### Description

  Policing rate value

### Identifiers

  <acl-id>    ACL ID
  <rule-id>   ACL rule number
  
## nv set acl <acl-id> rule <rule-id> action span <interface-name>

### Usage

  nv set acl <acl-id> rule <rule-id> action span [options] <interface-name>

### Description

  SPAN session

### Identifiers

  <acl-id>    ACL ID
  <rule-id>   ACL rule number