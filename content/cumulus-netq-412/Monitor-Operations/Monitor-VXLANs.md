---
title: VXLAN
author: NVIDIA
weight: 980
toc: 3
---

Use the CLI to monitor Virtual Extensible LAN (VXLAN) and validate overlay communication paths. See the {{<link title="show/#netq-show-vxlan" text="command line reference">}} for additional options, definitions, and examples.

```
netq show vxlan
netq show interfaces type vxlan
netq show events message_type vxlan
```
The {{<link title="check/#netq check vxlan" text="netq check vxlan">}} command verifies the consistency of the VXLAN nodes and interfaces across all links in your network fabric.

```
netq check vxlan
```