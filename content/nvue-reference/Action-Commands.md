---
title: Action Commands
author: Cumulus Networks
weight: 55

type: nojsscroll
---
<style>
h { color: RGB(118,185,0)}
</style>
<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv action

Resets counters for interfaces, BGP, QoS buffers and pools, removes conflicts from protodown MLAG bonds, and disconnects system users.

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show action</h>

Shows the action jobs.

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@switch:~$ nv show action
'1':
  detail: acl counters cleared.
  http_status: 200
  issue: []
  percentage: ''
  state: action_success
  status: acl counters cleared.
  timeout: 60
  type: ''
'2':
  detail: Local Time is now Wed 2024-05-29 09:47:30 UTC
  http_status: 200
  issue: []
  percentage: ''
  state: action_success
  status: Local Time is now Wed 2024-05-29 09:47:30 UTC
  timeout: 60
  type: ''
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show action \<action-job-id\></h>

Shows information about the specified action.

### Command Syntax

| Syntax   |  Description  |
| ----------    | ------------  |
| `<action-job-id>` | The action ID. |

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@switch:~$ nv show action 3
detail: acl counters cleared.
http_status: 200
issue: []
state: action_success
status: acl counters cleared.
timeout: 60
type: ''
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv action abort system ztp</h>

Terminates ZTP if it is in the discovery process or is not currently running a script.

### Version History

Introduced in Cumulus Linux 5.11.0

### Example

```
cumulus@switch:~$ nv action abort system ztp
```

If you add the `force` option (`nv action abort system ztp force`), ZTP terminates without prompting you for confirmation.

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv action boot-next system image \<partition-id\> rollback</h>

Rolls back the optimized image upgrade if the upgrade fails or you want to go back to the Cumulus Linux release from which you upgraded.  The switch boots back to the previous release image and restores the switch configuration.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<partition-id>`| The name of the partition, such as `other`. |

### Version History

Introduced in Cumulus Linux 5.12.0

### Example

```
cumulus@switch:~$ nv action boot-next system image partition2 rollback
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv action cancel system telemetry hft job \<job-id\> profile \<profile-id\></h>

Cancels a specific or all high frequency telemetry data collection jobs, or a specific or all jobs for a high frequency telemetry profile. You can specify a job ID or `all` to cancel all jobs.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<job-id>`| The high frequency telemetry data collection job ID or `all`. To see the list of job IDs, run the `nv show system telemetry hft job` command. |
| `<profile-id>` |  The name of the profile. High frequency telemetry uses profiles for data collection. A profile is a set of configurations. Cumulus Linux provides a default profile called `standard`. You can create a maximum of four new profiles (four profiles in addition to the default profile).|

### Version History

Introduced in Cumulus Linux 5.10.0

### Example

```
cumulus@switch:~$ nv action cancel system telemetry hft job 6 profile profile1
Action executing ...
Action succeeded
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv action change system time</h>

Configures the Cumulus Linux software clock. The switch contains a battery backed hardware clock that maintains the date and time while the switch powers off and between reboots. When the switch is running, the Cumulus Linux operating system maintains its own software clock.

During boot up, the switch copies the date and time from the hardware clock to the operating system software clock. The software clock takes care of all the timekeeping. During system shutdown, the switch copies the software clock back to the battery backed hardware clock.

The format is YYYY-MM-DD HH:MM:SS

### Version History

Introduced in Cumulus Linux 5.10.0

### Example

```
cumulus@switch:~$ nv action change system time 2023-12-04 02:33:30
System Date-time changed successfully
Local Time is now Mon 2023-12-04 02:33:30 UTC
Action succeeded
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv action clear system aaa authentication restrictions</h>

Clears the restriction state for all users that are locked out.

### Version History

Introduced in Cumulus Linux 5.15.0

### Example

```
cumulus@switch:~$ nv action clear system aaa authentication restrictions
Action executing ...
Clearing restrictions for all users
Action executing ...
Successfully cleared all users
Action succeeded
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv action clear system aaa authentication restrictions user \<user-id\></h>

Clears the restriction state for a user that is locked out.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<user-id>` |  The user name.|

### Version History

Introduced in Cumulus Linux 5.15.0

### Example

```
cumulus@switch:~$ nv action clear system aaa authentication restrictions user USER1
Action executing ...
Clearing restrictions for user USER1
Action executing ...
Successfully cleared user name USER1
Action succeeded
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv action clear acl counters</h>

Clears all ACL counters.

### Version History

Introduced in Cumulus Linux 5.6.0

### Example

```
cumulus@switch:~$ nv action clear acl counters
acl counters cleared.
Action succeeded
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv action clear bridge domain \<bridge-id\> mac-table dynamic</h>

Clears all dynamic MAC addresses from the forwarding database.

{{%notice note%}}
This command clears static entries learned on ES bonds that are installed as static entries in EVPN multihoming including static VXLAN entries in the bridge driver.
{{%/notice%}}

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<bridge-id>` |  The bridge name.|

### Version History

Introduced in Cumulus Linux 5.12.0

### Example

```
cumulus@switch:~$ nv action clear bridge domain br_default mac-table dynamic
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv action clear bridge domain \<bridge-id\> mac-table dynamic interface \<interface-id\></h>

Clears all dynamic MAC addresses for a specific interface from the forwarding database.

{{%notice note%}}
This command does not clear sticky entries, permanent entries, and EVPN MAC entries.
{{%/notice%}}

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<bridge-id>` |  The bridge name.|
| `<interface-id>` |  The IP address or interface name.|

### Version History

Introduced in Cumulus Linux 5.12.0

### Example

```
cumulus@switch:~$ nv action clear bridge domain br_default mac-table dynamic interface swp1
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv action clear bridge domain \<bridge-id\> mac-table dynamic interface \<interface-id\> vlan \<vlan-id\></h>

Clears all dynamic MAC addresses for a specific interface and VLAN from the forwarding database.

{{%notice note%}}
This command does not clear sticky entries, permanent entries, and EVPN MAC entries.
{{%/notice%}}

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<bridge-id>` |  The bridge name.|
| `<interface-id>` |  The IP address or interface name.|
| `<vlan-id>` |  The VLAN ID.|

### Version History

Introduced in Cumulus Linux 5.12.0

### Example

```
cumulus@switch:~$ nv action clear bridge domain br_default mac-table dynamic interface swp1 vlan 10
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv action clear bridge domain \<bridge-id\> mac-table dynamic mac \<mac-address\> interface \<interface-id\></h>

Clears a specific dynamic MAC address for an interface from the forwarding database.

{{%notice note%}}
This command does not clear sticky entries, permanent entries, and EVPN MAC entries.
{{%/notice%}}

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<bridge-id>` |  The bridge name.|
| `<mac-address>` |  The MAC address.|
| `<interface-id>` |  The IP address or interface name.|

### Version History

Introduced in Cumulus Linux 5.12.0

### Example

```
cumulus@switch:~$ nv action clear bridge domain br_default mac-table dynamic mac 00:00:0A:BB:28:FC interface swp1
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv action clear bridge domain \<bridge-id\> mac-table dynamic mac \<mac-address\> vlan \<vlan-id\></h>

Clears a specific dynamic MAC addresses for a VLAN from the forwarding database.

{{%notice note%}}
This command does not clear sticky entries, permanent entries, and EVPN MAC entries.
{{%/notice%}}

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<bridge-id>` |  The bridge name.|
| `<mac-address>` |  The MAC address.|
| `<vlan-id>` |  The VLAN ID.|

### Version History

Introduced in Cumulus Linux 5.12.0

### Example

```
cumulus@switch:~$ nv action clear bridge domain br_default mac-table dynamic mac 00:00:0A:BB:28:FC vlan 10
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv action clear bridge domain \<bridge-id\> mac-table dynamic mac \<mac-address\> vlan \<vlan-id\> interface \<interface-id\></h>

Clears a specific dynamic MAC address for a VLAN and interface from the forwarding database.

{{%notice note%}}
This command does not clear sticky entries, permanent entries, and EVPN MAC entries.
{{%/notice%}}

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<bridge-id>` |  The bridge name.|
| `<mac-address>` |  The MAC address.|
| `<VLAN-id>` |  The VLAN ID.|

### Version History

Introduced in Cumulus Linux 5.12.0

### Example

```
cumulus@switch:~$ nv action clear bridge domain br_default mac-table dynamic mac 00:00:0A:BB:28:FC vlan 10 interface swp1
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv action clear bridge domain \<bridge-id\> mac-table dynamic vlan \<vlan-id\></h>

Clears all dynamic MAC addresses for a specific VLAN from the forwarding database.

{{%notice note%}}
This command does not clear sticky entries, permanent entries, and EVPN MAC entries.
{{%/notice%}}

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<bridge-id>` |  The bridge name.|
| `<VLAN-id>` |  The VLAN ID.|

### Version History

Introduced in Cumulus Linux 5.12.0

### Example

```
cumulus@switch:~$ nv action clear bridge domain br_default mac-table dynamic vlan 10
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv action clear evpn vni</h>

Clears duplicate addresses for all VNIs.

### Version History

Introduced in Cumulus Linux 5.6.0

### Example

```
cumulus@switch:~$ nv action clear evpn vni
Action succeeded
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv action clear evpn vni \<vni-id\></h>

Clears duplicate addresses for the specified VNI.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vni-id>` |  The VNI ID.|

### Version History

Introduced in Cumulus Linux 5.6.0

### Example

```
cumulus@switch:~$ nv action clear evpn vni 10
Action succeeded
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv action clear evpn vni \<vni-id\> host \<host-id\></h>

Clears the duplicate host address for the specified VNI.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vni-id>` |  The VNI ID.|
| `<host-id>` | The IP address of the host. |

### Version History

Introduced in Cumulus Linux 5.6.0

### Example

```
cumulus@switch:~$ nv action clear evpn vni 10 host 10.0.0.9
Action succeeded
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv action clear evpn vni \<vni\> mac \<mac-address\></h>

Clears the duplicate MAC address for the specified VNI.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vni-id>` |  The VNI ID.|
| `<mac-address>` | The MAC address you want to clear. |

### Version History

Introduced in Cumulus Linux 5.6.0

### Example

```
cumulus@switch:~$ nv action clear evpn vni 10 mac 00:e0:ec:20:12:62
Action succeeded
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv action clear interface counters</h>

Clears all interface-specific counters from all interfaces. Interface counters provide information about an interface, such as the number of packets intentionally or intentionally dropped, the number of inbound and outbound packets discarded (even if the switch detected no errors), the number of inbound and outbound packets not transmitted because of errors, and so on.

This command does not clear counters in the kernel or hardware.

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv action clear interface counters
all interface counters cleared.
Action succeeded
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv action clear interface \<interface\> bond mlag lacp-conflict</h>

Clears the MLAG LACP conflict on the specified interface bond. A conflict can be an LACP partner MAC address mismatch or a duplicate LACP partner MAC address.

### Command Syntax

| Syntax   |  Description  |
| ----------    | ------------  |
| `<interface-id>` | The interface that has an LACP conflict. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv action clear interface swp1 bond mlag lacp-conflict
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv action clear interface \<interface-id\> bridge domain \<domain-id\> stp bpduguardviolation</h>

Clears the BPDU guard violation from the specified interface and recovers the interface from the `protodown` state.

### Command Syntax

| Syntax   |  Description  |
| ----------    | ------------  |
| `<interface-id>` | The interface on which you want to clear the BPDU guard violation. |

### Version History

Introduced in Cumulus Linux 5.7.0

### Example

```
cumulus@switch:~$ nv action clear interface swp1 bridge domain br_default stp bpduguardviolation
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv action clear interface \<interface\> counters</h>

Clears all interface-specific counters from the specified interface. Interface counters provide information about an interface, such as the number of packets intentionally or intentionally dropped, the number of inbound and outbound packets discarded even though the switch detected no errors, the number of inbound and outbound packets not transmitted because of errors, and so on.

{{%notice note%}}
This command does not clear counters in the kernel or hardware.
{{%/notice%}}

### Command Syntax

| Syntax   |  Description  |
| ----------    | ------------  |
| `<interface-id>` | The interface on which you want to clear counters. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv action clear interface swp1 counters
swp1 counters cleared.
Action succeeded
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv action clear interface \<interface-id\> counters ptp</h>

Clears PTP counters on the specified interface.

### Command Syntax

| Syntax   |  Description  |
| ----------    | ------------  |
| `<interface-id>` | The interface on which you want to clear PTP counters. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv action clear interface swp1 counters ptp
Action succeeded
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv action clear interface \<interface-id\> counters synce</h>

Clears SyncE counters on the specified interface.

{{%notice note%}}
In Cumulus Linux 5.6 and earlier, this command is `nv action clear interface <interface-id> synce counters`.
{{%/notice%}}

### Command Syntax

| Syntax   |  Description  |
| ----------    | ------------  |
| `<interface-id>` | The interface on which you want to clear SyncE counters. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv action clear interface swp1 counters synce
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv action clear interface \<interface-id\> link flap-protection violation</h>

Clears the `protodown` state of the interface and brings the interface back up.

{{%notice note%}}
In Cumulus Linux 5.8 and earlier, this command is `nv action clear interface <interface-id> link protodown link-flap`.
{{%/notice%}}

### Command Syntax

| Syntax   |  Description  |
| ----------    | ------------  |
| `<interface-id>` | The interface on which you want to clear the `protodown` state. |

### Version History

Introduced in Cumulus Linux 5.9.0

### Example

```
cumulus@switch:~$ nv action clear interface swp1 link flap-protection violation
link-flap state cleared on swp1.
Action succeeded
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv action clear interface \<interface-id\> link phy health</h>

Clears interface physical layer error counters.

{{%notice note%}}
In Cumulus Linux 5.14, this command is `nv action clear interface <interface-id> link phy-detail`.
{{%/notice%}}

### Command Syntax

| Syntax   |  Description  |
| ----------    | ------------  |
| `<interface-id>` | The interface name. |

### Version History

Introduced in Cumulus Linux 5.15.0

### Example

```
cumulus@switch:~$ nv action clear interface swp1 link phy health
Action executing ... 
swp1 link phy-detail counters cleared. 
Action succeeded
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv action clear interface \<interface-id\> qos buffer</h>

Clears QoS buffer counters on the specified interface.

### Command Syntax

| Syntax   |  Description  |
| ----------    | ------------  |
| `<interface-id>` | The interface on which you want to clear the QoS buffer. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv action clear interface swp1 qos buffer
Action succeeded
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv action clear interface \<interface-id\> qos pfc-watchdog deadlock-count</h>

Clears the QoS PFC watchdog deadlock count on the specified interface. PFC watchdog detects and mitigates pause storms on ports where you enable PFC or link pause.

### Command Syntax

| Syntax   |  Description  |
| ----------    | ------------  |
| `<interface-id>` | The interface on which you want to clear the PFC watchdog deadlock count. |

### Version History

Introduced in Cumulus Linux 5.6.0

### Example

```
cumulus@switch:~$ nv action clear interface swp1 qos pfc-watchdog deadlock-count
Action succeeded
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv action clear interface \<interface-id\> qos roce counters</h>

Clears QoS RoCE counters on the specified interface.

### Command Syntax

| Syntax   |  Description  |
| ----------    | ------------  |
| `<interface-id>` | The interface on which you want to clear RoCE counters. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv action clear interface swp1 qos roce counters
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv action clear mlag lacp-conflict</h>

Clears the MLAG LACP conflict. A conflict can be an LACP partner MAC address mismatch or a duplicate LACP partner MAC address.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv action clear mlag lacp-conflict 
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv action clear qos buffer multicast-switch-priority</h>

Clears the QoS multicast switch priority buffers.

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@switch:~$ nv action clear qos buffer multicast-switch-priority 
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv action clear qos buffer pool</h>

Clears the QoS pool buffers.

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@switch:~$ nv action clear qos buffer pool 
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv action clear router bgp</h>

Clears BGP sessions with all neighbors.

### Version History

Introduced in Cumulus Linux 5.6.0

### Example

```
cumulus@switch:~$ nv action clear router bgp
Action succeeded
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv action clear router bgp in prefix-filter</h>

Clears and refreshes inbound routes for all neighbors, address families, and VRFs and refreshes the outbound route filtering prefix list.

### Version History

Introduced in Cumulus Linux 5.6.0

### Example

```
cumulus@switch:~$ nv action clear router bgp in prefix-filter
Action succeeded
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv action clear router bgp soft</h>

Clears all routes with all neighbors, address families, and VRFs.

### Version History

Introduced in Cumulus Linux 5.6.0

### Example

```
cumulus@switch:~$ nv action clear router bgp soft
Action succeeded
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv action clear router bgp soft in</h>

Clears and refreshes all inbound routes with all neighbors, address families, and VRFs.

### Version History

Introduced in Cumulus Linux 5.6.0

### Example

```
cumulus@switch:~$ nv action clear router bgp soft in
Action succeeded
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv action clear router bgp soft out</h>

Clears and resends all outbound routes with all neighbors, address families, and VRFs.

### Version History

Introduced in Cumulus Linux 5.6.0

### Example

```
cumulus@switch:~$ nv action clear router bgp soft out
Action succeeded
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv action clear router bgp out</h>

Clears and refreshes outbound routes for all neighbors, address families, and VRFs.

### Version History

Introduced in Cumulus Linux 5.6.0

### Example

```
cumulus@switch:~$ nv action clear router bgp out
Action succeeded
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv action clear router igmp interfaces</h>

Clears the IGMP interface state.

### Version History

Introduced in Cumulus Linux 5.6.0

### Example

```
cumulus@switch:~$ nv action clear router igmp interfaces
Action succeeded
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv action clear router policy prefix-list</h>

Clears all IP prefix list statistics.

### Version History

Introduced in Cumulus Linux 5.6.0

### Example

```
cumulus@switch:~$ nv action clear router policy prefix-list
Action succeeded
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv action clear router policy prefix-list \<prefix-list-id\></h>

Clears statistics for the specified prefix list.

### Command Syntax

| Syntax   |  Description  |
| ----------    | ------------  |
| `<prefix-list-id>` | The name of the prefix list whose statistics you want to clear. |

### Version History

Introduced in Cumulus Linux 5.6.0

### Example

```
cumulus@switch:~$ nv action clear router policy prefix-list prefixlist1
Action succeeded
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv action clear router policy prefix-list \<prefix-list-id\> rule \<rule-id\> match \<match-id\></h>

Clears statistics for a specific prefix list rule number and match ID.

### Command Syntax

| Syntax   |  Description  |
| ----------    | ------------  |
| `<prefix-list-id>` | The name of the prefix list whose statistics you want to clear. |
| `<rule-id>` | The prefix list rule number. |
| `<match-id>` | The prefix list match criteria. |

### Version History

Introduced in Cumulus Linux 5.6.0

### Example

```
cumulus@switch:~$ nv action clear router policy prefix-list prefixlist1 rule 10 match 10.0.0.0/16
Action succeeded
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv action clear router policy route-map</h>

Clears all route map counters.

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv action clear router policy route-map
Action succeeded
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv action clear router policy route-map \<route-map-id\></h>

Clears counters for the specified route map.

### Command Syntax

| Syntax   |  Description  |
| ----------    | ------------  |
| `<route-map-id>` | The route map you want to clear. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv action clear router policy route-map ROUTEMAP1
Action succeeded
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv action clear router segment-routing srv6 stats</h>

Clears all segment routing statistics.

### Version History

Introduced in Cumulus Linux 5.14.0

### Example

```
cumulus@switch:~$ nv action clear router segment-routing srv6 stats 
Action succeeded
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv action clear router segment-routing srv6 stats sid \<sid-id\></h>

Clears the segment routing statistics for a specific SID.

### Command Syntax

| Syntax   |  Description  |
| ----------    | ------------  |
| `<sid-id>` |  The static segment identifier. |

### Version History

Introduced in Cumulus Linux 5.14.0

### Example

```
cumulus@switch:~$ nv action clear router segment-routing srv6 stats sid 2001:db8:1:1::100/48
Action succeeded
```
<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv action clear router segment-routing srv6 stats sid no-sid-drops</h>

Clears segment routing statistics for no-SID dropped packets.

### Version History

Introduced in Cumulus Linux 5.14.0

### Example

```
cumulus@switch:~$ nv action clear router segment-routing srv6 stats no-sid-drops 
Action succeeded
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv action clear service ptp \<instance-id\> monitor violations log max-offset</h>

Clears the PTP monitor violation log maximum offset value.

### Command Syntax

| Syntax   |  Description  |
| ----------    | ------------  |
| `<instance-id>` |  The PTP instance number used for management purposes. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv action clear service ptp 1 monitor violations log max-offset
Action succeeded
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv action clear service ptp \<instance-id\> monitor violations log min-offset</h>

Clears the PTP monitor violation log minumum offset value.

### Command Syntax

| Syntax   |  Description  |
| ----------    | ------------  |
| `<instance-id>` |  The PTP instance number used for management purposes. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv action clear service ptp 1 monitor violations log min-offset
Action succeeded
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv action clear service ptp \<instance-id\> monitor violations log path-delay</h>

Clears the PTP monitor violation log path delay value.

### Command Syntax

| Syntax   |  Description  |
| ----------    | ------------  |
| `<instance-id>` |  The PTP instance number used for management purposes. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv action clear service ptp 1 monitor violations log path-delay
Action succeeded
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv action clear system api session user \<user-id\></h>

Clears an NVUE user session.

NVUE uses sessions to authenticate and authorize requests. After authenticating the user with the first request, NVUE stores the session in the `nvued` cache. NVUE authenticates subsequent interactions within the session locally, eliminating the need to repeatedly check with external authentication servers. This process enhances system performance and efficiency, making it ideal for high-traffic environments.
- If you make changes to a user group, password, RADIUS, TACACS, or LDAP server setting locally on the switch, NVUE clears the current session automatically.
- If you make changes directly on the RADIUS, TACACS, or LDAP server, you must clear the user session with the `nv action clear system api session user <user>` command or clear all sessions with the `nv action clear system api session` command.

   {{%notice note%}}
If you do not clear a user session after making changes directly on the RADIUS, TACACS, or LDAP server, NVUE uses the existing session for authentication and authorization until the session times out (up to 60 minutes).
{{%/notice%}}

### Command Syntax

| Syntax   |  Description  |
| ----------    | ------------  |
| `<user-id>` |  The user account. |

### Version History

Introduced in Cumulus Linux 5.10.0

### Example

```
cumulus@switch:~$ nv action clear system api session user admin
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv action clear system link flap-protection violation</h>

Clears the `protodown` links on the switch.

{{%notice note%}}
In Cumulus Linux 5.8 and earlier, this command is `nv action clear system link protodown link-flap`.
{{%/notice%}}

### Version History

Introduced in Cumulus Linux 5.9.0

### Example

```
cumulus@switch:~$ nv action clear system link flap-protection violation
Action succeeded
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv action clear system forwarding packet-trim counters</h>

Clears the global packet trimming counter that is shown in the `nv show system forwarding packet-trim` command output.

### Version History

Introduced in Cumulus Linux 5.14.0

### Example

```
cumulus@switch:~$ nv action clear system forwarding packet-trim counters
Action succeeded
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv action clear vrf \<vrf-id\> router bgp address-family ipv4-unicast in</h>

Clears BGP IPv4 inbound routes.

This command does not clear counters in the kernel or hardware and does not reset BGP neighbor adjacencies.

- When the switch has a neighbor configured with `soft-reconfiguration inbound` enabled, this command clears the routes in the soft reconfiguration table for the address family. This results in reevaluating routes in the BGP table against any applied input policies.
- When the switch has a neighbor configured *without* the `soft-reconfiguration inbound` option enabled, this command sends the peer a route refresh message.

### Command Syntax

| Syntax   |  Description  |
| ----------    | ------------  |
| `<vrf-id>` |  The VRF name.  |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv action clear vrf default router bgp address-family ipv4-unicast in
Action succeeded
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv action clear vrf \<vrf-id\> router bgp address-family ipv4-unicast soft in</h>

Clears BGP IPv4 inbound routes for all BGP peers.

This command does not clear counters in the kernel or hardware and does not reset BGP neighbor adjacencies.

- When the switch has a neighbor configured with `soft-reconfiguration inbound` enabled, this command clears the routes in the soft reconfiguration table for the address family. This results in reevaluating routes in the BGP table against any applied input policies.
- When the switch has a neighbor configured *without* the `soft-reconfiguration inbound` option enabled, this command sends the peer a route refresh message.
- If you do not specify the direction `in`, the command affects both inbound and outbound routes depending on whether you enable soft-reconfiguration inbound.

### Command Syntax

| Syntax   |  Description  |
| ----------    | ------------  |
| `<vrf-id>` |  The VRF name.  |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv action clear vrf default router bgp address-family soft in
Action succeeded
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv action clear vrf \<vrf-id\> router bgp address-family ipv4-unicast soft out</h>

Clears BGP IPv4 outbound routes for all BGP peers.

This command does not:
- Clear counters in the kernel or hardware.
- Reset BGP neighbor adjacencies.
- Readvertise all routes to BGP peers.

If you do not specify the direction `out`, the command affects both inbound and outbound routes depending on whether soft-reconfiguration inbound is enabled.

### Command Syntax

| Syntax   |  Description  |
| ----------    | ------------  |
| `<vrf-id>` |  The VRF name.  |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv action clear vrf default router bgp address-family soft out
Action succeeded
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv action clear vrf \<vrf-id\> router bgp address-family ipv4-unicast out</h>

Clears BGP IPv4 outbound routes.

This command does not:
- Clear counters in the kernel or hardware.
- Reset BGP neighbor adjacencies.
- Readvertise all routes to BGP peers.

### Command Syntax

| Syntax   |  Description  |
| ----------    | ------------  |
| `<vrf-id>` |  The VRF name.  |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv action clear vrf default router bgp address-family ipv4-unicast in
Action succeeded
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv action clear vrf \<vrf-id\> router bgp address-family ipv6-unicast in</h>

Clears BGP IPv6 inbound routes.

This command does not clear counters in the kernel or hardware and does not reset BGP neighbor adjacencies.

- When the switch has a neighbor configured with `soft-reconfiguration inbound` enabled, this command clears the routes in the soft reconfiguration table for the address family. This results in reevaluating routes in the BGP table against any applied input policies.
- When the switch has a neighbor configured *without* the `soft-reconfiguration inbound` option enabled, this command sends the peer a route refresh message.

### Command Syntax

| Syntax   |  Description  |
| ----------    | ------------  |
| `<vrf-id>` |  The VRF name.  |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv action clear vrf default router bgp address-family ipv6-unicast in
Action succeeded
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv action clear vrf \<vrf-id\> router bgp address-family ipv6-unicast soft in</h>

Clears BGP IPv6 inbound routes for all BGP peers.

This command does not clear counters in the kernel or hardware and does not reset BGP neighbor adjacencies.

- When the switch has a neighbor configured with `soft-reconfiguration inbound` enabled, this command clears the routes in the soft reconfiguration table for the address family. This results in reevaluating routes in the BGP table against any applied input policies.
- When the switch has a neighbor configured *without* the `soft-reconfiguration inbound` option enabled, this command sends the peer a route refresh message.
- If you do not specify the direction `in`, the command affects both inbound and outbound routes depending on whether soft-reconfiguration inbound is enabled.

### Command Syntax

| Syntax   |  Description  |
| ----------    | ------------  |
| `<vrf-id>` |  The VRF name.  |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv action clear vrf default router bgp address-family ipv6-unicast soft in
Action succeeded
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv action clear vrf \<vrf-id\> router bgp address-family ipv6-unicast soft out</h>

Clears BGP IPv6 outbound routes for all BGP peers.

This command does not:
- Clear counters in the kernel or hardware.
- Reset BGP neighbor adjacencies.
- Readvertise all routes to BGP peers.

If you do not specify the direction `out`, the command affects both inbound and outbound routes depending on whether soft-reconfiguration inbound is enabled.

### Command Syntax

| Syntax   |  Description  |
| ----------    | ------------  |
| `<vrf-id>` |  The VRF name.  |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv action clear vrf default router bgp address-family ipv6-unicast soft out
Action succeeded
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv action clear vrf \<vrf-id\> router bgp address-family ipv6-unicast out</h>

Clears BGP IPv6 outbound routes.

This command does not:
- Clear counters in the kernel or hardware.
- Reset BGP neighbor adjacencies.
- Readvertise all routes to BGP peers.

### Command Syntax

| Syntax   |  Description  |
| ----------    | ------------  |
| `<vrf-id>` |  The VRF name.  |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv action clear vrf default router bgp address-family ipv6-unicast out
Action succeeded
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv action clear vrf \<vrf-id\> router bgp address-family l2vpn-evpn in</h>

Clears BGP EVPN inbound routes.

This command does not clear counters in the kernel or hardware and does not reset BGP neighbor adjacencies.

- When the switch has a neighbor configured with `soft-reconfiguration inbound` enabled, this command clears the routes in the soft reconfiguration table for the address family. This results in reevaluating routes in the BGP table against any applied input policies.
- When the switch has a neighbor configured *without* the `soft-reconfiguration inbound` option enabled, this command sends the peer a route refresh message.

### Command Syntax

| Syntax   |  Description  |
| ----------    | ------------  |
| `<vrf-id>` |  The VRF name.  |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv action clear vrf default router bgp address-family l2vpn-evpn in
Action succeeded
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv action clear vrf \<vrf-id\> router bgp address-family l2vpn-evpn soft in</h>

Clears BGP EVPN inbound routes for all BGP peers.

This command does not clear counters in the kernel or hardware and does not reset BGP neighbor adjacencies.

- When the switch has a neighbor configured with `soft-reconfiguration inbound` enabled, this command clears the routes in the soft reconfiguration table for the address family. This results in reevaluating routes in the BGP table against any applied input policies.
- When the switch has a neighbor configured *without* the `soft-reconfiguration inbound` option enabled, this command sends the peer a route refresh message.
- If you do not specify the direction `in`, the command affects both inbound and outbound routes depending on whether soft-reconfiguration inbound is enabled.

### Command Syntax

| Syntax   |  Description  |
| ----------    | ------------  |
| `<vrf-id>` |  The VRF name.  |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv action clear vrf default router bgp address-family l2vpn-evpn soft in
Action succeeded
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv action clear vrf \<vrf-id\> router bgp address-family l2vpn-evpn soft out</h>

Clears BGP EVPN outbound routes for all BGP peers.

This command does not:
- Clear counters in the kernel or hardware.
- Reset BGP neighbor adjacencies.
- Readvertise all routes to BGP peers.

If you do not specify the direction `out`, the command affects both inbound and outbound routes depending on whether soft-reconfiguration inbound is enabled.

### Command Syntax

| Syntax   |  Description  |
| ----------    | ------------  |
| `<vrf-id>` |  The VRF name.  |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv action clear vrf default router bgp address-family l2vpn-evpn soft out
Action succeeded
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv action clear vrf \<vrf-id\> router bgp address-family l2vpn-evpn out</h>

Clears BGP EVPN outbound routes.

This command does not:
- Clear counters in the kernel or hardware.
- Reset BGP neighbor adjacencies.
- Readvertise all routes to BGP peers.

### Command Syntax

| Syntax   |  Description  |
| ----------    | ------------  |
| `<vrf-id>` |  The VRF name.  |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv action clear vrf default router bgp address-family l2vpn-evpn out
Action succeeded
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv action clear vrf \<vrf-id\> router bgp in prefix-filter</h>

Clears and refreshes inbound routes for all neighbors and address families in the specified VRF and refreshes the outbound route filtering prefix list.

### Command Syntax

| Syntax   |  Description  |
| ----------    | ------------  |
| `<vrf-id>` |  The VRF name.  |

### Version History

Introduced in Cumulus Linux 5.6.0

### Example

```
cumulus@switch:~$ nv action clear vrf default router bgp in prefix-filter
Action succeeded
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv action clear vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv4-unicast in</h>

Clears IPv4 inbound routes for a specific BGP peer in the specified VRF.

This command does not clear counters in the kernel or hardware and does not reset BGP neighbor adjacencies.

- When the switch has a neighbor configured with `soft-reconfiguration inbound` enabled, this command clears the routes in the soft reconfiguration table for the address family. This results in reevaluating routes in the BGP table against any applied input policies.
- When the switch has a neighbor configured *without* the `soft-reconfiguration inbound` option enabled, this command sends the peer a route refresh message.

### Command Syntax

| Syntax   |  Description  |
| ----------    | ------------  |
| `<vrf-id>` |  The VRF name.  |
| `<neighbor-id>` | The IP address of the BGP peer or the interface if you are using unnumbered BGP. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv action clear vrf default router bgp neighbor swp51 address-family ipv4-unicast in
Action succeeded
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv action clear vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv4-unicast soft in</h>

Clears IPv4 inbound routes for a specific BGP peer in the specified VRF without resetting the peer session.

This command does not clear counters in the kernel or hardware and does not reset BGP neighbor adjacencies.

- When the switch has a neighbor configured with `soft-reconfiguration inbound` enabled, this command clears the routes in the soft reconfiguration table for the address family. This results in reevaluating routes in the BGP table against any applied input policies.
- When the switch has a neighbor configured *without* the `soft-reconfiguration inbound` option enabled, this command sends the peer a route refresh message.
- If you do not specify the direction `in`, the command affects both inbound and outbound routes depending on whether soft-reconfiguration inbound is enabled.

### Command Syntax

| Syntax   |  Description  |
| ----------    | ------------  |
| `<vrf-id>` |  The VRF name.  |
| `<neighbor-id>` | The IP address of the BGP peer or the interface if you are using unnumbered BGP. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv action clear vrf default router bgp neighbor swp51 address-family ipv4-unicast soft in
Action succeeded
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv action clear vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv4-unicast soft out</h>

Clears IPv4 outbound routes for a specific BGP peer in the specified VRF without resetting the peer session.

This command does not:
- Clear counters in the kernel or hardware.
- Reset BGP neighbor adjacencies.
- Readvertise all routes to BGP peers.

If you do not specify the direction `out`, the command affects both inbound and outbound routes depending on whether soft-reconfiguration inbound is enabled.

### Command Syntax

| Syntax   |  Description  |
| ----------    | ------------  |
| `<vrf-id>` |  The VRF name.  |
| `<neighbor-id>` | The IP address of the BGP peer or the interface if you are using unnumbered BGP. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv action clear vrf default router bgp neighbor swp51 address-family ipv4-unicast soft out
Action succeeded
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv action clear vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv4-unicast out</h>

Clears IPv4 outbound routes for a specific BGP peer in the specified VRF.

This command does not:
- Clear counters in the kernel or hardware.
- Reset BGP neighbor adjacencies.
- Readvertise all routes to BGP peers.

### Command Syntax

| Syntax   |  Description  |
| ----------    | ------------  |
| `<vrf-id>` |  The VRF name.  |
| `<neighbor-id>` | The IP address of the BGP peer or the interface if you are using unnumbered BGP. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv action clear vrf default router bgp neighbor swp51 address-family ipv4-unicast out
Action succeeded
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv action clear vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv6-unicast in</h>

Clears IPv6 inbound routes for a specific BGP peer in the specified VRF.

This command does not clear counters in the kernel or hardware and does not reset BGP neighbor adjacencies.

- When the switch has a neighbor configured with `soft-reconfiguration inbound` enabled, this command clears the routes in the soft reconfiguration table for the address family. This results in reevaluating routes in the BGP table against any applied input policies.
- When the switch has a neighbor configured *without* the `soft-reconfiguration inbound` option enabled, this command sends the peer a route refresh message.

### Command Syntax

| Syntax   |  Description  |
| ----------    | ------------  |
| `<vrf-id>` |  The VRF name.  |
| `<neighbor-id>` | The IP address of the BGP peer or the interface if you are using unnumbered BGP. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv action clear vrf default router bgp neighbor swp51 address-family ipv6-unicast in
Action succeeded
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv action clear vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv6-unicast soft in</h>

Clears IPv6 inbound routes for a specific BGP peer in the specified VRF without resetting the peer session.

This command does not clear counters in the kernel or hardware and does not reset BGP neighbor adjacencies.

- When the switch has a neighbor configured with `soft-reconfiguration inbound` enabled, this command clears the routes in the soft reconfiguration table for the address family. This results in reevaluating routes in the BGP table against any applied input policies.
- When the switch has a neighbor configured *without* the `soft-reconfiguration inbound` option enabled, this command sends the peer a route refresh message.
- If you do not specify the direction `in`, the command affects both inbound and outbound routes depending on whether soft-reconfiguration inbound is enabled.

### Command Syntax

| Syntax   |  Description  |
| ----------    | ------------  |
| `<vrf-id>` |  The VRF name.  |
| `<neighbor-id>` | The IP address of the BGP peer or the interface if you are using unnumbered BGP. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv action clear vrf default router bgp neighbor swp51 address-family ipv6-unicast soft in
Action succeeded
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv action clear vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv6-unicast soft out</h>

Clears IPv6 outbound routes for a specific BGP peer in the specified VRF without resetting the peer session.

This command does not:
- Clear counters in the kernel or hardware.
- Reset BGP neighbor adjacencies.
- Readvertise all routes to BGP peers.

If you do not specify the direction `out`, the command affects both inbound and outbound routes depending on whether soft-reconfiguration inbound is enabled.

### Command Syntax

| Syntax   |  Description  |
| ----------    | ------------  |
| `<vrf-id>` |  The VRF name.  |
| `<neighbor-id>` | The IP address of the BGP peer or the interface if you are using unnumbered BGP. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv action clear vrf default router bgp neighbor swp51 address-family ipv6-unicast soft out
Action succeeded
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv action clear vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv6-unicast out</h>

Clears IPv6 outbound routes for a specific BGP peer in the specified VRF.

This command does not:
- Clear counters in the kernel or hardware.
- Reset BGP neighbor adjacencies.
- Readvertise all routes to BGP peers.

### Command Syntax

| Syntax   |  Description  |
| ----------    | ------------  |
| `<vrf-id>` |  The VRF name.  |
| `<neighbor-id>` | The IP address of the BGP peer or the interface if you are using unnumbered BGP. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv action clear vrf default router bgp neighbor swp51 address-family ipv6-unicast out
Action succeeded
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv action clear vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family l2vpn-evpn in</h>

Clears EVPN inbound routes for a specific BGP peer in the specified VRF.

This command does not clear counters in the kernel or hardware and does not reset BGP neighbor adjacencies.

- When the switch has a neighbor configured with `soft-reconfiguration inbound` enabled, this command clears the routes in the soft reconfiguration table for the address family. This results in reevaluating routes in the BGP table against any applied input policies.
- When the switch has a neighbor configured *without* the `soft-reconfiguration inbound` option enabled, this command sends the peer a route refresh message.

### Command Syntax

| Syntax   |  Description  |
| ----------    | ------------  |
| `<vrf-id>` |  The VRF name.  |
| `<neighbor-id>` | The IP address of the BGP peer or the interface if you are using unnumbered BGP. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv action clear vrf default router bgp neighbor swp51 address-family l2vpn-evpn in
Action succeeded
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv action clear vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family l2vpn-evpn soft in</h>

Clears EVPN inbound routes for a specific BGP peer in the specified VRF without resetting the peer session.

This command does not clear counters in the kernel or hardware and does not reset BGP neighbor adjacencies.

- When the switch has a neighbor configured with `soft-reconfiguration inbound` enabled, this command clears the routes in the soft reconfiguration table for the address family. This results in reevaluating routes in the BGP table against any applied input policies.
- When the switch has a neighbor configured *without* the `soft-reconfiguration inbound` option enabled, this command sends the peer a route refresh message.
- If you do not specify the direction `in`, the command affects both inbound and outbound routes depending on whether soft-reconfiguration inbound is enabled.

### Command Syntax

| Syntax   |  Description  |
| ----------    | ------------  |
| `<vrf-id>` |  The VRF name.  |
| `<neighbor-id>` | The IP address of the BGP peer or the interface if you are using unnumbered BGP. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv action clear vrf default router bgp neighbor swp51 address-family l2vpn-evpn soft in
Action succeeded
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv action clear vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family l2vpn-evpn soft out</h>

Clears EVPN outbound routes for a specific BGP peer in the specified VRF without resetting the peer session.

This command does not:
- Clear counters in the kernel or hardware.
- Reset BGP neighbor adjacencies.
- Readvertise all routes to BGP peers.

If you do not specify the direction `out`, the command affects both inbound and outbound routes depending on whether soft-reconfiguration inbound is enabled.

### Command Syntax

| Syntax   |  Description  |
| ----------    | ------------  |
| `<vrf-id>` |  The VRF name.  |
| `<neighbor-id>` | The IP address of the BGP peer or the interface if you are using unnumbered BGP. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv action clear vrf default router bgp neighbor swp51 address-family l2vpn-evpn soft out
Action succeeded
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv action clear vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family l2vpn-evpn out</h>

Clears EVPN outbound routes for a specific BGP peer in the specified VRF.

This command does not:
- Clear counters in the kernel or hardware.
- Reset BGP neighbor adjacencies.
- Readvertise all routes to BGP peers.

### Command Syntax

| Syntax   |  Description  |
| ----------    | ------------  |
| `<vrf-id>` |  The VRF name.  |
| `<neighbor-id>` | The IP address of the BGP peer or the interface if you are using unnumbered BGP. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv action clear vrf default router bgp neighbor swp51 address-family l2vpn-evpn out
Action succeeded
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv action clear vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> in</h>

Clears inbound routes for a specific BGP peer in the specified VRF.

This command does not clear counters in the kernel or hardware and does not reset BGP neighbor adjacencies.

- When the switch has a neighbor configured with `soft-reconfiguration inbound` enabled, this command clears the routes in the soft reconfiguration table for the address family. This results in reevaluating routes in the BGP table against any applied input policies.
- When the switch has a neighbor configured *without* the `soft-reconfiguration inbound` option enabled, this command sends the peer a route refresh message.

### Command Syntax

| Syntax   |  Description  |
| ----------    | ------------  |
| `<vrf-id>` |  The VRF name.  |
| `<neighbor-id>` | The IP address of the BGP peer or the interface if you are using unnumbered BGP. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv action clear vrf default router bgp neighbor swp51 in
Action succeeded
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv action clear vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> soft in</h>

Clears inbound routes for a specific BGP peer in the specified VRF without resetting the peer session.

This command does not clear counters in the kernel or hardware and does not reset BGP neighbor adjacencies.

- When the switch has a neighbor configured with `soft-reconfiguration inbound` enabled, this command clears the routes in the soft reconfiguration table for the address family. This results in reevaluating routes in the BGP table against any applied input policies.
- When the switch has a neighbor configured *without* the `soft-reconfiguration inbound` option enabled, this command sends the peer a route refresh message.
- If you do not specify the direction `in`, the command affects both inbound and outbound routes depending on whether soft-reconfiguration inbound is enabled.

### Command Syntax

| Syntax   |  Description  |
| ----------    | ------------  |
| `<vrf-id>` |  The VRF name.  |
| `<neighbor-id>` | The IP address of the BGP peer or the interface if you are using unnumbered BGP. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv action clear vrf default router bgp neighbor swp51 soft in
Action succeeded
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv action clear vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> soft out</h>

Clears outbound routes for a specific BGP peer in the specified VRF without resetting the peer session.

This command does not:
- Clear counters in the kernel or hardware.
- Reset BGP neighbor adjacencies.
- Readvertise all routes to BGP peers.

If you do not specify the direction `out`, the command affects both inbound and outbound routes depending on whether soft-reconfiguration inbound is enabled.

### Command Syntax

| Syntax   |  Description  |
| ----------    | ------------  |
| `<vrf-id>` |  The VRF name.  |
| `<neighbor-id>` | The IP address of the BGP peer or the interface if you are using unnumbered BGP. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv action clear vrf default router bgp neighbor swp51 soft out
Action succeeded
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv action clear vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> out</h>

Clears outbound routes for a specific BGP peer in the specified VRF.

This command does not:
- Clear counters in the kernel or hardware.
- Reset BGP neighbor adjacencies.
- Readvertise all routes to BGP peers.

### Command Syntax

| Syntax   |  Description  |
| ----------    | ------------  |
| `<vrf-id>` |  The VRF name.  |
| `<neighbor-id>` | The IP address of the BGP peer or the interface if you are using unnumbered BGP. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv action clear vrf default router bgp neighbor swp51 out
Action succeeded
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv action clear vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv4-unicast in</h>

Clears IPv4 inbound routes for a specific BGP peer group in the specified VRF.

This command does not clear counters in the kernel or hardware and does not reset BGP neighbor adjacencies.

- When the switch has a neighbor configured with `soft-reconfiguration inbound` enabled, this command clears the routes in the soft reconfiguration table for the address family. This results in reevaluating routes in the BGP table against any applied input policies.
- When the switch has a neighbor configured *without* the `soft-reconfiguration inbound` option enabled, this command sends the peer a route refresh message.

### Command Syntax

| Syntax   |  Description  |
| ----------    | ------------  |
| `<vrf-id>` |  The VRF name.  |
| `<peer-group-id>` |  The peer group name. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv action clear vrf default router bgp peer-group SPINES address-family ipv4-unicast in
Action succeeded
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv action clear vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv4-unicast soft in</h>

Clears IPv4 inbound routes for a specific BGP peer group in the specified VRF.

This command does not clear counters in the kernel or hardware and does not reset BGP neighbor adjacencies.

- When the switch has a neighbor configured with `soft-reconfiguration inbound` enabled, this command clears the routes in the soft reconfiguration table for the address family. This results in reevaluating routes in the BGP table against any applied input policies.
- When the switch has a neighbor configured *without* the `soft-reconfiguration inbound` option enabled, this command sends the peer a route refresh message.
- If you do not specify the direction `in`, the command affects both inbound and outbound routes depending on whether soft-reconfiguration inbound is enabled.

### Command Syntax

| Syntax   |  Description  |
| ----------    | ------------  |
| `<vrf-id>` |  The VRF name.  |
| `<peer-group-id>` |  The peer group name. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv action clear vrf default router bgp peer-group SPINES address-family ipv4-unicast soft in
Action succeeded
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv action clear vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv4-unicast soft out</h>

Clears IPv4 outbound routes for a specific BGP peer group in the specified VRF.

This command does not:
- Clear counters in the kernel or hardware.
- Reset BGP neighbor adjacencies.
- Readvertise all routes to BGP peers.

If you do not specify the direction `out`, the command affects both inbound and outbound routes depending on whether soft-reconfiguration inbound is enabled.

### Command Syntax

| Syntax   |  Description  |
| ----------    | ------------  |
| `<vrf-id>` |  The VRF name.  |
| `<peer-group-id>` |  The peer group name. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv action clear vrf default router bgp peer-group SPINES address-family ipv4-unicast soft out
Action succeeded
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv action clear vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv4-unicast out</h>

Clears IPv4 outbound routes for a specific BGP peer group in the specified VRF.

This command does not:
- Clear counters in the kernel or hardware.
- Reset BGP neighbor adjacencies.
- Readvertise all routes to BGP peers.

### Command Syntax

| Syntax   |  Description  |
| ----------    | ------------  |
| `<vrf-id>` |  The VRF name.  |
| `<peer-group-id>` |  The peer group name. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv action clear vrf default router bgp peer-group SPINES address-family ipv4-unicast out
Action succeeded
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv action clear vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv6-unicast in</h>

Clears IPv6 inbound routes for a specific BGP peer group in the specified VRF.

This command does not clear counters in the kernel or hardware and does not reset BGP neighbor adjacencies.

- When the switch has a neighbor configured with `soft-reconfiguration inbound` enabled, this command clears the routes in the soft reconfiguration table for the address family. This results in reevaluating routes in the BGP table against any applied input policies.
- When the switch has a neighbor configured *without* the `soft-reconfiguration inbound` option enabled, this command sends the peer a route refresh message.

### Command Syntax

| Syntax   |  Description  |
| ----------    | ------------  |
| `<vrf-id>` |  The VRF name.  |
| `<peer-group-id>` |  The peer group name. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv action clear vrf default router bgp peer-group SPINES address-family ipv6-unicast in
Action succeeded
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv action clear vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv6-unicast soft in</h>

Clears IPv6 inbound routes for a specific BGP peer group in the specified VRF.

This command does not clear counters in the kernel or hardware and does not reset BGP neighbor adjacencies.

- When the switch has a neighbor configured with `soft-reconfiguration inbound` enabled, this command clears the routes in the soft reconfiguration table for the address family. This results in reevaluating routes in the BGP table against any applied input policies.
- When the switch has a neighbor configured *without* the `soft-reconfiguration inbound` option enabled, this command sends the peer a route refresh message.
- If you do not specify the direction `in`, the command affects both inbound and outbound routes depending on whether soft-reconfiguration inbound is enabled.

### Command Syntax

| Syntax   |  Description  |
| ----------    | ------------  |
| `<vrf-id>` |  The VRF name.  |
| `<peer-group-id>` |  The peer group name. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv action clear vrf default router bgp peer-group SPINES address-family ipv6-unicast soft in
Action succeeded
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv action clear vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv6-unicast soft out</h>

Clears IPv6 outbound routes for a specific BGP peer group in the specified VRF.

This command does not:
- Clear counters in the kernel or hardware.
- Reset BGP neighbor adjacencies.
- Readvertise all routes to BGP peers.

If you do not specify the direction `out`, the command affects both inbound and outbound routes depending on whether soft-reconfiguration inbound is enabled.

### Command Syntax

| Syntax   |  Description  |
| ----------    | ------------  |
| `<vrf-id>` |  The VRF name.  |
| `<peer-group-id>` |  The peer group name. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv action clear vrf default router bgp peer-group SPINES address-family ipv6-unicast soft out
Action succeeded
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv action clear vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv6-unicast out</h>

Clears IPv6 outbound routes for a specific BGP peer group in the specified VRF.

This command does not:
- Clear counters in the kernel or hardware.
- Reset BGP neighbor adjacencies.
- Readvertise all routes to BGP peers.

### Command Syntax

| Syntax   |  Description  |
| ----------    | ------------  |
| `<vrf-id>` |  The VRF name.  |
| `<peer-group-id>` |  The peer group name. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv action clear vrf default router bgp peer-group SPINES address-family ipv6-unicast out
Action succeeded
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv action clear vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family l2vpn-evpn in</h>

Clears EVPN inbound routes for a specific BGP peer group in the specified VRF.

This command does not clear counters in the kernel or hardware and does not reset BGP neighbor adjacencies.

- When the switch has a neighbor configured with `soft-reconfiguration inbound` enabled, this command clears the routes in the soft reconfiguration table for the address family. This results in reevaluating routes in the BGP table against any applied input policies.
- When the switch has a neighbor configured *without* the `soft-reconfiguration inbound` option enabled, this command sends the peer a route refresh message.

### Command Syntax

| Syntax   |  Description  |
| ----------    | ------------  |
| `<vrf-id>` |  The VRF name.  |
| `<peer-group-id>` |  The peer group name. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv action clear vrf default router bgp peer-group SPINES address-family l2vpn-evpn in
Action succeeded
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv action clear vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family l2vpn-evpn soft in</h>

Clears EVPN inbound routes for a specific BGP peer group in the specified VRF.

This command does not clear counters in the kernel or hardware and does not reset BGP neighbor adjacencies.

- When the switch has a neighbor configured with `soft-reconfiguration inbound` enabled, this command clears the routes in the soft reconfiguration table for the address family. This results in reevaluating routes in the BGP table against any applied input policies.
- When the switch has a neighbor configured *without* the `soft-reconfiguration inbound` option enabled, this command sends the peer a route refresh message.
- If you do not specify the direction `in`, the command affects both inbound and outbound routes depending on whether soft-reconfiguration inbound is enabled.

### Command Syntax

| Syntax   |  Description  |
| ----------    | ------------  |
| `<vrf-id>` |  The VRF name.  |
| `<peer-group-id>` |  The peer group name. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv action clear vrf default router bgp peer-group SPINES address-family l2vpn-evpn soft in
Action succeeded
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv action clear vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family l2vpn-evpn soft out</h>

Clears EVPN outbound routes for a specific BGP peer group in the specified VRF.

This command:
- Does not clear counters in the kernel or hardware
- Does not reset BGP neighbor adjacencies.
- Does not readvertise all routes to BGP peers.

If you do not specify the direction `out`, the command affects both inbound and outbound routes depending on whether soft-reconfiguration inbound is enabled.

### Command Syntax

| Syntax   |  Description  |
| ----------    | ------------  |
| `<vrf-id>` |  The VRF name.  |
| `<peer-group-id>` |  The peer group name. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv action clear vrf default router bgp peer-group SPINES address-family l2vpn-evpn soft out
Action succeeded
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv action clear vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family l2vpn-evpn out</h>

Clears EVPN outbound routes for a specific BGP peer group in the specified VRF.

This command does not:
- Clear counters in the kernel or hardware.
- Reset BGP neighbor adjacencies.
- Readvertise all routes to BGP peers.

### Command Syntax

| Syntax   |  Description  |
| ----------    | ------------  |
| `<vrf-id>` |  The VRF name.  |
| `<peer-group-id>` |  The peer group name. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv action clear vrf default router bgp peer-group SPINES address-family l2vpn-evpn out
Action succeeded
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv action clear vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> in</h>

Clears inbound routes for a specific BGP peer group in the specified VRF.

This command does not clear counters in the kernel or hardware and does not reset BGP neighbor adjacencies.

- When the switch has a neighbor configured with `soft-reconfiguration inbound` enabled, this command clears the routes in the soft reconfiguration table for the address family. This results in reevaluating routes in the BGP table against any applied input policies.
- When the switch has a neighbor configured *without* the `soft-reconfiguration inbound` option enabled, this command sends the peer a route refresh message.

### Command Syntax

| Syntax   |  Description  |
| ----------    | ------------  |
| `<vrf-id>` |  The VRF name.  |
| `<peer-group-id>` |  The peer group name. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv action clear vrf default router bgp peer-group SPINES in
Action succeeded
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv action clear vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> soft in</h>

Clears inbound routes for a specific BGP peer group in the specified VRF.

This command does not clear counters in the kernel or hardware and does not reset BGP neighbor adjacencies.

- When the switch has a neighbor configured with `soft-reconfiguration inbound` enabled, this command clears the routes in the soft reconfiguration table for the address family. This results in reevaluating routes in the BGP table against any applied input policies.
- When the switch has a neighbor configured *without* the `soft-reconfiguration inbound` option enabled, this command sends the peer a route refresh message.
- If you do not specify the direction `in`, the command affects both inbound and outbound routes depending on whether soft-reconfiguration inbound is enabled.

### Command Syntax

| Syntax   |  Description  |
| ----------    | ------------  |
| `<vrf-id>` |  The VRF name.  |
| `<peer-group-id>` |  The peer group name. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv action clear vrf default router bgp peer-group SPINES soft in
Action succeeded
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv action clear vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> soft out</h>

Clears outbound routes for a specific BGP peer group in the specified VRF.

This command does not:
- Clear counters in the kernel or hardware.
- Reset BGP neighbor adjacencies.
- Readvertise all routes to BGP peers.

If you do not specify the direction `out`, the command affects both inbound and outbound routes depending on whether soft-reconfiguration inbound is enabled.

### Command Syntax

| Syntax   |  Description  |
| ----------    | ------------  |
| `<vrf-id>` |  The VRF name.  |
| `<peer-group-id>` |  The peer group name. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv action clear vrf default router bgp peer-group SPINES soft out
Action succeeded
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv action clear vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> out</h>

Clears outbound routes for a specific BGP peer group in the specified VRF.

This command does not:
- Clear counters in the kernel or hardware.
- Reset BGP neighbor adjacencies.
- Readvertise all routes to BGP peers.

### Command Syntax

| Syntax   |  Description  |
| ----------    | ------------  |
| `<vrf-id>` |  The VRF name.  |
| `<peer-group-id>` |  The peer group name. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv action clear vrf default router bgp peer-group SPINES out
Action succeeded
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv action clear vrf \<vrf-id\> router bgp soft</h>

Clears all routes with all neighbors and address families in the specified VRF.

### Command Syntax

| Syntax   |  Description  |
| ----------    | ------------  |
| `<vrf-id>` |  The VRF name.  |

### Version History

Introduced in Cumulus Linux 5.6.0

### Example

```
cumulus@switch:~$ nv action clear vrf default router bgp soft
Action succeeded
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv action clear vrf \<vrf-id\> router bgp soft in</h>

Clears and refreshes all inbound routes with all neighbors and address families in the specified VRF.

### Command Syntax

| Syntax   |  Description  |
| ----------    | ------------  |
| `<vrf-id>` |  The VRF name.  |

### Version History

Introduced in Cumulus Linux 5.6.0

### Example

```
cumulus@switch:~$ nv action clear vrf default router bgp soft in
Action succeeded
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv action clear vrf \<vrf-id\> router bgp soft out</h>

Clears and resends all outbound routes with all neighbors and address families in the specified VRF.

### Command Syntax

| Syntax   |  Description  |
| ----------    | ------------  |
| `<vrf-id>` |  The VRF name.  |

### Version History

Introduced in Cumulus Linux 5.6.0

### Example

```
cumulus@switch:~$ nv action clear vrf default router bgp soft out
Action succeeded
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv action clear vrf \<vrf-id\> router bgp out</h>

Clears and refreshes outbound routes for all neighbors and address families in the specified VRF.

### Command Syntax

| Syntax   |  Description  |
| ----------    | ------------  |
| `<vrf-id>` |  The VRF name.  |

### Version History

Introduced in Cumulus Linux 5.6.0

### Example

```
cumulus@switch:~$ nv action clear vrf default router bgp out
Action succeeded
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv action clear vrf \<vrf-id\> router ospf database</h>

Clear the OSPF database, reestablishes neighborships, and reoriginates LSAs.

### Command Syntax

| Syntax   |  Description  |
| ----------    | ------------  |
| `<vrf-id>` |  The VRF name.  |

### Version History

Introduced in Cumulus Linux 5.10.0

### Example

```
cumulus@switch:~$ nv action clear vrf default router ospf database
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv action clear vrf \<vrf-id\> router ospf interface</h>

Clears all counters for the OSPF interfaces.

### Command Syntax

| Syntax   |  Description  |
| ----------    | ------------  |
| `<vrf-id>` |  The VRF name.  |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv action clear vrf default router ospf interface
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv action clear vrf \<vrf-id\> router ospf interface \<interface-id\></h>

Clears OSPF neighbor adjacency on the specified interface.

### Command Syntax

| Syntax   |  Description  |
| ----------    | ------------  |
| `<vrf-id>` |  The VRF name.  |
| `<interface-id>` | The interface on which you want to clear OSPF neighbor adjacency. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv action clear vrf default router ospf interface swp2
Action succeeded
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv action clear vrf \<vrf-id\> router pim interfaces</h>

Clears PIM neighbors for all PIM interfaces in the specified VRF.

### Command Syntax

| Syntax   |  Description  |
| ----------    | ------------  |
| `<vrf-id>` |  The VRF name.  |

### Version History

Introduced in Cumulus Linux 5.6.0

### Example

```
cumulus@switch:~$ nv action clear vrf default router pim interfaces
Action succeeded
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv action clear vrf \<vrf-id\> router pim interface-traffic</h>

Clears traffic statistics for all PIM interfaces in the specified VRF.

### Command Syntax

| Syntax   |  Description  |
| ----------    | ------------  |
| `<vrf-id>` |  The VRF name.  |

### Version History

Introduced in Cumulus Linux 5.6.0

### Example

```
cumulus@switch:~$ nv action clear vrf default router pim interface-traffic
Action succeeded
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv action deauthenticate interface \<interface-id\> dot1x authorized-sessions \<mac-address\></h>

Deauthenticates the 802.1X supplicant on the specified interface. If you do not want to notify the supplicant that they are being deauthenticated, you can add the `silent` option.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<interface-id>` |  The interface on which you want to deauthenticate the 802.1X supplicant. |
| `<mac-address>` |  The MAC address. |

### Version History

Introduced in Cumulus Linux 5.8.0

### Example

```
cumulus@switch:~$ nv action deauthenticate interface swp1 dot1x authorized-sessions 00:55:00:00:00:09 silent
Action succeeded
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv action delete system health history files \<file-name\></h>

Deletes the specified health history report file on the switch.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<file-name>` | The system health history report file you want to delete. |

### Version History

Introduced in Cumulus Linux 5.15.0

### Example

```
cumulus@switch:~$ nv action delete system health history files FILE1
```


<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv action delete system log file \<file-name\></h>

Deletes the specified system log file.

Deleting log files enables you to manage storage space and ensure that only relevant logs remain. You typically delete log files after you upload or archive them, or when you no longer need the logs for troubleshooting or auditing. Log file deletion is a crucial step in log management to ensure that outdated or irrelevant data does not occupy system resources.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<file-name>` | The system log file you want to delete. |

### Version History

Introduced in Cumulus Linux 5.12.0

### Example

```
cumulus@switch:~$ nv action delete system log file mstpd.log 
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv action delete system log component \<component-name\> file \<filename\></h>

Deletes a log file from a specific system component.

### Command Syntax

| Syntax   |  Description  |
| ----------    | ------------  |
| `<component-name>` | The system component from which you want to delete a log file. |
| `<filename>` | The name of the log file you want to delete. |

### Version History

Introduced in Cumulus Linux 5.12.0

### Example

```
cumulus@switch:~$ nv action delete system log component nvue file nvued.log
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv action delete system packages key \<key\></h>

Deletes a package repository key.

### Command Syntax

| Syntax   |  Description  |
| ----------    | ------------  |
| `<key-id>` | The repository key. |

### Version History

Introduced in Cumulus Linux 5.12.0

### Example

```
cumulus@switch:~$ nv action delete system packages key debian-archive-bookworm-automatic.asc
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv action delete system security ca-certificate \<cert-id\></h>

Deletes the CA certificate you specify.

### Command Syntax

| Syntax   |  Description  |
| ----------    | ------------  |
| `<cert-id>` | The CA certificate you want to delete. |

### Version History

Introduced in Cumulus Linux 5.7.0

### Example

```
cumulus@switch:~$ nv action delete system security ca-certificate cert-1
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv action delete system security certificate \<cert-id\></h>

Deletes the entity certificate you specify.

### Command Syntax

| Syntax   |  Description  |
| ----------    | ------------  |
| `<cert-id>` | The entity certificate you want to delete. |

### Version History

Introduced in Cumulus Linux 5.7.0

### Example

```
cumulus@switch:~$ nv action delete system security certificate cert-1
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv action disable system maintenance mode</h>

Disables maintenance mode and restores normal operation.

{{%notice note%}}
Cumulus Linux 5.12 and earlier provides this command. For Cumulus Linux 5.13 and later use the `nv set maintenance unit all-protocols state production` command instead.
{{%/notice%}}

### Version History

Introduced in Cumulus Linux 5.7.0

### Example

```
cumulus@switch:~$ nv action disable system maintenance mode
System maintenance mode has been disabled successfully
 Current System Mode: cold  
 frr             : cold, up, up time: 12:57:48 (1 restart)
 switchd         : cold, up, up time: 13:12:13
 System Services : cold, up, up time: 13:12:32
Action succeeded
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv action disable system maintenance ports</h>

Restores the port admin state after maintenance.

{{%notice note%}}
Cumulus Linux 5.12 and earlier provides this command. For Cumulus Linux 5.13 and later use the `nv set maintenance unit all-interfaces state production` command instead.
{{%/notice%}}

### Version History

Introduced in Cumulus Linux 5.7.0

### Example

```
cumulus@switch:~$ nv action disable system maintenance ports
System maintenance ports has been disabled successfully
 Current System Mode: cold  
 Ports shutdown for Maintenance
 frr             : cold, up, up time: 13:00:57 (1 restart)
 switchd         : cold, up, up time: 13:15:22
 System Services : cold, up, up time: 13:15:41
Action succeeded
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv action disable system ztp</h>

Disables ZTP and deactivates the provisioning process. If a ZTP script is currently running, ZTP is not disabled.

### Version History

Introduced in Cumulus Linux 5.11.0

### Example

```
cumulus@switch:~$ nv action disable system ztp
The operation will perform disable of the ZTP.
Type [y] to perform disable of the ZTP.
Type [N] to cancel an action.

Do you want to continue? [y/N]
```

If you add the `force` option (`nv action disable system ztp force`), ZTP disables and deactivates the provisioning process without prompting you for confirmation.

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv action disconnect system aaa user \<user-id\></h>

Disconnects authenticated and authorized users.

### Command Syntax

| Syntax   |  Description  |
| ----------    | ------------  |
| `<user-id>` | The user you want to disconnect. |

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@switch:~$ nv action disconnect system aaa user admin2
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv action enable system maintenance mode</h>

Enables maintenance mode. When maintenance mode is on, ISSU performs a graceful BGP shutdown, redirects traffic over the peerlink and brings down the MLAG port link. `switchd` maintains full capability.

{{%notice note%}}
Cumulus Linux 5.12 and earlier provides this command. For Cumulus Linux 5.13 and later use the `nv set maintenance unit all-protocols state maintenance` command instead.
{{%/notice%}}

### Version History

Introduced in Cumulus Linux 5.7.0

### Example

```
cumulus@switch:~$ nv action enable system maintenance mode
System maintenance mode has been enabled successfully
 Current System Mode: Maintenance, cold  
 Maintenance mode since Sat Nov 18 07:09:25 2023 (Duration: 00:00:00)
 frr             : Maintenance, cold, down, up time: 12:55:51 (1 restart)
 switchd         : Maintenance, cold, down, up time: 13:10:16
 System Services : Maintenance, cold, down, up time: 13:10:35
Action succeeded
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv action enable system maintenance ports</h>

Brings down the ports for maintenance.


{{%notice note%}}
Cumulus Linux 5.12 and earlier provides this command. For Cumulus Linux 5.13 and later use the `nv set maintenance unit all-interfaces state maintenance` command instead.
{{%/notice%}}

### Version History

Introduced in Cumulus Linux 5.7.0

### Example

```
cumulus@switch:~$ nv action enable system maintenance ports
System maintenance ports has been enabled successfully
 Current System Mode: Maintenance, cold  
 Maintenance mode since Sat Nov 18 07:09:25 2023 (Duration: 00:00:56)
 frr             : Maintenance, cold, down, up time: 12:56:47 (1 restart)
 switchd         : Maintenance, cold, down, up time: 13:11:12
 System Services : Maintenance, cold, down, up time: 13:11:31
Action succeeded
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv action enable system security encryption folder-encrypt password \<passsword\></h>

Enables and disables secure mount directory encryption with a password or changes the existing secure mount directory encryption password.

Make sure the USB device is plugged in before running the command. The switch reboots after you run the command.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<passsword>` |  The password. |

### Version History

Introduced in Cumulus Linux 5.15.0

### Example

```
cumulus@switch:~$ nv action enable system security encryption folder-encrypt password MYPASSWORD
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv action enable system ztp</h>

Enables ZTP and activates the provisioning process. ZTP tries to run the next time the switch boots. However, if ZTP already ran on a previous boot up or if you made manual configuration changes, ZTP exits without trying to look for a script.

### Version History

Introduced in Cumulus Linux 5.11.0

### Example

```
cumulus@switch:~$ nv action enable system ztp
The operation will perform enable of the ZTP.
Type [y] to perform enable of the ZTP.
Type [N] to cancel an action.

Do you want to continue? [y/N]
```

If you add the `force` option (`nv action enable system ztp force`), ZTP enables and activates the provisioning process without prompting you for confirmation.


<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv action erase system disk</h>

Erases all data on the switch SSD securely to prevent leaking critical data. Erasing data is an important process when you return a switch with RMA if the switch is defective or move a switch between buildings.

When you erase all data on the switch, most services stop except for critical ones, such as sshd so that you can erase the data remotely.

NVUE prompts you to confirm that you want to proceed before destroying all data.

{{%notice note%}}
- This command is in Beta.
- You can erase all data only on switches with the Spectrum-4 and later ASIC.
- You can erase all data on a functioning SSD only.
- You cannot recover erased data.
{{%/notice%}}

### Version History

Introduced in Cumulus Linux 5.13.0

### Example

```
cumulus@switch:~$ nv action erase system disk
WARNING! This will destroy all 
data and will NOT be recoverable. 
Execution may take up to X minutes. 
Would you like to proceed? [y/N] 
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv action fetch system image \<remote-url\></h>

Fetches a binary image from the specified URL.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<remote-url>` |  The remote URL.|

### Version History

Introduced in Cumulus Linux 5.12.0

### Example

```
cumulus@switch:~$ nv action fetch system image http://10.0.1.251/cumulus-linux-5.12.0-mlx-amd64.bin
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv action fetch system packages key \<key\></h>

Fetches a repository key and saves it globally in the `/etc/apt/trusted.gpg.d/` directory.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<key>` |  The repository key.|

### Version History

Introduced in Cumulus Linux 5.12.0

### Example

```
cumulus@switch:~$ nv action fetch system packages key http://deb.opera.com/archive.key 
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv action fetch system packages key \<key\> scope repository</h>

Fetches and saves the repository key in the `/etc/apt/keyrings/` directory.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<key>` |  The repository key.|

### Version History

Introduced in Cumulus Linux 5.12.0

### Example

```
cumulus@switch:~$ nv action fetch system packages key http://deb.opera.com/archive.key scope repository
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv action generate file-hash md5 <filename></h>

Calculates and generates a unique hash value (checksum) for a file using md5.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<filename>`  |  The technical support file name and location. |

### Version History

Introduced in Cumulus Linux 5.13.0

### Example

```
cumulus@switch:~$ nv action generate file-hash md5 /var/log/text.txt  
Action executing ... 
Generated Hash Checksum  
5073306b0629c047d090e2c96b5eec4b /var/log/text.txt

Action succeeded
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv action generate file-hash sha1 <filename></h>

Calculates and generates a unique hash value (checksum) for a file using sha1.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<filename>`  |  The technical support file name and location. |

### Version History

Introduced in Cumulus Linux 5.13.0

### Example

```
cumulus@switch:~$ nv action generate file-hash sha1 /var/log/text.txt  
Action executing ...  
Generated Hash Checksum  
c0965ec47c1557d671e36abb5c55ec13b8378e44  /var/log/text.txt

Action succeeded
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv action generate file-hash sha224 <filename></h>

Calculates and generates a unique hash value (checksum) for a file using sha224.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<filename>`  |  The technical support file name and location. |

### Version History

Introduced in Cumulus Linux 5.13.0

### Example

```
cumulus@switch:~$ nv action generate file-hash sha224  /var/log/text.txt  
Action executing ...  
Generated Hash Checksum  
c414b2b7eaa757162f41183c42a02cf329ab86719be9f8583195d9ab  /var/log/text.txt

Action succeeded
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv action generate file-hash sha256 <filename></h>

Calculates and generates a unique hash value (checksum) for a file using sha256.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<filename>`  |  The technical support file name and location. |

### Version History

Introduced in Cumulus Linux 5.13.0

### Example

```
cumulus@switch:~$ nv action generate file-hash sha256 /var/log/text.txt  
Action executing ...  
Generated Hash Checksum  
3fe4bf60ed8d1ce9ffca7f578a94cab88b907951c92e1f8605f59a2bb0a2ab8b  /var/log/text.txt  

Action succeeded
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv action generate file-hash sha512 <filename></h>

Calculates and generates a unique hash value (checksum) for a file using sha512.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<filename>`  |  The technical support file name and location. |

### Version History

Introduced in Cumulus Linux 5.13.0

### Example

```
cumulus@switch:~$ nv action generate file-hash sha512 /var/log/text.txt
Action executing ...  
Generated Hash Checksum  
9420cdea5577569d60c986f0da39dc31be9d08a8945e42a4445c518e105cf4c3d93bc587b770bee4719836b92a65c7cb6efef283e74592f7cf3a0fc2cccc18bf  /var/log/text.txt  

Action succeeded
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv action delete system tech-support files \<file-id\></h>

Deletes the specified technical support file (a compressed archive file of useful information for troubleshooting). 

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<file-id>`  |  The technical support file name and location. |

### Version History

Introduced in Cumulus Linux 5.10.0

### Example

```
cumulus@switch:~$ nv action delete system tech-support files /var/support/cl_support_leaf01_20240725_221237.txz
Action executing ...
File Delete Succeeded
Action succeeded
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv action generate system tech-support</h>

Generates a technical support file (compressed archive file of useful information for troubleshooting). 

### Version History

Introduced in Cumulus Linux 5.10.0

### Example

```
cumulus@switch:~$ nv action generate system tech-support
Action executing ...
Generating system tech-support file, it might take a few minutes...

Action executing ...
Generated tech-support
Action succeeded
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv action import system docker image \<image-url\> repository \<repository-name\> tag \<tag-name\></h>

Imports a Docker image from an archive.

Supported archive formats include `.tar`, `.tar.gz`, `.tgz`, `.bzip`, `.tar.xz`, and `.txz`.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<image-url>`  |  The URL for the image. |
| `<repository-name>` | The name of the repository. |
| `<tag-name>`  |  The tag name. If you do not specify a tag name, the name defaults to `latest`.

### Version History

Introduced in Cumulus Linux 5.15.0

### Example

```
cumulus@switch:~$ nv action import system docker image /path/to/exampleimage.tgz repository xyz tag imported
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv action import system security crl</h>

Imports a Certificate Revocation List to verify server certificates. You can specify either `uri` (a local or remote URI from where to retrieve the crl bundle file) or `data` (for a PEM encoded CRL).

### Version History

Introduced in Cumulus Linux 5.15.0

### Example

```
cumulus@switch:~$ nv action import system security crl uri scp://user:password@hostname/path/crl.crt
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv action import system security ca-certificate \<cert-id\></h>

Imports a CA certificate.

Cumulus Linux includes a self-signed certificate and private key to use on the server so that it works out of the box. The switch generates the self-signed certificate and private key when it boots for the first time. The X.509 certificate with the public key is in `/etc/ssl/certs/cumulus.pem` and the corresponding private key is in `/etc/ssl/private/cumulus.key`.

NVIDIA recommends you use your own certificates and keys. 

- You can import a maximum of 50 CA certificates on the switch.
- The CA certificate you import contains sensitive private key information. NVIDIA recommends that you use a secure transport such as SFTP, SCP, or HTTPS.
- If the certificate is passphrase protected, you need to include the passphrase.
- You must provide a certificate ID (`<cert-id>`) to uniquely identify the certificate you import.

### Version History

Introduced in Cumulus Linux 5.7.0

### Example

```
cumulus@switch:~$ nv action import system security ca-certificate tls-cert-1 passphrase mypassphrase data "<public-key>" 
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv action import system security certificate \<cert-id\></h>

Imports an entity certificate or certificate bundle.

Cumulus Linux includes a self-signed certificate and private key to use on the server so that it works out of the box. The switch generates the self-signed certificate and private key when it boots for the first time. The X.509 certificate with the public key is in `/etc/ssl/certs/cumulus.pem` and the corresponding private key is in `/etc/ssl/private/cumulus.key`.

NVIDIA recommends you use your own certificates and keys. 

- You can import a maximum of 25 entity certificates on the switch.
- The certificate you import contains sensitive private key information. NVIDIA recommends that you use a secure transport such as SFTP, SCP, or HTTPS.
- If the certificate is passphrase protected, you need to include the passphrase.
- A certificate bundle must be in .PFX or .P12 format.
- You must provide a certificate ID (`<cert-id>`) to uniquely identify the certificate you import.

### Version History

Introduced in Cumulus Linux 5.7.0

### Example

```
cumulus@switch:~$ nv action import system security certificate tls-cert-1 passphrase mypassphrase uri-bundle scp://user@pass:1.2.3.4:/opt/certs/cert.p12
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv action install system image file \<filename\>

Installs the specified binary image on the second partition (optimized upgrade).

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<filename>` |  The binary image filename.|

### Version History

Introduced in Cumulus Linux 5.12.0

### Example

```
cumulus@switch:~$ nv action install system image files cumulus-linux-5.12.0-mlx-amd64.bin
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv action generate system file-hash</h>

Calculates and generates a unique hash value (checksum) for a file using md5, sha1, sha224, ssa256, and sha512 algorithms. A hash file checksum is a unique string of characters generated by a cryptographic hash function to represent the contents of a file allowing you to verify the integrity of the file.

### Version History

Introduced in Cumulus Linux 5.13.0

### Example

```
cumulus@switch:~$ nv action generate system file-hash md5 /var/log/text.txt  
Action executing ... 
Generated Hash Checksum  
5073306b0629c047d090e2c96b5eec4b /var/log/text.txt

Action succeeded
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv action list system file-path \<path\></h>

Lists the contents of a directory, including files, subdirectories, and other file system objects. This NVUE command is equivalent to the Linux `ls -la --full-time <path>` command.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<path>` |  The path to the directory you want to list.|

### Version History

Introduced in Cumulus Linux 5.13.0

### Example

```
cumulus@switch:~$ nv action list system file-path /var/log
Action executing ... 
[ 
     { 
        "filename": "runit", 
        "flags": "drwxr-xr-x", 
        "links": 5, 
        "owner": "root", 
        "group": "root", 
        "size": 4096, 
        "date": "2024-10-05 15:02:22.395910058 +0000", 
        "epoch": 1728140542, 
        "epoch_utc": 1728140542 
    }, 
    { *-
        "filename": "switchd.log", 
        "flags": "-rw-r-----", 
        "links": 1, 
        "owner": "root", 
        "group": "adm", 
        "size": 3886, 
        "date": "2025-02-20 16:48:23.865423228 +0000", 
        "epoch": 1740070103, 
        "epoch_utc": 1740070103 
    }, 
    { 
        "filename": "syslog.4.gz", 
        "flags": "-rw-r-----", 
        "links": 1, 
        "owner": "root", 
        "group": "adm", 
        "size": 444948, 
        "date": "2025-02-21 23:14:43.321379607 +0000", 
        "epoch": 1740179683, 
        "epoch_utc": 1740179683 
    }, 
    { 
        "filename": "wtmp", 
        "flags": "-rw-rw-r--", 
        "links": 1, 
        "owner": "root", 
        "group": "utmp", 
        "size": 14976, 
        "date": "2025-02-24 13:47:41.846513274 +0000", 
        "epoch": 1740404861, 
        "epoch_utc": 1740404861 
    }  
] 
Action succeeded
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv action lookup vrf \<vrf-id\> router fib \<address-family\> \<ip-address\></h>

Looks up the route in the routing table for a specific destination.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |  The VRF name.|
| `<address-family>` |  The address family; IPv4 or IPv6.|
| `<ip-address>` |  The IP address.|

### Version History

Introduced in Cumulus Linux 5.12.0

### Example

```
cumulus@switch:~$ nv action lookup vrf default router fib ipv4 10.10.10.3
Action executing ... 
 [{"dst":"10.10.10.3","nhid":455,"table":"default","protocol":"bgp","metric":20,"flags":[]}] 

 Action succeeded
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv action ping system \<destination\></h>

Sends Echo Request packets to a destination (IP address or a hostname) to check if it is reachable.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<destination>` |  The IP address or hostname of the destination you want to ping.|

### Version History

Introduced in Cumulus Linux 5.12.0

### Example

```
cumulus@switch:~$ nv action ping system 10.10.10.10
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv action ping system \<destination\> count</h>

Configures the number of Echo Request packets to send. You can specify a value between 1 and 10. The default packet count is 3.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<destination>` |  The IP address or hostname of the destination you want to ping.|

### Version History

Introduced in Cumulus Linux 5.12.0

### Example

```
cumulus@switch:~$ nv action ping system 10.10.10.10 count 5
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv action ping system \<destination\> do-not-fragment</h>

Configures *Do not fragment*. If the packet is larger than the maximum transmission unit (MTU) of any network segment it traverses, drop the packet instead of fragmenting the packet. 

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<destination>` |  The IP address or hostname of the destination you want to ping.|

### Version History

Introduced in Cumulus Linux 5.12.0

### Example

```
cumulus@switch:~$ nv action ping system 10.10.10.10 do-not-fragment
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv action ping system \<destination\> interval</h>

Configures how often two send Echo Request packets. You can specify a value between 0.1 and 5 seconds. The default value is 4.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<destination>` |  The IP address or hostname of the destination you want to ping.|

### Version History

Introduced in Cumulus Linux 5.12.0

### Example

```
cumulus@switch:~$ nv action ping system 10.10.10.10 interval 2
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv action ping system \<destination\> l3protocol</h>

Configures the layer 3 protocol you want to use to send the Echo Request packets. You can specify IPv4 or IPv6.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<destination>` |  The IP address or hostname of the destination you want to ping.|

### Version History

Introduced in Cumulus Linux 5.12.0

### Example

```
cumulus@switch:~$ nv action ping system 10.10.10.10 l3protocol ipv4
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv action ping system \<destination\> size</h>

Configures the packet size in bytes. You can specify a value between 1 and 9216. The default value is 64.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<destination>` |  The IP address or hostname of the destination you want to ping.|

### Version History

Introduced in Cumulus Linux 5.12.0

### Example

```
cumulus@switch:~$ nv action ping system 10.10.10.10 size 200
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv action ping system \<destination\> source</h>

Configures the source IP address from which to send the Echo Request packets.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<destination>` |  The IP address or hostname of the destination you want to ping.|

### Version History

Introduced in Cumulus Linux 5.12.0

### Example

```
cumulus@switch:~$ nv action ping system 10.10.10.10 source 10.10.5.1
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv action ping system \<destination\> source-interface</h>

Configures the source interface for which you want to test the routing path for a link local address. IPv6 only.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<destination>` |  The IP address or hostname of the destination you want to ping.|

### Version History

Introduced in Cumulus Linux 5.12.0

### Example

```
cumulus@switch:~$ nv action ping system fe80::a00:27ff:fe00:0 source-interface eth0
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv action ping system \<destination\> wait</h>

Configures the number of seconds to wait for an Echo Reply packet before the ping request times out. You can specify a value between 0.1 and 10. The default value is 10.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<destination>` |  The IP address or hostname of the destination you want to ping.|

### Version History

Introduced in Cumulus Linux 5.12.0

### Example

```
cumulus@switch:~$ nv action ping system 10.10.10.10 wait 3
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv action ping system \<destination\> vrf</h>

Configures the VRF for which you want to test the routing paths.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<destination>` |  The IP address or hostname of the destination you want to ping.|

### Version History

Introduced in Cumulus Linux 5.12.0

### Example

```
cumulus@switch:~$ nv action ping system 10.10.10.10 vrf mgmt
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv action power-cycle system</h>

Power cycles the switch remotely to recover from certain conditions, such as a thermal ASIC shutdown due to high temperatures. 

When you run the `nv action power-cycle system` command, the switch prompts you for confirmation before power cycling. To power cycle the switch without being prompted for confirmation, run the `nv action power-cycle system force` command

{{%notice note%}}
Cumulus Linux 5.15 and later no longer supports this command. Use the `nv action reboot system mode power-cycle` command instead.
{{%/notice%}}

### Version History

Introduced in Cumulus Linux 5.13.0

### Example

```
cumulus@switch:~$ nv action power-cycle system
The operation will Power Cycle the switch. 

Type [y] to power cycle. 
Type [N] to abort. 
Do you want to continue? [y/N] y 
Action executing ... 
Power cycling the switch ... 
Action executing ... 
Action succeeded
``` 

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv action pull system docker image \<image-id\></h>

Downloads a Docker image from a registry.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<image-id>` |  The Docker image ID.|

### Version History

Introduced in Cumulus Linux 5.15.0

### Example

```
cumulus@switch:~$ nv action pull system docker image nginx
```


<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv action pull system docker image \<image-id\> tag</h>

Downloads a Docker image from a registry with the specified tag name.

If you do not specify a tag name, NVUE uses the latest image.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<image-id>` |  The image ID.|

### Version History

Introduced in Cumulus Linux 5.15.0

### Example

```
cumulus@switch:~$ nv action pull system docker image nginx tag latest
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv action reboot system</h>

Reboots the switch in cold mode.

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv action reboot system
Rebooting System in cold mode
True
Action succeeded
```


<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv action reboot system mode \<mode\></h>

Reboots the switch in the mode you select: `cold`, `fast`, `halt`, `immediate`, `power-cycle`, or `warm`.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<mode-id>` |  The reboot mode.|

### Version History

Introduced in Cumulus Linux 5.15.0

### Example

```
cumulus@switch:~$ nv action reboot system mode warm
Rebooting System in cold mode
True
Action succeeded
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv action release interface \<interface-id\> ipv4 dhcp-client</h>

Releases the IPv4 DHCP client for an interface.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<interface-id>` |  The interface ID.|

### Version History

Introduced in Cumulus Linux 5.15.0

### Example

```
cumulus@switch:~$ nv action release interface swp1 ipv4 dhcp-client
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv action release interface \<interface-id\> ipv6 dhcp-client</h>

Releases the IPv6 DHCP client for an interface.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<interface-id>` |  The interface ID.|

### Version History

Introduced in Cumulus Linux 5.15.0

### Example

```
cumulus@switch:~$ nv action release interface swp1 ipv6 dhcp-client
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv action renew interface \<interface-id\> ipv4 dhcp-client</h>

Renews the current DHCPv4 lease for an interface.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<interface-id>` |  The interface ID.|

### Version History

Introduced in Cumulus Linux 5.15.0

### Example

```
cumulus@switch:~$ nv action renew interface swp1 ipv4 dhcp-client
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv action renew interface \<interface-id\> ipv6 dhcp-client</h>

Renews the current DHCPv6 lease for an interface.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<interface-id>` |  The interface ID.|

### Version History

Introduced in Cumulus Linux 5.15.0

### Example

```
cumulus@switch:~$ nv action renew interface swp1 ipv6 dhcp-client
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv action remove system docker image \<image-id\></h>

Removes a Docker image from the switch.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<image-id>` |  The image ID.|

### Version History

Introduced in Cumulus Linux 5.15.0

### Example

```
cumulus@switch:~$ nv action remove system docker image nginx
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv action remove system docker image \<image-id\> tag</h>

Removes a Docker image with a specific tag from the switch.

If you do not specify a tag name, NVUE removes the latest tagged image.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<image-id>` |  The image ID.|

### Version History

Introduced in Cumulus Linux 5.15.0

### Example

```
cumulus@switch:~$ nv action remove system docker image nginx tag latest
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv action reset platform transceiver \<port-id\></h>

Resets a specific transceiver to its initial, stable state without having to be present physically in the data center to pull the transceiver. You can specify a single port, a range of ports (such as swp1-4) or comma-separated ports (such as swp1,swp4,swp5).

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<port-id>` |  The port in which the transceiver you want to reset is attached.|

### Version History

Introduced in Cumulus Linux 5.12.0

### Example

```
cumulus@switch:~$ nv action reset platform transceiver swp1
Action executing ... 
Resetting module swp1 ... OK 
Action succeeded
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv action reset system factory-default</h>

Resets the switch to the factory defaults and removes all configuration, system files, and log files. When you perform a factory reset, the currently installed image remains on the switch.

{{%notice note%}}
- To run factory reset with NVUE commands, the `nvued` service must be running.
- When you run the NVUE factory reset commands, the switch prompts you to confirm that you want to continue. To run the commands without the prompts to continue, add the `force` option at the end of the command.
- The switch always reboots in cold mode after a factory reset even if the switch is in warm boot mode when you run factory reset commands.
- If ZTP fails (the ZTP configuration file is not present, there is no USB drive, or there are DHCP errors), factory reset continues successfully; ZTP is a separate task and does not affect the factory reset status.
- If there is an issue when running factory reset, the switch reverts to the previous configuration and logs the exceptions and errors.
- The factory reset command is similar to the onie-select -k command; however, onie-select -k also removes the installed image.
{{%/notice%}}

### Version History

Introduced in Cumulus Linux 5.11.0

### Example

```
cumulus@switch:~$ nv action reset system factory-default
This operation will reset the system configuration, delete the log files and reboot the switch.
Type [y] continue. 
Type [n] to abort. 
Do you want to continue? [y/n] y
...
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv action reset system factory-default keep basic</h>

Resets the switch to the factory defaults but keeps password policy rules, management interface configuration (such as eth0), local user accounts and roles, and SSH configuration.

{{%notice note%}}
- To run factory reset with NVUE commands, the `nvued` service must be running.
- When you run the NVUE factory reset commands, the switch prompts you to confirm that you want to continue. To run the commands without the prompts to continue, add the `force` option at the end of the command.
- The switch always reboots in cold mode after a factory reset even if the switch is in warm boot mode when you run factory reset commands.
- If ZTP fails (the ZTP configuration file is not present, there is no USB drive, or there are DHCP errors), factory reset continues successfully; ZTP is a separate task and does not affect the factory reset status.
- If there is an issue when running factory reset, the switch reverts to the previous configuration and logs the exceptions and errors.
- The factory reset command is similar to the onie-select -k command; however, onie-select -k also removes the installed image.
{{%/notice%}}

### Version History

Introduced in Cumulus Linux 5.11.0

### Example

```
cumulus@switch:~$ nv action reset system factory-default keep basic
This operation will keep only the basic system configuration, delete the log files and reboot the switch.
Type [y] to continue. 
Type [n] to abort. 
Do you want to continue? [y/n] y
...
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv action reset system factory-default keep all-config</h>

Resets the switch to the factory defaults but keeps all configuration.

{{%notice note%}}
- To run factory reset with NVUE commands, the `nvued` service must be running.
- When you run the NVUE factory reset commands, the switch prompts you to confirm that you want to continue. To run the commands without the prompts to continue, add the `force` option at the end of the command.
- The switch always reboots in cold mode after a factory reset even if the switch is in warm boot mode when you run factory reset commands.
- If ZTP fails (the ZTP configuration file is not present, there is no USB drive, or there are DHCP errors), factory reset continues successfully; ZTP is a separate task and does not affect the factory reset status.
- If there is an issue when running factory reset, the switch reverts to the previous configuration and logs the exceptions and errors.
- The factory reset command is similar to the onie-select -k command; however, onie-select -k also removes the installed image.
{{%/notice%}}

### Version History

Introduced in Cumulus Linux 5.11.0

### Example

```
cumulus@switch:~$ nv action reset system factory-default keep all-config
This operation will not reset the system configuration, only delete the log files and reboot the switch.
Type [y] to continue.
Type [n] to abort.
Do you want to continue? [y/n] y 
...
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv action reset system factory-default keep only-files</h>

Resets the switch to the factory defaults but keeps all system files and log files

{{%notice note%}}
- To run factory reset with NVUE commands, the `nvued` service must be running.
- When you run the NVUE factory reset commands, the switch prompts you to confirm that you want to continue. To run the commands without the prompts to continue, add the `force` option at the end of the command.
- The switch always reboots in cold mode after a factory reset even if the switch is in warm boot mode when you run factory reset commands.
- If ZTP fails (the ZTP configuration file is not present, there is no USB drive, or there are DHCP errors), factory reset continues successfully; ZTP is a separate task and does not affect the factory reset status.
- If there is an issue when running factory reset, the switch reverts to the previous configuration and logs the exceptions and errors.
- The factory reset command is similar to the onie-select -k command; however, onie-select -k also removes the installed image.
{{%/notice%}}


### Version History

Introduced in Cumulus Linux 5.11.0

### Example

```
cumulus@switch:~$ nv action reset system factory-default keep only-files
This operation will reset the system configuration, not delete the log files and reboot the switch.
Type [y] to continue. 
Type [n] to abort. 
Do you want to continue? [y/n] y 
...
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv action rotate system log</h>

Rotates the system log files. Cumulus Linux automatically manages log file size, preventing the logs from filling the storage space and slowing down the system.

### Version History

Introduced in Cumulus Linux 5.10.0

### Example

```
cumulus@switch:~$ nv action rotate system log
Action executing ...
Log rotation successful
Action succeeded
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv action run system docker <container-id> image <image></h>

Creates and runs a new Docker container from an image.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<continer-id>` |  The docker container ID.|
| `<image-id>` |  The image ID.|

### Version History

Introduced in Cumulus Linux 5.15.0

### Example

```
cumulus@switch:~$ nv action run system docker container CONTAINER1 image nginx options '\-\-storage-opt size=120G'
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv action run system ztp</h>

Manually runs ZTP from the beginning. If you made manual configuration changes, ZTP considers the switch as already provisioned and exits.

You can also specify a custom URL (`nv action run system ztp url <url-and-filename`) or directory (`nv action run system ztp url <directory-and-filename`) on the switch for the ZTP script.

### Version History

Introduced in Cumulus Linux 5.11.0

### Example

```
cumulus@switch:~$ nv action run system ztp
The operation will perform rerun of the ZTP.
Type [y] to perform rerun of the ZTP.
Type [N] to cancel an action.

Do you want to continue? [y/N]
```

If you add the force option (`nv action run system ztp force`), ZTP runs without prompting you for confirmation.

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv action schedule system telemetry hft job \<date-time\> duration \<duration\> profile \<profile\> ports \<port-id\> description \<text\></h>

Configures the schedule for a high frequency telemetry data collection.

{{%notice note%}}
- You can schedule a maximum of 10 sessions (jobs). The switch can retain data for 10 jobs (completed, cancelled, or failed) in addition to the active jobs.
- You must configure data export (the target) before you can configure the schedule.
{{%/notice%}}

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<date-time>` |  The start date and time for high frequency telemetry data collection in `YYYY-MM-DD HH:MM:SS` format. |
| `duration` | The session duration in seconds. The default value is 20 seconds. |
| `profile-id` | The high frequency telemetry data collection profile name. |
| `port-id` | The ports on which you want to collect the data. You can specify a range of ports, multiple comma separated ports, or `all` for all the ports. The default value is `all`. |
| `<text>` | A short reason why you are collecting the data. If the description contains more than one word, you must enclose the description in quotes. A description is optional.|

### Version History

Introduced in Cumulus Linux 5.10.0

### Example

```
cumulus@switch:~$ nv action schedule system telemetry hft job 2024-07-17 10:00:00 duration 30 profile profile1 ports swp1-swp9 description "bandwidth profiling"
Action executing ...
Job schedule successfull.

Action succeeded
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv action start system docker container \<container-name\> image \<image-id\></h>

Creates and runs a new Docker container from an image.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<image-id>` |  The image ID.|
| `<container-name>` |  The container name.|

### Version History

Introduced in Cumulus Linux 5.15.0

### Example

```
cumulus@switch:~$ nv action start system docker container CONTAINER1 image nginx
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv action remove system docker container \<container-name\></h>

Deletes a Docker container.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<container-name>` |  The hexadecimal string or name of the container.|

### Version History

Introduced in Cumulus Linux 5.15.0

### Example

```
cumulus@switch:~$ nv action remove system docker container CONTAINER1
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv action stop system docker container \<container-name\></h>

Stops a Docker container.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<container-name>` |  The hexadecimal string or name of the container.|

### Version History

Introduced in Cumulus Linux 5.15.0

### Example

```
cumulus@switch:~$ nv action stop system docker container CONTAINER1
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv action traceroute system \<destination\></h>

Sends traceroute packets to a destination so you can validate the route. You can specify either an IP address or a domain name.

### Command Syntax

| Syntax   |  Description  |
| ----------    | ------------  |
| `<destination>` |  The IP address or a domain name.  |

### Version History

Introduced in Cumulus Linux 5.12.0

### Example

```
cumulus@switch:~$ nv action traceroute system 10.10.10.10
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv action traceroute system \<destination\> do-not-fragment</h>

Drops the traceroute packet instead of fragmenting it if the packet is larger than the maximum transmission unit (MTU) of any network segment it traverses.

### Command Syntax

| Syntax   |  Description  |
| ----------    | ------------  |
| `<destination>` |  The IP address or a domain name.  |

### Version History

Introduced in Cumulus Linux 5.12.0

### Example

```
cumulus@switch:~$ nv action traceroute system 10.10.10.10 do-not-fragment
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv action traceroute system \<destination\> initial-ttl</h>

Sends traceroute packets to the destination with the minimum number of hops specified. You can specify a value between 1 and 30. The default value is 1.

The minimum number of hops must be less than or equal to the maximum number of hops.

### Command Syntax

| Syntax   |  Description  |
| ----------    | ------------  |
| `<destination>` |  The IP address or a domain name.  |

### Version History

Introduced in Cumulus Linux 5.12.0

### Example

```
cumulus@switch:~$ nv action traceroute system 10.10.10.10 initial-ttl 3
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv action traceroute system \<destination\> l3protocol</h>

Sends layer 3 traceroute packets to the destination specified. You can specify `ipv4` or `ipv6`. The default is `ipv4`.

### Command Syntax

| Syntax   |  Description  |
| ----------    | ------------  |
| `<destination>` |  The IP address or a domain name.  |

### Version History

Introduced in Cumulus Linux 5.12.0

### Example

```
cumulus@switch:~$ nv action traceroute system fe80::a00:27ff:fe00:0 l3protocol ipv6
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv action traceroute system \<destination\> l4protocol</h>

Sends the specified layer 4 traceroute packets to the destination. You can specify `icmp`, `tcp`, or `udp`. The default is `icmp`.

### Command Syntax

| Syntax   |  Description  |
| ----------    | ------------  |
| `<destination>` |  The IP address or a domain name.  |

### Version History

Introduced in Cumulus Linux 5.12.0

### Example

```
cumulus@switch:~$ nv action traceroute system 10.10.10.10 l4protocol udp
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv action traceroute system \<destination\> max-ttl</h>

Sends traceroute packets to the destination with the minimum number of hops specified. You can specify a value between 1 and 30.

### Command Syntax

| Syntax   |  Description  |
| ----------    | ------------  |
| `<destination>` |  The IP address or a domain name.  |

### Version History

Introduced in Cumulus Linux 5.12.0

### Example

```
cumulus@switch:~$ nv action traceroute system 10.10.10.10 max-ttl 10
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv action traceroute system \<destination\> source-address</h>

Sends traceroute packets to the destination from the specified source IP address.

### Command Syntax

| Syntax   |  Description  |
| ----------    | ------------  |
| `<destination>` |  The IP address or a domain name.  |

### Version History

Introduced in Cumulus Linux 5.12.0

### Example

```
cumulus@switch:~$ nv action traceroute system 10.10.10.10 source-address 10.10.5.1
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv action traceroute system \<destination\> vrf</h>

Sends traceroute packets to the destination using the specified VRF.

### Command Syntax

| Syntax   |  Description  |
| ----------    | ------------  |
| `<destination>` |  The IP address or a domain name.  |

### Version History

Introduced in Cumulus Linux 5.12.0

### Example

```
cumulus@switch:~$ nv action traceroute system 10.10.10.10 vrf RED
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv action traceroute system \<destination\> wait</h>

Sends traceroute packets to the destination and waits for the specified maximum number of nanoseconds for a response from each hop. You can specify a value between 0.1 and 10.

### Command Syntax

| Syntax   |  Description  |
| ----------    | ------------  |
| `<destination>` |  The IP address or a domain name.  |

### Version History

Introduced in Cumulus Linux 5.12.0

### Example

```
cumulus@switch:~$ nv action traceroute system 10.10.10.10 wait 2
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv action upgrade system packages to latest use-vrf \<vrf-id\></h>

Upgrades all the packages to the latest distribution.

By default, the NVUE `nv action upgrade system packages` command runs in the management VRF. To run the command in a non-management VRF such as `default`, you must use the `use-vrf <vrf-id>` option.

### Command Syntax

| Syntax   |  Description  |
| ----------    | ------------  |
| `<vrf-id>` |  The VRF name.  |

### Version History

Introduced in Cumulus Linux 5.9.0

### Example

```
cumulus@switch:~$ nv action upgrade system packages to latest use-vrf default
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv action upgrade system packages to latest use-vrf \<vrf\> dry-run</h>

Fetches the latest update metadata from the repository so you can review potential upgrade issues (in some cases, upgrading new packages might also upgrade additional existing packages due to dependencies).

By default, the NVUE `nv action upgrade system packages` command runs in the management VRF. To run the command in a non-management VRF such as `default`, you must use the `use-vrf <vrf-id>` option.

### Command Syntax

| Syntax   |  Description  |
| ----------    | ------------  |
| `<vrf-id>` |  The VRF name.  |

### Version History

Introduced in Cumulus Linux 5.9.0

### Example

```
cumulus@switch:~$ nv action upgrade system packages to latest use-vrf default dry-run
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv action upload tech-support files \<file-id\> \<remote-url\></h>

Uploads a technical support file (`cl-support`) off the switch to an external location.

### Command Syntax

| Syntax   |  Description  |
| ----------    | ------------  |
| `<file-id>` |  The technical support file you want to upload.  |
| `<remote-url>` |  The URL to where you want to upload the technical support file.  |

### Version History

Introduced in Cumulus Linux 5.10.0

### Example

```
cumulus@switch:~$ nv action upload tech-support files cl_support_leaf01_20240725_225811.txz scp://root@host1:/home/tech-support/
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv action upload system health history files \<file-name\></h>

Uploads the specified health history report file.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<file-name>` | The name of the system health history report file. |

### Version History

Introduced in Cumulus Linux 5.15.0

### Example

```
cumulus@switch:~$ nv action upload system health history files FILE1
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv action upload system telemetry hft job \<hft-job-id\> \<remote-url\></h>

Uploads high frequency telemetry data for a specific session (job) off the switch to an external location.

### Command Syntax

| Syntax   |  Description  |
| ----------    | ------------  |
| `<hft-job-id>` |  The job ID. You can see the list of jobs with the `nv show system telemetry hft job` command.  |
| `<remote-url>` |  The URL to where you want to upload the data.  |

### Version History

Introduced in Cumulus Linux 5.10.0

### Example

```
cumulus@switch:~$ nv action upload system telemetry hft job 1 scp://root@host1:/home/telemetry/
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show action</h>

Shows actions, such as cleared interface counters and routes, removed protodown MLAG bond conflicts, and disconnected system users.

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@switch:~$ nv show action
id  state         
--  --------------
1   action_success
2   action_error  
3   action_success
4   action_success 
5   action_success
6   action_success
```
