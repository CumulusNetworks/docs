---
title: Thermal Control
author: Cumulus Networks
weight: 680
product: SONiC
version: 201911_MUR5
siteSlug: sonic
---

Thermal Control keeps the switch at a proper temperature by using cooling devices, e.g., fan. Thermal Control daemon monitors the devices' temperature (CPU, ASIC, optical modules, etc) and the fan's running status. It stores the temperature values fetched from the sensors and the thermal device running status to a database for future usage by the CLI and SNMP or other applications interested in such information.

SONiC Thermal Control runs on both the kernel and the user space. The kernel Thermal Control algorithm monitors the thermal zone temperature such as ASIC, optical modules and gearboxes, and triggers any change to the fan's speed according to the temperature's change. The user space Thermal Control algorithm handles abnormal cases such as fan unit absence, fan broken, PSU absence.

To get fan information, run `show platform fan`:


```
admin@sonic# show platform fan
FAN    Speed      Direction  Presence     Status  Timestamp
-----  ---------  ---------  -----------  ------  -----------------
FAN 1  85%        intake     Present      OK      20191112 09:38:16
FAN 2  60%        intake     Present      OK      20191112 09:38:16
FAN 3  75%        exhaust    Present      Not OK  20191112 09:38:16
FAN 4  65%        exhaust    Present      Not OK  20191112 09:38:16
```

To get thermal zone information, run `show platform temperature`:

```
                Sensor    Temperature    High TH    Low TH    Crit High TH    Crit Low TH    Warning          Timestamp
----------------------  -------------  ---------  --------  --------------  -------------  ---------  -----------------
 
                  ASIC           54.0      105.0       N/A           110.0            N/A      False  20200618 03:37:45
 
Ambient Fan Side Temp           25.5        N/A       N/A             N/A            N/A      False  20200618 03:37:45
 
Ambient Port Side Temp           32.0        N/A       N/A             N/A            N/A      False  20200618 03:37:45
```

## Configuring Thermal Control

SONiC provides a JSON configuration file for the Thermal Control. The configuration file is located at: /usr/share/sonic/device/$(platform name)/ thermal_policy.json. The default configuration file is:

```
{
    "thermal_control_algorithm": {
        "run_at_boot_up": "true",
        "fan_speed_when_suspend": "60"
    },
    "info_types": [
        {
            "type": "fan_info"
        },
        {
            "type": "psu_info"
        },
        {
            "type": "chassis_info"
        }
    ],
    "policies": [
        {
            "name": "any fan absence",
            "conditions": [
                {
                    "type": "fan.any.absence"
                }
            ],
            "actions": [
                {
                    "type": "fan.all.set_speed",
                    "speed": "100"
                }
            ]
        },
        {
            "name": "any psu absence",
            "conditions": [
                {
                    "type": "psu.any.absence"
                }
            ],
            "actions": [
                {
                    "type": "fan.all.set_speed",
                    "speed": "100"
                }
            ]
        },
        {
            "name": "any fan broken",
            "conditions": [
                {
                    "type": "fan.any.fault"
                }
            ],
            "actions": [
                {
                    "type": "fan.all.set_speed",
                    "speed": "100"
                }
            ]
        },
        {
            "name": "all fan and psu presence",
            "conditions": [
                {
                    "type": "fan.all.presence"
                },
                {
                    "type": "psu.all.presence"
                },
                {
                    "type": "fan.all.good"
                }
            ],
            "actions": [
                {
                    "type": "thermal.recover"
                }
            ]
        }
    ]
}
```

Where:

- "thermal_control_algorithm": Configures the status of the kernel thermal control algorithm.
  - To enable it when the thermal control daemon boots up, set `run_at_boot_up` to _true_
  - To disable it and set a fix FAN speed value, set `run_at_boot_up` to _false_
  - To set a percentage value, set the `fan_speed_when_suspend` to the required value

    {{%notice note%}}
It is recommended to always enable kernel thermal control.

{{%/notice%}}
- "info_types": Configures the thermal information required to be collected. This configuration is for developing purpose and might be used by different vendors.
- "policies": Configures the thermal policies that will be ran by the thermal control daemon. Each policy is constructed by a list of conditions and actions. For example, the user can change the fan speed value when any fan is broken. User can even remove a policy although it is not recommended.

### Dynamic Minimum Fan Speed Policy

Besides the policies in the configuration file above, some NVIDIA® Mellanox® switch platforms support an additional private policy called “Dynamic minimum fan speed policy”. The purpose of this policy is to set the minimum allowed fan speed according to the ambient temperature so that the fan speed will not be too low or too high. Thermal Control daemon will set fan speed to the minimum allowed value only if all thermal zones are in normal state.

| Platform | Support Dynamic Fan Speed Policy | Expected Behavior |
| -------- | -------------------------------- | ----------------- |
| SN2010 | Yes | Dynamic minimum fan speed |
| SN2100 | Yes | Dynamic minimum fan speed |
| SN2410 | Yes | Dynamic minimum fan speed |
| SN2700 | Yes | Dynamic minimum fan speed |
| SN2740 | Yes | Dynamic minimum fan speed |
| SN3420 | No | Fixed fan speed 60% |
| SN3700 | Yes | Dynamic minimum fan speed |
| SN3700C | Yes | Dynamic minimum fan speed |
| SN3800 | Yes | Dynamic minimum fan speed |
| SN4600C | No | Fixed fan speed 60% |
| SN4700 | No | Fixed fan speed 60% |
