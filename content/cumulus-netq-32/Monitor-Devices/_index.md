---
title: Monitor Devices
author: Cumulus Networks
weight: 820
toc: 3
---
With the NetQ UI and CLI, a user can monitor the network inventory of switches and hosts, including such items as the number of each and what operating systems are installed. Additional details are available about the hardware and software components on individual switches, such as  the motherboard, ASIC, microprocessor, disk, memory, fan and power supply information. The commands and cards available to obtain this type of information help you to answer questions such as:

- What switches do I have in the network?
- What is the distribution of ASICs across my network?
- Do all switches have valid licenses?
- Are NetQ agents running on all of my switches?
- What hardware is installed on my switches?
- How many transmit and receive packets have been dropped?
- How healthy are the fans and power supply?
- What software is installed on my switches?
- Are all switches licensed correctly?
- What is the ACL and forwarding resources usage?
- Do all switches have NetQ Agents running?



<!-- NetQ uses {{<exlink url="https://docs.cumulusnetworks.com/cumulus-linux/Layer-2/Link-Layer-Discovery-Protocol/" text="LLDP">}} (Link Layer Discovery Protocol) to collect port information. NetQ can also identify peer ports connected to DACs (Direct Attached Cables) and AOCs (Active Optical Cables) without using LLDP, even if the link is not UP. -->

