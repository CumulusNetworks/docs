---
title: BMC
author: NVIDIA
weight: 62
toc: 3
---

The Spectrum-6 switch requires <span class="a-tooltip">[BMC](## "Baseboard Management Controller")</span>, which is a specialized microcontroller designed to deliver out-of-band remote monitoring and management for servers and switches. Operating independently from the main CPU and operating system, the BMC enables administrative control even when the switch is powered down or unresponsive. It streamlines server and switch management while enhancing network efficiency, reliability, and security through automation of critical tasks.

You can access BMC either through Cumulus Linux or directly through the BMC RJ45 Ethernet port.

Cumulus Linux includes the BMC package. To update the BMC package files to the latest versions, run the following commands.

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

To install available BMC package files, run the `nv action fetch platform firmware BMC files <package-name>` command.

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
