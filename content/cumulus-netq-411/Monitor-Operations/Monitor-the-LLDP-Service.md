---
title: LLDP
author: NVIDIA
weight: 860
toc: 3
---

Network devices use Layer Link Discovery Protocol (LLDP) to advertise their identity, capabilities, and neighbors on a LAN. You can view this information for one or more devices. You can also view the information at an earlier point in time or view changes that have occurred to the information during a specified time period. For an overview and how to configure LLDP in your network, refer to {{<kb_link latest="cl" url="Layer-2/Link-Layer-Discovery-Protocol.md" text="Link Layer Discovery Protocol">}}.

## LLDP Commands

Monitor LLDP with the following commands. See the {{<link title="show/#netq-show-lldp" text="command line reference">}} for additional options, definitions, and examples.

```
netq show lldp
netq show events message_type lldp
```

## View LLDP in the UI

To add the LLDP card to your workbench, navigate to the header and select <img src="https://icons.cumulusnetworks.com/44-Entertainment-Events-Hobbies/02-Card-Games/card-game-diamond.svg" height="18" width="18"/> **Add card&nbsp;<span aria-label="and then">></span> Other card&nbsp;<span aria-label="and then">></span> Network services&nbsp;<span aria-label="and then">></span> All LLDP Sessions card&nbsp;<span aria-label="and then">></span> Open cards**. In this example, there are 25 nodes running the LLDP protocol, 184 established sessions, and no LLDP-related events from the past 24 hours:

{{<figure src="/images/netq/lldap-med-460.png" alt="" width="200" >}}

Expand to the large card for additional LLDP information. This view displays the number of missing neighbors and how that number has changed over time. This is a good indicator of link communication issues. This info is displayed in the bottom chart, under **Total sessions with no NBR**. The right half of the card displays the switches handling the most LLDP traffic. Select the dropdown to view switches with unestablished LLDP sessions.

{{<figure src="/images/netq/lldp-large-460.png" width="650">}}

Expand the LLDP card to full-screen to view, filter, or export:

- A list of all switches running LLDP
- Peer information and attributes

{{<figure src="/images/netq/lldp-fullscreen-460.png" alt="" width="1100">}}

From this table, you can select a row, then click <img src="https://icons.cumulusnetworks.com/44-Entertainment-Events-Hobbies/02-Card-Games/card-game-diamond.svg" height="18" width="18"/> **Add card** above the table.

NetQ adds a new, LLDP 'single-session' card to your workbench. 

## Monitor a Single LLDP Session

From the LLDP single-session card, you can view the number of nodes running the LLDP service, view neighbor state changes, and monitor the running LLDP configuration and any changes to the configuration file. This view is helpful for determining the stability of the LLDP session between two devices.

{{<figure src="/images/netq/lldp-single-large-460.png" width="200">}}

### Understanding the Heat Map

On the medium and large single-session cards, vertically stacked heat maps represent the status of the neighboring peers: one for peers that are reachable (neighbor detected) and one for peers that are unreachable (neighbor not detected). Depending on the time period of data on the card, the number of smaller time blocks used to indicate the status varies. A vertical stack of time blocks, one from each map, includes the results from all checks during that time. The results appear by how saturated the color is for each block. If LLDP detected all peers during that time period for the entire time block, then the top block is 100% saturated (white) and the neighbor not detected block is 0% saturated (gray). As peers become reachable, the neighbor-detected block increases in saturation and the peers that are unreachable (neighbor not detected) block is proportionally reduced in saturation. The following table lists the most common time periods, their corresponding number of blocks, and the amount of time represented by one block:


| Time Period | Number of Runs | Number Time Blocks | Amount of Time in Each Block |
| ----------- | -------------- | ------------------ | ---------------------------- |
| 6 hours     | 18             | 6                  | 1 hour                       |
| 12 hours    | 36             | 12                 | 1 hour                       |
| 24 hours    | 72             | 24                 | 1 hour                       |
| 1 week      | 504            | 7                  | 1 day                        |
| 1 month     | 2,086          | 30                 | 1 day                        |
| 1 quarter   | 7,000          | 13                 | 1 week                       |

### View Changes to the LLDP Service Configuration File

Each time a change is made to the configuration file for the LLDP service, NetQ logs the change and lets you compare it with the last version using the NetQ UI. This can be useful when you are troubleshooting potential causes for alarms or sessions losing their connections.

1. From the large single-session card, select the <img src="https://icons.cumulusnetworks.com/16-Files-Folders/01-Common-Files/common-file-settings-1.svg" height="18" width="18"/> **Configuration file evolution** tab.

2. Select the time.

3. Choose between the **File** view and the **Diff** view.

    The File view displays the content of the file:

    {{<figure src="/images/netq/lldp-file-460.png" width="600">}}

    The Diff view highlights the changes (if any) between this version (on left) and the most recent version (on right) side by side:

    {{<figure src="/images/netq/lldp-diff-460.png" width="600">}}