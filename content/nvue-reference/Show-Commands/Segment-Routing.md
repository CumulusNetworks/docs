---
title: Segment Routing
author: Cumulus Networks
weight: 357

type: nojsscroll
---
<style>
h { color: RGB(118,185,0)}
</style>
<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show router segment-routing</h>

Shows if segment routing is enabled, and to show the configured locators and SRv6 segment identifiers.

### Version History

Introduced in Cumulus Linux 5.14.0

### Example

```
cumulus@switch:~$ nv show router segment-routing
              operational   applied             
------------  --------      --------------------
srv6                                        
  state       disabled      enabled             
  [locator]                 LEAF                
static                                      
  [srv6-sid]                 2001:db8:1:1::100/48
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show router segment-routing srv6</h>

Shows SRv6 configuration.

### Version History

Introduced in Cumulus Linux 5.14.0

### Example

```
cumulus@switch:~$ nv show router segment-routing srv6
          applied   pending
---------  --------  -------
state      disabled  enabled
[locator]            LEAF  
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show router segment-routing srv6 stats</h>

Shows counter values for all SRv6 segment identifiers.

### Version History

Introduced in Cumulus Linux 5.14.0

### Example

```
cumulus@switch:~$ nv show router segment-routing srv6 stats
Hit Counters
------------------------------
SID                                             Packets
---------------------------------------      ----------
2001:db8:1:1::100/48                                   0
2001:db8:1:1::101/48                                   0

Drop Counters
------------------------------
Total no-sid-dropped packets
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show router segment-routing srv6 stats sid <sid></h>

Shows counter values for a specific SRv6 segment identifier.

### Version History

Introduced in Cumulus Linux 5.14.0

### Example

```
cumulus@switch:~$ nv show router segment-routing srv6 stats sid 2001:db8:1:1::100/48
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show router segment-routing srv6 stats no-sid-drops</h>

Shows the number of non-SID dropped packets.

### Version History

Introduced in Cumulus Linux 5.14.0

### Example

```
cumulus@switch:~$ nv show router segment-routing srv6 stats no-sid-drops
                        operational
----------------------  -----------
no-sid-dropped-packets  0
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show router segment-routing srv6 locator</h>

Shows SRv6 locator configuration.

### Version History

Introduced in Cumulus Linux 5.14.0

### Example

```
cumulus@switch:~$ nv show router segment-routing srv6 locator
No Data
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show router segment-routing srv6 locator \<locator-name\></h>

Shows the configuration for a specific SRv6 locator.

### Version History

Introduced in Cumulus Linux 5.14.0

### Example

```
cumulus@switch:~$ nv show router segment-routing srv6 locator LEAF
              operational  applied          
------------  -----------  -------
prefix                     2001:db8:1:1::/32
block-length               16               
node-length                16               
func-length                0
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show router segment-routing static</h>

Shows static segment routing configuration.

### Version History

Introduced in Cumulus Linux 5.14.0

### Example

```
cumulus@switch:~$ nv show router segment-routing static
           applied  pending             
----------  -------  --------------------
[srv6-sid]           2001:db8:1:1::100/48
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show router segment-routing static srv6-sid <sid></h>

Shows information about a specific SRv6 static segment identifier.

### Version History

Introduced in Cumulus Linux 5.14.0

### Example

```
cumulus@switch:~$ nv show router segment-routing static srv6-sid 2001:db8:1:1::100/48
              applied  pending
------------  -------  -------
locator-name           LEAF   
behavior               uA     
interface              swp1 
```
