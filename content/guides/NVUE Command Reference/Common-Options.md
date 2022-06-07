---
title: Common Options
author: Cumulus Networks
weight: 60
product: Cumulus Linux
type: nojs
---
All NVUE commands have `-h` and `--help` options that provide command description and usage. This reference guide is based on the command `-h` output.

The NVUE `nv show` commands have these common options.

## Revision Options

| <div style="width:200px">Option | Description |
| ------ | ----------- |
|`--rev <revision>` | Shows a detached pending configuration. `<revsion>` is the ID. For example, `nv show --rev changeset/cumulus/2021-06-11_16.16.41_FPKK interface bond1`. |
|`--pending` | Shows configuration that is `set` and `unset` but not yet applied or saved. For example, `nv show --pending interface bond1`. |
|`--applied` | Shows configuration applied with the `nv config apply` command. For example, `nv show --applied interface bond1`.`|
|`--startup` | Shows configuration saved with the `nv config save` command. This is the configuration after the switch boots.|
|`--operational` | Shows the running configuration (the actual system state). For example, `nv show --operational interface bond1` shows the running configuration for bond1. The running and applied configuration should be the same. If different, inspect the logs.|

## Show Options

| <div style="width:200px">Option | Description |
| ------ | ----------- |
|`--view <view>`<br>`-w <view>` | Shows these different views: brief, lldp, mac, pluggables, and small. This option is available for the `nv show interface` command only. For example, the `nv show interface --view=small` command shows a list of the interfaces on the switch and the `nv show interface --view=brief` command shows information about each interface on the switch, such as the interface type, speed, remote host and port. |

## Output Options

| <div style="width:200px">Option | Description |
| ------ | ----------- |
| `--output <format>`<br> `-o <format>`| Shows command output in table format (auto), `json` format or `yaml` format. For example:<br>`nv show --ouptut auto interface bond1`<br>`nv show --output json interface bond1`<br>`nv show --ouptut yaml interface bond1`|
| `--color` (`on`, `off`, or `auto`) |  Turns colored output on or off. The default is auto. For example<br>`nv show --color on interface bond1` |
| `--paginate` (`on`, `off`, or `auto`) | Paginates the output. The default is `off`. For example<br>`nv show --paginate on interface bond1`.  |
