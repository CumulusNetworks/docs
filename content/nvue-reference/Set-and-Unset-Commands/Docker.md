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

Introduced in Cumulus Linux 5.13.0

### Example

```
cumulus@switch:~$ nv set system docker vrf RED
```
