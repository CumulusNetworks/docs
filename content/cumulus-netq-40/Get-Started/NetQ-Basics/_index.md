---
title: NetQ Overview
author: NVIDIA
weight: 50
toc: 3
---

{{<product>}} is a highly scalable, modern network operations tool set that provides visibility and troubleshooting of your overlay and underlay networks in real-time. NetQ delivers actionable insights and operational intelligence about the health of your data center - from the container, virtual machine, or host, all the way to the switch and port. NetQ correlates configuration and operational status, and instantly identifies and tracks state changes while simplifying management for the entire Linux-based data center. With NetQ, network operations change from a manual, reactive, node-by-node approach to an automated, informed and agile one.

NetQ performs three primary functions:

- **Data collection**: real-time and historical telemetry and network state information
- **Data analytics**: deep processing of the data
- **Data visualization**: rich graphical user interface (GUI) for actionable insight

NetQ is available as an on-site or in-cloud deployment.

Unlike other network operations tools, NetQ delivers significant operational improvements to your network management and maintenance processes. It simplifies the data center network by reducing the complexity through real-time visibility into hardware and software status and eliminating the guesswork associated with investigating issues through the analysis and presentation of detailed, focused data.

## Demystify Overlay Networks

While overlay networks provide significant advantages in network management, it can be difficult to troubleshoot issues that occur in the overlay one node at a time. You are unable to correlate what events (configuration changes, power outages, and so forth) might have caused problems in the network and when they occurred. Only a sampling of data is available to use for your analysis. By contrast, with NetQ deployed, you have a networkwide view of the overlay network, can correlate events with what is happening now or in the past, and have real-time data to fill out the complete picture of your network health and operation.

In summary:

| Without NetQ                               | With NetQ                                                           |
| ------------------------------------------ | ------------------------------------------------------------------- |
| Difficult to debug overlay network         | View networkwide status of overlay network                          |
| Hard to find out what happened in the past | View historical activity with time-machine view                     |
| Periodically sampled data                  | Real-time collection of telemetry data for a more complete data set |

## Protect Network Integrity with NetQ Validation

Network configuration changes can cause the creation of many trouble tickets because you cannot test a new configuration before deploying it. When the tickets start pouring in, you <!-- vale off -->are stuck with a large amount of data that is collected<!-- vale on --> and stored in multiple tools, making correlation of the events to the resolution required difficult at best. Isolating faults in the past is challenging. By contract, with NetQ deployed, you can proactively verify a configuration change as inconsistencies and can catch misconfigurations before deployment. And historical data is readily available to correlate past events with current issues.

In summary:

| Without NetQ | With NetQ |
| ------------ | --------- |
| Reactive to trouble tickets | Catch inconsistencies and misconfigurations before deployment with integrity checks/validation    |
| Large amount of data and multiple tools to correlate the logs/events with the issues | Correlate network status, all in one place |
| Periodically sampled data | Readily available historical data for viewing and correlating changes in the past with current issues |

## Troubleshoot Issues Across the Network

Troubleshooting networks is challenging in the best of times, but trying to do so manually, one node at a time, and digging through a series of long and ugly logs make the job harder than it needs to be. NetQ provides rolled up and correlated network status on a regular basis, enabling you to get down to the root of the problem quickly, whether it occurred recently or over a week ago. The graphical user interface makes this possible visually to speed the analysis.

In summary:

| Without NetQ | With NetQ |
| ------------ | --------- |
| Large amount of data and multiple tools to correlate the logs/events with the issues | Rolled up and correlated network status, view events and status together |
| Past events <!-- vale off -->are lost<!-- vale on --> | Historical data gathered and stored for comparison with current network state |
| Manual, node-by-node troubleshooting | View issues on all devices all at one time, pointing to the source of the problem |

## Track Connectivity with NetQ Trace

Conventional trace only traverses the data path looking for problems, and does so on a node to node basis. For paths with a small number of hops that might be fine, but in larger networks, it can become very time consuming. NetQ verifies both the data and control paths, providing additional information. It discovers misconfigurations along all hops in one go, speeding the time to resolution.

In summary:

| Without NetQ                                            | With NetQ                                                            |
| ------------------------------------------------------- | -------------------------------------------------------------------- |
| Trace covers only data path; hard to check control path | Verifies both data and control paths                                 |
| View portion of entire path                             | View all paths between devices at one time to find problem paths     |
| Node-to-node check on misconfigurations                 | View any misconfigurations along all hops from source to destination |
