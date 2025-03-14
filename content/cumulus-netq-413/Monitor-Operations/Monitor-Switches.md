---
title: Switches
author: NVIDIA
weight: 960
toc: 3
---
With the NetQ UI and NetQ CLI, you can monitor the health of individual switches, including interface performance and resource utilization.

NetQ reports switch performance metrics for the following categories:

- **System configuration**: events, interfaces, IP and MAC addresses, VLANs, IP routes, and IP neighbors
- **Utilization statistics**: CPU, memory, disk, ACL and forwarding resources, SSD, BTRFS, and processes
- **Physical sensing**: digital optics and switch sensors
- **RoCE** and **Precision Time Protocol**

## View Switch Metrics and Attributes

{{<tabs "TabID20" >}}

{{<tab "NetQ UI" >}}
{{<notice tip>}}
The quickest way to access monitoring information for an individual switch is by searching for its hostname in the global search field. Search for the hostname and select the switch to open a full-screen overview of attributes and performance information.
{{</notice>}}
Alternately, you can add a device card to your workbench:

1. From the header select <img src="https://icons.cumulusnetworks.com/44-Entertainment-Events-Hobbies/02-Card-Games/card-game-diamond.svg" height="18" width="18"/> **Add card&nbsp;<span aria-label="and then">></span> Device card**.

2. Select a switch from the list:

    {{<figure src="/images/netq/open-device-dropdown-450.png" alt="dropdown displaying switches" width="300" height="275">}}

3. Click **Add**.

4. Adjust the card's size to view information at different levels of granularity. 

Attributes are displayed as the default tab on the large Switch card. You can view the static information about the switch, including its hostname, addresses, server and ASIC vendors and models, OS and NetQ software information. You can also view the state of the interfaces and NetQ Agent on the switch.

{{<figure src="/images/netq/indswitch-412.png" alt="large switch card displaying attributes" width="700" height="350">}}

Hover over the top of the card and select the appropriate icon to view utilization info, interface statistics, digital optics info, RoCE metrics, and PTP clock graphs. This example displays utilization information, including CPU, memory, and disk utilization from the past 24 hours:

{{<figure src="/images/netq/switch-util-411.png" alt="large switch card displaying attributes" width="700" height="350">}}

Expand the card to full-screen to view, filter, or export information about events, interfaces, MAC addresses, VLANs, IP routes, IP neighbors, IP addresses, BTRFS utilization, SSD utilization, forwarding resources, ACL resources, What Just Happened events, sensors, RoCE counters, digital optics, BGP and EVPN sessions, PTP, and process monitoring for a given switch: 

{{<figure src="/images/netq/fullscreen-switch-412.png" alt="" width="1200" height="625">}}

{{</tab>}}

{{<tab "NetQ CLI" >}}

The information available in the UI can also be displayed via the CLI with a corresponding {{<link title="show" text="netq show">}} command. Each command that begins with `netq show` includes the option `<hostname>`. When the `<hostname>` option is included in the command, the output displays results limited to the switch or host you specified.

For example, you can view all events across your network with the {{<link title="show/#netq-show-events" text="netq show events">}} command. To view all events on a particular switch, specify its name in the `<hostname>` field in `netq <hostname> show events`. The following example displays all events on the leaf01 switch:

```
cumulus@switch:~$ netq leaf01 show events

Matching events records:
Hostname          Message Type             Severity         State      Message                             Timestamp
----------------- ------------------------ ---------------- ---------- ----------------------------------- -------------------------
leaf01            tca_procdevstats         info             open       RX bytes exceeded threshold,        Tue Dec  3 16:18:40 2024
                                                                       for ifname: eth0 value: 228
leaf01            tca_procdevstats         info             open       RX bytes exceeded threshold,        Tue Dec  3 16:18:11 2024
                                                                       for ifname: swp50 value: 898
leaf01            tca_procdevstats         info             open       RX bytes exceeded threshold,        Tue Dec  3 16:13:36 2024
                                                                       for ifname: eth0 value: 253
leaf01            tca_procdevstats         info             open       RX bytes exceeded threshold,        Tue Dec  3 16:13:05 2024
                                                                       for ifname: swp50 value: 885
leaf01            tca_procdevstats         info             open       RX bytes exceeded threshold,        Tue Dec  3 16:08:21 2024
                                                                       for ifname: eth0 value: 240
leaf01            tca_procdevstats         info             open       RX bytes exceeded threshold,        Tue Dec  3 16:07:50 2024
                                                                       for ifname: swp50 value: 919
leaf01            tca_procdevstats         info             open       RX bytes exceeded threshold,        Tue Dec  3 16:03:08 2024
                                                                       for ifname: eth0 value: 250
```

Refer to the command line reference for a comprehensive list of {{<link title="show" text="netq show commands">}}.


{{</tab>}}

{{</tabs>}}

## View CPU and Memory Utilization for Processes and Services

Use the UI or CLI to visualize which services and processes are consuming the most CPU and memory on a switch. NetQ displays only active processes with the exception of `netqd`, which is displayed regardless of its active or inactive status. You can add or remove specific services that NetQ monitors using the CLI. 

{{<notice note>}}

Process monitoring is only supported on Spectrum switches. 

{{</notice>}}

{{<tabs "TabID46" >}}

{{<tab "NetQ UI" >}}

To visualize CPU and memory utilization at the process level, open a large device card and navigate to the **Utilization** tab. Then select **Show process monitoring data**. The UI depicts two charts---one each for CPU and memory utilization---along with a list of services and processes.

Select a process from the **Process name** column for its usage data to be reflected in the CPU and memory utilization charts. The data presented is aggregated over a 5-minute period; NetQ lists the process consuming the most CPU resources (aggregated over a 5-minute period or the **CPU 5min** column) from highest to lowest. The process whose data is reflected in the charts is indicated by an icon {{<img src="/images/netq/analytics-bars.svg" alt="" height="18" width="18">}} next to the name of the process.

The following graphs depict CPU and memory usage over a 6-hour time period from the system monitor daemon, *smond*.

{{<figure src="/images/netq/procmon-470.png" alt="CPU and memory utilization info for the smond service" width="1200" height="475">}}

{{</tab>}}

{{<tab "NetQ CLI" >}}

The information displayed in the UI can be viewed using the CLI with the {{<link title="show/#netq-show-services" text="netq show services resource-util">}} command:

```
cumulus@switch:~$ netq show services resource-util

Matching services records:
Hostname          Service              PID   VRF                  Enabled Active Uptime               CPU one Minute       CPU five Minute      Memory one Minute    Memory five Minute   Last Updated
----------------- -------------------- ----- -------------------- ------- ------ -------------------- -------------------- -------------------- -------------------- -------------------- ------------------------
r-3700-02         sx_sdk               19012 default              yes     yes    81 day 17h ago       7.7                  24.65                9.44                 9.44                 Tue Jul 18 18:49:19 2023
r-3700-03         sx_sdk               13627 default              yes     yes    81 day 18h ago       0                    17.82                9.44                 9.44                 Tue Jul 18 18:49:19 2023
r-3700-02         switchd              21100 default              yes     yes    81 day 17h ago       56.77                15.07                1.13                 1.13                 Tue Jul 18 18:49:19 2023
r-3700-03         switchd              15768 default              yes     yes    81 day 18h ago       0                    8.28                 1.11                 1.11                 Tue Jul 18 18:49:19 2023
neo-switch02      sx_sdk               1841  default              yes     yes    2h 29min ago         30.1                 6.55                 9.67                 9.67                 Tue Jul 18 18:49:19 2023
ufm-switch19      sx_sdk               2343  default              yes     yes    21h 3min ago         5.22                 5.73                 2.84                 2.84                 Tue Jul 18 18:49:19 2023
ufm-switch29      sx_sdk               2135  default              yes     yes    8 day 4h ago         2.88                 5.73                 9.54                 9.54                 Tue Jul 18 18:49:19 2023
r-3420-01         sx_sdk               1885  default              yes     yes    9 day 3h ago         5.28                 5.01                 9.3                  9.3                  Tue Jul 18 18:49:19 2023
ufm-switch29      clagd                7095  default              no      yes    8 day 4h ago         23.57                4.71                 0.63                 0.63                 Tue Jul 18 18:49:19 2023
r-3700-01         smond                7301  default              yes     yes    9 day 3h ago         0                    4.7                  0.2                  0.2                  Tue Jul 18 18:49:19 2023
... 
```

To configure the NetQ Agent to start monitoring additional services, run {{<link title="config/#netq-config-add-agent-services" text="netq config add agent services">}}, specifying the services you want the agent to monitor in the command. Restart the agent, then run {{<link title="config/#netq-config-show-agent" text="netq config show agent services">}} to display a list of services that the NetQ Agent is monitoring for CPU and memory usage.

To stop the agent from monitoring a service run {{<link title="config/#netq-config-del-agent-services" text="netq config del agent services">}}. Some services and processes cannot be excluded from monitoring.

{{</tab>}}

{{</tabs>}}

To actively monitor process-level CPU and memory utilization, you can create {{<link title="Configure and Monitor Threshold-Crossing Events" text="threshold-crossing rules">}}. These rules generate events when a process or service exceeds the utilization limit you defined when creating the rule. Refer to the {{<link title="Threshold-Crossing Events Reference/#resource-utilization" text="resource utilization table in the TCA Events Reference">}} for service memory and service CPU utilization event IDs.

## View Queue Lengths as Histograms

Monitoring queue lengths in your network’s fabric is useful for detecting microbursts or packet buffer congestion, which can lead to higher latency or packet drops. The {{<kb_link latest="cl" url="Monitoring-and-Troubleshooting/ASIC-Monitoring.md" text="Cumulus Linux documentation">}} provides a detailed description of ASIC monitoring, including example bin configurations and information on interpreting histogram queue lengths. 

{{%notice note%}}

- Queue length monitoring is supported on Spectrum switches running Cumulus Linux 5.1 or later. To display queue histogram data, you must set the snapshot file count to at least 120 when you are configuring ASIC monitoring, as described in the Snapshots section in the {{<kb_link latest="cl" url="Monitoring-and-Troubleshooting/ASIC-Monitoring.md" text="ASIC monitoring configuration">}} documentation.
- If you restart the `asic-monitor` service or edit the `/monitor.conf` configuration file, you must restart the NetQ agent with `netq config restart agent`.
- NetQ displays histogram data for all switch ports, even if the ports are down or have not been configured.

{{%/notice%}}

The information available in the UI can also be displayed via the CLI with the {{<link title="show/#netq-show-histogram" text="netq show histogram">}} command. 

To add the queue histogram card to your workbench, select **Add card** and search for the 'Top 5 longest buffers' card. For a more detailed view, expand the {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/03-Menu/navigation-menu.svg" height="18" width="18">}} **Menu**. In the Spectrum-X section, select **Queue histogram**.

Devices are {{<link title="Switch Management/#role-management" text="grouped according to their roles">}}: superspine, leaf, spine, or exit. If you haven't assigned roles to your devices, they appear in the 'unassigned' group. Each group lists the five devices with the highest P95 values. From here, you can select an individual device or **View all** to view all devices assigned a particular role along with their queue length values.

{{<figure src="/images/netq/fabric-overview-queue-413.png" alt="dashboard displaying devices grouped according to their respective roles" width="1200" height="425">}}

Each device is represented by a card that displays its hostname, the port with the longest queue length (displayed horizontally, divided into bins), standard deviation, P95 value across all ports that have ASIC monitoring configured, and average queue length over the past five minutes. The values reflected in the bins are color-coded, with higher values displayed in darker colors and lower values in lighter colors. Hover over a bin to view its corresponding queue length count.

{{<figure src="/images/netq/single-device-queue-413.png" alt="single device with standard deviation, P95, and average queue length values" width="250" height="225">}}

Select **View more** to open a dashboard that displays the full range of ports configured to send histogram data along with their LLDP peers, which are visible when you hover over a section with your cursor. From this view, you can compare devices against each other or the same devices over a different time period. For example, the following view compares queue length data from two switches over the past 30 minutes.

{{<figure src="/images/netq/queue-compare-413.png" alt="histogram comparison of the same device with different time parameters" width="1100" height="500">}}

The y-axis represents the values contained in bins 0 through 9. The switch's ports are displayed on the x-axis. Hover your mouse over the data to view the associated port name, count data, bin number, and LLDP peer.

## Related Information

- {{<link title="Switch Inventory">}}
- {{<link title="Switch Management" text="Switch Lifecycle Management">}}