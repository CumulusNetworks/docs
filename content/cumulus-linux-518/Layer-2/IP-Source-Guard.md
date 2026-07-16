---
title: IP Source Guard
author: NVIDIA
weight: 475
toc: 3
---
IP Source Guard is a layer 2 security feature that prevents IP address spoofing on untrusted interfaces. The `dhcpsnoop` daemon filters ingress frames based on a validated binding table; the switch forwards traffic that ingresses a port with IP Source Guard enabled only if its source MAC and source IP address match an authorized entry.

{{%notice note%}}
Before you enable IP Source Guard on an interface, you must configure {{<link url="DHCP-Snooping" text="DHCP snooping">}} for the bridge VLAN.
{{%/notice%}}

To enable IP Source Guard on an interface, run the `nv set interface <interface-id> security ip-source-guard enabled` command. The following example enables IP Source Guard on swp1:

```
cumulus@switch:~$ nv set interface swp1 security ip-source-guard enabled
cumulus@switch:~$ nv config apply
```

You can specify a range of interfaces; for example `nv set interface swp5-9 security ip-source-guard enabled`.

To disable IP Source Guard on an interface, run the `nv set interface <interface-id> security ip-source-guard disabled` command.

To show the IP Source Guard configuration and operational status for an interface, run the `nv show interface <interface-id> security` command.

```
cumulus@switch:~$ nv show interface swp1 security
                 operational  applied
---------------  -----------  -------
ip-source-guard  enabled      enabled
```

{{%notice note%}}
Cumulus Linux does not support static (manually pinned) IP source guard bindings but enforces only the dynamic bindings learned by DHCP snooping. A host that never obtains its address through DHCP has no binding and the switch drops its traffic on a port with IP source guard enabled.

To allow a host that uses a static IP address on a port with IP source guard enabled, either:
- Mark the port as trusted for DHCP snooping with the `nv set bridge domain <bridge-id> dhcp-snoop vlan <vlan-id> trust <interface-id>` command. Trusted ports are exempt from IP source guard so a statically addressed server or uplink on that port forwards normally.
- Configure an ACL that permits the source IP address and MAC address of the host on the ingress interface when you need to allow a static host without trusting the whole port.
{{%/notice%}}

## Validate IP Source Guard

IP source guard enforces the DHCP snooping binding table. To validate IP source guard, confirm that bindings are learned and that only bound sources forward traffic. No traffic spoofing is required.

To confirm that bindings are learned, have the client obtain an address over DHCP, then run the `nv show bridge domain <bridge-id> dhcp-snoop vlan <vlan-id> bind` command for IPv4 or the `nv show bridge domain <bridge-id> dhcp-snoop6 vlan <vlan-id> bind`. The binding is the allow-entry that IP source guard enforces for that host.

```
cumulus@switch:~$ nv show bridge domain br_default dhcp-snoop vlan 100 bind
Interface  IP address   MAC                State    Lease
---------  -----------  -----------------  -------  -----
swp1       10.1.1.50    00:02:00:00:00:01  DHCPACK  3542
```

To confirm that the bound client forwards traffic normally, send traffic from the client, (ping its gateway or another host). Traffic is forwarded if the source IP address and MAC address match the learned binding.

To confirm an unauthorized source is blocked, connect a host to the same untrusted port and give it a static IP address without obtaining a DHCP lease. Because it has no binding, its traffic is dropped; the host regains connectivity only after it completes DHCP and a binding is installed. This demonstrates enforcement using an unleased source; no address spoofing is required.