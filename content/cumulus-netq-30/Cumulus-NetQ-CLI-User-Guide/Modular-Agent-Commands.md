---
title: Modular NetQ Agent Commands
author: Cumulus Networks
weight: 595
toc: 3
---

The NetQ Agent contains a pre-configured set of modular commands that run periodically and send event and resource data to the NetQ appliance or VM. You can fine tune which events the agent can poll and vary frequency of polling.

For example, if your network is not running OSPF, you can disable the command that polls for OSPF events. Or you can decrease the polling interval for LLDP from the default of 60 seconds to 120 seconds. This way you can reduce agent CPU usage due to less frequent polling.

In addition, depending on the switch platform, some supported protocol commands may not be executed by the agent. For example, if a switch has no VXLAN capability, then all VXLAN-related commands get skipped by agent.

You cannot create new commands in this release.

## Supported Commands

To see the list of supported modular commands, run:

```
cumulus@switch:~$ netq config show agent commands
 Service Key               Period  Active       Command
-----------------------  --------  --------  ---------------------------------------------------------------------
bgp-neighbors                  60  yes       ['/usr/bin/vtysh', '-c', 'show ip bgp vrf all neighbors json']
evpn-vni                       60  yes       ['/usr/bin/vtysh', '-c', 'show bgp l2vpn evpn vni json']
lldp-json                     120  yes       /usr/sbin/lldpctl -f json
clagctl-json                   60  yes       /usr/bin/clagctl -j
dpkg-query                  21600  yes       dpkg-query --show -f ${Package},${Version},${Status}\n
ptmctl-json                   120  yes       ptmctl
mstpctl-bridge-json            60  yes       /sbin/mstpctl showall json
cl-license                  21600  yes       /usr/sbin/switchd -lic
ports                        3600  yes       Netq Predefined Command
proc-net-dev                   30  yes       Netq Predefined Command
agent_stats                   300  yes       Netq Predefined Command
agent_util_stats               30  yes       Netq Predefined Command
tcam-resource-json            120  yes       /usr/cumulus/bin/cl-resource-query -j
btrfs-json                   1800  yes       /sbin/btrfs fi usage -b /
config-mon-json               120  yes       Netq Predefined Command
running-config-mon-json        30  yes       Netq Predefined Command
cl-support-json               180  yes       Netq Predefined Command
resource-util-json            120  yes       findmnt / -n -o FS-OPTIONS
smonctl-json                   30  yes       /usr/sbin/smonctl -j
sensors-json                   30  yes       sensors -u
ssd-util-json               86400  yes       sudo /usr/sbin/smartctl -a /dev/sda
ospf-neighbor-json             60  yes       ['/usr/bin/vtysh', '-c', 'show ip ospf vrf all neighbor detail json']
ospf-interface-json            60  yes       ['/usr/bin/vtysh', '-c', 'show ip ospf vrf all interface json']
```

The NetQ predefined commands are described as follows:

- **agent_stats**: Collects the NetQ agent's statistics every 5 minutes.
- **agent_util_stats**: Collects the NetQ agent's CPU and memory utilization every 30 seconds.
- **cl-support-json**: Polls the switch every 3 minutes to determine if a `cl-support` file was generated.
- **config-mon-json**: Polls the `/etc/network/interfaces`, `/etc/frr/frr.conf`, `/etc/lldpd.d/README.conf` and `/etc/ptm.d/topology.dot` files every 2 minutes looking to see if the contents of any of these files changes. If a change occurs, the contents of the file and its modification time are transmitted to the NetQ appliance or VM.
- **ports**: Polls for optics plugged into the switch every hour.
- **proc-net-dev**: Polls for network statistics on the switch every 30 seconds.
- **running-config-mon-json**: Polls the `clagctl` parameters every 30 seconds and sends a diff of any changes to the NetQ appliance or VM.

## Modify the Polling Frequency

You can change the polling frequency of a modular command. The frequency is specified in seconds. For example, to change the polling frequency of the `lldp-json` command to 60 seconds, run:

```
cumulus@switch:~$ netq config add agent command service-key lldp-json poll-period 60
Successfully added/modified Command service lldpd command /usr/sbin/lldpctl -f json

cumulus@switch:~$ netq config show agent commands
 Service Key               Period  Active       Command
-----------------------  --------  --------  ---------------------------------------------------------------------
bgp-neighbors                  60  yes       ['/usr/bin/vtysh', '-c', 'show ip bgp vrf all neighbors json']
evpn-vni                       60  yes       ['/usr/bin/vtysh', '-c', 'show bgp l2vpn evpn vni json']
lldp-json                      60  yes       /usr/sbin/lldpctl -f json
clagctl-json                   60  yes       /usr/bin/clagctl -j
dpkg-query                  21600  yes       dpkg-query --show -f ${Package},${Version},${Status}\n
ptmctl-json                   120  yes       /usr/bin/ptmctl -d -j
mstpctl-bridge-json            60  yes       /sbin/mstpctl showall json
cl-license                  21600  yes       /usr/sbin/switchd -lic
ports                        3600  yes       Netq Predefined Command
proc-net-dev                   30  yes       Netq Predefined Command
agent_stats                   300  yes       Netq Predefined Command
agent_util_stats               30  yes       Netq Predefined Command
tcam-resource-json            120  yes       /usr/cumulus/bin/cl-resource-query -j
btrfs-json                   1800  yes       /sbin/btrfs fi usage -b /
config-mon-json               120  yes       Netq Predefined Command
running-config-mon-json        30  yes       Netq Predefined Command
cl-support-json               180  yes       Netq Predefined Command
resource-util-json            120  yes       findmnt / -n -o FS-OPTIONS
smonctl-json                   30  yes       /usr/sbin/smonctl -j
sensors-json                   30  yes       sensors -u
ssd-util-json               86400  yes       sudo /usr/sbin/smartctl -a /dev/sda
ospf-neighbor-json             60  no        ['/usr/bin/vtysh', '-c', 'show ip ospf vrf all neighbor detail json']
ospf-interface-json            60  no        ['/usr/bin/vtysh', '-c', 'show ip ospf vrf all interface json']
```

## Disable a Command

You can disable any of these commands if they are not needed on your network. This can help reduce the compute resources the agent consumes. For example, if your network does not run OSPF, you can disable the two OSPF commands:

```
cumulus@switch:~$ netq config add agent command service-key ospf-interface-json enable False
Command Service ospf-interface-json is disabled
cumulus@switch:~$ netq config add agent command service-key ospf-neighbor-json enable False
Command Service ospf-neighbor-json is disabled
cumulus@switch:~$ netq config show agent commands
 Service Key               Period  Active       Command
-----------------------  --------  --------  ---------------------------------------------------------------------
bgp-neighbors                  60  yes       ['/usr/bin/vtysh', '-c', 'show ip bgp vrf all neighbors json']
evpn-vni                       60  yes       ['/usr/bin/vtysh', '-c', 'show bgp l2vpn evpn vni json']
lldp-json                      60  yes       /usr/sbin/lldpctl -f json
clagctl-json                   60  yes       /usr/bin/clagctl -j
dpkg-query                  21600  yes       dpkg-query --show -f ${Package},${Version},${Status}\n
ptmctl-json                   120  yes       /usr/bin/ptmctl -d -j
mstpctl-bridge-json            60  yes       /sbin/mstpctl showall json
cl-license                  21600  yes       /usr/sbin/switchd -lic
ports                        3600  yes       Netq Predefined Command
proc-net-dev                   30  yes       Netq Predefined Command
agent_stats                   300  yes       Netq Predefined Command
agent_util_stats               30  yes       Netq Predefined Command
tcam-resource-json            120  yes       /usr/cumulus/bin/cl-resource-query -j
btrfs-json                   1800  yes       /sbin/btrfs fi usage -b /
config-mon-json               120  yes       Netq Predefined Command
running-config-mon-json        30  yes       Netq Predefined Command
cl-support-json               180  yes       Netq Predefined Command
resource-util-json            120  yes       findmnt / -n -o FS-OPTIONS
smonctl-json                   30  yes       /usr/sbin/smonctl -j
sensors-json                   30  yes       sensors -u
ssd-util-json               86400  yes       sudo /usr/sbin/smartctl -a /dev/sda
ospf-neighbor-json             60  no        ['/usr/bin/vtysh', '-c', 'show ip ospf vrf all neighbor detail json']
ospf-interface-json            60  no        ['/usr/bin/vtysh', '-c', 'show ip ospf vrf all interface json']
```

## Reset to Default

To quickly revert to the original command settings, run `netq config agent factory-reset commands`:

```
cumulus@switch:~$ netq config agent factory-reset commands
Netq Command factory reset successfull
cumulus@switch:~$ netq config show agent commands
 Service Key               Period  Active       Command
-----------------------  --------  --------  ---------------------------------------------------------------------
bgp-neighbors                  60  yes       ['/usr/bin/vtysh', '-c', 'show ip bgp vrf all neighbors json']
evpn-vni                       60  yes       ['/usr/bin/vtysh', '-c', 'show bgp l2vpn evpn vni json']
lldp-json                     120  yes       /usr/sbin/lldpctl -f json
clagctl-json                   60  yes       /usr/bin/clagctl -j
dpkg-query                  21600  yes       dpkg-query --show -f ${Package},${Version},${Status}\n
ptmctl-json                   120  yes       /usr/bin/ptmctl -d -j
mstpctl-bridge-json            60  yes       /sbin/mstpctl showall json
cl-license                  21600  yes       /usr/sbin/switchd -lic
ports                        3600  yes       Netq Predefined Command
proc-net-dev                   30  yes       Netq Predefined Command
agent_stats                   300  yes       Netq Predefined Command
agent_util_stats               30  yes       Netq Predefined Command
tcam-resource-json            120  yes       /usr/cumulus/bin/cl-resource-query -j
btrfs-json                   1800  yes       /sbin/btrfs fi usage -b /
config-mon-json               120  yes       Netq Predefined Command
running-config-mon-json        30  yes       Netq Predefined Command
cl-support-json               180  yes       Netq Predefined Command
resource-util-json            120  yes       findmnt / -n -o FS-OPTIONS
smonctl-json                   30  yes       /usr/sbin/smonctl -j
sensors-json                   30  yes       sensors -u
ssd-util-json               86400  yes       sudo /usr/sbin/smartctl -a /dev/sda
ospf-neighbor-json             60  yes       ['/usr/bin/vtysh', '-c', 'show ip ospf vrf all neighbor detail json']
ospf-interface-json            60  yes       ['/usr/bin/vtysh', '-c', 'show ip ospf vrf all interface json']
```
