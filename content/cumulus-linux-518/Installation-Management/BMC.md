---
title: BMC
author: NVIDIA
weight: 62
toc: 3
---

The Spectrum-6 switch requires <span class="a-tooltip">[BMC](## "Baseboard Management Controller")</span>, which is a specialized microcontroller designed to deliver out-of-band remote monitoring and management for servers and switches. Operating independently from the main CPU and operating system, the BMC enables administrative control even when the switch is powered down or unresponsive. It streamlines server and switch management while enhancing network efficiency, reliability, and security through automation of critical tasks.

Cumuls Linux includes the BMC package.


<!--
To download the BMC package, run the `nv action fetch platform firmware BMC <remote-url-to-package>` command:

```
cumulus@switch:~$ nv action fetch platform firmware BMC http://path/to/file
Action executing ... Firmware downloaded successfully. File: /tmp/firmware_downloads/sw_bmc_arm_chameleon5_chameleon_bu_kernel-001.fwpkg. SHA256: 19439f4a6695473386a9bb5f2fe253126825c0336890cd0e7366c7a10bda97c0 Action succeeded.
```

To install the BMC package, run the `nv action fetch platform firmware BMC files <package-name>` command: `

```
cumulus@switch:~$ nv action install platform firmware BMC files sw_bmc_arm_chameleon5_chameleon_bu_kernel-001.fwpkg
The operation will install the firmware. 
Type [y] to install the firmware. 
Type [N] to abort. 
 
Do you want to continue? [y/N] y 
Action executing ... 
Firmware installation completed for bmc. Version: unknown 
Action succeeded 
```
-->
## Show Information About BMC

Use the following commands to show information about the installed BMC package on your Spectrum-6 switch.

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

        HW Version                    Model               Serial        State  Type   
------  ----------------------------  ------------------  ------------  -----  ------ 
BMC     chameleon_bu_kernel_leak-003  OpenBMC             N/A           ok     bmc    
PDB1    N/A                           N/A                 N/A           ok     psu    
SWITCH  A1                            920-9N54M-00MB-GNS  MT2550601PNB  ok     switch
```

The following example shows the BMC model, serial number, operational state, and type.

```
cumulus@switch:~$ nv show platform inventory BMC
                 operational
---------------  ----------------------------
state            ok
hardware-version chameleon_bu_kernel_leak-002
model            Baseboard Management Controller
serial           MT2538600R0B
type             bmc
```

The following example shows the BMC firmware part number and name.

```
cumulus@switch:~$ nv show platform firmware BMC
                 operational                  
---------------  ---------------------------- 
part-number      NVIDIA                       
actual-firmware  chameleon_bu_kernel_leak-003 
fw-source        default
```

The following example shows the available BMC files.

```
cumulus@switch:~$ nv show platform firmware BMC files
Available Firmware Files                                  File Path                                                                        
--------------------------------------------------------  -------------------------------------------------------------------------------- 
sw_bmc_arm_chameleon5_chameleon_bu_kernel-001.fwpkg       /tmp/firmware_downloads/sw_bmc_arm_chameleon5_chameleon_bu_kernel-001.fwpkg      
sw_bmc_arm_chameleon5_chameleon_bu_kernel_leak-003.fwpkg  /tmp/firmware_downloads/sw_bmc_arm_chameleon5_chameleon_bu_kernel_leak-003.fwpkg 
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
