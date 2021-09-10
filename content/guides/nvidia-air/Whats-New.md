---
title: What's New in NVIDIA Air
author: NVIDIA
weight: 20
version: "1.0"
---

Check out some of the latest features added to the {{<exlink url="https://air.nvidia.com" text="NVIDIA Air Infrastructure Simulation Platform">}}.

## September 2021
<!-- vale off -->
<!-- Air:WhatsNew -->
- {{<exlink url="https://air.nvidia.com/marketplace" text="Demo Marketplace">}}: Get a jump start on your network configuration by checking out some pre-built feature demos, or submit your own!
<!-- Air:WhatsNew -->
- This page! Be sure to check back often to see the latest features we're adding to NVIDIA Air.
<!-- vale on -->
## August 2021
- {{<exlink url="https://air.nvidia.com/migrate" text="NVUE migration tool">}}
- Specify the location of a node's bootable OS with the `boot` option in your DOT file. For example, boot a node via PXE using `boot="network"`:

```
"server" [function="server" os="generic/ubuntu1804" boot="network"]
```
