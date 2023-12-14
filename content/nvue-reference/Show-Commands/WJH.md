---
title: WJH
author: Cumulus Networks
weight: 460

type: nojsscroll
---
<style>
h { color: RGB(118,185,0)}
</style>
<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system wjh</h>

Shows <span class="a-tooltip">[WJH](## "What Just Happened")</span> configuration on the switch. WJH provides real time visibility into network problems.

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv show system wjh
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system wjh channel</h>

Shows WJH channel configuration on the switch.

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv show system wjh channel
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system wjh channel \<channel-id\></h>

Shows configuration for the specified WJH channel on the switch.

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv show system wjh channel forwarding
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system wjh channel \<channel-id\> trigger</h>

Shows the configuration for packet drop categories in a WJH channel.

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv show system wjh channel forwarding trigger
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system wjh packet-buffer</h>

Shows all dropped packets monitored by WJH and the reason for the drop.

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv show system wjh packet-buffer
#   dMAC  dPort  Dst IP:Port  EthType  Drop group  IP Proto  Drop reason - Recommended action                         Severity  sMAC  sPort    Src IP:Port  Timestamp              VLAN
--  ----  -----  -----------  -------  ----------  --------  -------------------------------------------------------  --------  ----  -------  -----------  ---------------------  ----
1   N/A   N/A    N/A          N/A      L1          N/A       Generic L1 event - Check layer 1 aggregated information  Warn      N/A   swp17    N/A          22/11/03 01:00:35.458  N/A
2   N/A   N/A    N/A          N/A      L1          N/A       Generic L1 event - Check layer 1 aggregated information  Warn      N/A   swp18    N/A          22/11/03 01:00:35.458  N/A
3   N/A   N/A    N/A          N/A      L1          N/A       Generic L1 event - Check layer 1 aggregated information  Warn      N/A   swp19    N/A          22/11/03 01:00:35.458  N/A
4   N/A   N/A    N/A          N/A      L1          N/A       Generic L1 event - Check layer 1 aggregated information  Warn      N/A   swp20    N/A          22/11/03 01:00:35.458  N/A
```
