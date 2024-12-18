---
title: Log Files with NVUE
author: NVIDIA
weight: 145
toc: 3
---
NVUE provides commands to:
- Show the current system logging configuration and the contents of the log files on the switch.
- Upload log files to a remote URL
- Delete log files

## Show System Logging Configuration

To show the current system log configuration on the switch, run the `nv show system log` command:

```
cumulus@switch:~$ nv show system log
```

## Show System Log Files

To show the contents of the most current system log file, run the `nv show system log file` command. The contents are shown with the `less` command, which enables you to scroll through the file interactively. The `less` command is typically used to view the most recent log entries.

```
cumulus@switch:~$ nv show system log file
```

The `nv show system log file` command provides the following options:

| Option  | Description |
| ------- | ----------- |
| `brief` | Shows the contents of the most current system log file but in a more concise format. |
| `follow`| Shows the contents of a system log file in real-time.  The command shows the log file output continuously as it is updated, similar to the behavior of the `tail -f` command.|
| `list` |  Shows the available system log files on the system with their filenames and corresponding file paths. |
| `<file-name>`|  Shows the contents of a specific system log file. If the file is a regular log file (such as `syslog.1`), the system uses `less` so that you can scroll and search through the log entries. If the file is compressed (such as `syslog.2.gz`), the system displays the contents without decompressing the file. This command is useful for viewing both archived and compressed log files.|

The following example shows the contents of the most current system log file:

```
cumulus@switch:~$ nv show system log file
```

The following example shows the contents of the most current system log file in a more concise format:

```
cumulus@switch:~$ nv show system log file brief
```

The following example shows the contents of a system log file in real-time:

```
cumulus@switch:~$ nv show system log file follow
```

The following example shows the available system log files on the system with their filenames and corresponding file paths:

```
cumulus@switch:~$ nv show system log file list
```

The following example shows the contents of `syslog.1`

```
cumulus@switch:~$ nv show system log file syslog.1
```

## Show Components Generating the Logs

To show the components of the system generating the logs and the log severity levels associated with each component, run the `nv show system log component` command.

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

The `nv show system log component` command provides the following options:

| Option  | Description |
| ------- | ----------- |
| `<component-name> file` | Shows the contents of the most current file for a specific component. The system uses the `less` command so that you can scroll through the file interactively. |
|  `<component-name> file list` | Provides a list of log files for the specified component and shows the associated logs.|

{{< expand "Component File List" >}}
| System Component  | Files |
| ---------- | ----------- |
| `apt` | All files in the `/var/log/apt` directory. The most current file is `history.log`. |
| `routing` | All files in `/var/log/frr` directory. The most current file is `frr.log`.  |
| `auth` | `auth.log` |
| `audit` | All files in the `/var/log/audit` directory.|
| `boot` | `boot.log`|
| `dpkg` | All files in the `/var/log/dpkg` directory. |
| `installer` | All files in the `/var/log/installer` directory. |
| `stp` | `mstpd.log` |
| `nvue` | `nvued.log`, `nv-cli.log`. The most current file is `nvued.log` |
| `otlp-telemetry` | All files in the `/var/log/otlp-telemetry` directory. |
| `nv-telemetry` | All files in the `/var/log/nv-telemetry` directory. |
| `mlag` | `clagd.log` |
| `csmgr` | `csmgrd.log`, `cl-system-services.log` |
| `platform-thermal` | `tc_log` |
| `ptp` | `ptp4l.log` |
| `synce` | `synced.log`, `synced.log`, `synced-selector.log` |
| `pps` | `ts2phc.log` |
| `platform-phc` | `phc2sys.log` |
| `ptp-firefly-servo` |
| `ptm` | `ptmd.log` |
| `ifupdown2` | `ifupdown2/*/ifupdown2.debug.log` |
| `nginx` | All files in the `nginx` folder. The most current file is `access.log`. |
| `datapath` | `mswitchd.log` |
{{< /expand >}}

The following example shows the contents of the most current file for NVUE:

```
cumulus@switch:~$ nv show system log component nvue file
```

The following example shows the log files and associated logs for NVUE:

```
cumulus@switch:~$ nv show system log component nvue file list 
```

## Upload System Log Files to a Remote URL

You can transfer specific log files or system component-specific log files for remote analysis, backup, or troubleshooting, you can upload the file to a remote URL or server.

To upload a specific system log file to a remote URL, run the `nv action upload system log file <file-name> <remote-url-upload>` command:

```
cumulus@switch:~$ nv action upload system log file mstpd.log <remote-url-upload> 
```

To upload a system component-specific log file to a remote URL, run the `nv action upload system log component <component-name> file <file-name> <remote-url-upload>` command.

```
cumulus@switch:~$ nv action upload system log component nvue file nvued.log <remote-url-upload> 
```

You can perform the upload within a specific VRF context; for example:

```
cumulus@switch:~$ nv action upload system log component nvue file nvued.log <remote-url-upload> vrf RED
```

## Delete System Log Files

Deleting log files enables you to manage storage space and ensure that only relevant logs remain. You typically delete log files after you upload or archive them, or when you no longer need the logs for troubleshooting or auditing.
Log file deletion is a crucial step in log management to ensure that outdated or irrelevant data does not occupy system resources.

To delete a log file, run the `nv action delete system log file <file-name>` command:

```
cumulus@switch:~$ nv action delete system log file mstpd.log 
```

To delete a log file from a specific system component, run the `nv action delete system log component <component-name> file <file-name>` command:

```
cumulus@switch:~$ nv action delete system log component nvue file nvued.log
```
