---
title: System Logs
author: Cumulus Networks
weight: 405

type: nojsscroll
---
<style>
h { color: RGB(118,185,0)}
</style>
<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system log</h>

Shows the current system log configuration on the switch.

### Version History

Introduced in Cumulus Linux 5.12.0

### Example

```
cumulus@switch:~$ nv show system log
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system log component</h>

Shows the components of the system generating the logs and the log severity levels associated with each component.

### Version History

Introduced in Cumulus Linux 5.12.0

### Example

```
cumulus@switch:~$ nv show system log component 
Component         Level 
----------------  ------ 
nvue             info  
orchagent         notice 
portsyncd         notice 
sai_api_port      notice 
sai_api_switch    notice 
symmetry-manager  info  
syncd             notice
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system log component \<component-name\> file</h>

Shows the contents of the most current file for a specific component. The system uses the less command so that you can scroll through the file interactively.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<component-name>` | The system component whose log file contents you want to see. |

### Version History

Introduced in Cumulus Linux 5.12.0

### Example

```
cumulus@switch:~$ nv show system log component nvue file
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system log component \<component-name\> file list</h>

Shows a list of log files for the specified component and shows the associated logs.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<component-name>` | The system component whose list of log files you want to see. |

### Version History

Introduced in Cumulus Linux 5.12.0

### Example

```
cumulus@switch:~$ nv show system log component nvue file list
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system log file</h>

Shows the contents of the most current system log file.

### Version History

Introduced in Cumulus Linux 5.12.0

### Example

```
cumulus@switch:~$ nv show system log file
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system log file \<file-name\></h>

Shows the contents of a specific system log file. If the file is a regular log file (such as syslog.1), the system uses less so that you can scroll and search through the log entries. If the file is compressed (such as syslog.2.gz), the system displays the contents without decompressing the file. This command is useful for viewing both archived and compressed log files.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<file-name>` | The system log file you want to view. |

### Version History

Introduced in Cumulus Linux 5.12.0

### Example

```
cumulus@switch:~$ nv show system log file syslog.1
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system log file brief</h>

Shows the contents of the most current system log file in a concise format.

### Version History

Introduced in Cumulus Linux 5.12.0

### Example

```
cumulus@switch:~$ nv show system log file brief
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system log file follow</h>

Shows the contents of a system log file in real-time. The command shows the log file output continuously as it is updated, similar to the behavior of the tail -f command.

### Version History

Introduced in Cumulus Linux 5.12.0

### Example

```
cumulus@switch:~$ nv show system log file follow
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system log file list</h>

Shows the available system log files on the system with their filenames and corresponding file paths.

### Version History

Introduced in Cumulus Linux 5.12.0

### Example

```
cumulus@switch:~$ nv show system log file list
```
