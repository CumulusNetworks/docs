---
title: Domain Name System DNS
author: NVIDIA
weight: 135
toc: 3
---
The Cumulus Linux switch acts as a DNS client. You configure the nameservers the switch queries, the VRF it uses to reach each one, the order in which it tries them, and optionally the source address of the queries themselves.

To configure the domain name of the switch, see {{<link url="Quick-Start-Guide/#configure-the-domain-name" text="Configure the Domain Name">}}.

## DNS Servers

Cumulus Linux supports both DHCP and static DNS entries. You can associate each nameserver with a VRF; the switch adds forwarding information base (FIB) rules that direct lookups for that nameserver address out of the correct VRF.

You cannot specify the same DNS server address twice to associate it with different VRFs.

For the management VRF specific behavior of these rules, see {{<link url="Management-VRF/#management-vrf-and-dns" text="Management VRF and DNS">}}.

To configure a nameserver, run the `nv set system dns server <dns-server-id>` command. To associate the nameserver with a VRF, run the `nv set system dns server <dns-server-id> vrf <vrf-id>` command. The following example configures three nameservers and associates two of them with the management VRF:

{{< tabs "TabID01 ">}}
{{< tab "NVUE Commands ">}}

```
cumulus@switch:~$ nv set system dns server 192.0.2.1 vrf default
cumulus@switch:~$ nv set system dns server 198.51.100.31 vrf mgmt
cumulus@switch:~$ nv set system dns server 203.0.113.13 vrf mgmt
cumulus@switch:~$ nv config apply
```

{{< /tab >}}
{{< tab "Linux Commands ">}}

Edit the `/etc/resolv.conf` file to add the nameservers and associate some of them with the management VRF. For example:

```
cumulus@switch:~$ sudo nano /etc/resolv.conf
nameserver 192.0.2.1
nameserver 198.51.100.31 # vrf mgmt
nameserver 203.0.113.13 # vrf mgmt
```

Run the `ifreload -a` command to load the new configuration:

```
cumulus@switch:~$ ifreload -a
```

{{< /tab >}}
{{< /tabs >}}

To set the order in which the switch tries the nameservers, run the `nv set system dns server <dns-server-id> priority <priority>` command.

## DNS Query Source Address

By default, the kernel selects the source address of a DNS query from the egress interface the route chooses. That address can change when links or routes change, and it differs between routing contexts, so it does not provide the stable identity that management and control plane access control lists (ACLs) on the nameserver expect.

To send DNS queries from an address you choose instead, configure a source on the nameserver. A nameserver with a configured source is a *sourced* nameserver. The switch binds the configured address to the query, so the query leaves the switch with that address as its source. A loopback address is the typical choice because it stays present and unchanged regardless of link and route state, but you can use any routable local address.

You configure the source in one of two ways, which are mutually exclusive on a single nameserver:

- `source-ip` names the address directly.
- `source-interface` names an interface from which the switch selects an address. You can also name an explicit address on that interface.

A nameserver accepts at most one source interface.

{{%notice note%}}
- The source must be an address on the switch, either configured with NVUE or learned through DHCP, and must belong to the same VRF as the nameserver. The switch rejects a source in a different VRF and a leaked route does not change which VRF owns the address.
- The address family of the source and the nameserver must match. An IPv6 nameserver requires an IPv6 source.
- Host-only addresses in the `127.0.0.0/8` range and `::1`, and link-local addresses in the `169.254.0.0/16` and `fe80::/10` ranges, cannot source queries. The switch does not route these addresses off the switch.
- Configuring a source does not create return reachability. You must advertise or install a route so that the nameserver can reach the source address in the same VRF. An unadvertised address times out even when the outbound routing and the source binding are both correct.
- Sourced and unsourced nameservers coexist in the same VRF and keep their configured priority and failover order. A nameserver with no configured source continues to use the kernel-selected source.
- Nameservers that the switch learns through DHCP do not inherit a source. A DHCP refresh can change the global DNS information, and a newly learned nameserver remains unsourced until you configure it with NVUE.
{{%/notice%}}

{{%notice warning%}}
A DNS query does not use the configured source unless the application that sends it runs with the resolver view for that VRF. Running a command under `ip vrf exec` alone is not sufficient, so an interactive session, such as a command you run over SSH, sends unsourced queries. A packet capture taken from such a session shows the kernel-selected egress address instead of the address you configured, even when the configuration is correct. To run a command with the resolver view of a VRF, use `dns-vrf-exec`. See {{<link url="#run-a-command-with-the-configured-source" text="Run a Command with the Configured Source">}}.
{{%/notice%}}

### Configure a Source Address

To send queries to a nameserver from a specific local address, run the `nv set system dns server <dns-server-id> source-ip <source-ip>` command. The following example configures the switch to query the nameserver 192.0.2.1 from the loopback address 10.10.10.1:

```
cumulus@switch:~$ nv set interface lo ip address 10.10.10.1/32
cumulus@switch:~$ nv set system dns server 192.0.2.1 vrf default
cumulus@switch:~$ nv set system dns server 192.0.2.1 source-ip 10.10.10.1
cumulus@switch:~$ nv config apply
```

### Configure a Source Interface

To send queries from an address on a particular interface, run the `nv set system dns server <dns-server-id> source-interface <interface-id>` command. The switch selects one address from that interface, as described in {{<link url="#automatic-address-selection" text="Automatic Address Selection">}}:

```
cumulus@switch:~$ nv set system dns server 192.0.2.1 source-interface lo
cumulus@switch:~$ nv config apply
```

In the default VRF, the source interface is typically `lo`. In the management VRF and in a user-defined VRF, it is typically the VRF device, which carries the loopback address of that VRF.

To use a specific address on the interface instead of the one the switch selects, run the `nv set system dns server <dns-server-id> source-interface <interface-id> address <source-ip>` command:

```
cumulus@switch:~$ nv set system dns server 192.0.2.1 source-interface lo address 10.10.10.2
cumulus@switch:~$ nv config apply
```

The `address` option defaults to `auto`. Automatic selection never replaces an address you configure explicitly.

### Use a DHCP-Learned Address as the Source

You can use an address that an interface learns through DHCP or DHCPv6 as the source, with `source-ip`, with `source-interface`, or with `source-interface <interface-id> address <source-ip>`. The same VRF, address family, and scope rules apply as for a configured address.

The interface must hold the lease when you run `nv config apply`. If the address is not present on the interface at that time, the switch rejects the configuration.

The switch uses the address present when you apply the configuration. It does not track later lease changes. If the lease expires or the DHCP server assigns a different address, including after a reboot, queries to that nameserver fail to bind and fail over to the next nameserver until you update the configuration and run `nv config apply` again. To keep the source stable, configure a DHCP reservation for the interface on the DHCP server, or use a configured address such as a loopback address.

The following example sources queries to 192.0.2.1 from the DHCP-learned address 198.51.100.10 on swp1 in VRF BLUE:

```
cumulus@switch:~$ nv set system dns server 192.0.2.1 vrf BLUE
cumulus@switch:~$ nv set system dns server 192.0.2.1 source-interface swp1 address 198.51.100.10
cumulus@switch:~$ nv config apply
```

### Automatic Address Selection

When you configure a source interface without an explicit address, the switch selects one address from that interface for the address family of the nameserver. It excludes addresses that cannot serve as a query source:
- Host-only addresses in the `127.0.0.0/8` range and `::1`.
- Link-local addresses in the `169.254.0.0/16` and `fe80::/10` ranges.
- Addresses learned through DHCP that fail duplicate address detection.

From the addresses that remain, the switch sorts the interface addresses with the NVUE natural sort, the same order `nv config show` displays and `nv config save` writes, then selects the first one. The order does not depend on the order in which you enter the addresses, so the selection is the same in the running configuration, in the saved configuration, after a reboot, and on any switch with the same set of addresses. A DHCP-learned address can change after a reboot or a lease change. See {{<link url="#use-a-dhcp-learned-address-as-the-source" text="Use a DHCP-Learned Address as the Source">}}.

The switch selects from the addresses in the NVUE configuration for the interface first. If none of them is usable for the address family of the nameserver, the switch selects from the addresses the interface learned through DHCP, sorted in the same way. A configured address always takes precedence over a learned one.

In the following example, the switch selects 10.10.10.2 even though you configure 10.10.10.10 first, because the natural sort orders 10.10.10.2 ahead of 10.10.10.10:

```
cumulus@switch:~$ nv set interface lo ip address 10.10.10.10/32
cumulus@switch:~$ nv set interface lo ip address 10.10.10.2/32
cumulus@switch:~$ nv set system dns server 192.0.2.1 source-interface lo
cumulus@switch:~$ nv config apply
```

<!-- TODO: capture the `nv show system dns server <dns-server-id> source-interface <interface-id>` output below on a switch and replace this adapted sample -->

To confirm which address the switch selected, run the `nv show system dns server <dns-server-id> source-interface <interface-id>` command:

```
cumulus@switch:~$ nv show system dns server 192.0.2.1 source-interface lo
              operational   applied
------------  ------------  -------
address       10.10.10.2    auto
```

If no address on the interface survives the exclusions, the switch rejects the configuration when you run `nv config apply` and the previously applied configuration remains in effect. For example, an interface that has only an IPv4 address cannot source queries to an IPv6 nameserver.

### Remove a Source

To remove a source address, run the `nv unset system dns server <dns-server-id> source-ip` command.

To remove a source interface, run the `nv unset system dns server <dns-server-id> source-interface` command.

To remove only the explicit address and return the interface to automatic selection, run the `nv unset system dns server <dns-server-id> source-interface <interface-id> address` command. The source interface remains configured.

{{%notice note%}}
A command that deletes an address a nameserver uses as its source stages successfully, but the apply fails. The error names both the address and the nameserver using it, and the address remains on the switch. To remove the address, remove or repoint the DNS source in the same `nv config apply`; NVUE evaluates the final state rather than the individual commands.

This protection covers changes you make with NVUE. If something outside NVUE deletes the address, or a DHCP lease for the address expires or changes, queries to that nameserver fail to bind and fail over to the next nameserver.
{{%/notice%}}

### Show the DNS Configuration

To show the DNS configuration, run the `nv show system dns` command. To list the configured nameservers, run the `nv show system dns server` command. To show a single nameserver, including its configured source, run the `nv show system dns server <dns-server-id>` command.

For a nameserver that uses a source interface, {{<link url="#automatic-address-selection" text="Automatic Address Selection">}} shows how the output distinguishes the address you configured from the address the switch selected.

### Run a Command with the Configured Source

When a VRF has at least one sourced nameserver, the switch installs the `dns-vrf-exec` command. It runs a command in that VRF with the VRF's resolver view, so the command's DNS queries leave the switch from the configured source address.

`dns-vrf-exec` is not on the default path, so run it with its full path:

```
/usr/lib/cumulus/dns/dns-vrf-exec <vrf> <command> [args...]
```

The following example resolves a name through the sourced nameservers of the default VRF, and then fetches a URL through those of the management VRF:

```
cumulus@switch:~$ /usr/lib/cumulus/dns/dns-vrf-exec default getent hosts example.com
cumulus@switch:~$ /usr/lib/cumulus/dns/dns-vrf-exec mgmt curl https://example.com
```

- The command runs as root. If you are not root, `dns-vrf-exec` runs the command with `sudo`, so you need sudo privileges.
- The resolver view applies only to the command and the processes it starts. Other processes on the switch are not affected.
- You can run a command in the default VRF from a session in the management VRF.
- If the VRF has no sourced nameserver, the command fails with `dns-vrf-exec: VRF <vrf> has no source-selected DNS server`.
- NVUE manages this file. It overwrites local changes whenever you apply a DNS configuration, and removes the file when you remove the last sourced nameserver.

## Considerations

- Source selection applies to DNS queries only.
- An application that names a nameserver directly, such as `dig @192.0.2.1`, bypasses the resolver configuration and does not use the configured source.
- The switch remains a DNS client. The configuration does not make the switch a DNS server for other devices.
