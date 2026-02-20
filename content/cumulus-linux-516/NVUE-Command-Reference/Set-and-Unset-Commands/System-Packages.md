---
title: System Packages
author: Cumulus Networks
weight: 772

type: nojsscroll
---
<style>
h { color: RGB(118,185,0)}
</style>
{{%notice note%}}
The `nv unset` commands remove the configuration you set with the equivalent `nv set` commands. This guide only describes an `nv unset` command if it differs from the `nv set` command.
{{%/notice%}}

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system packages repository \<repository\> distribution \<distribution\> pool \<pool-id\></h>

Configures the distribution pool for the repository from which you want to add packages.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<repository>` | The repository URL in https or http format, or the directory and file name on the switch (`/etc/myrepo`).|
| `<distribution>` | The repository distribution. |
| `<pool-id>` | The repository distribution pool. |

### Version History

Introduced in Cumulus Linux 5.12.0

### Example

```
cumulus@switch:~$ nv set system packages repository http://test.myrepo.com distribution mydist pool mypool
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system packages repository \<repository\> insecure</h>

Configures the repository from which you want to add packages to trusted.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<repository>` | The repository URL in https or http format, or the directory and file name on the switch (`/etc/myrepo`).|

### Version History

Introduced in Cumulus Linux 5.12.0

### Example

```
cumulus@switch:~$ nv set system packages repository http://test.myrepo.com insecure enabled
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system packages repository \<repository\> key \<key\></h>

Configures the secure key for the repository from which you want to add packages.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<repository>` | The repository URL in https or http format, or the directory and file name on the switch (`/etc/myrepo`).|
| `<key>` |  The secure key. |

### Version History

Introduced in Cumulus Linux 5.12.0

### Example

```
cumulus@switch:~$ nv set system packages repository http://test.myrepo.com key thekey.asc
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system packages repository \<repository\> source</h>

Enables adding source files from the specified repository.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<repository>` | The repository URL in https or http format, or the directory and file name on the switch (`/etc/myrepo`).|

### Version History

Introduced in Cumulus Linux 5.12.0

### Example

```
cumulus@switch:~$ nv set system packages repository http://test.myrepo.com source enabled
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system packages use-vrf</h>

Configures the VRF to use when adding an additional repository. The default VRF is `mgmt`.

### Version History

Introduced in Cumulus Linux 5.12.0

### Example

```
cumulus@switch:~$ nv set system packages use-vrf default
```
