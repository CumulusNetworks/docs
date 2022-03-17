---
title: What's New in NVIDIA Air
author: NVIDIA
weight: 20
product: NVIDIA Air
---

Check out some of the latest features added to the {{<exlink url="https://air.nvidia.com" text="NVIDIA Air Infrastructure Simulation Platform">}}.

## March 2022
<!-- Air:WhatsNew -->
- Updated the visual design of the header and navigation panels [82.2022.0317-014]
- Fixed a bug that prevented VMs from being `Reset` after the guest OS is shutdown [82.2022.0317-014]
- Fixed a bug that prevented NetQ accounts from being created for some simulations [82.2022.0317-014]
- Fixed a visual issue that prevented the simulation list from using all of its available space [82.2022.0317-014]
<!-- Air:WhatsNew -->
- Share simulations with your colleagues using the new and improved organizations feature. {{<link url="/Organizations" text="Click here">}} for more details. [82.2022.0314-010]
- Resolved an error that occurred when logging in to Air via https://www.nvidia.com/en-us/networking/network-simulation/ [82.2022.0309]

## February 2022
- Fixed incorrect sorting of simulations [82.2022.0228-008]
- NVIDIA Cumulus Linux 4.4.3 is now available for use in custom topologies [82.2022.0223]
- Fixed a bug that redirected to the login page when "liking" a marketplace demo [82.2022.0216]
- Fixed a bug that may prevent new simulations from starting [82.2022.0216]
- Improved UI transitions for "Try It" documentation examples [82.2022.0208-009]
- Fixed a bug that caused new simulations to appear as sleeping while they were loading [82.2022.0204-013]
- Fixed a bug that could prevent an error from being displayed when resource budgets were exceeded [82.2022.0204-013]

## January 2022
- Customizable templates for simulation email notifications [82.2022.0131]
- NVIDIA Cumulus Linux 5.0.1 is now available for use in custom topologies  [82.2022.0112]

## December 2021
- NVIDIA Cumulus Linux 5.0 is now available for use in custom topologies
- VMs in a custom topology now use their operating system's default username and password. See the {{<link url="/Quick-Start#logging-into-virtual-machines" text="Quick Start">}} guide for more details.

## September 2021
<!-- vale off -->
- Enable UEFI SecureBoot for virtual machines using the `secureboot` option in your DOT file. For example:

```
"server" [function="server" os="generic/ubuntu2004" secureboot="true"]
```

- {{<exlink url="https://air.nvidia.com/marketplace" text="Demo Marketplace">}}: Get a jump start on your network configuration by checking out some pre-built feature demos, or submit your own!
- This page! Be sure to check back often to see the latest features we're adding to NVIDIA Air.
<!-- vale on -->
## August 2021
- {{<exlink url="https://air.nvidia.com/migrate" text="NVUE migration tool">}}
- Specify the location of a node's bootable OS with the `boot` option in your DOT file. For example, boot a node via PXE using `boot="network"`:

```
"server" [function="server" os="generic/ubuntu1804" boot="network"]
```
