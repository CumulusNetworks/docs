---
title: IP Addresses
author: NVIDIA
weight: 850
toc: 3
---

Use the UI or CLI to monitor Internet Protocol (IP) addresses, neighbors, and routes.

This information can help you:

- Determine the IP neighbors for each switch.
- Calculate the total number of IPv4 and IPv6 addresses and their corresponding interfaces.
- Identify which routes are owned by which switches.
- Pinpoint when changes occurred to an IP configuration.

## IP Address Commands

Monitor IP addresses and determine neighbors and routes with {{<link title="show/#netq show ip/ipv6 addresses" text="netq show ip addresses">}}, {{<link title="show/#netq show ip/ipv6 neighbors" text="netq show ip neighbors">}}, and {{<link title="show/#netq show ip routes" text="netq show ip routes">}}. Two sets of IP commands are available---one for IPv4 and one for IPv6.

```
netq show ip addresses
netq show ipv6 addresses

netq show ip neighbors
netq show ipv6 neighbors 

netq show ip routes    
netq show ipv6 routes
```
- The {{<link title="show/#netq show address-history" text="netq show address-history">}} command displays when an IP address configuration changed for an interface.
- The {{<link title="show/#netq show neighbor-history" text="netq show neighbor-history">}} command displays when the neighbor configuration changed for an IP address.
- The {{<link title="check/#netq check addresses" text="netq check addresses">}} command searches for duplicate IPv4 and IPv6 addresses assigned to interfaces across devices in the inventory, and checks for duplicate /32 host routes in each VRF.

## View IP Addresses in the UI

IPv4 and IPv6 address, neighbor, and route information is available in the NetQ UI. 

To access this information, select the {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/03-Menu/navigation-menu.svg" height="18" width="18">}} **Menu**, then enter **IP addresses**, **IP neighbors**, or **IP routes** in the search field. The following image displays a list of IP addresses:

{{<figure src="/images/netq/ip-addr-490.png" alt="" width="1100">}}