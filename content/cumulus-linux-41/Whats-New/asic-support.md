---
title: ASIC Supported Features
weight: 10
toc: 2
Draft: true
---

Cumulus Linux supports a number of switching platforms and networking ASICs. The network ASIC is responsible for hardware accelerating packet forwarding and a number of features.

Not every ASIC supports every feature Cumulus Linux offers. This may be due to the ASIC lacking the capabilities of the feature (hardware limitation) or because Cumulus Linux has not yet enabled the capabilities in the hardware (software limit).

The following table describes the features available in both Cumulus Linux software and the hardware ASIC for Cumulus Linux version {{< version >}}.

## Broadcom-based ASICs

### Trident Family

| Feature                                                                                                                    | Maverick            | Trident2            | Trident2+           | Trident3 <br /> (all variants) |
| -------------------------------------------------------------------------------------------------------------------------- | ------------------- | ------------------- | ------------------- | ------------------------------ |
| {{< link title="ASIC Monitoring" text="Buffer Monitoring" >}}                                                              | {{< unsupported >}} | {{< unsupported >}} | {{< unsupported >}} | {{< unsupported >}}            |
| {{< link title="Buffer and Queue Management#Congestion Notification" text="ECN" >}}                                        | {{< unsupported >}} | {{< supported >}}   | {{< supported >}}   | {{< supported >}}              |
| {{< link title="GRE Tunneling" text="GRE" >}}                                                                              | {{< unsupported >}} | {{< unsupported >}} | {{< unsupported >}} | {{< unsupported >}}            |
| {{< link title="Network Address Translation - NAT" text="NAT" >}}                                                          | {{< unsupported >}} | {{< unsupported >}} | {{< unsupported >}} | {{< supported >}}\*            |
| {{< link title="Buffer and Queue Management#priority-flow-control" text="PFC" >}}                                          | {{< unsupported >}} | {{< supported >}}   | {{< supported >}}   | {{< supported >}}              |
| {{< link title="Buffer and Queue Management" text="Quality of Service" >}}                                                 | {{< unsupported >}} | {{< supported >}}   | {{< supported >}}   | {{< supported >}}              |
| {{< link title="Monitoring System Statistics and Network Traffic with sFlow" text="sFlow" >}}                              | {{< supported >}}   | {{< supported >}}   | {{< supported >}}   | {{< supported >}}              |
| {{< link title="Network Virtualization" text="VXLAN Bridging (L2 Only)" >}}                                                | {{< supported >}}   | {{< supported >}}   | {{< supported >}}   | {{< supported >}}              |
| {{< link title="Setting Date and Time#precision-time-protocol-ptp-boundary-clock" text="Precision Time Protocol (PTP)" >}} | {{< unsupported >}} | {{< unsupported >}} | {{< unsupported >}} | {{< unsupported >}}            |
| {{< link title="VXLAN Routing" text="VXLAN Routing (L2 + L3)" >}}                                                          | {{< supported >}}   | {{< unsupported >}} | {{< supported >}}   | {{< supported >}}              |
| {{< link title="Mellanox What Just Happened (WJH)" text="What Just Happened" >}}                                           | {{< unsupported >}} | {{< unsupported >}} | {{< unsupported >}} | {{< unsupported >}}            |

\* NAT is only supported on the Trident3 X7 family.

### Tomahawk Family

| Feature                                                                                                                    | Tomahawk            | Tomahawk+           | Tomahawk2           | Tomahawk3           |
| -------------------------------------------------------------------------------------------------------------------------- | ------------------- | ------------------- | ------------------- | ------------------- |
| {{< link title="ASIC Monitoring" text="Buffer Monitoring" >}}                                                              | {{< unsupported >}} | {{< unsupported >}} | {{< unsupported >}} | {{< unsupported >}} |
| {{< link title="Buffer and Queue Management#Congestion Notification" text="ECN" >}}                                        | {{< supported >}}   | {{< supported >}}   | {{< unsupported >}} | {{< unsupported >}} |
| {{< link title="GRE Tunneling" text="GRE" >}}                                                                              | {{< unsupported >}} | {{< unsupported >}} | {{< unsupported >}} | {{< unsupported >}} |
| {{< link title="Network Address Translation - NAT" text="NAT" >}}                                                          | {{< unsupported >}} | {{< unsupported >}} | {{< unsupported >}} | {{< unsupported >}} |
| {{< link title="Buffer and Queue Management#priority-flow-control" text="PFC" >}}                                          | {{< supported >}}   | {{< supported >}}   | {{< unsupported >}} | {{< unsupported >}} |
| {{< link title="Buffer and Queue Management" text="Quality of Service" >}}                                                 | {{< supported >}}   | {{< unsupported >}} | {{< unsupported >}} | {{< unsupported >}} |
| {{< link title="Monitoring System Statistics and Network Traffic with sFlow" text="sFlow" >}}                              | {{< supported >}}   | {{< supported >}}   | {{< supported >}}   | {{< supported >}}   |
| {{< link title="Network Virtualization" text="VXLAN Bridging (L2 Only)" >}}                                                | {{< supported >}}   | {{< supported >}}   | {{< supported >}}   | {{< unsupported >}} |
| {{< link title="Setting Date and Time#precision-time-protocol-ptp-boundary-clock" text="Precision Time Protocol (PTP)" >}} | {{< unsupported >}} | {{< unsupported >}} | {{< unsupported >}} | {{< unsupported >}} |
| {{< link title="VXLAN Routing" text="VXLAN Routing (L2 + L3)" >}}                                                          | {{< supported >}}   | {{< supported >}}   | {{< supported >}}   | {{< unsupported >}} |
| {{< link title="Mellanox What Just Happened (WJH)" text="What Just Happened" >}}                                           | {{< unsupported >}} | {{< unsupported >}} | {{< unsupported >}} | {{< unsupported >}} |

### Other ASIC Families

| Feature                                                                                                                    | Helix4              |
| -------------------------------------------------------------------------------------------------------------------------- | ------------------- |
| {{< link title="ASIC Monitoring" text="Buffer Monitoring" >}}                                                              | {{< unsupported >}} |
| {{< link title="Buffer and Queue Management#Congestion Notification" text="ECN" >}}                                        | {{< unsupported >}} |
| {{< link title="GRE Tunneling" text="GRE" >}}                                                                              | {{< unsupported >}} |
| {{< link title="Network Address Translation - NAT" text="NAT" >}}                                                          | {{< unsupported >}} |
| {{< link title="Buffer and Queue Management#priority-flow-control" text="PFC" >}}                                          | {{< unsupported >}} |
| {{< link title="Buffer and Queue Management" text="Quality of Service" >}}                                                 | {{< unsupported >}} |
| {{< link title="Monitoring System Statistics and Network Traffic with sFlow" text="sFlow" >}}                              | {{< unsupported >}} |
| {{< link title="Network Virtualization" text="VXLAN Bridging (L2 Only)" >}}                                                | {{< unsupported >}} |
| {{< link title="Setting Date and Time#precision-time-protocol-ptp-boundary-clock" text="Precision Time Protocol (PTP)" >}} | {{< unsupported >}} |
| {{< link title="VXLAN Routing" text="VXLAN Routing (L2 + L3)" >}}                                                          | {{< unsupported >}} |
| {{< link title="Mellanox What Just Happened (WJH)" text="What Just Happened" >}}                                           | {{< unsupported >}} |

## Mellanox-based ASICs

| Feature                                                                                                                    | Spectrum            | Spectrum 2          |
| -------------------------------------------------------------------------------------------------------------------------- | ------------------- | ------------------- |
| {{< link title="ASIC Monitoring" text="Buffer Monitoring" >}}                                                              | {{< supported >}}   | {{< supported >}}   |
| {{< link title="Buffer and Queue Management#Congestion Notification" text="ECN" >}}                                        | {{< supported >}}   | {{< supported >}}   |
| {{< link title="GRE Tunneling" text="GRE" >}}                                                                              | {{< supported >}}   | {{< supported >}}   |
| {{< link title="Network Address Translation - NAT" text="NAT" >}}                                                          | {{< unsupported >}} | {{< supported >}}   |
| {{< link title="Buffer and Queue Management#priority-flow-control" text="PFC" >}}                                          | {{< supported >}}   | {{< supported >}}   |
| {{< link title="Buffer and Queue Management" text="Quality of Service" >}}                                                 | {{< supported >}}   | {{< unsupported >}} |
| {{< link title="Monitoring System Statistics and Network Traffic with sFlow" text="sFlow" >}}                              | {{< supported >}}   | {{< supported >}}   |
| {{< link title="Network Virtualization" text="VXLAN Bridging (L2 Only)" >}}                                                | {{< supported >}}   | {{< supported >}}   |
| {{< link title="Setting Date and Time#precision-time-protocol-ptp-boundary-clock" text="Precision Time Protocol (PTP)" >}} | {{< unsupported >}} | {{< supported >}} |
| {{< link title="VXLAN Routing" text="VXLAN Routing (L2 + L3)" >}}                                                          | {{< supported >}}   | {{< supported >}}   |
| {{< link title="Mellanox What Just Happened (WJH)" text="What Just Happened" >}}                                           | {{< supported >}}   | {{< supported >}}   |
