---
title: Troubleshooting the support Directory
author: Cumulus Networks
weight: 165
aliases:
 - /display/RMP25ESR/Troubleshooting+the+support+Directory
 - /pages/viewpage.action?pageId=5116333
pageID: 5116333
product: Cumulus RMP
version: 2.5.12 ESR
imgData: cumulus-rmp-2512-esr
siteSlug: cumulus-rmp-2512-esr
---
The `support` directory is unique in the fact that it is not a copy of
the switch's filesystem. Actually, it is the output from various
commands. For example:

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr class="header">
<th><p>File</p></th>
<th><p>Equivalent Command</p></th>
<th><p>Description</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>support/ip.addr</p></td>
<td><pre><code>cumulus@sw$ ip addr show</code></pre></td>
<td><p>This shows you all the interfaces (including swp front panel ports), IP address information, admin state and physical state.</p></td>
</tr>
</tbody>
</table>
