---
title: NVUE Commands
author: NVIDIA
weight: 121
toc: 2
---
This section shows you how to list all the NVUE commands and see command descriptions.

## List All Commands

To see a list of all the NVUE `nv show`, `nv set`, `nv unset`, `nv action`, and `nv config` commands, run `nv list-commands`.

{{%notice note%}}
The following is only a small sample of the NVUE command list. To see the full and most up to date list of commands, run `nv list-commands` on your switch.
{{%/notice%}}

```
cumulus@leaf01:mgmt:~$ nv list-commands
nv show platform
nv show platform hardware
nv show platform hardware component
nv show platform hardware component <component-id>
nv show platform software
nv show platform software installed
nv show platform software installed <installed-id>
nv show platform capabilities
nv show platform environment
nv show platform environment fan
nv show platform environment fan <fan-id>
nv show platform environment psu
nv show platform environment psu <psu-id>
nv show platform environment led
nv show platform environment led <led-id>
nv show platform environment sensor
nv show platform environment sensor <sensor-id>
nv show action
nv show action <action-job-id>
nv show router
nv show router ptm
nv show router nexthop
...
```

## Show a Command Description

To see a description for a command, type the command with `-h` at the end:

```
cumulus@leaf01:mgmt:~$ nv set mlag backup -h
usage: 
  nv [options] set mlag backup <backup-ip>

Description:
  backup                Set of MLAG backups

Identifiers:
  <backup-ip>           Backup IP of MLAG peer (ipv4 | ipv6)

Output Options:
  -o <format>, --output <format>
                        Supported formats: json, yaml, auto, constable, end-table, commands (default:auto)
  --color (on|off|auto)
                        Toggle coloring of output (default: auto)
  --paginate (on|off|auto)
                        Whether to send output to a pager (default: off)

General Options:
  -h, --help            Show help.
```

When you use `-h`, replace any variables in the command with a value. For example, for the `nv set vrf <vrf-id> router pim` command, type `nv set vrf default router pim -h`:

```
cumulus@leaf01:mgmt:~$ nv set vrf default router pim -h
usage: 
  nv [options] set vrf <vrf-id> router pim [address-family ...]
  nv [options] set vrf <vrf-id> router pim [ecmp ...]
  nv [options] set vrf <vrf-id> router pim [enable ...]
  nv [options] set vrf <vrf-id> router pim [msdp-mesh-group ...]
  nv [options] set vrf <vrf-id> router pim [timers ...]

Description:
  pim                   PIM VRF configuration.

Identifiers:
  <vrf-id>              VRF (vrf-name)

Attributes:
  address-family        Address family specific configuration
  ecmp                  Choose all available ECMP paths for a particular RPF.  If 'off', the first nexthop found will be used.  This is the default.
  enable                Turn the feature 'on' or 'off'.  The default is 'off'.
  msdp-mesh-group       To connect multiple PIM-SM multicast domains using RPs.
  timers                Timers

Output Options:
  -o <format>, --output <format>
                        Supported formats: json, yaml, auto, constable, end-table, commands (default:auto)
  --color (on|off|auto)
                        Toggle coloring of output (default: auto)
  --paginate (on|off|auto)
                        Whether to send output to a pager (default: off)

General Options:
  -h, --help            Show help.
```
