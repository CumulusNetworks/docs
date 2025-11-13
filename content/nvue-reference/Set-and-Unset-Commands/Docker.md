---
title: Docker
author: Cumulus Networks
weight: 555

type: nojsscroll
---
<style>
h { color: RGB(118,185,0)}
</style>
{{%notice note%}}
The `nv unset` commands remove the configuration you set with the equivalent `nv set` commands. This guide only describes an `nv unset` command if it differs from the `nv set` command.
{{%/notice%}}

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system docker state</h>

Enables and disables the Docker service.

The Docker package installs as part of the Cumulus Linux installation or ONIE upgrade process and the service is running by default. The Docker package includes Docker Engine, and dependencies and configuration files required to run the Docker service.

### Version History

Introduced in Cumulus Linux 5.15.0

### Example

```
cumulus@switch:~$ nv set system docker state disabled
```

{{%notice note%}}
The What Just Happened (WJH) service relies on Docker. If you disable Docker, WJH must also be disabled.
{{%/notice%}}

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system docker vrf \<vrf-name\></h>

Sets the VRF in which to run the Docker service. By default, the Docker service runs in the management VRF.

{{%notice note%}}
Changing the Docker VRF restarts the Docker service, which disrupts all running containers.
{{%/notice%}}

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `vrf-id` | The VRF in which to run the Docker service. |

### Version History

Introduced in Cumulus Linux 5.15.0

### Example

```
cumulus@switch:~$ nv set system docker vrf RED
```
