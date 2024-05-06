---
title: Common Options
author: Cumulus Networks
weight: 60

type: nojsscroll
---
<style>
h { color: RGB(118,185,0)}
</style>

All NVUE commands have `-h` and `--help` options that provide command description and usage.

The NVUE `nv show` commands have these common options.

## Revision Options

| <div style="width:200px">Option | Description |
| ------ | ----------- |
|`--rev <revision>` | Shows a detached pending configuration. `<revsion>` is the ID. For example, `nv show --rev 4`. |
|`--pending` | Shows configuration that is `set` and `unset` but not yet applied or saved. For example, `nv show --pending interface bond1`. |
|`--applied` | Shows configuration applied with the `nv config apply` command. For example, `nv show --applied interface bond1`.|
|`--startup` | Shows the saved configuration.|
|`--operational` | Shows the running configuration (the actual system state). For example, `nv show --operational interface bond1` shows the running configuration for bond1. The running and applied configuration should be the same. If different, inspect the logs.|

## View Options

| <div style="width:200px">Option | Description |
| ------ | ----------- |
|`--view <view>`<br>`-w <view>` | Shows these different views: `brief`, `lldp`, `mac`, `plugables`, and `small`. For example, the `nv show interface --view=small` command shows a list of the interfaces on the switch and the `nv show interface --view=brief` command shows information about each interface on the switch, such as the interface type, speed, remote host and port. |
| `--filter <filter>` | Filters on column output data. For example, the `nv show interface --filter mtu=1500` shows only the interfaces with MTU set to 1500.</br>To filter on multiple column outputs, enclose the filter types in parentheses; for example, `nv show interface --filter "type=bridge&mtu=9216"` shows data for bridges with MTU 9216.</br>You can use wildcards; for example, `nv show interface swp1 --filter "ip.address=1*"` shows all IP addresses that start with 1 for swp1.</br>You can filter on all revisions (operational, applied, and pending); for example, `nv show interface --filter "ip.address=1*" --rev=applied` shows all IP addresses that start with 1 for swp1 in the applied revision. |

## Output Options

| <div style="width:200px">Option | Description |
| ------ | ----------- |
| `--output <format>`<br> `-o <format>`| Shows command output in table (`auto`), `json`, `yaml`, or plain text (`raw`) format such as vtysh native output. For example:<br>`nv show interface bond1 --output auto`<br>`nv show interface bond1 --output json`<br>`nv show interface bond1 --output yaml`<br>`nv show router bgp -output raw`|
| `--color` (`on`, `off`, or `auto`) |  Turns colored output on or off. The default is auto. For example<br>`nv show --color on interface bond1`. |
| `--paginate` (`on`, `off`, or `auto`) | Paginates the output. The default is `off`. For example<br>`nv show --paginate on interface bond1`.  |
