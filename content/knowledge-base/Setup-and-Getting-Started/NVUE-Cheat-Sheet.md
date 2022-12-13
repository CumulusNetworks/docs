---
title: NVIDIA User Experience (NVUE) Cheat Sheet
weight: 102
toc: 4
---

<span style="background-color:#F5F5DC"> [NVUE](## "NVIDIA User Experience")</span> is an object-oriented, schema-driven model of a complete Cumulus Linux system providing a robust API that allows multiple interfaces to view and configure any element within a system.

You can use the NVUE through its <span style="background-color:#F5F5DC"> [CLI](## "Command Line Interface")</span> or the <span style="background-color:#F5F5DC"> [API](## "Application Programming Interface")</span>. As NVUE is an object model, both CLI and REST API interfaces have equivalent functionality and can work in parallel while keeping all management operations consistent; for example, the CLI `show` commands reflect any `PATCH` operation (create) you run through the REST API.  

NVUE follows a declarative model, removing context-specific commands and settings. It is structured as a big tree (like a filesystem path) representing the entire system state. At the tree’s base are high-level branches representing objects, such as router and interface. Under each branch, there are further branches, and as you navigate through the tree, you gain a more specific context of the objects. The tree’s leaves are actual attributes, represented as key-value pairs. 

This cheat sheet will help you get up to speed using [Cumulus Linux]({{<ref "/cumulus-linux-53">}}) and [NVUE CLI]({{<ref "/cumulus-linux-53/System-Configuration/NVIDIA-User-Experience-NVUE/NVUE-CLI">}}). 

For information about using the [NVUE REST API]({{<ref "/cumulus-linux-53/System-Configuration/NVIDIA-User-Experience-NVUE/NVUE-API">}}), refer to the [NVUE API documentation](https://docs.nvidia.com/networking-ethernet-software/cumulus-linux-53/api/index.html).

## Getting Started

Once you racked and powered on your Cumulus Linux switch use a serial console cable to configure it.

You can use either in band or <span style="background-color:#F5F5DC"> [OOB](## "Out of Band")</span> managment. The ethernet oob interface - `eth0` is set to use DHCPv4 for addressing by default.
If you are not using DHCP in your network, you can set static management IP address and defalt-gateway on eth0:
```
cumulus@switch:~$ nv set interface eth0 ip address 192.168.200.2/24
cumulus@switch:~$ nv set interface eth0 ip gateway 192.168.200.1
cumulus@switch:~$ nv config apply
``` 

Configure system's hostname:
```
cumulus@switch:~$ nv set system hostname leaf01
cumulus@switch:~$ nv config apply
```

Cumulus Linux boots with an  <span style="background-color:#F5F5DC"> [NTP](## "Network Time Protocol")</span> service enabled and default servers set. To add NTP servers:   
```
cumulus@switch:~$ nv set service ntp default server 4.cumulusnetworks.pool.ntp.org iburst on
cumulus@switch:~$ nv config apply
```
Check out [NTP]({{<ref "/cumulus-linux-53/System-Configuration/Date-and-Time/Network-Time-Protocol-NTP">}}) documentation for more information.

The switch is set with a default UTC (Coordinated Universal Time) time zone. To update the time zone to your location:
```
cumulus@switch:~$ nv set system timezone US/Eastern
cumulus@switch:~$ nv config apply
```
If you are not using NTP, you can update the date and time using the Linux `date` command:
```
cumulus@switch:~$ sudo date -s "Tue Jan 26 00:37:13 2021"
``` 

## Configuring the Interfaces

By default, all Cumulus Linux data interfaces are disabled (except `eth0` mgmt. port). To enable the interfaces on the switch:
```
cumulus@switch:~$ nv set interface swp1
cumulus@switch:~$ nv config apply
```
You can also enable all (or a range) interfaces at once:
```
cumulus@switch:~$ nv set interface swp1-52
cumulus@switch:~$ nv config apply
```

All interfaces in Cumulus Linux are routed (L3) once enabled.

To enable Show applied (running) configuration. The default configuration output is in YAML format.
```
cumulus@switch:~$ nv config show
```
Use the `commands` output to list configuration commands
```
cumulus@switch:~$ nv config show -o commands
```



