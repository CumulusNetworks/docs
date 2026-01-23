---
title: cl-support File
author: Cumulus Networks
weight: 145

type: nojsscroll
---
<style>
h { color: RGB(118,185,0)}
</style>
<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system tech-support auto-generation</h>

Shows if automatic cl-support file generation is active or inactive, and the reason for deactivation.

The switch generates the cl-support file automatically:
- When there is a core dump file in the /var/support/core directory for any application that Linux distributions support.
- When one of the monitored services fails for the first time after you reboot or power cycle the switch.

`cl-support` files can generate in quick succession due to a chain of faults, which burdens system resources and causes system instability. When this occurs, the switch deactivates automatic cl-support file generation and preserves the first cl-support file (which contains relevant diagnostic information) for troubleshooting.

### Version History

Introduced in Cumulus Linux 5.16.0

### Example

```
cumulus@switch:~$ nv show system tech-support auto-generation
                           operational                                                                                                                                                               applied
--------------         -----------------------------------------------------------------------------                                                  -------
state                    disabled                                                                                                             enabled
burst-duration      7200                                                                                                                    7200   
burst-size            5                                                                                                                          5      
reason                  found core file(s): lldpd.346499.1768799305.core lldpd.346502.1768799305.core         
support-file          /var/support/cl_support_cumulus_20260119_050826.txz                                   

Recovery Steps
=================
    Step  Action                                                                                                       
    ----  -------------------------------------------------------------------------------------------------------------
    1     Verify system health (CPU, memory, storage)                                                                  
    2     Collect the support files                                                                                    
    3     Re-activate tech support generation service manually "nv action activate system tech-support auto-generation”
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system tech-support files</h>

Shows the `cl-support` files on the switch. The `cl-support` script generates a compressed archive file of useful information for troubleshooting. The system either creates the file automatically or you can create the file manually.

### Version History

Introduced in Cumulus Linux 5.10.0

### Example

```
cumulus@switch:~$ nv show system tech-support files
File name                              File path                                         
-------------------------------------  --------------------------------------------------
cl_support_leaf01_20240725_225811.txz  /var/support/cl_support_leaf01_20240725_225811.txz
```
