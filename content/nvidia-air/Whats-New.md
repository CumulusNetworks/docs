---
title: What's New
author: NVIDIA
weight: 20
product: NVIDIA Air
---
<!-- vale off -->
Check out the latest updates to {{<exlink url="https://air.nvidia.com" text="NVIDIA Air">}}.

## July 2025
<!-- Air:WhatsNew -->
### 82.2025.0708-011
- Added ability to specify additional CPU features in node metadata
<!-- Air:WhatsNew -->

## June 2025
### 82.2025.0603-011
- Fixed a visibility and persistence issue with the "Add Port" button

## May 2025
### 82.2025.0529-011
- Added ability to disable the DHCP service in out-of-band networks via simulation manifest import or topology endpoints

### 82.2025.0522-011
- Added ability to take screenshots of simulations

### 82.2025.0520-011
- Fixed an issue with editing a simulation's name

### 82.2025.0508-011
- Added functionality for filtering OOB network

### 82.2025.0506-011
- Added functionality for rebuilding and resetting multiple nodes concurrently from the UI

## April 2025
### 82.2025.0424-011
- Added functionality for handling OOB enablement and usage of reserved eth0 interfaces
- Added loading spinner when deleting nodes on canvas

### 82.2025.0422-011
- Added ability to configure multiple breakout ports concurrently
- Fixed an issue when disabling OOB after modifying node ports

### 82.2025.0410-011
- Added the ability to update multiple nodes concurrently
- Improved infrastructure stability when running large-scale simulations
- Fixed missing data issue in node properties
- Fixed an issue where simulations were expiring prematurely
- Fixed an issue with missing console prompts within simulations

### 82.2025.0403-011
- Added ability to view link details by selecting a link

## March 2025
### 82.2025.0325-011
- Fixed an issue where outbound interfaces did not appear in the services list

### 82.2025.0318-011
- Fixed an issue with the System Palette when minimizing the Servers and Switches section
- Fixed an issue with services being intermittently unreachable

### 82.2025.0311-011
- Fixed an issue with loading the details panel for a demo by using the demo ID in the URL
- Fixed an issue in the node side panel when switching between nodes
- Fixed an issue with deleting nodes in non-new states
- Fixed TypeError in browser console when importing a DOT file while creating a simulation

### 82.2025.0306-011
- Fixed an issue which resulted in management IP duplicates when using the out-of-band management network
- Fixed an issue where the node name tooltip could get stuck on the screen when the mouse was moved off the workspace canvas

### 82.2025.0304-011
- Added ability to right-click a node to open the actions menu
- The node name field now accommodates up to 255 characters

## Feburary 2025
### 82.2025.0227-011
- Fixed an issue where pressing "enter" in the ZTP text box created a SIM instead of adding a new line
- Added support for NetQ configuration via JSON topology files

### 82.2025.0225-011
- Fixed an issue with scrolling in Nodes/Links list when console is open
- Added tooltip support for improved accessibility in navigation items

### 82.2025.0220-011
- Fixed an issue with launching NetQ
- Fixed a validation issue when importing JSON topologies with ZTP script
- Added ability to define unconnected interfaces via JSON topology files

### 82.2025.0213-011
- Fixed an issue with Demo Marketplace nodes not retaining their disk changes after waking up
- Added API endpoint for parsing topologies from DOT format to JSON format

### 82.2025.0204-011
- Fixed an issue where simulations entered an error state when started
- Fixed an issue where adding time to a simulation caused open consoles to reconnect
- Fixed an issue where importing topologies with DPU nodes would fail with a validation error
- Fixed an issue with out-of-band node resource scaling not being applied when defining custom resource amounts
- Fixed an issue with the simulation deletion prompt
- Added functionality to select or clear multiple nodes individually by pressing Ctrl + left-click 
- Updated Node.js runtime to v20.18.2
- Added ability to resize node consoles in the UI

## January 2025
### 82.2025.0130-011
- Fixed an issue with ZTP when importing a simulation from a JSON file
- Fixed an issue with handling failed auto-provisioning POST requests
- Fixed an issue with copying a node from topology files
- Fixed link formatting in Demo Marketplace simulation guides
- Added functionality to configure external ports and view outbound links in the topology builder

### 82.2025.0123-011
- Fixed an issue with scrollbars in the Demo Marketplace simulation guide
- Fixed an issue with services links in the node side panel
- Fixed an issue with CD-ROM image transfers between organizations

### 82.2025.0114-011
- Added support for exporting simulations to JSON topology files from the UI
- Added the ability to configure switch breakout ports prior to starting a simulation using the API or UI 
- Fixed an issue with node consoles when switching between topology, nodes, and links views
- Fixed an issue with port search in the node side panel 

### 82.2025.0110-011
- Fixed an issue where node instructions were not being executed on Demo Marketplace simulations

### 82.2025.0107-011
- Fixed an issue with the Demo Marketplace search results
- Fixed an issue where image details displayed an updated status even though the image update request failed

## Archive
{{< expand "Changelog Archive 2024" >}}
## December 2024

### 82.2024.1219-011
- Added SN5610 system to manager

### 82.2024.1212-011
- Added the ability to launch NetQ after you create a simulation
- Added the ability to search for simulations by UUID
- Fixed an error message display issue
- Fixed an issue with the modal that Air displays when creating a new API token

### 82.2024.1205-011
- Updated and clarified API error messages for invalid files

### 82.2024.1203-011
- UserConfigs are now budgeted based on the overall content length instead of the instance amount
- Fixed an issue where the Air agent did not run on nodes after a simulation woke up
- Fixed an issue where nodes did not start when the CDROM value was defined
- Added the ability to upload a JSON topology file that includes a title and ZTP
- Fixed an issue where the copy-to-clipboard button for a service always generated the username *ubuntu*. It now correctly displays the username based on the node’s type.
- Removed the `organization` field from the JSON export API

## November 2024
### 82.2024.1121-011
- Fixed issue where a modal could be larger than the window and scrolling was not available
- Fixed an issue with scrolling of a simulation guide when it was popped out
- Fixed an issue where the count in the Organization tabs was not updated
- Fixed an issue where node names could be duplicated, causing issues with the OOB configuration
- Fixed a performance issue when loading the menu bar

### 82.2024.1112-011
- Added support for customizing OOB nodes when using JSON 
- Fixed an issue where the `Enable OOB` toggle was available when it should not be 
- Fixed an issue with the alignment of the `Workspace` and `Services` menus 
- Fixed an issue with links when a node is renamed 
- Fixed an issue with the search functionality for ports when creating a link 
- Fixed an issue when node names were improperly formatted 
- Added the ability to create a simulation via JSON import 
- Fixed an issue where the `Workspace` menu was visible when it should not be
- Fixed an issue with user provided network configurations via `clould-init` in the `generic/ubuntu2004`, `generic/ubuntu2204` and `generic/ubuntu2404` images

### 82.2024.1104-011
- Fixed an issue when updating node location on the canvas after the simulation is started
- Fixed an issue when liking or unliking marketplace demos
- Added support for additional ports on generic server nodes
- Added ZTP script support when importing a simulation from JSON
- Improved support for large scale simulations

## October 2024

### 82.2024.1031-011
- Fixed an issue when creating a new simulation from the nodes or links tabs
- Fixed an issue when populating SSH keys on the oob-mgmt-server
- Fixed an issue where topology fields could be updated after the simulation was LOADED
- Improved the initial processing when applying a filter
- Added the ability to add additional ports to non-switch nodes
- Fixed an issue with link highlighting for newly created links
- Fixed an issue when creating a simulation within an organization
- Added the ability to disable node name popups

### 82.2024.1028-011
- Fixed an issue with autoprovision redirects

### 82.2024.1024-011
- Fixed an issue where simulations could be created with `expires_at` and `sleeps_at` set in the past
- Fixed an issue when parsing interface MAC addresses
- Improved the loading of the links tab when a large number of links exist
- Improved the validation of the `features` field for a node

### 82.2024.1021-011
- Fixed an issue related to autoprovision redirects
- Fixed a potential scheduling issue when creating multiple simulations
- Improved logic around the Enable OOB toggle behavior
- Improved the logout process
- Moved the interface list to the node properties side panel

### 82.2024.1007-011
- Added link highlighting when a node is selected
- Fixed an issue with the grid when creating a new simulation
- Fixed an issue when an empty name wass provided while editing a simulation
- Fixed an issue when creating a new service
- Fixed an issue when sorting simulations by `Created`

## September 2024
### 82.2024.0926-014
- Allow a ZTP script to be added to any simulation at time of creation
- Updated the topology API to allow retrieval of a topology based on the simulation ID
- Fixed an issue where the organization dropdown was not rendered properly
- Fixed an issue when creating a simulation using JSON containing an invalid interface name
- Fixed an issue when importing JSON with a link for an undefined node
- Fixed an issue when importing JSON containing a `network_pci` configuration
- Fixed an issue where interfaces could be assigned an invalid MAC address when using the topology API

### 82.2024.0919-011
- Fixed a pagination issue when viewing organization members
- Fixed an issue when sorting members of an organization
- Fixed an issue when adding multiple members to an organization
- Fixed an issue where tokens could be created with an expiration date in the past
- Fixed the SSH link content in the services list
- Streamlined the node deletion confirmation
- Updated the simulation edit dialog
- Added an API endpoint supporting JSON import for simulations
- Added a search field to the nodes and links tabs in the simulation workspace
- Added a tooltip to display the full node name in the simulation workspace
- Added layout options for the topology in the simulation workspace
- Added an actions column to the nodes list
- Added a running node count under the organization details
- Added the ability to manage user permissions for a simulation

## August 2024
### 82.2024.0826-011
- Updated ZTP script template

### 82.2024.0819-011
- Fixed an issue where the `Enable SSH` option was not displayed after deleting the service
- Fixed an issue with pop-out consoles in the Legacy UI

### 82.2024.0815-011
- New UI now available for all users

### 82.2024.0801-011
- Changed simulation title requirements

## July 2024
### 82.2024.0722-014
- Added `generic/ubuntu2404` image with support for `cloud-init`
- Updated `generic/ubuntu2204` and `generic/ubuntu2004` images with support for `cloud-init`

## June 2024
### 82.2024.0627-013
- Updated the template ZTP script

### 82.2024.0613-012
- Fixed an issue where specifying an image by name in a dot file could cause an error

## May 2024
### 82.2024.0523-014
- Added `cumulus-vx-5.9.1` to the OS dropdown of the builder
- Updated the Swagger API view

### 82.2024.0516-013
- Fixed an issue when waking up large simulations

### 82.2024.0513-013
- Fixed an issue where some content types were rejected in API requests
- Improved dot file parsing performance for larger topologies

## April 2024
### 82.2024.0418-011
- Fixed an issue where node rebuild was improperly handled when a worker was offline

## March 2024
### 82.2024.0321-013
- Increased the number of retries when the Air Agent connects to the API
- Fixed an issue when deleting an organization with existing simulations

### 82.2024.0314-013
- Fixed an issue where MAC addresses were not properly validated
- Fixed an issue where node hostnames were allowed to contain whitespace
- Fixed an issue where attempting to create a simulation could improperly return a 400
- Fixed an issue that caused invalid links to be created during DOT file parsing
- Fixed an issue that prevented updating a shared topology after a simulation was deleted

## February 2024
### 82.2024.0229-012
- Fixed an issue that would cause the console not to render for a device
- Updated the default NetQ URL

### 82.2024.0222-010
- Added an API endpoint to automatically generate an out-of-band network

### 82.2024.0215-013
- Fixed an issue where the simulation API did not return all jobs for a loading simulation
- Fixed an issue where the login API incorrectly returned a 500 error

### 82.2024.0206-010
- Signing up for a new account now requires a valid business email address

## January 2024
### 82.2024.0125-013
- Updated Swagger API docs for `/v1/login/` and `/v2/organization/{id}/members/`

### 82.2024.0104-012
- Updated font used by configuration migration tool
{{< /expand >}}
{{< expand "Changelog Archive 2023" >}}
## November 2023
### 82.2023.1109-012
- Fixed an issue where the font failed to render correctly
- Fixed an issue preventing sims from starting
- Fixed an issue where a simulation created with no nodes would become stuck in the LOADING state
- Fixed an issue where sim state lock could be released too early during a stop job
- Fixed an issue where the topology delete API did not remove the topology

## October 2023
### 82.2023.1023-012
- Updated minimum memory allocated for the oob-mgmt-switch to 2GB
- Fixed a bug where a user defined value for memory on the oob-mgmt-switch was not respected

## September 2023
### 82.2023.0925-011
- Added Cumulus Linux 5.2.1 to OS dropdown in the builder
- Added Cumulus Linux 5.4.0c to OS dropdown in the builder
- Added Cumulus Linux 5.6.0 to OS dropdown in the builder
- Added SONiC 202211_1 to OS dropdown in the builder
- Updated default version for Cumulus Linux to 5.6.0 in the builder
- Updated default version for SONiC to 202211_1 in the builder

### 82.2023.0921-012
- Improved messaging when a resource budget is exceeded
- Fixed a bug related to display of the NIC model for Ubuntu nodes
- Fixed a bug where new members of an organization were not allocated the appropriate resource budgets
- Updated config migrator to use Cumulus Linux 5.6.0

### 82.2023.0918-011
- Updated oob-mgmt-switch image
- Fixed an issue related to logging level of the Air Agent

## August 2023
### 82.2023.0824-012
- Added a new `link_id` field to the `/v1/interface/` API response

### 82.2023.0822-011
- Fixed an issue during creation of the configuration file for the Air agent on some nodes
- Fixed an issue where parallel jobs could result in an invalid simulation state
- Fixed an issue where stalled requests could prevent API access by some clients

## July 2023
### 82.2023.0724-011
- Updated API to support ordering
- Fixed an issue related to interface count limitations on certain platforms

### 82.2023.0717-011
- Updated user authorization process

### 82.2023.0706-012
- Fixed an issue when deleting a topology associated with active simulations
- Fixed an issue where links could be connected to the same interface on both ends

## June 2023
### 82.2023.0622-012
- Fixed an issue that caused the oob-mgmt-switch to lose the default route after reboot
- Increased resource budget limits for non-company emails

### 82.2023.0612-011
- Fixed an error encountered by the agent when a node woke up from sleep
- Added Cumulus Linux 5.5.1 to OS dropdown in the builder
- Added support for IPv4 based services

## May 2023
### 82.2023.0525-012
- Fixed a bug impacting simulation creation including a fake device with more than 256 interfaces

### 82.2023.0518-011
- Fixed a bug related to simulation state control and resource budgets
- Improved validation for the link API

### 82.2023.0515-016
- Added Cumulus Linux 5.5.0 to OS dropdown in the builder

### 82.2023.0511-015
- Added Cumulus Linux 5.5.0
- Fixed an issue related to image uploads

### 82.2023.0504-012
- Updated oob-mgmt-server to Ubuntu 22.04
- Added a limit of 256 for the maximum number of interfaces on a single node
- Updated resource budget limits for accounts using a company email
- Fixed a bug that prevented some simulations with TPM/UEFI from loading
- Fixed a bug in validation of image uploads

## April 2023
### 82.2023.0424-012
- Fixed an incorrect calculation for resource budgets in some scenarios
- Fixed an issue causing the login page to be shown instead of a node's console in some scenarios
- Applied new security updates

### 82.2023.0420-012
- Updated sleep handling for longer running simulations
- Fixed an issue related to reporting current state when loading larger simulations

### 82.2023.0418-011
- Added support for copying images between organizations
- Updated default resource limits

### 82.2023.0410-012
- Added Ubuntu 22.04
- Added SONiC 202205_2
- Backend infrastructure improvements

## March 2023
### 82.2023.0330-011
- Added new mechanism for anonymous simulation handling

### 82.2023.0323-011
- Added Cumulus Linux 4.3.1
- Added Cumulus Linux 4.4.5
- Added NetQ 4.5.0
- Updated Cumulus Linux 5.4.0

### 82.2023.0321-012
- Fixed a bug impacting automatic NetQ instructions impacting certain versions of Cumulus Linux
- Fixed a bug related to resource budget calculation

### 82.2023.0316-011
- Updated default resource limits
- Fixed a bug impacting filtering in the Demo Marketplace

### 82.2023.0306-011
- Added cookie management options

## February 2023
### 82.2023.0216-011
- Added Cumulus Linux 5.4.0
- Builder defaults to Cumulus Linux 5.4.0 for new nodes
- API documentation fixes

### 82.2023.0213-012
- Updated Cumulus Linux 3.7.9 image
- Updated Cumulus Linux 3.7.10 image
- Updated Cumulus Linux 3.7.11 image
- Updated Cumulus Linux 3.7.12 image
- Updated Cumulus Linux 3.7.13 image
- Updated Cumulus Linux 3.7.14 image
- Updated Cumulus Linux 3.7.14.2 image
- Updated Cumulus Linux 3.7.15 image
- Updated Cumulus Linux 3.7.16 image
- Fix for CVE-2022-25927

### 82.2023.0206-012
- API updates to protect against unsupported changes for running simulations

## January 2023
### 82.2023.0119-011
- Added Cumulus Linux 5.3.1

### 82.2023.0112-011
- Updated oob-mgmt-server image
  - Added socat package
- Updated generic/ubuntu1804 image
{{< /expand >}}
{{< expand "Changelog Archive 2022" >}}
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
{{< /expand >}}
{{< expand "Changelog Archive 2021" >}}
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
<!-- vale on -->
## August 2021
- {{<exlink url="https://air.nvidia.com/migrate" text="NVUE migration tool">}}
- Specify the location of a node's bootable OS with the `boot` option in your DOT file. For example, boot a node via PXE using `boot="network"`:

```
"server" [function="server" os="generic/ubuntu1804" boot="network"]
```
<!-- vale on -->
{{< /expand >}}