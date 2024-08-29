---
title: Storm Control
author: NVIDIA
weight: 470
toc: 3
---
Storm control provides protection against excessive inbound BUM (broadcast, unknown unicast, multicast) traffic on layer 2 switch port interfaces, which can cause poor network performance.

## Configure Storm Control

To configure storm control settings, you can either run NVUE commands or manually edit the `/etc/cumulus/switchd.conf` file.

The following command example enables broadcast storm control for swp4 at 400 packets per second (pps), multicast storm control at 3000 pps, and unknown unicast at 2000 pps.

{{< tabs "TabID15 ">}}
{{< tab "NVUE Commands">}}

```
cumulus@switch:~$ nv set interface swp4 storm-control broadcast 400
cumulus@switch:~$ nv set interface swp4 storm-control multicast 3000
cumulus@switch:~$ nv set interface swp4 storm-control unknown-unicast 2000
cumulus@switch:~$ nv config apply
```

{{%notice note%}}
The storm control settings require a `switchd` reload. Before applying the settings, NVUE indicates if it requires a `switchd` reload and prompts you for confirmation. When the `switchd` service reloads, there is no interruption to network services.
{{%/notice%}}

The following example command disables multicast storm control on swp4:

```
cumulus@switch:~$ nv unset interface swp4 storm-control multicast
cumulus@switch:~$ nv config apply
```

{{< /tab >}}
{{< tab "Linux Commands ">}}

Edit the `/etc/cumulus/switchd.conf` file and uncomment the `storm_control.broadcast`, `storm_control.multicast`, and `storm_control.unknown_unicast` lines:

```
cumulus@switch:~$ sudo nano /etc/cumulus/switchd.conf
...
# Storm Control setting on a port, in pps
interface.swp4.storm_control.broadcast = 400
interface.swp4.storm_control.multicast = 3000
interface.swp4.storm_control.unknown_unicast = 2000
...
```

When you change the storm control settings, you must reload `switchd` with the `sudo systemctl reload switchd.service` command for the changes to take effect. The reload does not interrupt network services.

{{< /tab >}}
{{< /tabs >}}

## Show Storm Control Settings

To show the current storm control settings for a layer 2 interface, run the `nv show interface <interface> storm-control` command.

```
cumulus@switch:~$ nv show interface swp4 storm-control
                 applied  description
---------------  -------  ----------------------------------------------------------
broadcast        400      Configure storm control for broadcast traffic in pps
multicast        3000     Configure storm control for multicast traffic in pps
unknown-unicast  2000      Configure storm control for unknown unicast traffic in pps
```
