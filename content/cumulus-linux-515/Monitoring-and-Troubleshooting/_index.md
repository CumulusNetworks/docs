---
title: Monitoring and Troubleshooting
author: NVIDIA
weight: 1010
toc: 2
---
This chapter introduces the basics for monitoring and troubleshooting Cumulus Linux.

## Serial Console

Use the serial console to debug issues if you reboot the switch often or if you do not have a reliable network connection.

The default serial console baud rate is 115200, which is the baud rate {{<exlink url="http://opencomputeproject.github.io/onie" text="ONIE">}} uses.

### Configure the Serial Console

On x86 switches, you configure serial console baud rate by editing `grub`.

{{%notice warning%}}
Incorrect configuration settings in `grub` cause the switch to be inaccessible through the console. Review `grub` changes before you implement them.
{{%/notice%}}

The valid values for the baud rate are:

- 300
- 600
- 1200
- 2400
- 4800
- 9600
- 19200
- 38400
- 115200

To change the serial console baud rate:

1. Edit the `/etc/default/grub` file and provide a valid value for the `--speed` and `console` variables:

   ```
   GRUB_SERIAL_COMMAND="serial --port=0x2f8 --speed=115200 --word=8 --parity=no --stop=1"
   GRUB_CMDLINE_LINUX="console=ttyS1,115200n8 cl_platform=accton_as5712_54x"
   ```

2. After you save your changes to the grub configuration, type the following at the command prompt:

   ```
   cumulus@switch:~$ update-grub
   ```

3. If you plan on accessing the switch BIOS over the serial console, you need to update the baud rate in the switch BIOS. For more information, see [this knowledge base article]({{<ref "/knowledge-base/Configuration-and-Usage/Administration/Accessing-the-BIOS-on-an-x86-Switch" >}}).

4. Reboot the switch.

### Change the Console Log Level

By default, the console prints all log messages except debug messages. To tune console logging to be less verbose so that certain levels of messages do not print, run the `dmesg -n <level>` command, where the log levels are:

| Level | Description                                                                          |
| ----- | ------------------------------------------------------------------------------------ |
| 0     | Emergency messages (the system is about to crash or is unstable).                    |
| 1     | Serious conditions; you must take action immediately.                                |
| 2     | Critical conditions (serious hardware or software failures).                         |
| 3     | Error conditions (often used by drivers to indicate difficulties with the hardware). |
| 4     | Warning messages (nothing serious but might indicate problems).                      |
| 5     | Message notifications for many conditions, including security events.                |
| 6     | Informational messages.                                                              |
| 7     | Debug messages.                                                                      |

Only messages with a value lower than the level specified print to the console. For example, if you specify level **3**, only level 2 (critical conditions), level 1 (serious conditions), and level 0 (emergency messages) print to the console:

```
cumulus@switch:~$ sudo dmesg -n 3
```

You can also run `dmesg --console-level <level>` command, where the log levels are `emerg`, `alert`, `crit`, `err`, `warn`, `notice`, `info`, or `debug`. For example, to print critical conditions, run the following command:

```
cumulus@switch:~$ sudo dmesg --console-level crit
```

The `dmesg` command applies until the next reboot.

For more details about the `dmesg` command, run `man dmesg`.

## Show System Information

Cumulus Linux provides commands to obtain system information and to show the version of Cumulus Linux you are running. Use these commands when performing system diagnostics, troubleshooting performance, or submitting a support request.

To show information about the version of Cumulus Linux running on the switch, run the `nv show system` command:

```
cumulus@switch:~$ nv show system
uptime             1 day, 0:00:39                                                 
hostname           leaf01                                         leaf01   leaf01 
product-name       Cumulus Linux                                                  
platform           N/A                                                            
system-memory      1.29 GB used / 171.84 MB free / 1.67 GB total                  
swap-memory        0 Bytes used / 0 Bytes free / 0 Bytes total                    
health-status      Not OK                                                         
date-time          2025-04-18 10:57:01                                            
status             N/A                                                            
timezone           Etc/UTC                                                        
version                                                                           
  onie             N/A                                                            
  kernel           6.1.0-cl-1-amd64                                               
  base-os          Debian GNU/Linux 12.10                                         
```

To show system memory information in bytes, run the `nv show system memory` command:

```
cumulus@switch:~$ nv show system memory
Type      Buffers     Cache        Free         Total         Used         Utilization
--------  ----------  -----------  -----------  ------------  -----------  -----------
Physical  81661952 B  571834368 B  373276672 B  1813528576 B  786755584 B  79.4%
Swap                               0 B          0 B           0 B          0.0%
```

To show system CPU information, run the `nv show system cpu` command:

```
cumulus@switch:~$ nv show system cpu
             operational                  
-----------  -----------------------------
model        QEMU Virtual CPU version 2.5+
core-count   1                            
utilization  0.3%
```

To show general information about the switch, run the `nv show platform` command:

```
cumulus@switch:~$ nv show platform
               operational 
-------------  ---------------------------------------
system-mac     44:38:39:22:01:b1                               
manufacturer   Cumulus                                         
product-name   VX                                              
cpu            x86_64 QEMU Virtual CPU version 2.5+ x1         
memory         1.67 GB                                         
disk-size      n/a                                             
port-layout    n/a                                             
part-number    5.15.0                                          
serial-number  44:38:39:22:01:7a                               
asic-model     n/a                                             
system-uuid    6de505b8-323c-42ab-b188-0ba5c666b668
```
<!-- vale off -->
## Diagnostics Using a cl-support File
<!-- vale on -->
You can generate a single export `cl-support` file that contains various details about switch configuration, and is useful for remote debugging and troubleshooting.

Generate a `cl-support` file to investigate issues before you submit a support request. You can either run the NVUE `nv action generate system tech-support` command or the Linux `sudo cl-support` command:

```
cumulus@switch:~$ nv action generate system tech-support
...
```

For more information, refer to {{<link url="Understanding-the-cl-support-Output-File">}}.
