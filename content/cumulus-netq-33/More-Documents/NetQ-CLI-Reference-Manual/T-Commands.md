---
title: T through Z Commands
author: Cumulus Networks
weight: 1107
toc: 3
right_toc_levels: 1
pdfhidden: true
draft: true
---
This topic includes all commands that begin with `netq t*`, `netq u*`, `netq v*`, `netq w*`, `netq x*`, `netq y*`, and `netq z*`.

## netq trace

    <ip>   :  IPv4 or v6 address (no mask)

### Syntax

There are three forms of this command; one for layer 3 and two for layer 2 traces.

```
netq trace
	<ip>
	from
	(<src-hostname>|<ip-src>)
	[vrf <vrf>]
	[around <text-time>]
	[json|detail|pretty]

netq trace
	(<mac> vlan <1-4096>)
	from (<src-hostname>|<ip-src>)
	[vrf <vrf>] [around <text-time>]
	[json|detail|pretty]
	
netq trace
	(<mac> vlan <1-4096>)
	from <mac-src>
	[around <text-time>]
	[json|detail|pretty]
```


- - -

## netq upgrade

netq upgrade bundle <text-bundle-url>
