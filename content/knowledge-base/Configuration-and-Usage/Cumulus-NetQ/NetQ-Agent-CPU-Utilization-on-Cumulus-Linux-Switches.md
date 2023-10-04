---
title: NetQ Agent CPU Utilization on Cumulus Linux Switches
author: NVIDIA
weight: 341
toc: 4
---

## Overview

NetQ Agent is an application running on switches. It monitors and collects telemetry data on the switch, and streams it to the NetQ Platform either in the cloud or on premises. NetQ Agents, like other applications running on the switch, might cause high CPU utilization when the CPU is available. This does not interfere with normal switch traffic, but can be manually limited.

## Issue Presentation

You might experience high CPU utilization by the NetQ Agent on switches running Cumulus Linux. You might see this high utilization when monitoring the CPU through SNMP or Grafana or other monitoring tools in the form of an alarm or event based on your threshold settings for CPU usage.

## Manage the NetQ Agent Behavior

One way you can monitor CPU usage by the NetQ Agent and other services is to run the following command on the Cumulus Linux switch:

    root@hostname:/var/log# ps %mem | head
    
    PID    PPID   CMD                          %MEM   %CPU
    889    1      /usr/sbin/switchd            6.5    18.8
    1246   1      /usr/share/venvs/netq-apps/  2.9    0.0
    10866  10773  /usr/share/venvs/netq-agent  2.2    11.9
    10773  1      /usr/share/venvs/netq-agent  2.0    1.3
    10957  10866  /usr/share/venvs/netq-agent  1.9    1.6
    1243   1      /usr/bin/python -O /usr/sbi  1.1    0.0
    1020   1      /usr/bin/python /usr/sbin/p  0.6    0.2
    1245   1      /usr/bin/python /usr/bin/ne  0.5    0.9
    1021   1      /usr/bin/python /usr/sbin/s  0.5    0.4

Cumulus Linux has a built-in load balancing algorithm that regulates CPU usage, allowing the NetQ Agent to only use the CPU when it is available. The NetQ Agent is a low priority Linux process, running at priority level 5. When there is no scheduling contention, the NetQ Agent can use as much bandwidth as the CPU has available. When there is contention, it yields to higher priority processes, such as protocol daemons and the switch ASIC driver and kernel tasks.

You have an additional option to set a limit on how much CPU bandwidth the NetQ Agent can use in the NetQ 2.4.1 and Cumulus Linux 3.6.x, 3.7.x, or 4.1 and later releases. Run the following NetQ CLI command on the Cumulus Linux switch to cap the CPU utilization by the NetQ Agent:

    netq config add agent cpu-limit <limit>

The recommended limit is 60% to start. If you find this is too high or too low, you can adjust it.

For example, you can check the value of the current setting, modify it, and then verify it changed.

1.  Check what the limit is set to now.

        root@hostname:/var/log# netq config show agent cpu-limit
        CPU Quota
        -----------
        100%

2.  Modify the limit to CPU usage by the NetQ Agent to a maximum of
    60%.  

        root@hostname:/var/log# netq config add agent cpu-limit 60
        Successfully set agent CPU limit to 60
        Please restart agent(netq config restart agent)
        
        root@hostname:/var/log# netq config restart agent
        Restarting netq-agent... Success!

3.  Verify the setting.

        root@hostname:/var/log# netq config show agent cpu-limit
        CPU Quota
        -----------
        60

    You can also view the setting in JSON format:

        root@hostname:/var/log# netq config show agent cpu-limit json
        {
        "cpu-limit":60
        }

## Conclusion

While the NetQ Agent might cause high CPU usage on switches, it does not interfere with normal operations. NetQ designates the NetQ Agent as a low priority service and thus only uses CPU when it is available. If you prefer, you can control the amount of available CPU bandwidth that the NetQ Agent uses by setting a limit with the NetQ CLI `netq config add agent cpu-limit` command.

## References

{{<kb_link latest="netq" url="Lifecycle-Management/Manage-NetQ-Agents.md" text="Manage NetQ Agents">}}
