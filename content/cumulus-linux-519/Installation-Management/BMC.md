---
title: BMC
author: NVIDIA
weight: 62
toc: 3
---

The Spectrum-6 switch requires <span class="a-tooltip">[BMC](## "Baseboard Management Controller")</span>, which is a specialized microcontroller designed to deliver out-of-band remote monitoring and management for servers and switches. Operating independently from the main CPU and operating system, the BMC enables administrative control even when the switch is powered down or unresponsive. It streamlines server and switch management while enhancing network efficiency, reliability, and security through automation of critical tasks.

You can access BMC either through Cumulus Linux or directly through the BMC RJ45 Ethernet port.

Cumulus Linux includes the BMC package. To update the BMC package files to the latest versions, run the following commands.

{{%notice note%}}
The commands on this page use BMC as the example component, but the `platform firmware` object and the `file-management`, `automatic-update`, and `firmware-source` commands described here apply to every upgradeable platform firmware component, such as BIOS, ASIC, and SSD. Substitute the platform component ID you are working with.
{{%/notice%}}

To fetch the latest BMC package, run the `nv action fetch platform firmware BMC <remote-url-to-package>` command:

```
cumulus@switch:~$ nv action fetch platform firmware BMC http://path/cec1736-ecfw-02.00.0023.0000-n05-dev-initial.fwpkg
Action executing ...
Fetching file ...
Action executing ...
Firmware downloaded successfully. File: /tmp/firmware_downloads/bmc/cec1736-ecfw-02.00.0023.0000-n05-dev-initial.fwpkg. SHA256: 585231eb5da5221adfdb90a88892aa65a1bf9a89517e841c654db2e9dbff99aa
Action succeeded
```

The following example shows the available BMC files.

```
cumulus@switch:~$ nv show platform firmware BMC files
Available Firmware Files                            File Path
--------------------------------------------------  ------------------------------------------------------------------------------
cec1736-ecfw-02.00.0023.0000-n05-dev-initial.fwpkg  /tmp/firmware_downloads/bmc/cec1736-ecfw-02.00.0023.0000-n05-dev-initial.fwpkg
sw_bmc_arm_spc6_ast2600_88.0060.0501.fwpkg          /tmp/firmware_downloads/bmc/sw_bmc_arm_spc6_ast2600_88.0060.0501.fwpkg 
```

To install available BMC package files, run the `nv action install platform firmware BMC files <package-name>` command.

```
cumulus@switch:~$ nv action install platform firmware BMC files sw_bmc_arm_spc6_ast2600_88.0060.0501.fwpkg
The operation will install the firmware.
 Type [y] to install the firmware. 
 Type [N] to abort. 
Do you want to continue? [y/N] y 
 Action executing ... 
 Firmware installation completed for bmc. Version: unknown 
 Action succeeded
```

You can add the following optional arguments to the install command:

- `force` — skip the applicable installation checks.
- `skip-reboot` — install the firmware without automatically resetting the BMC to activate it. By default, installing BMC firmware triggers a BMC reset.
- `skip-version-check` — install the firmware without checking whether the file's version is compatible with the running system. `skip-version-check` does not change the reboot or confirmation-prompt behavior; `force` and `skip-reboot` remain independent.

The following example installs BMC firmware and skips the version check:

```
cumulus@switch:~$ nv action install platform firmware BMC files sw_bmc_arm_spc6_ast2600_88.0060.0501.fwpkg skip-version-check
Action executing ...
Firmware installation completed for bmc. Version: 88.0060.0501. BMC reset triggered to activate new firmware
Action succeeded
```

## Manage Staged Firmware Files

After you fetch a firmware file to the switch, you can delete, rename, or upload a staged firmware file for any platform firmware component, not only BMC. The following examples use the SSD component; substitute the platform component ID you are working with.

To delete a staged firmware file, run the `nv action delete platform firmware <platform-component-id> files <file-id>` command:

```
cumulus@switch:~$ nv action delete platform firmware SSD files ssd-fw-2.1.bin
Action executing ...
Deleting file: ssd-fw-2.1.bin
Action executing ...
File delete successfully
Action succeeded
```

If the file does not exist, the action fails and names the missing file:

```
cumulus@switch:~$ nv action delete platform firmware BIOS files missing-fw.rom
Error: Action failed with the following issue:
File not found: missing-fw.rom
```

To rename a staged firmware file, run the `nv action rename platform firmware <platform-component-id> files <file-id> <new-name>` command:

```
cumulus@switch:~$ nv action rename platform firmware SSD files ssd-fw-2.1.bin ssd-fw-2.1-verified.bin
Action executing ...
File renamed successfully
Action succeeded
```

To upload a staged firmware file to a remote server, run the `nv action upload platform firmware <platform-component-id> files <file-id> <url>` command. This is the reverse direction of `nv action fetch`, which downloads a file from a remote server onto the switch; `upload` sends a file already staged on the switch out to a remote destination, for example to archive it before you delete it locally.

```
cumulus@switch:~$ nv action upload platform firmware SSD files ssd-fw-2.1.bin scp://admin@fw-archive.example.com/incoming/
Action executing ...
Uploading file ssd-fw-2.1.bin
Action executing ...
Successfully uploaded the file: ssd-fw-2.1.bin
Action succeeded
```

{{%notice note%}}
If the destination server requires a username and password, include them in the URL, for example `scp://<username>:<password>@<server>/<path>`. NVIDIA recommends key-based authentication where the destination server supports it, so a password does not appear in `nv config diff` or in the switch command history.
{{%/notice%}}

## Configure Automatic Firmware Updates

You can configure whether Cumulus Linux automatically updates the staged files for a platform firmware component, and whether a component uses the default firmware source or a custom one you staged yourself. Like the file-management commands above, these settings apply to any platform firmware component, not only BMC.

To enable or disable automatic updates for a component, run the `nv set platform firmware <platform-component-id> auto-update` command. The following example enables automatic updates for BIOS:

```
cumulus@switch:~$ nv set platform firmware BIOS auto-update enabled
cumulus@switch:~$ nv config apply
```

To configure whether a component uses the default firmware source or a custom one, run the `nv set platform firmware <platform-component-id> fw-source` command. Values are `default` and `custom`. The following example sets the ASIC component to use a custom firmware source:

```
cumulus@switch:~$ nv set platform firmware ASIC fw-source custom
cumulus@switch:~$ nv config apply
```

<!-- REVIEW: the spec states NVUE also writes these two settings to /etc/cumulus/<component>-auto-update.conf, and confirms this path for the ASIC and BIOS components specifically (asic-auto-update.conf, bios-auto-update.conf). It does not confirm the equivalent file exists for BMC or SSD. Drafted the ASIC and BIOS examples only, matching the spec; confirm before generalizing further. -->

To confirm the current settings for a component, run the `nv show platform firmware <platform-component-id>` command described below.

To reset `automatic-update` and `firmware-source` settings to the default for every platform firmware component, run the `nv unset platform firmware` command:

```
cumulus@switch:~$ nv unset platform firmware
cumulus@switch:~$ nv config apply
```

<!-- REVIEW: the spec shows only this unscoped form, which resets every component at once, and does not show a per-component nv unset platform firmware <platform-component-id> auto-update or fw-source form. Drafted the unscoped command as shown; confirm whether a scoped form also exists before publishing. -->

## Show Information About BMC

Use the following NVUE commands to show information about the installed BMC package on your Spectrum-6 switch.

| Command | Description |
|-------- | ----------- |
| `nv show platform inventory` | Shows the model, serial number, operational state, and type of each component on the switch. |
| `nv show platform inventory BMC` | Shows the BMC firmware model, serial number, operational state, and type. |
| `nv show platform firmware BMC` | Shows the BMC firmware part number and name. |
| `nv show platform firmware BMC files` | Shows the available BMC firmware files. |
| `nv show platform environment leakage`<br>`nv show platform environment leakage -o json`| Shows the switch environment leakage (low-current signals).|

The following example shows the model, serial number, operational state, and type of each component on the switch.

```
cumulus@switch:~$ nv show platform inventory
           HW Version    Model               Serial        State  Type
---------  ------------  ------------------  ------------  -----  ------
BMC        88.0060.2112  OpenBMC             MT2617606EXZ  ok     bmc
PDB1-HSC1  N/A           N/A                 N/A           ok     psu
PDB2-HSC1  N/A           N/A                 N/A           ok     psu
SWITCH     A3            920-9N62F-00LI-GC0  MT2617606EXZ  ok     switch
```

The following example shows the BMC model, serial number, operational state, and type.

```
cumulus@switch:~$ nv show platform inventory BMC
                  operational
----------------  ------------
state             ok
hardware-version  88.0060.2112
model             OpenBMC
serial            MT2617606EXZ
type              bmc
```

The following example shows the BMC firmware part number and name.

```
cumulus@switch:~$ nv show platform firmware BMC
                 operational
---------------  ------------
part-number      NVIDIA
actual-firmware  88.0060.2112
fw-source        default
```

## Liquid Cooling Leakage

Liquid-cooled NVIDIA switches contain leakage sensors that detect coolant leaks. These sensors are critical for data center safety as an undetected leak can cause equipment damage, fire risk, or unplanned downtime.

The following examples show the switch environment leakage (low-current signals).

```
cumulus@switch:~$ nv show platform environment leakage
Name      State  
--------  ------ 
leakage1  normal 
leakage2  normal
```

```
cumulus@switch:~$ nv show platform environment leakage -o json
{
   "leakage1": {
     "state": "normal"
   },
   "leakage2": {
     "state": "normal"
   }
 }
```

gNMI and OTEL telemetry lets you subscribe to real-time leakage status and trigger automated alerts. For OTEL metrics, refer to {{<link url="Open-Telemetry-Export/#platform-statistic-format" text="OTEL Telemetry Leakage Sensor Metrics">}}. For gNMI metrics, refer to {{<link url="New-and-Updated-Telemetry-Metrics/#new-gnmi-metrics" text="gNMI Leakage Sensor Metrics">}}.

For information about using out-of-band remote monitoring and management for the Cumulus Linux Spectrum-6 switch, refer to the {{<mib_link url="bmc-user-manual-88.0060.2110/Getting_Started.html" text="BMC user guide.">}}
