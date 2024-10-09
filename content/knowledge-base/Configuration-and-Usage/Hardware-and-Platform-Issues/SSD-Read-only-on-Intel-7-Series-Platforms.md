---
title: SSD is Read-only on Intel 7 Series Switches
author: NVIDIA
weight: 352
toc: 3
---

## Symptom

On the NVIDIA SN2410, SN2410B, SN2700, and SN2700B switches running Cumulus Linux 5.0 and later, SSDs might become read only.

Before failing into a read-only state, you see the following errors in the `/var/log/syslog` file:

```
kernel: [3238274.795264] ata1.00: exception Emask 0×10 SAct 0×40 SErr 0×4050000
action 0xe frozen
kernel: [3238274.803288] ata1.00: irq_stat 0×00000040, connection status
changed
kernel: [3238274.809868] ata1: SError: { PHYRdyChg CommWake DevExch }
kernel: [3238274.815419] ata1.00: failed command: WRITE FPDMA QUEUED
kernel: [3238274.820912] ata1.00: cmd 61/48:30:f8:3e:0d/00:00:00:00:00/40 tag 6
ncq dma 36864 out
kernel: [3238274.820912] res 40/00:30:f8:3e:0d/00:00:00:00:00/40 Emask 0×10
(ATA bus error)
kernel: [3238274.837175] ata1.00: status: { DRDY }
kernel: [3238274.841065] ata1: hard resetting link 
```

## Overview

In Cumulus Linux 5.0 and later, there is a change to the SATA Link Power Management (LPM) policy, which the kernel setting `SATA_MOBILE_LPM_POLICY` controls.
- Cumulus Linux 4.0 through 4.4 does not provide the `SATA_MOBILE_LPM_POLICY` configuration setting but uses the default value from firmware, which is `max_performace`.
- Cumulus Linux 5.0 and later uses the `SATA_MOBILE_LPM_POLICY` value from Debian default configurations, which is 3 or medium power with device initiated PM (`med_power_with_dipm`) enabled.

Not all combinations of SATA host controllers and storage devices work well with the default `med_power_with_dipm` setting. For example, platforms with the Intel 7 Series chipset controllers might experience timeouts and link degradation when accessing the SSD; the NVIDIA SN2410, SN2410B, SN2700, and SN2700B switches have Intel 7 controllers:

```
#lspci | grep SATA 
00:1f.2 SATA controller: Intel Corporation 7 Series Chipset Family 6-port SATA
Controller [AHCI mode] (rev 04) (prog-if 01 [AHCI 1.0])
```

## Resolution

To recover a switch currently in a read-only state, power cycle the switch. After recovery, follow these steps to resolve the issue.

{{< tabs "TabID47 ">}}
{{< tab "Runtime Fix ">}}

To apply the fix at runtime:

1. Set the SATA LPM policy to `max_perfomance`:

   ```
   cumulus@switch:~$ sudo -i
   cumulus@switch:~$ echo "max_performance" > /sys/class/scsi_host/host0/link_power_management_policy
   ```

    When you apply the solution at runtime, you do not need to reboot the switch.

2. Confirm the setting:

   ```
   cumulus@switch:~$ cat /sys/class/scsi_host/host0/link_power_management_policy
   max_performance
   ```

Runtime changes are not persistent after a reboot. After a switch reboot, reapply the change or implement the persistent fix.

{{< /tab >}}
{{< tab "Persistent Fix ">}}

To apply the fix so that it persists after a reboot:

1. Edit the `/etc/default/grub` file to add `ahci.mobile_lpm_policy=1` to the `GRUB_CMDLINE_LINUX` line:

   ```
   cumulus@switch:~$ vim /etc/default/grub
   GRUB_CMDLINE_LINUX="cl_platform=mlnx_x86_MSN2410 console=tty0 console=ttyS0,115200n8 ahci.   mobile_lpm_policy=1 acpi_enforce_resources=lax acpi=noirq"
   ```

   Alternatively, use `sed` to replace the last few characters in the console speed and add the LPM policy value, then validate the change:

   ```
   cumulus@switch:~$ sudo sed -i -e "s/200n8/200n8 ahci.mobile_lpm_policy=1/g" /etc/default/grub
   ```

   ```
   cumulus@switch:~$ grep 200n8 /etc/default/grub
   GRUB_CMDLINE_LINUX="cl_platform=mlnx_x86_MSN2410 console=tty0 console=ttyS0,115200n8 ahci.   mobile_lpm_policy=1 acpi_enforce_resources=lax acpi=noirq"
   ```

2. Run the `update-grub` command to apply the new `/etc/default/grub` configuration:

   ```
   cumulus@switch:~$ sudo update-grub
   ```

3. Reboot the switch:

   ```
   cumulus@switch:~$ sudo reboot
   ```

{{< /tab >}}
{{< /tabs >}}
