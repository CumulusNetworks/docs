---
title: Comparing Cumulus VX with Other Cumulus Networks Products
author: Cumulus Networks
weight: 21
aliases:
 - /display/VX25/Comparing+Cumulus+VX+with+Other+Cumulus+Networks+Products
 - /pages/viewpage.action?pageId=5115425
pageID: 5115425
product: Cumulus VX
version: '2.5'
imgData: cumulus-vx-25
siteSlug: cumulus-vx-25
---
Cumulus VX has the same foundation as other Cumulus Networks products;
that is, Cumulus Linux and Cumulus RMP. Cumulus VX includes all the
control plane elements of Cumulus Linux or Cumulus RMP but does not have
an actual ASIC or NPU for line rate performance or hardware
acceleration. Essentially, `switchd` is not a part of Cumulus VX.

Thus, Cumulus VX is not a production-ready virtual switch or virtual
router. It isn't meant to run on production switches or carry production
data traffic.

That said, you can use tools like `jdoo` in Cumulus VX to monitor the
virtual switch, the same automation and zero touch provisioning tools,
as well as security and QoS tools.

However, tools that interact with `switchd`, like `cl-cfg`, and other
hardware management tools, are not available.

And while you cannot upgrade the Cumulus VX operating system using
`apt-get upgrade`|`update` or use ONIE, you can use `apt-get` to install
additional software packages, whether they are Cumulus Linux-specific or
Debian-specific.

The following table outlines the similarities and differences between
Cumulus VX and other Cumulus Networks operating systems.

| Feature or Functionality                             | Cumulus VX                                                                                                                                                                                   |
| ---------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Installation and Upgrade                             | No ONIE, new images available with every GA release, no upgrade path.                                                                                                                        |
| Hardware acceleration                                | No switchd. Datapath forwarding is dependent on the choice of hypervisor and VM resources.                                                                                                   |
| Hardware management                                  | None                                                                                                                                                                                         |
| Hardware limitations                                 | None. Dependent on hypervisor and VM resources. Certain features such as route-table-size could accommodate more routes than are supported in hardware (32K routes), given available memory. |
| Production-ready                                     | No                                                                                                                                                                                           |
| Linux extensibility                                  | Yes                                                                                                                                                                                          |
| Layer 2 features                                     | Yes; hypervisor/topology manager dependent.                                                                                                                                                  |
| Layer 3 features                                     | Yes                                                                                                                                                                                          |
| Network virtualization                               | Yes (software forwarding)                                                                                                                                                                    |
| OS management (ZTP, ifupdown2, third party packages) | Yes                                                                                                                                                                                          |
| Automation, monitoring, troubleshooting              | Yes (excluding ONIE and hardware dependencies)                                                                                                                                               |
| Security                                             | Yes                                                                                                                                                                                          |
| QoS                                                  | Yes                                                                                                                                                                                          |

## <span>Comparing Cumulus VX with Cumulus Workbench</span>

The following table describes how Cumulus VX differs from [Cumulus
Workbench](http://cumulusnetworks.com/cumulus-workbench/).

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr class="header">
<th><p> </p></th>
<th><p>Cumulus Workbench</p></th>
<th><p>Cumulus VX</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Offering</p></td>
<td><p>Based on Cumulus Linux, uses physical hardware with a ready-to-use topology.</p></td>
<td><p>Virtual appliance, not the complete operating system, no hardware components and datapath acceleration.</p></td>
</tr>
<tr class="even">
<td><p>Scheduling</p></td>
<td><p><a href="http://cumulusnetworks.com/get-started/test-drive-open-networking-in-our-remote-lab/" class="external-link">Reserve a workbench</a>.</p></td>
<td><p><a href="https://cumulusnetworks.com/cumulus-vx/" class="external-link">Sign up and download</a>.</p></td>
</tr>
<tr class="odd">
<td><p>Access</p></td>
<td><p>Remote access for a limited time.</p></td>
<td><p>On premise, on your own time.</p></td>
</tr>
<tr class="even">
<td><p>Use Cases</p></td>
<td><p>For potential customers looking to deploy Cumulus Linux in their data centers in the near future.</p></td>
<td><ul>
<li><p>Learn Cumulus Networks technology and open networking concepts.</p></li>
<li><p>Prototype network configuration updates before rolling out to production.</p></li>
<li><p>Develop portable, custom applications easily.</p></li>
</ul></td>
</tr>
</tbody>
</table>

<article id="html-search-results" class="ht-content" style="display: none;">

</article>

<footer id="ht-footer">

</footer>
