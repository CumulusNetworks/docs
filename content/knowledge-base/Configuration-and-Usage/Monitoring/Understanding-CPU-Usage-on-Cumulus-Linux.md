---
title: Understanding CPU Usage on Cumulus Linux
author: NVIDIA
weight: 375
toc: 4
---

## Issue
<!-- vale off -->
My Cumulus Linux switch is sitting idle with just a few ports active, no routing config, no traffic. When looking at the output of `top`, `switchd` is using 15 to 25% of the CPU. Should I be concerned about routing or switching performance when my network gets loaded with traffic?
<!-- vale on -->
## Background

Before you start to understand CPU usage, you need to understand some concepts regarding routing and switching performance.

*Performance* is a word used for many different types of measurements, including:

**Max Traffic Rate (data plane)**

  - Maximum traffic rate (Mbps or Gbps) in and out between two ports on a switch or router.
  - Maximum aggregate traffic rate in and out of all ports on a switch or router simultaneously.

**Routing and Switching Table Size (control plane)**

  - Maximum number of layer 3 subnet prefixes that you can store in the routing tables and layer 3 hardware switching tables.
  - Maximum number of layer 2 MAC entries that you can store in the switch hardware tables.

**Stability under Stress (control and data plane)**

  - How the switch/router performs and how fast it converges back to a steady state when a large amount of steady state traffic is flowing (data plane) and routing becomes unstable (control plane).

It is important to understand the separation of the control plane from the data plane. The data plane is the place where packets get switched *through* the system. In all modern routers/switches, this occurs in hardware by the switching ASICs. Nearly all modern switches can switch packets at essentially *line rate*, and most can switch at maximum rate through all the ports simultaneously.

So, when you look at CPU statistics, you are looking at how the switch is handling control plane activities, not data plane switching.

For the control plane, the primary concerns, as mentioned above, are *routing and switching table sizes* and *stability under stress*.

The amount of memory in the switching ASICs limits the *routing and switching table sizes*. For Cumulus Linux switches, the NVIDIA hardware guides have these numbers, which you can find on the {{<exlink url="https://www.nvidia.com/en-us/networking/ethernet-switching/hardware-compatibility-list/" text="hardware compatibility list">}}.

*Stability under stress*: The amount of network churn that a switch is capable of handling well depends much more on your particular network design than anything else. A solid network design and choice of routing protocols to match your requirements reduces the amount of protocol processing required during a network event, and increases the stability of your network. All modern switches of the same throughput category use CPUs of essentially the same performance category. Also, Cumulus Linux uses *control plane policing* and *QoS-based buffering* to protect the CPU and help ensure the processing of critical control plane traffic during times of network instability.

## What Is switchd Doing?

The primary task of `switchd` is to watch for layer 2 and layer 3 routing changes, update the routing/switching tables if needed, and then update the switching ASICs of any changes. It also updates switching counters from the data stored on the ASICs and does error checking. So it spends idle time doing housekeeping activities.

## Linux CPU Usage Basics

CPU measurement is an imprecise science, especially at low CPU usage. Basically it is a measurement of the work done divided by a time interval, then converted to a percentage. Several pages on the web describe how to do this calculation.

The Linux OS round-robins through all the active processes. When each process wakes up, it looks to see if it has work to do. If it does, it essentially has the CPU for a period of time to process all that work. If it has a lot of work to do, the CPU runs essentially at 100% until the work is complete. If a process shows up in `top` as 20% usage, that means it ran at about 100% for 1/5 of the time measurement interval. You can attribute some of that work to the overhead associated with the wake-up/sleep processing. `switchd` has to wake up regularly and run through its maintenance.

15 to 25% CPU is the basic overhead of `switchd` when "nothing" is happening. If work comes along, then CPU usage increases for a short amount of time to process that work. The main thing you need to remember is that `switchd` can scale to a large amount of changes. A 100% load is much more than 5 times the idle state of 20% load.

## Multiple CPUs

If you are looking at `top` to watch the CPU, you generally see statistics *per CPU*, so theoretically you only need to worry when the total activity starts approaching 200% (or 2.0 in the load average at the top). A `switchd` usage of 20% is the measurement of the percentage used on only one CPU, not an average of the two.

If you press the *1* key while watching `top` it toggles the `top` display to show both CPUs on the output. In an idle router, you can see that only one CPU is getting any noticeable activity.

## What to Watch for

If the CPU jumps up to some amount over 50%, but returns back to normal within a few seconds, you have nothing to worry about. This just indicates that some work came along and the process took time to handle that work.

However, if the CPU runs hot for a while (steady state), that would indicate that something is changing or unstable in the network, or there is some other cause of a large amount of control plane traffic. At that point, look for those processes that are receiving the most activity and try to determine what network events are creating that activity and fix the root cause, or adjust your network configuration accordingly.

Cumulus Linux uses `systemd` to monitor system health, including high CPU. When CPU usage reaches critical levels for a period of time, `systemd` alerts you of this condition.
