---
title: RDMA over Converged Ethernet - RoCE
author: NVIDIA
weight: 322
toc: 3
---
<span class="a-tooltip">[RoCE](## "RDMA over Converged Ethernet")</span> enables you to write to compute or storage elements using <span class="a-tooltip">[RDMA](## "Remote Direct Memory Access")</span> over an Ethernet network instead of using host CPUs. RoCE relies on <span class="a-tooltip">[ECN](## "Explicit Congestion Notification")</span> and <span class="a-tooltip">[PFC](## "Priority Flow Control")</span> to operate. Cumulus Linux supports features that can enable lossless Ethernet for RoCE environments.

{{%notice note%}}
While Cumulus Linux can support RoCE environments, the end hosts must support the RoCE protocol.
{{%/notice%}}

RoCE helps you obtain a *converged network*, where all services run over the Ethernet infrastructure, including Infiniband apps.

## Default RoCE Mode Configuration

The following table shows the default RoCE configuration for lossy and lossless mode.

| Configuration | Lossy Mode| Lossless Mode|
| --------| ----- | ------- |
| Port trust mode | YES | YES |
| Port switch priority to traffic class mapping<ul><li>Switch priority 3 to traffic class 3 (RoCE)</li><li>Switch priority 6 to traffic class 6 (CNP)</li><li>Other switch priority to traffic class 0</li></ul> | YES | YES |
| Port ETS:<ul><li>Traffic class 6 (CNP) - Strict</li><li>Traffic class 3 (RoCE) - WRR 50%</li><li>Traffic class 0 (Other traffic) - WRR 50%</li></ul>|YES|YES|
| Port ECN absolute threshold is 1501500 bytes for traffic class 3 (RoCE)|YES|YES|
| LLDP and Application TLV (RoCE)<br>(UDP, Protocol:4791, Priority: 3)| YES | YES |
| Enable PFC on switch priority 3 (RoCE)|NO|YES|
| Switch priority 3 allocated to RoCE lossless traffic pool| NO | YES |

## RDMA over Converged Ethernet lossless (with PFC and ECN)

RoCE uses the Infiniband (IB) Protocol over converged Ethernet. The IB global route header rides directly on top of the Ethernet header. The lossless Ethernet layer handles congestion hop by hop.

To enable RoCE with PFC and ECN:

```
cumulus@switch:~$ nv set qos roce
cumulus@switch:~$ nv config apply
```

{{% notice note %}}
NVUE defaults to `roce mode lossless`. The command `nv set qos roce` and `nv set qos roce mode lossless` are equivalent.

If you enable `roce mode lossy`, configuring `nv set qos roce` without a `mode` does not change the RoCE mode. To change to lossless, you must configure lossless mode with the `nv set qos roce mode lossless` command.
{{% /notice %}}

{{%notice note%}}
{{<link url="Quality-of-Service#link-pause" text="Link pause">}} is another way to provide lossless ethernet; however, PFC is the preferred method. PFC allows more granular control by pausing the traffic flow for a given CoS group instead of the entire link.
{{%/notice%}}

## Enable RDMA over Converged Ethernet lossy (with ECN)

RoCEv2 requires flow control for lossless Ethernet. RoCEv2 uses the Infiniband (IB) Transport Protocol over UDP. The IB transport protocol includes an end-to-end reliable delivery mechanism and has its own sender notification mechanism.

RoCEv2 congestion management uses RFC 3168 to signal congestion experienced to the receiver. The receiver generates an RoCEv2 congestion notification packet directed to the source of the packet.

To enable RoCE with ECN:

```
cumulus@switch:~$ nv set qos roce mode lossy
cumulus@switch:~$ nv config apply
```

## Remove RoCE Configuration

To remove RoCE configuration:

```
cumulus@switch:~$ nv unset qos roce
cumulus@switch:~$ nv config apply
```

## Verify RoCE Configuration

You can verify RoCE configuration with NVUE `nv show` commands.

To show detailed information about the configured buffers, utilization and DSCP markings, run the `nv show qos roce` command:

```
cumulus@switch:mgmt:~$ nv show qos roce
                   operational  applied 
------------------  -----------  --------
enable                           on      
mode                lossless     lossless
congestion-control                       
  congestion-mode   ECN                  
  enabled-tc        0,3                  
  max-threshold     1.43 MB              
  min-threshold     146.48 KB            
  probability       100                  
lldp-app-tlv                             
  priority          3                    
  protocol-id       4791                 
  selector          UDP                  
pfc                                      
  pfc-priority      3                    
  rx-enabled        enabled              
  tx-enabled        enabled              
trust                                    
  trust-mode        pcp,dscp             

RoCE PCP/DSCP->SP mapping configurations
===========================================
       pcp  dscp                     switch-prio
    -  ---  -----------------------  -----------
    0  0    0,1,2,3,4,5,6,7          0          
    1  1    8,9,10,11,12,13,14,15    1          
    2  2    16,17,18,19,20,21,22,23  2          
    3  3    24,25,26,27,28,29,30,31  3          
    4  4    32,33,34,35,36,37,38,39  4          
    5  5    40,41,42,43,44,45,46,47  5          
    6  6    48,49,50,51,52,53,54,55  6          
    7  7    56,57,58,59,60,61,62,63  7          

RoCE SP->TC mapping and ETS configurations
=============================================
       switch-prio  traffic-class  scheduler-weight
    -  -----------  -------------  ----------------
    0  0            0              DWRR-50%        
    1  1            0              DWRR-50%        
    2  2            0              DWRR-50%        
    3  3            3              DWRR-50%        
    4  4            0              DWRR-50%        
    5  5            0              DWRR-50%        
    6  6            6              strict-priority 
    7  7            0              DWRR-50%        

RoCE pool config
===================
       name                   mode     size  switch-priorities  traffic-class
    -  ---------------------  -------  ----  -----------------  -------------
    0  lossy-default-ingress  Dynamic  50%   0,1,2,4,5,6,7      -            
    1  roce-reserved-ingress  Dynamic  50%   3                  -            
    2  lossy-default-egress   Dynamic  50%   -                  0,6          
    3  roce-reserved-egress   Dynamic  inf   -                  3            

Exception List
=================
No Data
```

To show detailed RoCE information about a single interface, run the `nv show interface qos roce status` command.

```
cumulus@switch:mgmt:~$ nv show interface swp16 qos roce status
                    operational    applied  description
------------------  -------------  -------  ---------------------------------------------------
congestion-control
  congestion-mode   ecn, absolute           Congestion config mode
  enabled-tc        0,3                     Congestion config enabled Traffic Class
  max-threshold     1.43 MB                 Congestion config max-threshold
  min-threshold     153.00 KB               Congestion config min-threshold
  probability       100                  
lldp-app-tlv                             
  priority          3                    
  protocol-id       4791                 
  selector          UDP
pfc
  pfc-priority      3                       switch-prio on which PFC is enabled
  rx-enabled        yes                     PFC Rx Enabled status
  tx-enabled        yes                     PFC Tx Enabled status
trust
  trust-mode        pcp,dscp                Trust Setting on the port for packet classification
mode                lossless                Roce Mode
 
 
RoCE PCP/DSCP->SP mapping configurations
===========================================
          pcp  dscp  switch-prio
    ----  ---  ----  -----------
    cnp   6    48    6
    roce  3    26    3
 
 
RoCE SP->TC mapping and ETS configurations
=============================================
          switch-prio  traffic-class  scheduler-weight
    ----  -----------  -------------  ----------------
    cnp   6            6              strict priority
    roce  3            3              dwrr-50%
 
 
RoCE Pool Status
===================
        name                   mode     pool-id  switch-priorities  traffic-class  size      current-usage  max-usage
    --  ---------------------  -------  -------  -----------------  -------------  --------  -------------  ---------
    0   lossy-default-ingress  DYNAMIC  2        0,1,2,4,5,6,7      -              15.16 MB  0 Bytes        16.00 MB
    1   roce-reserved-ingress  DYNAMIC  3        3                  -              15.16 MB  7.30 MB        7.90 MB
    2   lossy-default-egress   DYNAMIC  13       -                  0,6            15.16 MB  0 Bytes        16.01 MB
    3   roce-reserved-egress   DYNAMIC  14       -                  3              inf       7.29 MB        13.47 MB
```

To show detailed information about current buffer utilization as well as historic RoCE byte and packet counts, run the `nv show interface <interface> qos roce counters` command:

```
cumulus@switch:mgmt:~$ nv show interface swp16 qos roce counters
                               operational   applied  description
-----------------------------  ------------  -------  ------------------------------------------------------
rx-stats
  rx-non-roce-stats
    buffer-max-usage           144 Bytes              Max Ingress Pool-buffer usage for non-RoCE traffic
    buffer-usage               0 Bytes                Current Ingress Pool-buffer usage for non-RoCE traffic
    no-buffer-discard          55                     Rx buffer discards for non-RoCE traffic
    non-roce-bytes             56.52 MB               non-roce rx bytes
    non-roce-packets           462975                 non-roce rx packets
    pg-max-usage               144 Bytes              Max PG-buffer usage for non-RoCE traffic
    pg-usage                   0 Bytes                Current PG-buffer usage for non-RoCE traffic
  rx-pfc-stats
    pause-duration             0                      Rx PFC pause duration for RoCE traffic
    pause-packets              0                      Rx PFC pause packets for RoCE traffic
  rx-roce-stats
    buffer-max-usage           0 Bytes                Max Ingress Pool-buffer usage for RoCE traffic
    buffer-usage               0 Bytes                Current Ingress Pool-buffer usage for RoCE traffic
    no-buffer-discard          0                      Rx buffer discards for RoCE traffic
    pg-max-usage               0 Bytes                Max PG-buffer usage for RoCE traffic
    pg-usage                   0 Bytes                Current PG-buffer usage for RoCE traffic
    roce-bytes                 0 Bytes                Rx RoCE Bytes
    roce-packets               0                      Rx RoCE Packets
tx-stats
  tx-cnp-stats
    buffer-max-usage           16.02 MB               Max Egress Pool-buffer usage for CNP traffic
    buffer-usage               0 Bytes                Current Egress Pool-buffer usage for CNP traffic
    cnp-bytes                  0 Bytes                Tx CNP Packet Bytes
    cnp-packets                0                      Tx CNP Packets
    tc-max-usage               0 Bytes                Max TC-buffer usage for CNP traffic
    tc-usage                   0 Bytes                Current TC-buffer usage for CNP traffic
    unicast-no-buffer-discard  0                      Tx buffer discards for CNP traffic
  tx-ecn-stats
    ecn-marked-packets         693777677344           Tx ECN marked packets
  tx-pfc-stats
    pause-duration             0                      Tx PFC pause duration for RoCE traffic
    pause-packets              0                      Tx PFC pause packets for RoCE traffic
  tx-roce-stats
    buffer-max-usage           13.47 MB               Max Egress Pool-buffer usage for RoCE traffic
    buffer-usage               7.29 MB                Current Egress Pool-buffer usage for RoCE traffic
    roce-bytes                 92824.38 GB            Tx RoCE Packet bytes
    roce-packets               803785675319           Tx RoCE Packets
    tc-max-usage               16.02 MB               Max TC-buffer usage for RoCE traffic
    tc-usage                   7.29 MB                Current TC-buffer usage for RoCE traffic
    unicast-no-buffer-discard  663060754115           Tx buffer discards for RoCE traffic
```

To reset the counters in the `nv show interface <interface> qos roce` command output, run the `nv action clear interface <interface> qos roce counters` command.

## Change RoCE Configuration

You can adjust RoCE settings using NVUE after you enable RoCE. To change the memory allocation for RoCE lossless mode to 60 percent:

```
cumulus@switch:mgmt:~$ nv set qos traffic-pool default-lossy memory-percent 40
cumulus@switch:mgmt:~$ nv set qos traffic-pool roce-lossless memory-percent 60
cumulus@switch:mgmt:~$ nv config apply
```

To change the memory allocation of the RoCE lossy traffic pool to 60 percent and remap switch priority 4 to RoCE lossy traffic:

```
cumulus@switch:mgmt:~$ nv set qos traffic-pool default-lossy switch-priority 0-3,5-7
cumulus@switch:mgmt:~$ nv set qos traffic-pool roce-lossy memory-percent 60
cumulus@switch:mgmt:~$ nv set qos traffic-pool default-lossy memory-percent 40
cumulus@switch:mgmt:~$ nv set qos traffic-pool roce-lossy switch-priority 4
cumulus@switch:mgmt:~$ nv set qos egress-queue-mapping default-global switch-priority 4 traffic-class 3
cumulus@switch:mgmt:~$ nv set qos egress-queue-mapping default-global switch-priority 3 traffic-class 0
cumulus@switch:mgmt:~$ nv set qos mapping default-global trust both
cumulus@switch:mgmt:~$ nv set qos mapping default-global dscp 26 switch-priority 4
cumulus@switch:mgmt:~$ nv config apply
```

To change the RoCE lossless switch priority from switch priority 3 to switch priority 2:

```
cumulus@switch:mgmt:~$ nv set qos pfc default-global switch-priority 2
cumulus@switch:mgmt:~$ nv set qos egress-queue-mapping default-global switch-priority 2 traffic-class 3
cumulus@switch:mgmt:~$ nv set qos egress-queue-mapping default-global switch-priority 3 traffic-class 0
cumulus@switch:mgmt:~$ nv set qos mapping default-global trust both
cumulus@switch:mgmt:~$ nv set qos mapping default-global dscp 26 switch-priority 2
```

## Related Information

- {{<exlink url="http://www.roceinitiative.org/roce-introduction/" text="RoCE introduction">}} - roceinitiative.org
