---
title: Thermal Control
author: NVIDIA
weight: 680
product: SONiC
version: 202012
siteSlug: sonic
---

Thermal control keeps the switch at a proper temperature by using fans and other cooling devices. The thermal control daemon monitors the temperature of the CPU, ASIC and optical modules as well as the fan's running status. It stores the temperature values fetched from the sensors and the thermal devices, sending status to a database for future usage by the CLI, SNMP and other applications that utilize such information.

SONiC thermal control runs in both the kernel and user space. The kernel thermal control algorithm monitors the thermal zone temperature on devices such as the ASIC, optical modules and gearboxes, and triggers any change to the fan's speed according to the temperature's change. The user space thermal control algorithm handles abnormal cases such as fan unit absence, broken fans and PSU absence.

To get fan information, run `show platform fan`:

```
admin@switch:~$ show platform fan
FAN    Speed      Direction  Presence     Status  Timestamp
-----  ---------  ---------  -----------  ------  -----------------
FAN 1  85%        intake     Present      OK      20201212 09:38:16
FAN 2  60%        intake     Present      OK      20201212 09:38:16
FAN 3  75%        exhaust    Present      Not OK  20201212 09:38:16
FAN 4  65%        exhaust    Present      Not OK  20201212 09:38:16
```

To get thermal zone information, run `show platform temperature`:

```
admin@switch:~$ show platform temperature 
                Sensor    Temperature    High TH    Low TH    Crit High TH    Crit Low TH    Warning          Timestamp
----------------------  -------------  ---------  --------  --------------  -------------  ---------  -----------------
     Ambient ASIC Temp           34.0        N/A       N/A             N/A            N/A      False  20210325 23:42:09
 Ambient Fan Side Temp           27.0        N/A       N/A             N/A            N/A      False  20210325 23:42:09
Ambient Port Side Temp           26.5        N/A       N/A             N/A            N/A      False  20210325 23:42:09
       CPU Core 0 Temp           18.0       98.0       N/A            98.0            N/A      False  20210325 23:42:09
       CPU Core 1 Temp           18.0       98.0       N/A            98.0            N/A      False  20210325 23:42:09
       CPU Core 2 Temp           19.0       98.0       N/A            98.0            N/A      False  20210325 23:42:09
       CPU Core 3 Temp           19.0       98.0       N/A            98.0            N/A      False  20210325 23:42:09
    xSFP module 1 Temp            N/A        N/A       N/A             N/A            N/A      False  20210325 23:42:09
    xSFP module 2 Temp            N/A        N/A       N/A             N/A            N/A      False  20210325 23:42:09
    xSFP module 3 Temp            N/A        N/A       N/A             N/A            N/A      False  20210325 23:42:09
    xSFP module 4 Temp            N/A        N/A       N/A             N/A            N/A      False  20210325 23:42:09
    xSFP module 5 Temp            N/A        N/A       N/A             N/A            N/A      False  20210325 23:42:09
    xSFP module 6 Temp            N/A        N/A       N/A             N/A            N/A      False  20210325 23:42:09
    xSFP module 7 Temp            N/A        N/A       N/A             N/A            N/A      False  20210325 23:42:09
    xSFP module 8 Temp            N/A        N/A       N/A             N/A            N/A      False  20210325 23:42:09
    xSFP module 9 Temp            N/A        N/A       N/A             N/A            N/A      False  20210325 23:42:09
   xSFP module 10 Temp            N/A        N/A       N/A             N/A            N/A      False  20210325 23:42:09
   xSFP module 11 Temp            N/A        N/A       N/A             N/A            N/A      False  20210325 23:42:09
   xSFP module 12 Temp            N/A        N/A       N/A             N/A            N/A      False  20210325 23:42:09
   xSFP module 13 Temp            N/A        N/A       N/A             N/A            N/A      False  20210325 23:42:09
   xSFP module 14 Temp            N/A        N/A       N/A             N/A            N/A      False  20210325 23:42:09
   xSFP module 15 Temp            N/A        N/A       N/A             N/A            N/A      False  20210325 23:42:09
   xSFP module 16 Temp            N/A        N/A       N/A             N/A            N/A      False  20210325 23:42:09
```

## Configure Thermal Control

SONiC provides a JSON configuration file called `/usr/share/sonic/device/<platform name>/thermal_policy.json` for thermal control. The default configuration is:

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

- `thermal_control_algorithm`: Configures the status of the kernel thermal control algorithm.
  - To enable it when the thermal control daemon boots up, set `run_at_boot_up` to _true_.
  - To disable it and set a fix FAN speed value, set `run_at_boot_up` to _false_.
  - To set a percentage value, set the `fan_speed_when_suspend` to the required value.

    {{%notice note%}}
It is recommended to always enable kernel thermal control.

{{%/notice%}}
- `info_types`: Configures the thermal information required to be collected. This configuration is for development purpose and might be used by different vendors.
- `policies`: Configures the thermal policies that are run by the thermal control daemon. Each policy is constructed by a list of conditions and actions. For example, you can change the fan speed value when any fan is broken. You can even remove a policy, although this is not recommended.

### Dynamic Minimum Fan Speed Policy

Besides the policies in the configuration file above, some NVIDIA switch platforms support an additional private policy called *Dynamic minimum fan speed policy*. This policy sets the minimum allowed fan speed according to the ambient temperature so that the fan speed does not get too low or too high. The thermal control daemon sets fan speed to the minimum allowed value only if all thermal zones are in a normal state.

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
