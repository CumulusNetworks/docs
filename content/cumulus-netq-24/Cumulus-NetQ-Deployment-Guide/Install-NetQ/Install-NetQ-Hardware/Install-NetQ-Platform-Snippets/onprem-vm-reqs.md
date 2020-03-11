---
title: On-premises Virtual Machine Requirements
author: Cumulus Networks
weight: 
aliases:
 - /display/NETQ/Install+NetQ
 - /pages/viewpage.action?pageId=12320951
pageID: 12320951
toc: 5
---
The NetQ Platform requires a VM with the following system resources allocated:

<table>
<colgroup>
<col style="width: 40%" />
<col style="width: 60%" />
</colgroup>
<thead>
<tr class="header">
<th>Resource</th>
<th>Minimum Requirement</th>
</tr>
</thead>
<tbody>
<tr class="even">
<td>Processor</td>
<td>Eight (8) virtual CPUs</td>
</tr>
<tr class="odd">
<td>Memory</td>
<td>64 GB RAM</td>
</tr>
<tr class="even">
<td>Local disk storage</td>
<td>256 GB SSD <br>(<strong>Note</strong>: This <em>must</em> be an SSD; use of other storage options can lead to system instability and are not supported.)</td>
</tr>
<tr class="odd">
<td>Network interface speed</td>
<td>1 Gb NIC</td>
</tr>
<tr class="even">
<td>Hypervisor</td>
<td><ul><li>VMware ESXi™ 6.5 or later (OVA image) for servers running Cumulus Linux, CentOS, Ubuntu and RedHat operating systems</li><li>KVM/QCOW (QEMU Copy on Write) image for servers running CentOS, Ubuntu and RedHat operating systems</li></ul></td>
</tr>
</tbody>
</table>
