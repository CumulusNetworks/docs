---
title: SSD is Read-only on Intel 7 Series Switches
author: NVIDIA
weight: 352
toc: 3
---

## Symptom

On Cumulus Linux 5 versions, SSDs might become read-only on the following platforms: SN2410/SN2410B and SN2700/SN2700B.

The following errors appear in `/var/log/syslog` before failing into R/O state:
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


# Issue Overview 

In Cumulus Linux 5 there was a change to the SATA Link Power Management (LPM) policy. LPM policy is controlled by the kernel setting `SATA_MOBILE_LPM_POLICY`. In Cumulus Linux 5, the `SATA_MOBILE_LPM_POLICY` value was taken from Debian default configurations which is 3, or medium power with device initiated PM (`med_power_with_dipm`) enabled and imported into Cumulus. In Cumulus Linux 4, this configuration value was not specified and it is assigned the default value from firmware which is `max_performace`.

It was discovered that not all combinations of SATA host controllers and storage devices work well with the default `med_power_with_dipm` setting. For example, platforms with Intel 7 Series Chipset controllers might experience timeouts and link degradation when accessing the SSD.

The NVIDIA switch platforms SN2410/SN2410B and SN2700/SN2700B have Intel 7 controllers:

```
#lspci | grep SATA 
00:1f.2 SATA controller: Intel Corporation 7 Series Chipset Family 6-port SATA
Controller [AHCI mode] (rev 04) (prog-if 01 [AHCI 1.0])
```

## Resolution

Switches that are currently in a read-only state will need to be power cycled to recover. After recovery, the following steps should be followed to resolve the issue:

### Implement the Fix at Runtime (non-persistent)

1. Reconfigure the SATA LPM policy setting to `max_perfomance`. To apply the solution at runtime which doesn't require a switch reboot, run the following commands:

```
#sudo -i
#echo "max_performance" > /sys/class/scsi_host/host0/link_power_management_policy
```

Confirm that the setting is applied:

```
#cat /sys/class/scsi_host/host0/link_power_management_policy
max_performance
```

This setting change at runtime is not persistent through a reboot. After a switch reboot, reapply the change or use the persistent fix as outlined below. 

### Implement the Fix Persistently

1. To apply the fix in a persistent manner, add `ahci.mobile_lpm_policy=1` to the `/etc/default/grub` file in the `GRUB_CMDLINE_LINUX` line as outlined below:

```
vim /etc/default/grub

GRUB_CMDLINE_LINUX="cl_platform=mlnx_x86_MSN2410 console=tty0 console=ttyS0,115200n8 ahci.mobile_lpm_policy=1 acpi_enforce_resources=lax acpi=noirq"

```

Alternatively, use `sed` to replace the latter characters in the console speed and add the LPM policy value as outlined below:

```
sudo sed -i -e "s/200n8/200n8 ahci.mobile_lpm_policy=1/g" /etc/default/grub
```

Validate the change:
```
#grep 200n8 /etc/default/grub
GRUB_CMDLINE_LINUX="cl_platform=mlnx_x86_MSN2410 console=tty0 console=ttyS0,115200n8 ahci.mobile_lpm_policy=1 acpi_enforce_resources=lax acpi=noirq"
```

2. Run the `update-grub` command to apply the new `/etc/default/grub` configuration:

```
#sudo update-grub
```

3. Reboot the switch with the `sudo reboot command`

The software fix for this issue will be integrated into Cumulus Linux 5.11.0.