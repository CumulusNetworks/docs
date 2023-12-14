---
title: VXLAN Tunnel DSCP Operations
author: NVIDIA
weight: 625
toc: 3
---
Cumulus Linux provides configuration options to control <span class="a-tooltip">[DSCP](## "Differentiated Services Code Point")</span> operations during VXLAN encapsulation and decapsulation, specifically for solutions that require end-to-end quality of service, such as <span class="a-tooltip">[RDMA](## "Remote Direct Memory Access")</span> over Converged Ethernet.

The configuration options propagate <span class="a-tooltip">[ECN](## "Explicit Congestion Notification")</span> between the underlay and overlay according to {{<exlink url="https://tools.ietf.org/html/rfc6040" text="RFC 6040">}}, which describes how to construct the IP header of an ECN field on both ingress to and egress from an IP-in-IP tunnel.

## Configure DSCP Operations

You can set the following DSCP operations:
- The VXLAN encapsulation DSCP action. The action can be `copy` if the inner packet is IP, `set` to configure a specific value, or `derive` to derive the value from the switch priority. The default setting is `derive`.
- The VXLAN decapsulation DSCP or COS action. The action can be `copy` to copy the DSCP value from the outer packet (underlay), `preserve` to keep the values configured in the inner packet (overlay), or `derive` to derive the value from the switch priority. The default setting is `derive`.

{{< tabs "TabID27 ">}}
{{< tab "NVUE Commands ">}}

The following example sets the VXLAN encapsulation DSCP action to `copy`.

```
cumulus@switch:~$ nv set nve vxlan encapsulation dscp action copy
cumulus@switch:~$ nv config apply
```

The following example sets the VXLAN encapsulation DSCP value to 16.

```
cumulus@switch:~$ nv set nve vxlan encapsulation dscp action set
cumulus@switch:~$ nv set nve vxlan encapsulation dscp value 16
cumulus@switch:~$ nv config apply
```

The following example sets the VXLAN decapsulation DSCP value to `preserve`.

```
cumulus@switch:~$ nv set nve vxlan decapsulation dscp action preserve
cumulus@switch:~$ nv config apply
```

{{< /tab >}}
{{< tab "Linux Commands ">}}

Edit the `/etc/cumulus/switchd.conf` file, then restart `switchd`.

The following example sets the VXLAN encapsulation DSCP action to `copy`.

```
cumulus@switch:~$ sudo nano /etc/cumulus/switchd.conf
...
# vxlan encapsulation update
vxlan.def_encap_dscp_action = copy
# default vxlan encap dscp value, only applicable if action is 'set'
#vxlan.def_encap_dscp_value =

# vxlan decapsulation update
#vxlan.def_decap_dscp_action = derive
```

The following example sets the VXLAN encapsulation DSCP value to 16.

```
cumulus@switch:~$ sudo nano /etc/cumulus/switchd.conf
...
# vxlan encapsulation update
vxlan.def_encap_dscp_action = set
# default vxlan encap dscp value, only applicable if action is 'set'
vxlan.def_encap_dscp_value = 16

# vxlan decapsulation update
#vxlan.def_decap_dscp_action = derive
```

The following example sets the VXLAN decapsulation DSCP value to `preserve`.

```
cumulus@switch:~$ sudo nano /etc/cumulus/switchd.conf
...
# vxlan encapsulation update
#vxlan.def_encap_dscp_action = derive
# default vxlan encap dscp value, only applicable if action is 'set'
#vxlan.def_encap_dscp_value =

# vxlan decapsulation update
vxlan.def_decap_dscp_action = preserve
...
```

After you modify `/etc/cumulus/switchd.conf` file, you must restart `switchd` for the changes to take effect.
<!-- vale off -->
{{<cl/restart-switchd>}}
<!-- vale on -->

{{< /tab >}}
{{< /tabs >}}

## Show the DSCP Setting

To show the VXLAN encapsulation DSCP setting, run the `nv show nve vxlan encapsulation dscp` command:

```
cumulus@switch:~$ nv show nve vxlan encapsulation dscp 
       operational  applied
------  -----------  -------
action  copy         copy
```

To show the VXLAN decapsulation DSCP setting, run the `nv show nve vxlan decapsulation dscp` command.

```
cumulus@switch:~$ nv show nve vxlan decapsulation dscp
        operational  applied
------  -----------  --------
action  preserve     preserve
```

## Considerations

You can only set the VXLAN encapsulation and decapsulation DSCP actions globally. Cumulus Linux does not support per-VXLAN or per-tunnel settings.
