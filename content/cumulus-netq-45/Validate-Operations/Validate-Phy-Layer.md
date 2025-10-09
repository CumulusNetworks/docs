---
title: Physical Layer Configurations
author: NVIDIA
weight: 0
toc: 3
---
Beyond knowing what physical components are in the deployment, it is valuable to know that their configurations are correct and they operate correctly. NetQ enables you to confirm that peer connections are present, discover any misconfigured ports, peers, or unsupported modules, and monitor for link flaps.

NetQ uses {{<kb_link latest="cl" url="Layer-2/Link-Layer-Discovery-Protocol.md" text="LLDP">}} (Link Layer Discovery Protocol) to collect port information. NetQ can also identify peer ports connected to DACs (Direct Attached Cables) and AOCs (Active Optical Cables) without using LLDP, even if the link is not UP.

## Confirm Peer Connections

You can validate peer connections for all devices in your network or for a specific device or port. This example shows the peer hosts and their status for the leaf03 switch.

```
cumulus@switch:~$ netq leaf03 show interfaces physical peer
Matching cables records:
Hostname          Interface                 Peer Hostname     Peer Interface            State      Message
----------------- ------------------------- ----------------- ------------------------- ---------- -----------------------------------
leaf03            swp1                      oob-mgmt-switch   swp7                      up                                
leaf03            swp2                                                                  down       Peer port unknown                             
leaf03            swp47                     leaf04            swp47                     up                                
leaf03            swp48                     leaf04            swp48                     up              
leaf03            swp49                     leaf04            swp49                     up                                
leaf03            swp50                     leaf04            swp50                     up                                
leaf03            swp51                     exit01            swp51                     up                                
leaf03            swp52                                                                 down       Port cage empty                                
```
## Discover Misconfigurations

You can verify that the following configurations are the same on both sides of a peer interface:

- Admin state
- Operational state
- Link speed
- Auto-negotiation setting

Use the `netq check interfaces` command to determine if any of the interfaces have continuity errors. This command only checks the physical interfaces; it does not check bridges, bonds, or other software constructs. The command syntax is:

```
netq check interfaces [around <text-time>] [json]
```

{{%notice tip%}}

If NetQ cannot determine a peer for a given device, the port shows as *unverified*.

{{%/notice%}}

If you find a misconfiguration, use the `netq show interfaces physical` command for clues about the cause.

### Find Mismatched Operational States

This example checks every interface for misconfiguration and you can find that one interface port has an error. Look for clues about the cause and see that the operational states do not match on the connection between leaf 03 and leaf04: leaf03 is up, but leaf04 is down. If the misconfiguration was due to a mismatch in the administrative state, the message would have been *Admin state mismatch (up, down)* or *Admin state mismatch (down, up)*.

```
cumulus@switch:~$ netq check interfaces
Checked Nodes: 18, Failed Nodes: 8
Checked Ports: 741, Failed Ports: 1, Unverified Ports: 414
 
cumulus@switch:~$ netq show interfaces physical peer
Matching cables records:
Hostname          Interface                 Peer Hostname     Peer Interface            Message
----------------- ------------------------- ----------------- ------------------------- -----------------------------------
...
leaf03            swp1                      oob-mgmt-switch   swp7                                                      
leaf03            swp2                                                                  Peer port unknown                             
leaf03            swp47                     leaf04            swp47                                                     
leaf03            swp48                     leaf04            swp48                     State mismatch (up, down)     
leaf03            swp49                     leaf04            swp49                                                     
leaf03            swp50                     leaf04            swp50                                                     
leaf03            swp52                                                                 Port cage empty                                    
...   
```

### Find Mismatched Peers

This example uses the *and* keyword to check the connections between two peers. You can see an error, so you check the physical peer information and discover that someone specified an incorrect peer. After fixing it, run the check again, and see that there are no longer any interface errors.

```
cumulus@switch:~$ netq check interfaces
Checked Nodes: 1, Failed Nodes: 1
Checked Ports: 1, Failed Ports: 1, Unverified Ports: 0
cumulus@switch:~$ netq show interfaces physical peer
    
Matching cables records:
Hostname          Interface                 Peer Hostname     Peer Interface            Message
----------------- ------------------------- ----------------- ------------------------- -----------------------------------
leaf01            swp50                     leaf04            swp49                     Incorrect peer specified. Real peer
                                                                                        is leaf04 swp50      
    
cumulus@switch:~$ netq check interfaces
Checked Nodes: 1, Failed Nodes: 0
Checked Ports: 1, Failed Ports: 0, Unverified Ports: 0
```

### Find Mismatched Link Speeds

This example checks for configuration mismatches and finds a link speed mismatch on server03. The link speed on swp49 is *40G* and the peer port swp50 shows as *unknown*.

```
cumulus@switch:~$ netq check interfaces
Checked Nodes: 10, Failed Nodes: 1
Checked Ports: 125, Failed Ports: 2, Unverified Ports: 35
Hostname          Interface                 Peer Hostname     Peer Interface            Message
----------------- ------------------------- ----------------- ------------------------- -----------------------------------
server03          swp49                     server03          swp50                     Speed mismatch (40G, Unknown)      
server03          swp50                     server03          swp49                     Speed mismatch (Unknown, 40G)  
```

<!-- vale off -->
### Find Mismatched Auto-negotiation Settings
<!-- vale on -->

This example checks for configuration mismatches and finds auto-negotiation setting mismatches between the servers and leafs. Auto-negotiation is *off* for the leafs, but *on* for the servers.

```
cumulus@switch:~$ netq check interfaces
Checked Nodes: 15, Failed Nodes: 8
Checked Ports: 118, Failed Ports: 8, Unverified Ports: 94
Hostname          Interface                 Peer Hostname     Peer Interface            Message
----------------- ------------------------- ----------------- ------------------------- -----------------------------------
leaf01            swp1                      server01          eth1                      Autoneg mismatch (off, on)         
leaf02            swp2                      server02          eth2                      Autoneg mismatch (off, on)         
leaf03            swp1                      server03          eth1                      Autoneg mismatch (off, on)         
leaf04            swp2                      server04          eth2                      Autoneg mismatch (off, on)         
server01          eth1                      leaf01            swp1                      Autoneg mismatch (on, off)         
server02          eth2                      leaf02            swp2                      Autoneg mismatch (on, off)         
server03          eth1                      leaf03            swp1                      Autoneg mismatch (on, off)         
server04          eth2                      leaf04            swp2                      Autoneg mismatch (on, off)         
```

## Identify Flapping Links

You can also determine whether a link is flapping using the `netq check interfaces` command:

```
cumulus@switch:~$ netq check interfaces
Checked Nodes: 18, Failed Nodes: 8
Checked Ports: 741, Failed Ports: 1, Unverified Ports: 414
 
Matching cables records:
Hostname          Interface                 Peer Hostname     Peer Interface            Message
----------------- ------------------------- ----------------- ------------------------- -----------------------------------
leaf02            -                         -                 -                         Link flapped 11 times in last 5
                                                                                        mins                    
```
