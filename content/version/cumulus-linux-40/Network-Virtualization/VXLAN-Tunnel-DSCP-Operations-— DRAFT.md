---
title: "VXLAN Tunnel DSCP Operations —\_DRAFT"
author: Cumulus Networks
weight: 157
aliases:
 - "/display/CL40/VXLAN-Tunnel-DSCP-Operations-—\_DRAFT"
 - /pages/viewpage.action?pageId=8366511
pageID: 8366511
product: Cumulus Linux
version: '4.0'
imgData: cumulus-linux-40
siteSlug: cumulus-linux-40
---
The following configuration options control DSCP operations during VXLAN
encapsulation and decapsulation. These operations work for applications
that require end-to-end quality of service, such as
<span style="color: #364149;"> [RDMA over Converged
Ethernet](/version/cumulus-linux-40/Network-Solutions/RDMA-over-Converged-Ethernet---RoCE).
</span>

On Mellanox switches, you can use these options to propagate [explicit
congestion
notification](Buffer-and-Queue-Management.html#src-8366755_BufferandQueueManagement-ecn)
(ECN) between the underlay and overlay. Because they are based on
[RFC-6040](https://tools.ietf.org/html/rfc6040), which describes how to
construct the IP header of an ECN field on both ingress to and egress
from an IP-in-IP tunnel, this feature is always enabled. Broadcom
switches do not support ECN propagation between the underlay and
overlay.

## <span>Configuration</span>

You can set these DSCP operations:

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Method</p></th>
<th><p>Operation</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>VXLAN encapsulation, IP overlay packet</p></td>
<td><p>Outer DSCP default actions are <em>copy</em>, <em>set</em> and <em>derive</em></p>
<p>Outer DSCP default value if action is <em>derive</em></p></td>
</tr>
<tr class="even">
<td><p>VXLAN encapsulation, non-IP overlay packet</p></td>
<td><p> </p></td>
</tr>
<tr class="odd">
<td><p>VXLAN decapsulation, IP overlay packet</p></td>
<td><p>Inner DSCP default actions are <em>copy</em>, <em>derive</em> and <em>preserve</em></p></td>
</tr>
<tr class="even">
<td><p>VXLAN decapsulation, non-IP overlay packet</p></td>
<td><p> </p></td>
</tr>
</tbody>
</table>

You set the DSCP operations in `/etc/cumulus/switchd.conf`. Edit the
`switchd.conf` file in a text editor. The following example file shows
that the outer DSCP action during encapsulation is *set*, with a value
of *16*:

    cumulus@switch:~$ sudo nano /etc/cumulus/switchd.conf
    ...
    # default vxlan outer dscp action during encap
    # {copy | set | derive}
    # copy: only if inner packet is IP
    # set: to specific value
    # derive: from switch priority
    vxlan.def_encap_dscp_action = set
     
    # default vxlan encap dscp value, only applicable if action is 'set'
    vxlan.def_encap_dscp_value = 16
     
    # default vxlan decap dscp/cos action
    # {copy | preserve | derive}
    # copy: only if inner packet is IP
    # preserve: inner dscp unchanged
    # derive: from switch priority
    #vxlan.def_decap_dscp_action = derive
    ...

You can also set the DSCP operations from the command line. Use the
`echo` command to change the settings in `/etc/cumulus/switchd.conf`.
For example, to change the encapsulation action to *copy*, run the
following command:

    cumulus@switch:~$ echo "copy" > /cumulus/switchd/config/vxlan/def_encap_dscp_action

To change the encapsulation action to *set* with a value of *32*, run
the following commands:

    cumulus@switch:~$ echo "32" > /cumulus/switchd/config/vxlan/def_encap_dscp_value
    cumulus@switch:~$ echo "set" > /cumulus/switchd/config/vxlan/def_encap_dscp_action

## <span>Caveats and Errata</span>

  - Cumulus Linux supports only the default global settings. Per-VXLAN
    and per-tunnel granularity are not supported.

  - Broadcom switches are not supported at this time.

<article id="html-search-results" class="ht-content" style="display: none;">

</article>

<footer id="ht-footer">

</footer>
