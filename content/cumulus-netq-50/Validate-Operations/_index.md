---
title: Validation Checks
author: NVIDIA
weight: 750
toc: 2
---

NetQ periodically runs default validations to verify whether devices, hosts, network protocols, and services are operating as expected. These validations measure what NetQ expects from a healthy network against the data it receives from the network it is monitoring. When NetQ detects an anomaly or inconsistency, the system will broadcast an event.

By default, NetQ excludes certain validation tests to reduce the number of event notifications. However, you can configure NetQ to run additional validations for the excluded protocols and services.

## Validation Categories

The following table displays the validation categories and the default frequency at which they run. Refer to the {{<link title="Validation Tests Reference" text="Validation Reference">}} for a comprehensive breakdown of each test included in each category.

| Item | NetQ UI | NetQ CLI | Run by Default | Frequency |
| --- | :---: | :---: | :---: |  :---: |
| Agents | Yes | Yes |  Yes |  60 mins |
| BGP | Yes | Yes | Yes |  60 mins |
| Cumulus Linux version | No | Yes |  No | on-demand, as scheduled |
| Duplicate IP addresses | Yes | Yes | No | on-demand, as scheduled |
| EVPN | Yes | Yes |  Yes | 60 mins |
| Interfaces | Yes | Yes |  Yes |  60 mins |
| MLAG (CLAG) | Yes | Yes |  Yes |  60 mins |
| MTU | Yes | Yes | Yes |  60 mins |
| NTP | Yes | Yes | Yes |  60 mins |
| RoCE | Yes | Yes | No | on-demand, as scheduled |
| Sensors | Yes | Yes |  Yes |  60 mins |
| Topology | Yes | Yes | No | on-demand, as scheduled |
| VLAN | Yes | Yes | Yes |  60 mins |
| VXLAN | Yes | Yes | Yes |  60 mins |

{{<notice note>}}
After logging in, it can take up to an hour for NetQ to display accurate validation data.
{{</notice>}}

## View and Run Validations in the UI

The {{<link title="Validate Network Protocol and Service Operations#view-validation-summary" text="validation summary">}} displays the results from the subset of hourly validation checks that NetQ runs by default. Select **Validation** in the header to create or schedule new validation checks, as well as view previous results.
## Validation with the NetQ CLI

The NetQ CLI uses the {{<link title="check" text="netq check commands">}} to validate the various elements of your network fabric, looking for inconsistencies in configurations across your fabric, connectivity faults, missing configurations, and so forth. You can run commands from any node in the network.