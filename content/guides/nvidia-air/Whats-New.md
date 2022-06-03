---
title: What's New
author: NVIDIA
weight: 20
product: NVIDIA Air
---
<!-- vale off -->
Check the latest updates to {{<exlink url="https://air.nvidia.com" text="NVIDIA Air">}}.

## May 2022
### 82.2022.0518
- Added Cumulus Linux 5.1.0
<!-- Air:WhatsNew -->
### 82.2022.0524
- Fixed a bug that prevented some organization members from viewing topology diagrams
<!-- Air:WhatsNew -->

## April 2022
### 82.2022.0406
- Fixed a bug that caused incorrect validation of updates to a simulation's sleep timer
- Fixed API filtering for interfaces in a simulation
### 82.2022.0412-015
- Removed unecessary `reboot` from ZTP script template for custom topologies
### 82.2022.0419-007
- Fixed a scenario where changing the name of a simulation caused an error to be shown
- Fixed a cosmetic issue where cards in the Demo Marketplace may have been displayed incorrectly
### 82.2022.0421-008
- Added a link to launch the NetQ UI in the sidebar
- Fixed a bug where organization admins might not have seen all users who have permissions to a simulation
- Fixed a bug that caused the header dropdown menu to not be visible on some pages
### 82.2022.0422-007
- Fixed a bug that prevented CPU and memory values from being set correctly in some custom topologies
### 82.2022.0425-009
- Fixed a cosmetic issue with displaying some VM memory values
### 82.2022.0427-008
- Fixed Demo Marketplace cards to display more than one line of description
### 82.2022.0428
- Fixed a race condition that could cause deleted simulations to show a "Loaded" status
<!-- Air:WhatsNew -->
### 82.2022.0429
- Added Cumulus Linux 3.7.16
<!-- Air:WhatsNew -->

## March 2022
### 82.2022.0309
- Resolved an error that occurred when logging in to Air via https://www.nvidia.com/en-us/networking/network-simulation/
### 82.2022.0314-010
- Share simulations with your colleagues using the new and improved organizations feature. {{<link url="/Organizations" text="Click here">}} for more details.
### 82.2022.0317-014
- Updated the visual design of the header and navigation panels
- Fixed a bug that prevented VMs from being `Reset` after the guest OS is shutdown
- Fixed a bug that prevented NetQ accounts from being created for some simulations
- Fixed a visual issue that prevented the simulation list from using all of its available space
### 82.2022.0318-009
- Fixed support for email addresses with non-alphanumeric characters
### 82.2022.0323-008
- Added better validation for simulation sleep times
- Improved UX for adding members to an organization

## February 2022
### 82.2022.0204-013
- Fixed a bug that caused new simulations to appear as sleeping while they were loading
- Fixed a bug that could prevent an error from being displayed when resource budgets were exceeded
### 82.2022.0208-009
- Improved UI transitions for "Try It" documentation examples
### 82.2022.0216
- Fixed a bug that redirected to the login page when "liking" a marketplace demo
- Fixed a bug that may prevent new simulations from starting
### 82.2022.0223
- NVIDIA Cumulus Linux 4.4.3 is now available for use in custom topologies
### 82.2022.0228-008
- Fixed incorrect sorting of simulations
- Updated the visual design of the header and navigation panels [82.2022.0317-014]
- Fixed a bug that prevented VMs from being `Reset` after the guest OS is shutdown [82.2022.0317-014]
- Fixed a bug that prevented NVIDIA Air from creating NetQ accounts for some simulations [82.2022.0317-014]
- Fixed a visual issue that prevented the simulation list from using all available space [82.2022.0317-014]
- Fixed support for email addresses with non-alphanumeric characters [82.2022.0318-009]
- Share simulations with your colleagues using the new and improved organizations feature. {{<link url="/Organizations" text="Click here">}} for more details. [82.2022.0314-010]
- Resolved an error that occurred when logging in to Air via https://www.nvidia.com/en-us/networking/network-simulation/ [82.2022.0309]

## February 2022
- Fixed incorrect sorting of simulations [82.2022.0228-008]
- NVIDIA Cumulus Linux 4.4.3 is now available for use in custom topologies [82.2022.0223]
- Fixed a bug that redirected to the login page when "liking" a marketplace demo [82.2022.0216]
- Fixed a bug that might prevent new simulations from starting [82.2022.0216]
- Improved UI transitions for "Try It" documentation examples [82.2022.0208-009]
- Fixed a bug that caused new simulations to appear as sleeping while they were loading [82.2022.0204-013]
- Fixed a bug that might prevent an error from displaying when resource budgets exceed the maximum [82.2022.0204-013]

## January 2022
### 82.2022.0112
- NVIDIA Cumulus Linux 5.0.1 is now available for use in custom topologies
### 82.2022.0131
- Customizable templates for simulation email notifications

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
<!-- vale on -->
