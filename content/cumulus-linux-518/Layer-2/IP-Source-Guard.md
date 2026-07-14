---
title: IP Source Guard
author: NVIDIA
weight: 475
toc: 3
---
IP Source Guard is a layer 2 security feature that prevents IP address spoofing on untrusted interfaces. The `dhcpsnoop` daemon filters ingress frames based on a validated binding table; the switch forwards traffic ingressing a port with IP Source Guard enabled only if its source MAC and source IP address match an authorized entry.

{{%notice note%}}
Before you enable IP Source Guard on an interface, you must configure {{<link url="DHCP-Snooping" text="DHCP snooping">}} for the bridge VLAN.
{{%/notice%}}

To enable IP Source Guard on an interface, run the `nv set interface <interface-id> security ip-source-guard enabled` command.

The following example enables IP Source Guard on swp1 and swp5, swp6, and swp7:

```
cumulus@switch:~$ nv set interface swp1 security ip-source-guard enabled
cumulus@switch:~$ nv set interface swp5-7 security ip-source-guard enabled
cumulus@switch:~$ nv config apply
```

To disable IP Source Guard on an interface, run the `nv set interface <interface-id> security ip-source-guard disabled` command.

To show the IP Source Guard configuration and operational status for an interface, run the `nv show interface <interface-id> security` command.

```
cumulus@switch:~$ nv show interface swp1 security
                 operational  applied
---------------  -----------  -------
ip-source-guard  enabled      enabled
```

