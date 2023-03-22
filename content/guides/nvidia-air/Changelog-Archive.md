---
title: Changelog Archive
author: NVIDIA
weight: 20
product: NVIDIA Air
bookhidden: true
---
<!-- vale off -->
## December 2022
### 82.2022.1215
- Fixed an issue with instruction execution by the agent on the oob-mgmt-switch

### 82.2022.1205
- Fixed an issue where agent instructions were executed multiple times
- Improved an error message related to uploads
- Improved how service connectivity is implemented
- Added support for filtering simulations by title in the API

## November 2022
### 82.2022.1107-011
- Removed link to Cumulus Networks Slack

### 82.2022.1103-013
- Fixed display of long organization names

## October 2022
### 82.2022.1031
- Updated {{<exlink url="https://air.nvidia.com/api/" text="Swagger documentation for Air API">}}

### 82.2022.1027
- Updated Air API & Python SDK Docs to include examples: https://docs.nvidia.com/networking-ethernet-software/guides/nvidia-air/Air-Python-SDK/

## September 2022
### 82.2022.0929-013
- Added new metadata fields for Images
- Fixed an incorrect redirect URL for autoprovisioned simulations

### 82.2022.0922-013
- Fixed an issue related to console access
- Disabled poweroff on simulations using certain images
- Updated support alias

### 82.2022.0919
- Changes to facilitate future platform support

### 82.2022.0912
- Fixed a bug related to querying service information for simulations in an organization
- Fixed a bug where Cumulus Linux nodes defaulted to a different image if the requested one was not found

### 82.2022.0908
- Added Cumulus Linux 5.2.0 to dropdown in Builder
- Fixed authentication issue impacting small subset of users

## August 2022
### 82.2022.0829
- Added Cumulus Linux 5.2.0
- Added NetQ 4.3.0
- Updated out-of-band MAC address randomization

### 82.2022.0815
- Fixed a timing related bug that prevented sign-in in some cases
- Fixed a bug where the initial node instructions on the `oob-mgmt-switch` were failing
- Updated templates for notification emails

### 82.2022.0801-011
- Fixed a bug that prevented some large simulations from waking up
- Fixed a cosmetic error that may be thrown when browsing the Image list
- Fixed a cosmetic error that may be thrown when clicking on an Organization's Image list

## July 2022
### 82.2022.0711
- Fixed a bug that prevented a VM's console and/or network interfaces from working properly for VMs with more than 63 interfaces
### 82.2022.0714-008
- Pre-built topologies have been moved from the "NVIDIA Networking Experience" into the {{<exlink url="https://air.nvidia.com/marketplace" text="Demo Marketplace">}}
### 82.2022.0721
- Added a warning when the number of nodes in a simulation exceeds the subnet size of the out-of-band management network
### 82.2022.0726
- MAC addresses for out-of-band management interfaces are now randomized and prefixed with the NVIDIA OUI

## June 2022
### 82.2022.0606-015
- Added unique URLs for marketplace demos
- Fixed a bug that caused IPv6 addresses to not be assigned after multiple power on/power off events

### 82.2022.0616
- Fixed an incorrect error message that may be displayed while a simulation is loading
- Fixed a bug that removed a simulation from its organization after updating its details
- Fixed a bug that caused some VM interfaces to be unreachable inside a simulation

### 82.2022.0628
- Added Cumulus Linux 4.4.4

## May 2022
### 82.2022.0518
- Added Cumulus Linux 5.1.0

### 82.2022.0524
- Fixed a bug that prevented some organization members from viewing topology diagrams

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
### 82.2022.0429
- Added Cumulus Linux 3.7.16

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
