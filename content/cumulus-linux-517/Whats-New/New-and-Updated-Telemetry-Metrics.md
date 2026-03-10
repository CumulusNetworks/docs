---
title: New and Updated Telemetry Metrics
author: Cumulus Networks
weight: -30
product: Cumulus Linux
version: "5.17"
toc: 1
---
The following tables list the new, updated, and deprecated gNMI and OTEL metrics in Cumulus Linux 5.17.

## gNMI Metrics

{{< tabs "TabID13 ">}}
{{< tab "Link Debounce ">}}

|  Name | Description |
|------ | ----------- |
| `/interfaces/interface[name=swp1]/hold-time/state/counters/ignored-up-events` | *UP events suppressed because debounce timer had not yet expired (transient UP spikes filtered). This metric indicates Noise or short UP spikes being filtered.|
| `/interfaces/interface[name=swp1]/hold-time/state/counters/ignored-down-events` | *DOWN events suppressed because debounce timer had not yet expired (transient link loss filtered). This metric indicates short interruptions being filtered.| 
| `/interfaces/interface[name=swp1]/hold-time/state/counters/received-up-events`| *UP events accepted and propagated after debounce delay (stable link recovery). This metric indicates stable link recovery events.|
| `/interfaces/interface[name=swp1]/hold-time/state/counters/received-down-events` | *DOWN events accepted and propagated after debounce delay (sustained link failure). This metric indicates sustained link failure events.| 
| `/interfaces/interface[name=swp1]/hold-time/state/counters/timer-cancellations` |  *Timer aborted because link state reverted before timer expired (quick reversal). This metric indicates Link flapping or oscillation.| 
| `/interfaces/interface[name=swp1]/hold-time/state/counters/timer-expirations` |  *Timer completed successfully, event sent after debounce delay (stable state change). This metric indicates Valid and stable state changes.|

{{< /tab >}}
{{< tab "PHY">}}

|  Name | Description |
|------ | ----------- |
| `/interfaces/interface[name]/phy/link_down_events` | *Total PHY link down events.|
| `/interfaces/interface[name]/phy/unintentional_link_down_events` | *Unintentional link drops (local and remote).|
| `/interfaces/interface[name]/phy/intentional_link_down_events` | *Intentional link drops (local and remote).|
| `/interfaces/interface[name]/phy/local_reason_opcode` | *Opcode of link down reason at the local end.|
| `/interfaces/interface[name]/phy/remote_reason_opcode` | *Opcode of link down reason at the remote end.|

{{< /tab >}}
{{< /tabs >}}

## OTEL Metrics

{{< tabs "TabID13 ">}}
{{< tab "Link Debounce ">}}

|  Name | Description |
|------ | ----------- |
| `nvswitch_interface_link_debounce_ignored_up_events` | * UP events suppressed because debounce timer had not yet expired (transient UP spikes filtered). This metric indicates Noise or short UP spikes being filtered.  |
| `nvswitch_interface_link_debounce_ignored_down_events`| * DOWN events suppressed because debounce timer had not yet expired (transient link loss filtered). This metric indicates short interruptions being filtered. |
| `nvswitch_interface_link_debounce_received_up_events` | *UP events accepted and propagated after debounce delay (stable link recovery). This metric indicates stable link recovery events.  |
| `nvswitch_interface_link_debounce_received_down_events` | *DOWN events accepted and propagated after debounce delay (sustained link failure). This metric indicates sustained link failure events.  |
| `nvswitch_interface_link_debounce_timer_cancellations` | *Timer aborted because link state reverted before timer expired (quick reversal). This metric indicates Link flapping or oscillation. |
| `nvswitch_interface_link_debounce_timer_expirations` | *Timer completed successfully, event sent after debounce delay (stable state change). This metric indicates Valid and stable state changes.  |

{{< /tab >}}
{{< tab "PHY">}}

|  Name | Description |
|------ | ----------- |
| `nvswitch_interface_phy_stats_link_down_events` | *Total PHY link down events. |
| `nvswitch_interface_phy_stats_intentional_link_down_events` | *Intentional link down events. |
| `nvswitch_interface_phy_stats_unintentional_link_down_events` | *Unintentional link down events. |
| `nvswitch_interface_phy_stats_link_down_reason_code_local ` | *Opcode of link down reason at the local end.|
| `nvswitch_interface_phy_stats_link_down_reason_code_remote ` | *Opcode of link down reason at the remote end. |

{{< /tab >}}
{{< /tabs >}}