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

Cumulus Linux provides a firmware package that contains both BMC and <span class="a-tooltip">[ERoT](## "External Root of Trust")</span> firmware. The ERoT firmware provides hardware-backed security, secure flash, and boot attestation for system firmware.

On the Spectrum-6 (SN6600) switch, you upgrade the following firmware components through BMC:

| Component | Upgradeable | Delivered As | Notes |
| --------- | ----------------------- | ------------ | ----- |
| BMC (Baseboard Management Controller) | Yes, with NVUE | Combined <span class="a-tooltip">[FLM](## "Firmware Lifecycle Management")</span> `.fwpkg` package that includes BMC and ERoT firmware | The package is separate from the Cumulus Linux image. You must upgrade BMC independently. You can upgrade BMC without resetting the host or the Cumulus Linux operating system. |
| ERoT (External Root of Trust) | Yes, with NVUE | The same combined FLM `.fwpkg` package | You must power cycle the switch to activate the ERoT firmware after you install the package. |

Keep the following in mind about the BMC and ERoT package:

- NVIDIA distributes the package separately; the Cumulus Linux upgrade image does not include it.
- The package is a combined FLM bundle that contains both BMC and ERoT firmware. For example, `nvfw_ETH-SPC6-2600_0001_261109.1.0_prod-signed.fwpkg`.
- One NVUE install action installs both the BMC and ERoT images, but only the BMC activates automatically (the install resets the BMC). The ERoT firmware stays staged until you power cycle the switch.
- A Cumulus Linux release might or might not include a new BMC and ERoT version. If the version changes, you must install the new package separately.
- You can download the package from the {{<exlink url="https://enterprise-support.nvidia.com/s/downloads" text="NVIDIA Enterprise Support Portal">}}.

## Upgrade BMC and Cumulus Linux

{{%notice warning%}}
You must upgrade BMC firmware before you upgrade Cumulus Linux. Before you upgrade to Cumulus Linux 5.20.0, you must upgrade the BMC firmware to version 88.0070.1910 and the ERoT firmware to version 02.00.0048.0000_n05. The ERoT firmware upgrade requires a power cycle of the switch to activate.
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
The commands on this page use BMC as the example component. The `platform firmware` file management commands apply to every platform firmware component. In Cumulus Linux 5.19 and later, the `auto-update` and `fw-source` settings apply only to the Spectrum-6 component. Substitute the platform component ID you are working with.
{{%/notice%}}

To fetch the BMC and ERoT package, run the `nv action fetch platform firmware BMC <remote-url-to-package>` command:

```
cumulus@switch:~$ nv action fetch platform firmware BMC http://path/nvfw_ETH-SPC6-2600_0001_261109.1.0_prod-signed.fwpkg
Action executing ...
Fetching file ...
Action executing ...
File has been successfully fetched
Action executing ...
Firmware downloaded successfully. File: /tmp/firmware_downloads/bmc/nvfw_ETH-SPC6-2600_0001_261109.1.0_prod-signed.fwpkg. SHA256: c8d7a00062df51f99d37483f7fd47ec01c42dd491c90516fced17698529a3970
Action succeeded
```

Alternatively, fetch the package from a local file path:

```
cumulus@switch:~$ nv action fetch platform firmware BMC file:///var/tmp/nvfw_ETH-SPC6-2600_0001_261109.1.0_prod-signed.fwpkg
```

The following example shows the available BMC files.

```
cumulus@switch:~$ nv show platform firmware BMC files
Available Firmware Files                               File Path
-----------------------------------------------------  ------------------------------------------------------------------------
nvfw_ETH-SPC6-2600_0001_261109.1.0_prod-signed.fwpkg   /tmp/firmware_downloads/bmc/nvfw_ETH-SPC6-2600_0001_261109.1.0_prod-signed.fwpkg
```

To install the BMC and ERoT package, run the `nv action install platform firmware BMC files <package-name>` command.

```
cumulus@switch:~$ nv action install platform firmware BMC files nvfw_ETH-SPC6-2600_0001_261109.1.0_prod-signed.fwpkg
The operation will install the firmware.
 Type [y] to install the firmware. 
 Type [N] to abort. 
Do you want to continue? [y/N] y 
 Action executing ... 
 Firmware installation completed for bmc. Version: 88.0070.1908. BMC reset triggered to activate new firmware. ERoT firmware 02.00.0048.0000_n05 is staged. Run 'nv action reboot system mode power-cycle' to activate it; a reboot or BMC reset does not. 
 Action succeeded
```

During the installation:

- The BMC activates after the automatic BMC reset.
- The ERoT is not active until you power cycle the switch. A BMC reset or reboot does not activate it.
- To confirm the running versions, run the `nv show platform firmware` command.

You can add the following optional arguments to the install command:

- `force` — skip the applicable installation checks.
- `skip-reboot` — install the firmware without automatically resetting the BMC to activate it. By default, installing BMC firmware triggers a BMC reset.
- `skip-version-check` — install the firmware without checking whether the file's version is compatible with the running system. `skip-version-check` does not change the reboot or confirmation-prompt behavior; `force` and `skip-reboot` remain independent.

The following example installs BMC firmware and skips the version check:

```
cumulus@switch:~$ nv action install platform firmware BMC files nvfw_ETH-SPC6-2600_0001_261109.1.0_prod-signed.fwpkg skip-version-check
Action executing ...
Firmware installation completed for bmc. Version: 88.0070.1908. BMC reset triggered to activate new firmware. ERoT firmware 02.00.0048.0000_n05 is staged. Run 'nv action reboot system mode power-cycle' to activate it; a reboot or BMC reset does not.
Action succeeded
```

### Power Cycle the Switch

After you install the BMC and ERoT package, power cycle the switch to activate the pending ERoT firmware. The power cycle is a real power loss. It takes down the entire switch, including the host, which is unreachable for about 4 minutes. The power cycle also clears staged firmware files. Schedule it in a maintenance window:

```
cumulus@switch:~$ nv action reboot system mode power-cycle force
```

You can also run the `nv action power-cycle system force` command. With either command, `force` skips the confirmation prompt.

After the power cycle, run the `nv show platform firmware` command to verify both the BMC and ERoT versions. The command lists the ERoT as `EROT-BMC`. To show only the ERoT, run the `nv show platform firmware EROT-BMC` command. The `nv show platform inventory` command lists only the BMC, the power distribution boards, and the switch; it does not show the ERoT. Refer to {{<link url="#show-information-about-bmc" text="Show Information About BMC">}}.

## Manage Staged Firmware Files

After you fetch a firmware file to the switch, you can delete, rename, or upload a staged firmware file for any platform firmware component. The following examples use the BMC component; substitute the platform component ID you are working with. If no firmware file is staged, the `nv show platform firmware BMC files` command shows `No Data`.

To delete a staged firmware file, run the `nv action delete platform firmware <platform-component-id> files <file-id>` command:

```
cumulus@switch:~$ nv action delete platform firmware BMC files test-renamed.fwpkg
File delete successfully
Action succeeded
```

To rename a staged firmware file, run the `nv action rename platform firmware <platform-component-id> files <file-id> <new-name>` command:

```
cumulus@switch:~$ nv action rename platform firmware BMC files nvfw_ETH-SPC6-2600_0001_261109.1.0_prod-signed.fwpkg test-renamed.fwpkg
File renamed successfully
Action succeeded
```

To upload a staged firmware file to a remote server, run the `nv action upload platform firmware <platform-component-id> files <file-id> <url>` command. This is the reverse direction of `nv action fetch`, which downloads a file from a remote server onto the switch; `upload` sends a file already staged on the switch out to a remote destination, for example to archive it before you delete it locally.

```
cumulus@switch:~$ nv action upload platform firmware BMC files nvfw_ETH-SPC6-2600_0001_261109.1.0_prod-signed.fwpkg scp://admin@fw-archive.example.com/incoming/
Action executing ...
Uploading file nvfw_ETH-SPC6-2600_0001_261109.1.0_prod-signed.fwpkg
Action executing ...
Successfully uploaded the file: nvfw_ETH-SPC6-2600_0001_261109.1.0_prod-signed.fwpkg
Action succeeded
```

{{%notice note%}}
If the destination server requires a username and password, include them in the URL, for example `scp://<username>:<password>@<server>/<path>`. NVIDIA recommends key-based authentication where the destination server supports it, so a password does not appear in `nv config diff` or in the switch command history.
{{%/notice%}}

## Configure Automatic Firmware Updates

You can configure whether Cumulus Linux automatically updates the staged files for a platform firmware component, and whether a component uses the default firmware source or a custom one you staged yourself. In Cumulus Linux 5.19 and later, these settings apply only to the Spectrum-6 component. The `nv show platform firmware` command shows `auto-update` and `fw-source` only for Spectrum-6; BIOS, BMC, CPLD1 through CPLD4, EROT-BMC, and SSD show neither. BIOS, SSD, and BMC do not support `auto-update`. Use `Spectrum-6` as the component ID; `ASIC` is not a valid ID.

To enable or disable automatic updates for a component, run the `nv set platform firmware <platform-component-id> auto-update` command. Automatic updates are enabled by default. The following example disables automatic updates for the Spectrum-6 component:

```
cumulus@switch:~$ nv set platform firmware Spectrum-6 auto-update disabled
cumulus@switch:~$ nv config apply
```

To configure whether a component uses the default firmware source or a custom one, run the `nv set platform firmware <platform-component-id> fw-source` command. Values are `default` and `custom`. The following example sets the Spectrum-6 component to use a custom firmware source:

```
cumulus@switch:~$ nv set platform firmware Spectrum-6 fw-source custom
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
| `nv show platform firmware` | Shows the firmware versions of the platform components, including BMC and ERoT (listed as `EROT-BMC`). |
| `nv show platform inventory` | Shows the model, serial number, operational state, and type of each component on the switch. |
| `nv show platform inventory BMC` | Shows the BMC firmware model, serial number, operational state, and type. |
| `nv show platform firmware BMC` | Shows the BMC firmware part number and name. |
| `nv show platform firmware EROT-BMC` | Shows the ERoT firmware part number and name. |
| `nv show platform firmware BMC files` | Shows the available BMC firmware files. |
| `nv show platform environment leakage`<br>`nv show platform environment leakage -o json`| Shows the switch environment leakage (low-current signals).|

The following example shows the firmware versions of the platform components, including the BMC and the ERoT (`EROT-BMC`).

```
cumulus@switch:~$ nv show platform firmware
Name        Actual FW            Part Number              FW Source
----------  -------------------  -----------------------  ---------
BIOS        0ACUZ_01.00.007      American Megatrends International, LLC.
BMC         88.0070.1910         NVIDIA
CPLD1       4.0                  454
CPLD2       2.6                  439
CPLD3       1.3                  440
CPLD4       1.3                  441
EROT-BMC    02.00.0048.0000_n05  NVIDIA
SSD         ORYAFV               MD681GEFBC82
Spectrum-6  39.2020.2100         920-9N62F-00LI-GC0_Ax    default
```

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
```

The following example shows the ERoT firmware part number and name.

```
cumulus@switch:~$ nv show platform firmware EROT-BMC
                 operational
---------------  -------------------
part-number      NVIDIA
actual-firmware  02.00.0048.0000_n05
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
