---
title: BMC
author: NVIDIA
weight: 62
toc: 3
---

The Spectrum-6 switch requires <span class="a-tooltip">[BMC](## "Baseboard Management Controller")</span>, which is a specialized microcontroller designed to deliver out-of-band remote monitoring and management for servers and switches. Operating independently from the main CPU and operating system, the BMC enables administrative control even when the switch is powered down or unresponsive. It streamlines server and switch management while enhancing network efficiency, reliability, and security through automation of critical tasks.

You can access BMC either through Cumulus Linux or directly through the BMC RJ45 Ethernet port.

{{%notice infonopad%}}
- NVIDIA distributes BMC as a separate package and does not include it in the Cumulus Linux upgrade image; you must upgrade BMC separately with NVUE.
- You must upgrade BMC before you upgrade Cumulus Linux.
{{%/notice%}}

## BMC and ERoT Firmware Package

On the Spectrum-6 (SN6600) switch, you can upgrade the following firmware components through BMC:

| Component | Upgradeable | Delivered As | Notes |
| --------- | ----------------------- | ------------ | ----- |
| BMC (Baseboard Management Controller) | Yes, with NVUE | Combined <span class="a-tooltip">[FLM](## "Firmware Lifecycle Management")</span> `.fwpkg` package that includes BMC and ERoT firmware | The package is separate from the Cumulus Linux image. You must upgrade BMC independently. You can upgrade BMC without resetting the host or the Cumulus Linux operating system. |
| ERoT (External Root of Trust) | Yes, with NVUE | The same combined FLM `.fwpkg` package | You must power cycle the switch to activate the ERoT firmware after you install the package. |

Keep the following in mind about the BMC and ERoT package:

- NVIDIA distributes the package separately; the Cumulus Linux upgrade image does not include it.
- The package is a combined FLM bundle that contains both BMC and ERoT firmware. For example, `nvfw_ETH-SPC6-2600_0001_260726.1.0_BMC_EROT.fwpkg`.
- One NVUE install action upgrades both BMC and ERoT.
- A Cumulus Linux release might or might not include a new BMC and ERoT version. If the version changes, you must install the new package separately.
- You can download the package from the {{<exlink url="https://enterprise-support.nvidia.com/s/downloads" text="NVIDIA Enterprise Support Portal">}}.

## Upgrade BMC and Cumulus Linux

{{%notice warning%}}
You must upgrade BMC firmware before you upgrade Cumulus Linux. Before you upgrade to Cumulus Linux 5.19.0, you must upgrade the BMC firmware to version 88.0070.1910 and the ERoT firmware to version 02.00.0048.0000_n05. The ERoT firmware upgrade requires a power cycle of the switch to activate.
{{%/notice%}}

To upgrade a Spectrum-6 switch, perform the upgrade in this order:

1. Upgrade the BMC and ERoT firmware (the combined FLM package) with NVUE, as described in {{<link url="#install-bmc" text="Install BMC">}}. The installation resets the BMC to activate the new firmware. The installation does not reset the host CPU or Cumulus Linux.
2. Power cycle the switch to activate the ERoT firmware with the `nv action reboot system mode power-cycle force` command.
3. Upgrade Cumulus Linux. Refer to {{<link url="Upgrading-Cumulus-Linux" text="Upgrading Cumulus Linux">}}.

{{%notice note%}}
Upgrade BMC firmware only with the NVUE commands in this section. NVIDIA validates BMC firmware upgrades through NVUE only; NVIDIA does not validate upgrading BMC firmware through Redfish.
{{%/notice%}}

## Install BMC

{{%notice note%}}
The commands on this page use BMC as the example component, but the `platform firmware` object and the `file-management`, `automatic-update`, and `firmware-source` commands described here apply to every upgradeable platform firmware component, such as BIOS, ASIC, and SSD. Substitute the platform component ID you are working with.
{{%/notice%}}

To fetch the BMC and ERoT package, run the `nv action fetch platform firmware BMC <remote-url-to-package>` command:

```
cumulus@switch:~$ nv action fetch platform firmware BMC http://path/nvfw_ETH-SPC6-2600_0001_2651115.1.0_prod-signed.fwpkg
Action executing ...
Fetching file ...
Action executing ...
Firmware downloaded successfully. File: /tmp/firmware_downloads/bmc/nvfw_ETH-SPC6-2600_0001_2651115.1.0_prod-signed.fwpkg. SHA256: 585231eb5da5221adfdb90a88892aa65a1bf9a89517e841c654db2e9dbff99aa
Action succeeded
```

Alternatively, fetch the package from a local file path:

```
cumulus@switch:~$ nv action fetch platform firmware BMC file:///var/tmp/nvfw_ETH-SPC6-2600_0001_2651115.1.0_prod-signed.fwpkg
```

The following example shows the available BMC files.

```
cumulus@switch:~$ nv show platform firmware BMC files
Available Firmware Files                                           File Path
-----------------------------------------------------------------  -------------------------------------------------------------------------
nvfw_ETH-SPC6-2600_0001_2651115.1.0_prod-signed.fwpkg              /tmp/firmware_downloads/bmc/nvfw_ETH-SPC6-2600_0001_2651115.1.0_prod-signed.fwpkg
```

To install the BMC and ERoT package, run the `nv action install platform firmware BMC files <package-name>` command.

```
cumulus@switch:~$ nv action install platform firmware BMC files nvfw_ETH-SPC6-2600_0001_2651115.1.0_prod-signed.fwpkg
The operation will install the firmware.
 Type [y] to install the firmware. 
 Type [N] to abort. 
Do you want to continue? [y/N] y 
 Action executing ... 
 Firmware installation completed for bmc. Version: 88.0070.1910. BMC reset triggered to activate new firmware 
 Action succeeded
```

During the installation:

- The BMC firmware activates immediately after the automatic BMC reset.
- The ERoT firmware stays in the `PendingActivation` state until you power cycle the switch.

You can add the following optional arguments to the install command:

- `force` — skip the applicable installation checks.
- `skip-reboot` — install the firmware without automatically resetting the BMC to activate it. By default, installing BMC firmware triggers a BMC reset.
- `skip-version-check` — install the firmware without checking whether the file's version is compatible with the running system. `skip-version-check` does not change the reboot or confirmation-prompt behavior; `force` and `skip-reboot` remain independent.

The following example installs BMC firmware and skips the version check:

```
cumulus@switch:~$ nv action install platform firmware BMC files nvfw_ETH-SPC6-2600_0001_2651115.1.0_prod-signed.fwpkg skip-version-check
Action executing ...
Firmware installation completed for bmc. Version: 88.0070.1910. BMC reset triggered to activate new firmware
Action succeeded
```

### Power Cycle the Switch

After you install the BMC and ERoT package, power cycle the switch to activate the pending ERoT firmware:

```
cumulus@switch:~$ nv action reboot system mode power-cycle force
```

After the power cycle, run the `nv show platform firmware` and `nv show platform inventory` commands to verify both the BMC and ERoT versions. To show only the BMC, run the `nv show platform firmware BMC` and `nv show platform inventory BMC` commands. Refer to {{<link url="#show-information-about-bmc" text="Show Information About BMC">}}.

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

To confirm the current settings for a component, run the `nv show platform firmware <platform-component-id>` command described below.

To reset `automatic-update` and `firmware-source` settings to the default for every platform firmware component, run the `nv unset platform firmware` command:

```
cumulus@switch:~$ nv unset platform firmware
cumulus@switch:~$ nv config apply
```

## Show Information About BMC

Use the following NVUE commands to show information about the installed BMC package on your Spectrum-6 switch.

| Command | Description |
|-------- | ----------- |
| `nv show platform firmware` | Shows the firmware versions of the platform components, including BMC and ERoT. |
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
BMC        88.0070.1910  OpenBMC             MT2617606EXZ  ok     bmc
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
hardware-version  88.0070.1910
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
actual-firmware  88.0070.1910
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
<!-- in ES but not 5.19
{{%notice note%}}
- The SN6810-LD has two leakage sensors, `leakage1` and `leakage2`. Each sensor shows `normal` or `alert`.
- The switch software derives the sensor names from the leak bits that the CPLD exposes through hardware management.
- Both sensors always appear in the command output. If the switch software cannot read the state of a sensor, the sensor shows `alert`. For a sensor that is unplugged, the switch shows the state that the CPLD reports.
- When a sensor shows `alert`, the `nv show system health` command lists the sensor as an issue and shows the status `Not OK`, the System LED turns amber, and the switch writes a message to syslog.
- By default, a leak raises an alarm only; the switch does not shut down. The default BMC leak policy is `None`, which means no automatic power-off.
{{%/notice%}}
-->
gNMI and OTEL telemetry lets you subscribe to real-time leakage status and trigger automated alerts. For OTEL metrics, refer to {{<link url="Open-Telemetry-Export/#platform-statistic-format" text="OTEL Telemetry Leakage Sensor Metrics">}}. For gNMI metrics, refer to {{<link url="New-and-Updated-Telemetry-Metrics/#new-gnmi-metrics" text="gNMI Leakage Sensor Metrics">}}.

For information about using out-of-band remote monitoring and management for the Cumulus Linux Spectrum-6 switch, refer to the {{<mib_link url="bmc-user-manual-88.0060.2114/index.html" text="BMC user guide.">}}
