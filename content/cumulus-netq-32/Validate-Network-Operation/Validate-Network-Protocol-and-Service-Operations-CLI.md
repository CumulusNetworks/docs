---
title: Validate Network Protocol and Service Operations Using the CLI
author: Cumulus Networks
weight: 1025
toc: 4
---
<!-- Put all of the validations here....from the monitoring sections of 3.1.0; grouped by layer or alphabetical? -->

### Validate BGP Operation

A single command enables you to validate that all configured route
peering is established across the network. The command checks for
duplicate router IDs and sessions that are in an unestablished state.
Either of these conditions trigger a configuration check failure. When a
failure is found, the reason is identified in the output along with the
time the issue occurred.

This example shows a check on the BGP operations that found no failed
sessions.

    cumulus@switch:~$ netq check bgp
    Total Nodes: 15, Failed Nodes: 0, Total Sessions: 16, Failed Sessions: 0

This example shows 24 failed BGP sessions with a variety of reasons.

    cumulus@switch:~$ netq check bgp
    Total Nodes: 25, Failed Nodes: 3, Total Sessions: 220 , Failed Sessions: 24,
    Hostname          VRF             Peer Name         Peer Hostname     Reason                                        Last Changed
    ----------------- --------------- ----------------- ----------------- --------------------------------------------- -------------------------
    exit-1            DataVrf1080     swp6.2            firewall-1        BGP session with peer firewall-1 swp6.2: AFI/ 1d:7h:56m:9s
                                                                          SAFI evpn not activated on peer              
    exit-1            DataVrf1080     swp7.2            firewall-2        BGP session with peer firewall-2 (swp7.2 vrf  1d:7h:49m:31s
                                                                          DataVrf1080) failed,                         
                                                                          reason: Peer not configured                  
    exit-1            DataVrf1081     swp6.3            firewall-1        BGP session with peer firewall-1 swp6.3: AFI/ 1d:7h:56m:9s
                                                                          SAFI evpn not activated on peer              
    exit-1            DataVrf1081     swp7.3            firewall-2        BGP session with peer firewall-2 (swp7.3 vrf  1d:7h:49m:31s
                                                                          DataVrf1081) failed,                         
                                                                          reason: Peer not configured                  
    exit-1            DataVrf1082     swp6.4            firewall-1        BGP session with peer firewall-1 swp6.4: AFI/ 1d:7h:56m:9s
                                                                          SAFI evpn not activated on peer              
    exit-1            DataVrf1082     swp7.4            firewall-2        BGP session with peer firewall-2 (swp7.4 vrf  1d:7h:49m:31s
                                                                          DataVrf1082) failed,                         
                                                                          reason: Peer not configured                  
    exit-1            default         swp6              firewall-1        BGP session with peer firewall-1 swp6: AFI/SA 1d:7h:56m:9s
                                                                          FI evpn not activated on peer                
    exit-1            default         swp7              firewall-2        BGP session with peer firewall-2 (swp7 vrf de 1d:7h:49m:31s
                                                                          fault) failed, reason: Peer not configured   
    exit-2            DataVrf1080     swp6.2            firewall-1        BGP session with peer firewall-1 swp6.2: AFI/ 1d:7h:56m:9s
                                                                          SAFI evpn not activated on peer              
    exit-2            DataVrf1080     swp7.2            firewall-2        BGP session with peer firewall-2 (swp7.2 vrf  1d:7h:49m:26s
                                                                          DataVrf1080) failed,                         
                                                                          reason: Peer not configured                  
    exit-2            DataVrf1081     swp6.3            firewall-1        BGP session with peer firewall-1 swp6.3: AFI/ 1d:7h:56m:9s
                                                                          SAFI evpn not activated on peer              
    ...