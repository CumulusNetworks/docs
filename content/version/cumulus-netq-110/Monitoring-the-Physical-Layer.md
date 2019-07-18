---
title: Monitoring the Physical Layer
author: Cumulus Networks
weight: 23
aliases:
 - /display/NETQ110/Monitoring+the+Physical+Layer
 - /pages/viewpage.action?pageId=7111335
pageID: 7111335
product: Cumulus NetQ
version: 1.1.0
imgData: cumulus-netq-110
siteSlug: cumulus-netq-110
---
NetQ provides the ability to monitor at layer 1 — the physical cabling
connecting the nodes of the network fabric. This includes the ability
to:

  - Manage the inventory: show all optics, determine all the plugged and
    empty ports, figure out optics expenses by auditing by vendor

  - Validate configurations: check peer connections, discover any
    misconfigured ports, peers, or unsupported modules, check for link
    flaps

  - Investigate errors: including CRC errors

NetQ uses [LLDP](/display/NETQ110/Link+Layer+Discovery+Protocol) to
collect port information. It can also identify peer ports for DACs and
AOCs without using LLDP or even if the link is not UP.

## <span>Managing the Layer 1 Inventory</span>

NetQ provides detailed information about the cabling on a given node:

    cumulus@cel-smallxp-13:~$ netq show interfaces physical 
    Matching cables records are:
    Hostname         Interface State Speed   AutoNeg Module    Vendor           Part No          Last Changed
    ---------------- --------- ----- ------- ------- --------- ---------------- ---------------- --------------
    act-5712-12      swp36     down  1G      off     SFP       AVAGO            AFBR-5715PZ-JU1  9:06:10 ago
    act-5712-12      swp27     up    10G     off     SFP       OEM              SFP-10GB-LR      17:13:23 ago
    act-5712-12      swp13     up    10G     off     SFP       JDSU             PLRXPLSCS4322N   17:13:44 ago
    act-5712-12      swp52     up    40G     off     QSFP+     Mellanox         MC2210130-002    17:13:28 ago
    act-5712-12      swp34     down  10G     off     empty     n/a              n/a              17:13:47 ago
    act-5712-12      swp37     up    1G      off     SFP       FINISAR CORP.    FCLF8522P2BTL    17:13:48 ago
    act-5712-12      swp17     up    1G      off     SFP       FINISAR CORP.    FTLF1318P3BTL    17:13:42 ago
    act-5712-12      swp35     down  1G      off     SFP       CISCO-AGILENT    QFBR-5766LP      9:06:10 ago
    act-5712-12      eth0      up    1G      on      RJ45      n/a              n/a              17:13:51 ago
    act-5712-12      swp8      up    10G     off     SFP       Mellanox         MC2609130-003    17:13:54 ago
    act-5712-12      swp51s3   up    10G     off     QSFP+     CISCO            AFBR-7IER05Z-CS1 17:13:32 ago
    act-5712-12      swp50s2   up    10G     off     QSFP+     Mellanox         MC2609130-003    17:13:39 ago
    act-5712-12      swp21     up    10G     off     SFP       FIBERSTORE       SFP-10GLR-31     17:13:27 ago
    act-5712-12      swp42     up    1G      off     SFP       OEM              SFP-GLC-T        17:13:17 ago
    act-5712-12      swp5      up    10G     off     SFP       Mellanox         MC2609130-003    17:13:41 ago
    act-5712-12      swp39     up    1G      off     SFP       FINISAR CORP.    FCLF8522P2BTL    17:13:55 ago
    act-5712-12      swp7      up    10G     off     SFP       Mellanox         MC2609130-003    17:13:52 ago
    act-5712-12      swp45     up    10G     off     SFP       Mellanox         MC3309130-001    17:13:14 ago
    act-5712-12      swp9      up    10G     off     SFP       CISCO-AVAGO      AFBR-7IER05Z-CS1 17:13:54 ago
    act-5712-12      swp48     up    10G     off     SFP       Mellanox         MC3309130-001    17:13:19 ago
    act-5712-12      swp2      down  1G      off     SFP       FINISAR CORP.    FCLF8520P2BTL    13:04:25 ago
    act-5712-12      swp41     up    1G      off     SFP       FINISAR CORP.    FCLF8522P2BTL    17:13:17 ago
    act-5712-12      swp50s3   up    10G     off     QSFP+     Mellanox         MC2609130-003    17:13:40 ago
     
    ...

By running the `netq NODE show interfaces physical module` command, you
can see detailed information about the modules on a given node:

    cumulus@cel-smallxp-13:~$ netq act-5712-12 show interfaces physical module 
    Matching cables records are:
    Hostname         Interface Module    Vendor           Part No          Serial No        Transceiver      Connector        Length Last Changed
    ---------------- --------- --------- ---------------- ---------------- ---------------- ---------------- ---------------- ------ --------------
    act-5712-12      swp36     SFP       AVAGO            AFBR-5715PZ-JU1  AM1113SK1A6      1000Base-SX,Mult LC               550m,  9:10:28 ago
                                                                                            imode,                            270m  
                                                                                            50um (M5),Multim
                                                                                            ode,            
                                                                                            62.5um (M6),Shor
                                                                                            twave laser w/o 
                                                                                            OFC (SN),interme
                                                                                            diate distance (
                                                                                            I)              
    act-5712-12      swp27     SFP       OEM              SFP-10GB-LR      ACSLR130408      10G Base-LR      LC               10km,  17:17:41 ago
                                                                                                                              10000m
    act-5712-12      swp13     SFP       JDSU             PLRXPLSCS4322N   CG03UF45M        10G Base-SR,Mult LC               80m,   17:18:02 ago
                                                                                            imode,                            30m,  
                                                                                            50um (M5),Multim                  300m  
                                                                                            ode,            
                                                                                            62.5um (M6),Shor
                                                                                            twave laser w/o 
                                                                                            OFC (SN),interme
                                                                                            diate distance (
                                                                                            I)              
    act-5712-12      swp52     QSFP+     Mellanox         MC2210130-002    MT1539VS03755    40G Base-CR4     n/a              2m     17:17:46 ago
    act-5712-12      swp34     empty     n/a              n/a              n/a              n/a              n/a              n/a    17:18:05 ago
    act-5712-12      swp37     SFP       FINISAR CORP.    FCLF8522P2BTL    PTN1VH2          1000Base-T       RJ45             100m   17:18:05 ago
    act-5712-12      swp17     SFP       FINISAR CORP.    FTLF1318P3BTL    PUC00GG          1000Base-LX,Long LC               10km,  17:17:59 ago
                                                                                            wave laser (LC),                  10000m
                                                                                            Longwave laser (
                                                                                            LL),Single Mode 
                                                                                            (SM),long distan
                                                                                            ce (L)          
    act-5712-12      swp35     SFP       CISCO-AGILENT    QFBR-5766LP      AGS10335337      1000Base-SX      LC               550m,  9:10:28 ago
                                                                                                                              270m  
    act-5712-12      eth0      RJ45      n/a              n/a              n/a              n/a              n/a              n/a    17:18:09 ago
    act-5712-12      swp8      SFP       Mellanox         MC2609130-003    MT1507VS05177    1000Base-CX,Copp Copper pigtail   3m     17:18:12 ago
                                                                                            er Passive,Twin 
                                                                                            Axial Pair (TW) 
    act-5712-12      swp51s3   QSFP+     CISCO            AFBR-7IER05Z-CS1 AVE1823402U      n/a              n/a              5m     17:17:49 ago
    act-5712-12      swp50s2   QSFP+     Mellanox         MC2609130-003    MT1507VS05177    40G Base-CR4,Twi n/a              3m     17:17:57 ago
                                                                                            n Axial Pair (TW
                                                                                            )               
    ...

To see empty ports on a node, use the `netq NODE show interfaces
physical empty` command:

    cumulus@cel-smallxp-13:~$ netq act-5712-12 show interfaces physical empty 
    Matching cables records are:
    Hostname         Interface State Speed   AutoNeg Module    Vendor           Part No          Last Changed
    ---------------- --------- ----- ------- ------- --------- ---------------- ---------------- --------------
    act-5712-12      swp34     down  10G     off     empty     n/a              n/a              17:19:10 ago
    act-5712-12      swp4      down  10G     off     empty     n/a              n/a              17:19:14 ago
    act-5712-12      swp46     down  10G     off     empty     n/a              n/a              17:18:42 ago
    act-5712-12      swp32     down  10G     off     empty     n/a              n/a              17:19:03 ago
    act-5712-12      swp3      down  10G     off     empty     n/a              n/a              17:19:15 ago
    act-5712-12      swp31     down  10G     off     empty     n/a              n/a              17:19:12 ago

Similarly, to see plugged in ports, run the `netq NODE show interfaces
physical plugged` command:

    cumulus@cel-smallxp-13:~$ netq act-5712-12 show interfaces physical plugged 
    Matching cables records are:
    Hostname         Interface State Speed   AutoNeg Module    Vendor           Part No          Last Changed
    ---------------- --------- ----- ------- ------- --------- ---------------- ---------------- --------------
    act-5712-12      swp36     down  1G      off     SFP       AVAGO            AFBR-5715PZ-JU1  9:12:54 ago
    act-5712-12      swp27     up    10G     off     SFP       OEM              SFP-10GB-LR      17:20:07 ago
    act-5712-12      swp13     up    10G     off     SFP       JDSU             PLRXPLSCS4322N   17:20:28 ago
    act-5712-12      swp52     up    40G     off     QSFP+     Mellanox         MC2210130-002    17:20:12 ago
    act-5712-12      swp37     up    1G      off     SFP       FINISAR CORP.    FCLF8522P2BTL    17:20:32 ago
    act-5712-12      swp17     up    1G      off     SFP       FINISAR CORP.    FTLF1318P3BTL    17:20:26 ago
    act-5712-12      swp35     down  1G      off     SFP       CISCO-AGILENT    QFBR-5766LP      9:12:54 ago
    act-5712-12      eth0      up    1G      on      RJ45      n/a              n/a              17:20:35 ago
    act-5712-12      swp8      up    10G     off     SFP       Mellanox         MC2609130-003    17:20:38 ago
    act-5712-12      swp51s3   up    10G     off     QSFP+     CISCO            AFBR-7IER05Z-CS1 17:20:16 ago
    act-5712-12      swp50s2   up    10G     off     QSFP+     Mellanox         MC2609130-003    17:20:23 ago
    act-5712-12      swp21     up    10G     off     SFP       FIBERSTORE       SFP-10GLR-31     17:20:11 ago
    act-5712-12      swp42     up    1G      off     SFP       OEM              SFP-GLC-T        17:20:01 ago
    act-5712-12      swp5      up    10G     off     SFP       Mellanox         MC2609130-003    17:20:25 ago
    act-5712-12      swp39     up    1G      off     SFP       FINISAR CORP.    FCLF8522P2BTL    17:20:39 ago
    act-5712-12      swp7      up    10G     off     SFP       Mellanox         MC2609130-003    17:20:36 ago
    act-5712-12      swp45     up    10G     off     SFP       Mellanox         MC3309130-001    17:19:58 ago
    act-5712-12      swp9      up    10G     off     SFP       CISCO-AVAGO      AFBR-7IER05Z-CS1 17:20:38 ago
    act-5712-12      swp48     up    10G     off     SFP       Mellanox         MC3309130-001    17:20:03 ago
    act-5712-12      swp2      down  1G      off     SFP       FINISAR CORP.    FCLF8520P2BTL    13:11:09 ago
    act-5712-12      swp41     up    1G      off     SFP       FINISAR CORP.    FCLF8522P2BTL    17:20:01 ago
    act-5712-12      swp50s3   up    10G     off     QSFP+     Mellanox         MC2609130-003    17:20:24 ago
    act-5712-12      swp43     up    10G     off     SFP       OEM              SFP-H10GB-CU1M   17:20:02 ago
    act-5712-12      swp40     up    1G      off     SFP       FINISAR CORP.    FCLF8522P2BTL    17:20:00 ago
    act-5712-12      swp24     up    1G      off     SFP       FINISAR CORP.    FTLF1318P3BTL    17:20:08 ago
     
     
    ...

By searching on specific vendors, you can run a cost analysis of your
network:

    cumulus@cel-smallxp-13:~$ netq act-5712-12 show interfaces physical vendor AVAGO 
    Matching cables records are:
    Hostname         Interface State Speed   AutoNeg Module    Vendor           Part No          Last Changed
    ---------------- --------- ----- ------- ------- --------- ---------------- ---------------- --------------
    act-5712-12      swp36     down  1G      off     SFP       AVAGO            AFBR-5715PZ-JU1  9:13:53 ago
    act-5712-12      swp29     up    1G      off     SFP       AVAGO            AFCT-5715PZ-JU1  17:21:04 ago

You can also search on part numbers using `netq NODE show interfaces
physical model PARTNUMBER`:

    cumulus@cel-smallxp-13:~$ netq act-5712-12 show interfaces physical model SFP-H10GB-CU1M 
    Matching cables records are:
    Hostname         Interface State Speed   AutoNeg Module    Vendor           Part No          Last Changed
    ---------------- --------- ----- ------- ------- --------- ---------------- ---------------- --------------
    act-5712-12      swp43     up    10G     off     SFP       OEM              SFP-H10GB-CU1M   17:22:10 ago
    act-5712-12      swp44     up    10G     off     SFP       OEM              SFP-H10GB-CU1M   17:22:06 ago
    act-5712-12      swp14     up    10G     off     SFP       OEM              SFP-H10GB-CU1M   17:22:36 ago

## <span>Checking Peer Connections</span>

NetQ checks peer connections using LLDP. For DACs and AOCs, NetQ
determines the peers using their serial numbers in the port EEPROMs,
even if the link is not UP.

    cumulus@cel-smallxp-13:~$ netq act-5712-12 show interfaces physical peer 
    Matching cables records are:
    Hostname         Interface Peer Hostname    Peer Interface State Message
    ---------------- --------- ---------------- -------------- ----- ----------------------------
    act-5712-12      swp27     act-5712-12      swp53s0        up                                
    act-5712-12      swp13     cel-red-08       swp6           up                                
    act-5712-12      swp52     dell-s6000-22    swp32          up                                
    act-5712-12      swp34                                     down  Port cage empty             
    act-5712-12      swp37     dell-s4000-10    swp37          up                                
    act-5712-12      swp17     cel-red-08       swp1           up                                
     
     
    ...
     
    act-5712-12      swp11     act-5712-12      swp51s1        up                                
    act-5712-12      swp10     act-5712-12      swp51s2        up                                
    act-5712-12      swp3                                      down  Port cage empty             
    act-5712-12      swp49     act-6712-06      swp32          up                                
    act-5712-12      swp12     act-5712-12      swp51s3        up                                
    act-5712-12      swp23     cel-red-08       swp5           up                                
    act-5712-12      swp31                                     down  Port cage empty             
    act-5712-12      swp38     dell-s4000-10    swp38          up                                
    act-5712-12      swp47     cel-red-08       swp45          up                                
    act-5712-12      swp51s0   act-5712-12      swp9           up                                
    act-5712-12      swp50s1   act-5712-12      swp7           up                                
    act-5712-12      swp53s2                                   down  Peer port unknown           
    act-5712-12      swp53s3                                   down  Peer port unknown           
    act-5712-12      swp25                                     down  Peer port unknown           
    ...

You can get peer data for a specific port:

``` 
cumulus@cel-smallxp-13:~$ netq cel-smallxp-13 show interfaces physical swp31 peer
Matching cables records are:
Hostname         Interface Peer Hostname    Peer Interface State Message
---------------- --------- ---------------- -------------- ----- ----------------------------
cel-smallxp-13   swp31     cel-smallxp-13   swp32          up   
```

## <span>Layer 1 Configuration Checks</span>

You can verify that the following configurations are the same on both
ends of two peer interfaces:

  - Admin state

  - Operational state

  - Autonegotiation setting

  - Link speed

You can also determine whether a link is flapping or if verify whether
both peers are the correct peers. If NetQ can't determine the peer, the
port is marked as *unverified*.

To do a layer 1 configuration check, you run the `netq check interfaces`
command, which only checks physical interfaces, not bridges, bonds or
other software constructs.

``` 
cumulus@cel-smallxp-13:~$ netq check interfaces 
Checked Nodes: 18, Failed Nodes: 8
Checked Ports: 741, Failed Ports: 1, Unverified Ports: 414
Hostname         Interface Peer Hostname    Peer Interface Message
---------------- --------- ---------------- -------------- --------------------------------
act-5712-12                -                -              Rotten Agent                    
act-6712-06                -                -              Rotten Agent                    
act-7712-04                -                -              Rotten Agent                    
cel-smallxp-13   swp2      cel-smallxp-13   swp1           State mismatch (up, down)       
dell-s4000-10              -                -              Rotten Agent                    
dell-s6000-22              -                -              Rotten Agent                    
mlx-2410-02                -                -              Rotten Agent                    
qct-ly8-04                 -                -              Rotten Agent   
```

Use the *and* keyword to check the connections between two peers:

    cumulus@cel-smallxp-13:~$ netq check interfaces cel-smallxp-13 swp2 and mlx-2410-02 swp54
    Checked Nodes: 1, Failed Nodes: 1
    Checked Ports: 1, Failed Ports: 1, Unverified Ports: 0
    Hostname         Interface Peer Hostname    Peer Interface Message
    ---------------- --------- ---------------- -------------- --------------------------------
    cel-smallxp-13   swp2      mlx-2410-02      swp54          Incorrect peer specified. Real p
                                                               eer is cel-smallxp-13 swp1      
    cumulus@cel-smallxp-13:~$ netq check interfaces cel-smallxp-13 swp1 and mlx-2410-02 swp54
    Checked Nodes: 1, Failed Nodes: 0
    Checked Ports: 1, Failed Ports: 0, Unverified Ports: 0

If a link is flapping, NetQ indicates this in a message:

``` 
cumulus@cel-smallxp-13:~$ netq check interfaces 
Checked Nodes: 18, Failed Nodes: 8
Checked Ports: 741, Failed Ports: 1, Unverified Ports: 414
Hostname         Interface Peer Hostname    Peer Interface Message
---------------- --------- ---------------- -------------- --------------------------------
dell-s6000-22              -                -              Link flapped 11 times in last 5
                                                           mins                    
```

<article id="html-search-results" class="ht-content" style="display: none;">

</article>

<footer id="ht-footer">

</footer>
