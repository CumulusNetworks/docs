---
title: Buffer and Queue Management
author: Cumulus Networks
weight: 79
aliases:
 - /display/CL25ESR/Buffer+and+Queue+Management
 - /pages/viewpage.action?pageId=5116100
pageID: 5116100
product: Cumulus Linux
version: 2.5.12 ESR
imgData: cumulus-linux-2512-esr
siteSlug: cumulus-linux-2512-esr
---
Hardware datapath configuration manages packet buffering, queueing, and
scheduling in hardware. There are two configuration input files:

  - `/etc/cumulus/datapath/traffic.conf`, which describes priority
    groups and assigns the scheduling algorithm and weights

  - `/etc/bcm.d/datapath/datapath.conf`, which assigns buffer space and
    egress queues

{{%notice warning%}}

Versions of these files prior to Cumulus Linux 2.1 are incompatible with
Cumulus Linux 2.1 and later; using older files will cause `switchd` to
fail to start and return an error that it cannot find the
`/var/lib/cumulus/rc.datapath` file.

{{%/notice%}}

Each packet is assigned to an ASIC Class of Service (CoS) value based on
the packet’s priority value stored in the 802.1p (Class of Service) or
DSCP (Differentiated Services Code Point) header field. The packet is
assigned to a priority group based on the CoS value.

Priority groups include:

  - *Control*: Highest priority traffic

  - *Service*: Second-highest priority traffic

  - *Lossless*: Traffic protected by priority flow control

  - *Bulk*: All remaining traffic

A lossless traffic group is protected from packet drops by configuring
the datapath to use priority pause. A lossless priority group requires a
port group configuration, which specifies the ports configured for
priority flow control and the additional buffer space assigned to each
port for packets in the lossless priority group.

The scheduler is configured to use a hybrid scheduling algorithm. It
applies strict priority to control traffic queues and a weighted round
robin selection from the remaining queues. Unicast packets and multicast
packets with the same priority value are assigned to separate queues,
which are assigned equal scheduling weights.

Datapath configuration takes effect when you initialize `switchd`.
Changes to the `traffic.conf` file require you to [restart
`switchd`](Configuring_switchd.html#src-5115907_Configuringswitchd-restartswitchd)
.

## <span>Commands</span>

If you modify the configuration in the
`/etc/cumulus/datapath/traffic.conf` file, you must [restart
`switchd`](Configuring_switchd.html#src-5115907_Configuringswitchd-restartswitchd)
for the changes to take effect:

    cumulus@switch:~$ sudo service switchd restart

## <span>Configuration Files</span>

The following configuration applies to 10G and 40G switches only ([any
switch](http://cumulusnetworks.com/hcl/) on the Trident, Trident+, or
Trident II platform).

  - `/etc/cumulus/datapath/traffic.conf`: The datapath configuration
    file.

Sample traffic.conf file (Click to expand)

``` 
cumulus@switch:~$ cat /etc/cumulus/datapath/traffic.conf
# 
# /etc/cumulus/datapath/traffic.conf
#                                                                              
 
# packet header field used to determine the packet priority level          
# fields include {802.1p, dscp}                                            
traffic.packet_priority_source = 802.1p                                    
                                        
# remark packet priority value                                             
# fields include {802.1p, none}                                            
traffic.remark_packet_priority = none                              
                                                                             
# packet priority values assigned to each internal cos value              
# internal cos values {cos_0..cos_7}                                   
# (internal cos 3 has been reserved for CPU-generated traffic)         
# 802.1p values = {0..7}, dscp values = {0..63}                         
traffic.cos_0.packet_priorities = [0]                                 
traffic.cos_1.packet_priorities = [1]                            
traffic.cos_2.packet_priorities = [2]                              
traffic.cos_3.packet_priorities = []                            
traffic.cos_4.packet_priorities = [3,4]                                    
traffic.cos_5.packet_priorities = [5] 
traffic.cos_6.packet_priorities = [6]                         
traffic.cos_7.packet_priorities = [7]                         
                                                              
# priority groups                                             
traffic.priority_group_list = [control, service, bulk]        
                                                              
# internal cos values assigned to each priority group         
# each cos value should be assigned exactly once              
# internal cos values {0..7}                                  
priority_group.control.cos_list = [7]                         
priority_group.service.cos_list = [2]                         
priority_group.bulk.cos_list = [0,1,3,4,5,6]                  
                                                              
# to configure a lossless priority group:                     
# -- uncomment the cos list config and and assign cos value(s)
# -- uncomment port_group_0 configurations and set the lossless flag, buffer si
ze, ports                                                                     
# -- (currently only one traffic group is allowed, with port range 'allports')
# priority_group.lossless.cos_list = [] 
 
# lossless port group 
# -- lossless flag    
arranging in: tiled
arranging in: tiled
# -- buffer size in bytes for each port                        
# -- port group                                                
# priority_group.lossless.lossless_flag = true                 
# priority_group.lossless.port_group_0.port_buffer_bytes = 4096
# priority_group.lossless.port_group_0.port_range = allports 
 
# to configure pause on a group of ports: 
# uncomment the link pause port group list
# add or replace a port group name to the list
# populate the port set, e.g. 
#    swp1-swp4,swp8,swp50s0-swp50s3
# enable pause frame transmit and/or pause frame receive
 
# link pause 
# link_pause.port_group_list = [port_group_0] 
# link_pause.port_group_0.port_set = swp1-swp4,swp6
# link_pause.port_group_0.rx_enable = true
# link_pause.port_group_0.tx_enable = true                   
  
# scheduling algorithm: algorithm values = {dwrr}
scheduling.algorithm = dwrr 
  
# traffic group scheduling weight
# weight values = {0..127}     
# '0' indicates strict priority
priority_group.control.weight = 0                         
priority_group.service.weight = 32                        
priority_group.bulk.weight = 16                           
priority_group.lossless.weight = 16                       
                                                          
# To turn on/off Denial of service (DOS) prevention checks
dos_enable = false                                
                                                  
# To enable cut-through forwarding                
cut_through_enable = true                         
                                                  
# Enable resilient hashing                        
#resilient_hash_enable = FALSE                    
                                                  
# Resilient hashing flowset entries per ECMP group
# Valid values - 64, 128, 256, 512, 1024
#resilient_hash_entries_ecmp = 128   
                             
# Enable symmetric hashing   
#symmetric_hash_enable = TRUE
 
# Set sflow/sample ingress cpu packet rate and burst in packets/sec 
# Values: {0..16384} 
#sflow.rate = 16384  
#sflow.burst = 16384 
 
#Specify the maximum number of paths per route entry. 
#  Maximum paths supported is 200. 
#  Default value 0 takes the number of physical ports as the max path size. 
#ecmp_max_paths = 0      
```

## <span>Configuring Traffic Marking through ACL Rules</span>

You can mark traffic for egress packets through `iptables` or
`ip6tables` rule classifications. To enable these rules, you do one of
the following:

  - Mark DSCP values in egress packets.

  - Mark 802.1p CoS values in egress packets.

To enable traffic marking, use `cl-acltool`. Add the `-p` option to
specify the location of the policy file. By default, if you don't
include the `-p` option, `cl-acltool` looks for the policy file in
`/etc/cumulus/acl/policy.d/`.

The iptables-/ip6tables-based marking is supported via the following
action extension:

    -j SETQOS --set-dscp 10 --set-cos 5

You can specify one of the following targets for SETQOS:

| Option                | Description                                                                                                                                                 |
| --------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| –set-cos INT          | Sets the datapath resource/queuing class value. Values are defined in [IEEE\_P802.1p](http://en.wikipedia.org/wiki/IEEE_P802.1p).                           |
| –set-dscp value       | Sets the DSCP field in packet header to a value, which can be either a decimal or hex value.                                                                |
| –set-dscp-class class | Sets the DSCP field in the packet header to the value represented by the DiffServ class value. This class can be EF, BE or any of the CSxx or AFxx classes. |

{{%notice note%}}

You can specify either `--set-dscp` or `--set-dscp-class`, but not both.

{{%/notice%}}

Here are two example rules:

    [iptables]
    -t mangle -A FORWARD --in-interface swp+ -p tcp --dport bgp -j SETQOS --set-dscp 10 --set-cos 5
    
    [ip6tables]
    -t mangle -A FORWARD --in-interface swp+ -j SETQOS --set-dscp 10

You can put the rule in either the *mangle* table or the default
*filter* table; the mangle table and filter table are put into separate
TCAM slices in the hardware.

To put the rule in the mangle table, include `-t mangle`; to put the
rule in the filter table, omit `-t mangle`.

## <span>Configuring Link Pause</span>

The PAUSE frame is a flow control mechanism that halts the transmission
of the transmitter for a specified period of time. A server or other
network node within the data center may be receiving traffic faster than
it can handle it, thus the PAUSE frame. In Cumulus Linux, individual
ports can be configured to execute link pause by:

  - Transmitting pause frames when its ingress buffers become congested
    (TX pause enable) and/or

  - Responding to received pause frames (RX pause enable).

Just like configuring buffer and queue management link pause is
configured by editing `/etc/cumulus/datapath/traffic.conf`.

Here is an example configuration which turns of both types of link pause
for swp2 and swp3:

``` 
# to configure pause on a group of ports:
# uncomment the link pause port group list
# add or replace a port group name to the list
# populate the port set, e.g.
# swp1-swp4,swp8,swp50s0-swp50s3
# enable pause frame transmit and/or pause frame receive 
# link pause
link_pause.port_group_list = [port_group_0] 
link_pause.port_group_0.port_set = swp2-swp3 
link_pause.port_group_0.rx_enable = true 
link_pause.port_group_0.tx_enable = true           
```

A *port group* refers to one or more sequences of contiguous ports.
Multiple port groups can be defined by:

  - Adding a comma-separated list of port group names to the
    port\_group\_list.

  - Adding the port\_set, rx\_enable, and tx\_enable configuration lines
    for each port group.

You can specify the set of ports in a port group in comma-separated
sequences of contiguous ports; you can see which ports are contiguous in
`/var/lib/cumulus/porttab`. The syntax supports:

  - A single port (swp1s0 or swp5)

  - A sequence of regular swp ports (swp2-swp5)

  - A sequence within a breakout swp port (swp6s0-swp6s3)

  - A sequence of regular and breakout ports, provided they are all in a
    contiguous range. For example:
    
        ...
        swp2
        swp3
        swp4
        swp5
        swp6s0
        swp6s1
        swp6s2
        swp6s3
        swp7
        ...

[Restart
`switchd`](Configuring_switchd.html#src-5115907_Configuringswitchd-restartswitchd)
to allow link pause configuration changes to take effect:

    cumulus@switch:~$ sudo service switchd restart

## <span>Useful Links</span>

  - [iptables-extensions man
    page](http://ipset.netfilter.org/iptables-extensions.man.html)

## <span>Caveats and Errata</span>

  - You can configure Quality of Service (QoS) for 10G and 40G switches
    only; that is, any switch on the Trident, Trident+, or Trident II
    platform.
