---
title: Monitor Switch Inventory
author: Cumulus Networks
weight: 822
toc: 4
---
With the NetQ UI, you can monitor individual switches separately from the network. You are able to view the status of services they are running, health of its various components, and connectivity performance. Being able to monitor switch component inventory aids in upgrade, compliance, and other planning tasks. Viewing individual switch health helps isolate performance issues.

With NetQ, a network administrator can monitor both the switch hardware and its operating system for misconfigurations or misbehaving services. Refer to {{<link title="Monitor Devices">}} for related commands and cards.

## View Switch Inventory Summary

All of the devices in your network can be viewed from either the NetQ CLI or NetQ UI.

{{< tabs "TabID13" >}}

{{< tab "NetQ CLI" >}}

To view the hardware and software components for a switch, run:

```
netq <hostname> show inventory brief
```

This example shows the type of switch (Cumulus VX), operating system (Cumulus Linux), CPU (x86_62), and ASIC (virtual) for the *spine01* switch.

```
cumulus@switch:~$ netq spine01 show inventory brief
Matching inventory records:
Hostname          Switch               OS              CPU      ASIC            Ports
----------------- -------------------- --------------- -------- --------------- -----------------------------------
spine01           VX                   CL              x86_64   VX              N/A
```

{{< /tab >}}

{{< tab "NetQ UI" >}}

{{< /tab >}}

{{< /tabs >}}

## View Switch Hardware Inventory

You can view all hardware components or narrow your view to specific hardware components for a given switch.

Switch component inventory can be viewed from either the NetQ CLI or NetQ UI.

{{< tabs "TabID47" >}}

{{< tab "NetQ CLI" >}}

To view switch components, run:

```
netq <hostname> show inventory brief
```

This example shows

{{< /tab >}}

{{< /tabs >}}

## View Switch Software Inventory
