---
title: VXLAN Tunnel DSCP Operations
author: NVIDIA
weight: 640
toc: 3
---
Cumulus Linux provides configuration options to control DSCP operations during VXLAN encapsulation and decapsulation, specifically for solutions that require end-to-end quality of service, such as RDMA over Converged Ethernet.

The configuration options propagate explicit congestion notification (ECN) between the underlay and overlay and are based on {{<exlink url="https://tools.ietf.org/html/rfc6040" text="RFC 6040">}}, which describes how to construct the IP header of an ECN field on both ingress to and egress from an IP-in-IP tunnel.

{{%notice note%}}

VXLAN Tunnel DSCP operations are supported on Mellanox Spectrum switches only.

{{%/notice%}}

## Configure DSCP Operations

You can set the following DSCP operations by editing the `/etc/cumulus/switchd.conf` file. After you modify `/etc/cumulus/switchd.conf` file, you must restart `switchd` for the changes to take effect; run the `cumulus@switch:~$ sudo systemctl restart switchd.service` command.

| Option | Description |
| ------ | ----------- |
|`vxlan.def_encap_dscp_action`| Sets the VXLAN outer DSCP action during encapsulation. You can specify one of the following options:<br>- `copy` (if the inner packet is IP)<br>- `set` (to a specific value)<br>- `derive` (from the switch priority).<br>The default setting is `derive`. |
| `vxlan.def_encap_dscp_value`| If the `vxlan.def_encap_dscp_action` option is `set`, you must specify a value. |
| `xlan.def_decap_dscp_action` | Sets the VXLAN decapsulation DSCP/COS action. You can specify one of the following options:<br>- `copy` (if the inner packet is IP)<br>- `preserve` (the inner DSCP is unchanged)<br>- `derive` (from the switch priority) |

The following example shows that the VXLAN outer DSCP action during encapsulation is `set` with a value of 16.

```
cumulus@switch:~$ sudo nano /etc/cumulus/switchd.conf
...
# default vxlan outer dscp action during encap
# {copy | set | derive}
# copy: only if inner packet is IP
# set: to specific value
# derive: from switch priority
vxlan.def_encap_dscp_action = set

# default vxlan encap dscp value, only applicable if action is 'set'
vxlan.def_encap_dscp_value = 16

# default vxlan decap dscp/cos action
# {copy | preserve | derive}
# copy: only if inner packet is IP
# preserve: inner dscp unchanged
# derive: from switch priority
#vxlan.def_decap_dscp_action = derive
...
```

You can also set the DSCP operations from the command line. Use the `echo` command to change the settings in the `/etc/cumulus/switchd.conf` file. For example, to change the encapsulation action to `copy`:

```
cumulus@switch:~$ echo "copy" > /cumulus/switchd/config/vxlan/def_encap_dscp_action
```

To change the VXLAN outer DSCP action during encapsulation to `set` with a value of 32:

```
cumulus@switch:~$ echo "32" > /cumulus/switchd/config/vxlan/def_encap_dscp_value
cumulus@switch:~$ echo "set" > /cumulus/switchd/config/vxlan/def_encap_dscp_action
```

## Caveats and Errata

Cumulus Linux supports only the default global settings. Per-VXLAN and per-tunnel granularity are not supported.
