---
title: Erase all Data from the Switch
author: NVIDIA
weight: 297
toc: 3
---
Cumulus Linux enables you to erase all data on the switch <span class="a-tooltip">[SSD](## "Solid state drive")</span> securely to prevent leaking critical data. Erasing data is an important process when you return a switch with <span class="a-tooltip">[RMA](## "Return Merchandise Authorization")</span> if the switch is defective or move a switch between buildings.

When you erase all data on the switch, most services stop except for critical ones, such as `sshd` so that you can erase the data remotely.

{{%notice note%}}
- You can erase all data only on the NVIDIA SN5400, SN5600, and SN5600D switch.
- You can erase all data on a functioning SSD only.
- You cannot recover erased data.
{{%/notice%}}

To erase all data on the switch:

{{< tabs "TabID18 ">}}
{{< tab "NVUE Commands ">}}

Run the `nv action erase system disk` command. NVUE prompts you to confirm that you want to proceed before destroying all data.

```
cumulus@switch:~$ nv action erase system disk 
WARNING! This will destroy all 
data and will NOT be recoverable. 
Execution may take up to X minutes. 
Would you like to proceed? [y/N] 
```

If there is an issue when starting to erase all data, NVUE prompts you to reboot the switch to return the switch to its normal functioning state. However, if there is an issue after starting to erase the data (for example in the middle of the process), you must reinstall the NOS to recover.

{{< /tab >}}
{{< tab "Linux Commands ">}}

Run the `systemctl start ssd-erase.service` command.

{{%notice warning%}}
When you run the Linux `systemctl start ssd-erase.service` command, the switch does not prompt you to confirm that you want to proceed before destroying all data or prompt you to reboot if there is an issue.
{{%/notice%}}

```
cumulus@switch:~$ sudo systemctl start ssd-erase.service
```

{{< /tab >}}
{{< /tabs >}}

Depending on disk type and size, it might take some time to erase all data from the disk. For example, for a very large disk, it might take 60 minutes or more.
