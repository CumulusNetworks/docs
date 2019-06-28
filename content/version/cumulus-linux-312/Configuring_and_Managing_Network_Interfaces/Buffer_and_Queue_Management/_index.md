---
title: Buffer and Queue Management
author: Cumulus Networks
weight: 83
aliases:
 - /display/CL31/Buffer+and+Queue+Management
 - /pages/viewpage.action?pageId=5122108
pageID: 5122108
product: Cumulus Linux
version: 3.1.2
imgData: cumulus-linux-312
siteSlug: cumulus-linux-312
---
Hardware datapath configuration manages packet buffering, queueing and
scheduling in hardware. There are two configuration input files:

  - `/etc/cumulus/datapath/traffic.conf`, which describes priority
    groups and assigns the scheduling algorithm and weights

  - `/etc/[bcm.d|mlx]/datapath/datapath.conf`, which assigns buffer
    space and egress queues

{{%notice warning%}}

Versions of these files prior to Cumulus Linux 2.1 are incompatible with
Cumulus Linux 2.1 and later; using older files will cause `switchd` to
fail to start and return an error that it cannot find the
`/var/lib/cumulus/rc.datapath` file.

{{%/notice%}}

Each packet is assigned to an ASIC Class of Service (CoS) value based on
the packet's priority value stored in the 802.1p (Class of Service) or
DSCP (Differentiated Services Code Point) header field. The packet is
assigned to a priority group based on the CoS value.

Priority groups include:

  - *Control*: Highest priority traffic

  - *Service*: Second-highest priority traffic

  - *Bulk*: All remaining traffic

The scheduler is configured to use a hybrid scheduling algorithm. It
applies strict priority to control traffic queues and a weighted round
robin selection from the remaining queues. Unicast packets and multicast
packets with the same priority value are assigned to separate queues,
which are assigned equal scheduling weights.

Datapath configuration takes effect when you initialize `switchd`.
Changes to the `traffic.conf` file require you to [restart the
`switchd`](Configuring_switchd.html#src-5121932_Configuringswitchd-restartswitchd)
service.

## <span>Commands</span>

If you modify the configuration in the
`/etc/cumulus/datapath/traffic.conf` file, you must [restart
`switchd`](Configuring_switchd.html#src-5121932_Configuringswitchd-restartswitchd)
for the changes to take effect:

    cumulus@switch:~$ sudo systemctl restart switchd.service

## <span>Configuration Files</span>

The following configuration applies to 10G, 40G, and 100G switches on
Tomahawk, Trident II+ or Trident II
[platforms](http://cumulusnetworks.com/hcl/) only.

  - `/etc/cumulus/datapath/traffic.conf`: The datapath configuration
    file.

Click to view sample traffic.conf file ...

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
     
    # to configure priority flow control on a group of ports:
    # -- assign cos value(s) to the cos list
    # -- add or replace a port group names in the port group list
    # -- for each port group in the list
    #    -- populate the port set, e.g.
    #       swp1-swp4,swp8,swp50s0-swp50s3
    #    -- set a PFC buffer size in bytes for each port in the group
    #    -- set the xoff byte limit (buffer limit that triggers PFC frame transmit to start)
    #    -- set the xon byte delta (buffer limit that triggers PFC frame transmit to stop)
    #    -- enable PFC frame transmit and/or PFC frame receive
    # priority flow control
    # pfc.port_group_list = [pfc_port_group]
    # pfc.pfc_port_group.cos_list = []
    # pfc.pfc_port_group.port_set = swp1-swp4,swp6
    # pfc.pfc_port_group.port_buffer_bytes = 25000
    # pfc.pfc_port_group.xoff_size = 10000
    # pfc.pfc_port_group.xon_delta = 2000
    # pfc.pfc_port_group.tx_enable = true
    # pfc.pfc_port_group.rx_enable = true                 
                                                                  
    # to configure pause on a group of ports: 
    # -- add or replace port group names in the port group list
    # -- for each port group in the list
    #    -- populate the port set, e.g.
    #       swp1-swp4,swp8,swp50s0-swp50s3
    #    -- set a pause buffer size in bytes for each port in the group
    #    -- set the xoff byte limit (buffer limit that triggers pause frames transmit to start)
    #    -- set the xon byte delta (buffer limit that triggers pause frames transmit to stop)
     
    # link pause 
    # link_pause.port_group_list = [pause_port_group]
    # link_pause.pause_port_group.port_set = swp1-swp4,swp6
    # link_pause.pause_port_group.port_buffer_bytes = 25000
    # link_pause.pause_port_group.xoff_size = 10000
    # link_pause.pause_port_group.xon_delta = 2000
    # link_pause.pause_port_group.rx_enable = true
    # link_pause.pause_port_group.tx_enable = true                   
      
    # scheduling algorithm: algorithm values = {dwrr}
    scheduling.algorithm = dwrr 
      
    # traffic group scheduling weight
    # weight values = {0..127}     
    # '0' indicates strict priority
    priority_group.control.weight = 0
    priority_group.service.weight = 32
    priority_group.bulk.weight = 16                     
                                                              
    # To turn on/off Denial of service (DOS) prevention checks
    dos_enable = false                                
                                                      
    # Cut-through is disabled by default on all chips with the exception of
    # Spectrum. On Spectrum cut-through cannot be disabled.
    #cut_through_enable = false
                                                      
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
     
    #Specify the hash seed for Equal cost multipath entries
    # Default value 0
    # Value Rang: {0..4294967295}
    #ecmp_hash_seed = 42
     
    # Specify the forwarding table resource allocation profile, applicable
    # only on platforms that support universal forwarding resources.
    #
    # /usr/cumulus/sbin/cl-rsource-query reports the allocated table sizes
    # based on the profile setting.
    # 
    #   Values: one of {'default', 'l2-heavy', 'v4-lpm-heavy', 'v6-lpm-heavy'}
    #   Default value: 'default'
    #   Note: some devices may support more modes, please consult user
    #         guide for more details
    #
    #forwarding_table.profile = default

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

## <span id="src-5122108_BufferandQueueManagement-pfc" class="confluence-anchor-link"></span><span>Configuring Priority Flow Control</span>

*Priority flow control*, as defined in the [IEEE 802.1Qbb
standard](http://www.ieee802.org/1/pages/802.1bb.html), provides a
link-level flow control mechanism that can be controlled independently
for each Class of Service (CoS) with the intention to ensure no data
frames are lost when congestion occurs in a bridged network.

{{%notice note%}}

Before Cumulus Linux 3.1.1, PFC was designated as a *lossless* priority
group. The lossless priority group has been removed from Cumulus Linux.

{{%/notice%}}

{{%notice warning%}}

Priority flow control is fully supported on [Broadcom
switches](https://cumulusnetworks.com/support/linux-hardware-compatibility-list/?CPUType=x86_64&SwitchSilicon=broadcomtrident&SwitchSilicon=broadcomtridentplus&SwitchSilicon=broadcomtrident2&SwitchSilicon=broadcomtrident2plus&SwitchSilicon=broadcomtriumph2)
but is an [early
access](https://support.cumulusnetworks.com/hc/en-us/articles/202933878)
feature on [Mellanox
switches](https://cumulusnetworks.com/support/linux-hardware-compatibility-list/?SwitchSilicon=mellanoxspectrum).

{{%/notice%}}

PFC is disabled by default in Cumulus Linux. Enabling priority flow
control (PFC) requires configuring the following settings in
`/etc/cumulus/datapath/traffic.conf` on the switch:

  - Specifying the name of the port group in `pfc.port_group_list` in
    brackets; for example, pfc.port\_group\_list = \[pfc\_port\_group\].

  - Assigning a CoS value to the port group in
    `pfc.pfc_port_group.cos_list` setting. Note that *pfc\_port\_group*
    is the name of a port group you specified above and is used
    throughout the following settings.

  - Populating the port group with its member ports in
    `pfc.pfc_port_group.port_set`.

  - Setting a PFC buffer size in `pfc.pfc_port_group.port_buffer_bytes`.
    This is the maximum number of bytes allocated for storing bursts of
    packets, guaranteed at the ingress port. The default is *25000*
    bytes.

  - Setting the xoff byte limit in `pfc.pfc_port_group.xoff_size`. This
    is a threshold for the PFC buffer; when this limit is reached, an
    xoff transition is initiated, signaling the upstream port to stop
    sending traffic, during which time packets continue to arrive due to
    the latency of the communication. The default is *10000* bytes.

  - Setting the xon delta limit in `pfc.pfc_port_group.xon_delta`. This
    is the number of bytes to subtract from the xoff limit, which
    results in a second threshold at which the egress port resumes
    sending traffic. After the xoff limit is reached and the upstream
    port stops sending traffic, the buffer begins to drain. When the
    buffer reaches 8000 bytes (assuming default xoff and xon settings),
    the egress port signals that it can start receiving traffic again.
    The default is *2000* bytes.

  - Enabling the egress port to signal the upstream port to stop sending
    traffic (`pfc.pfc_port_group.tx_enable`). The default is *true*.

  - Enabling the egress port to receive notifications and act on them
    (`pfc.pfc_port_group.rx_enable`). The default is *true*.

The following configuration example shows PFC configured for ports swp1
through swp4 and swp6:

``` 
# to configure priority flow control on a group of ports:
# -- assign cos value(s) to the cos list
# -- add or replace a port group names in the port group list
# -- for each port group in the list
#    -- populate the port set, e.g.
#       swp1-swp4,swp8,swp50s0-swp50s3
#    -- set a PFC buffer size in bytes for each port in the group
#    -- set the xoff byte limit (buffer limit that triggers PFC frame transmit to start)
#    -- set the xon byte delta (buffer limit that triggers PFC frame transmit to stop)
#    -- enable PFC frame transmit and/or PFC frame receive
# priority flow control
pfc.port_group_list = [pfc_port_group]
pfc.pfc_port_group.cos_list = []
pfc.pfc_port_group.port_set = swp1-swp4,swp6
pfc.pfc_port_group.port_buffer_bytes = 25000
pfc.pfc_port_group.xoff_size = 10000
pfc.pfc_port_group.xon_delta = 2000
pfc.pfc_port_group.tx_enable = true
pfc.pfc_port_group.rx_enable = true       
```

### <span>Understanding Port Groups</span>

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
`switchd`](Configuring_switchd.html#src-5121932_Configuringswitchd-restartswitchd)
to allow the PFC configuration changes to take effect:

    cumulus@switch:~$ sudo systemctl restart switchd.service

## <span id="src-5122108_BufferandQueueManagement-pause" class="confluence-anchor-link"></span><span>Configuring Link Pause</span>

The PAUSE frame is a flow control mechanism that halts the transmission
of the transmitter for a specified period of time. A server or other
network node within the data center may be receiving traffic faster than
it can handle it, thus the PAUSE frame. In Cumulus Linux, individual
ports can be configured to execute link pause by:

  - Transmitting pause frames when its ingress buffers become congested
    (TX pause enable) and/or

  - Responding to received pause frames (RX pause enable).

Link pause is disabled by default. Enabling link pause requires
configuring settings in `/etc/cumulus/datapath/traffic.conf`, similar to
how you configure priority flow control. The settings are explained in
that section as well.

Here is an example configuration which turns of both types of link pause
for swp1 through swp4 and swp6:

``` 
# to configure pause on a group of ports: 
# -- add or replace port group names in the port group list
# -- for each port group in the list
#    -- populate the port set, e.g.
#       swp1-swp4,swp8,swp50s0-swp50s3
#    -- set a pause buffer size in bytes for each port in the group
#    -- set the xoff byte limit (buffer limit that triggers pause frames transmit to start)
#    -- set the xon byte delta (buffer limit that triggers pause frames transmit to stop)
 
# link pause 
link_pause.port_group_list = [pause_port_group]
link_pause.pause_port_group.port_set = swp1-swp4,swp6
link_pause.pause_port_group.port_buffer_bytes = 25000
link_pause.pause_port_group.xoff_size = 10000
link_pause.pause_port_group.xon_delta = 2000
link_pause.pause_port_group.rx_enable = true
link_pause.pause_port_group.tx_enable = true                   
```

[Restart
`switchd`](Configuring_switchd.html#src-5121932_Configuringswitchd-restartswitchd)
to allow link pause configuration changes to take effect:

    cumulus@switch:~$ sudo systemctl restart switchd.service

## <span id="src-5122108_BufferandQueueManagement-ecn" class="confluence-anchor-link"></span><span>Configuring Explicit Congestion Notification</span>

{{%notice warning%}}

**Early Access Feature**

ECN is an [early access
feature](https://support.cumulusnetworks.com/hc/en-us/articles/202933878)
in Cumulus Linux 3.1.1. It is supported on [Mellanox
switches](https://cumulusnetworks.com/support/linux-hardware-compatibility-list/?SwitchSilicon=mellanoxspectrum)
only.

{{%/notice%}}

*Explicit Congestion Notification* (ECN) is defined by
[RFC 3168](https://tools.ietf.org/html/rfc3168). ECN gives a Cumulus
Linux switch the ability to mark a packet to signal impending congestion
instead of dropping the packet outright, which is how TCP typically
behaves when ECN is not enabled.

Click to learn how to configure ECN ...

ECN is disabled by default in Cumulus Linux. Enabling ECN requires
configuring the following settings in
`/etc/cumulus/datapath/traffic.conf` on the switch:

  - Specifying the name of the port group in `ecn.port_group_list` in
    brackets; for example, `ecn.port_group_list = [ecn_port_group]`.

  - Assigning a CoS value to the port group in
    `ecn.ecn_port_group.cos_list`. Note that *ecn\_port\_group* is the
    name of a port group you specified above.

  - Populating the port group with its member ports
    (`ecn.ecn_port_group.port_set`), where *ecn\_port\_group* is the
    name of the port group you specified above. Congestion is measured
    on the egress port queue for the ports listed here.

The following configuration example shows ECN configured for ports swp1
through swp4 and swp6:

    ecn.port_group_list = [ecn_port_group]
    ecn.ecn_port_group.cos_list = [3]
    ecn.ecn_port_group.port_set = swp1-swp4,swp6

[Restart
`switchd`](Configuring_switchd.html#src-5121932_Configuringswitchd-restartswitchd)
to allow the ECN configuration changes to take effect:

    cumulus@switch:~$ sudo systemctl restart switchd.service

## <span>Useful Links</span>

  - [iptables-extensions man
    page](http://ipset.netfilter.org/iptables-extensions.man.html)

## <span>Caveats and Errata</span>

  - You can configure Quality of Service (QoS) for 10G, 40G, and 100G
    switches on the Tomahawk, Trident II+ or Trident II platforms only.
