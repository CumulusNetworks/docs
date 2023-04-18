---
title: VLAN
author: NVIDIA
weight: 970
toc: 3
---

Use the UI or CLI to view Virtual Local Area Network (VLAN) information.

## VLAN Commands

Monitor VLAN with the following commands. Use these commands to display configuration information, interfaces associated with VLANs, MAC addresses associated with a given VLAN, MAC addresses associated with you vRR (virtual route reflector) interface configuration, and VLAN events.  See the {{<link title="show/#netq-show-vlan" text="command line reference">}} for additional options, definitions, and examples.

```
netq show vlan
netq show interfaces type macvlan
netq show interfaces type vlan 
netq show macs
netq show events message_type vlan 
```

## View VLAN in the UI

To view VLAN information, select the {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/03-Menu/navigation-menu.svg" height="18" width="18">}} **Menu**, then **VLAN**.

From here you can view a list of switches or hostnames and their associated VLANs, interfaces, SVIs (switch virtual interfaces), and ports.

{{<figure src="/images/netq/vlan-monitoring-460.png" alt="" width="1100">}}

To view MAC addresses associated with a given VLAN, select the {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/03-Menu/navigation-menu.svg" height="18" width="18">}} **Menu**, then **MACs**.