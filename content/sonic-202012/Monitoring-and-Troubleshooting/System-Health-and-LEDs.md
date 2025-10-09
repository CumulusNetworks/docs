---
title: System Health and LEDs
author: NVIDIA
weight: 650
product: SONiC
version: 202012
siteSlug: sonic
---

SONiC uses the `monit` command to monitor the status of critical services. SONiC also utilizes PMON (process monitor) and its daemons (such as `psud` or `thermaltcld`) to collect status on peripheral devices. Status is also gathered in `syslog` and can be determined by the color of various system LEDs. See {{<link url="#modify-system-led-settings" text="below">}} for a description of the default LED settings.

A system health monitor daemon runs on the switch. Every 60 seconds it checks the `monit summary` command output as well as the PSU, fan and thermal status stored in the state DB. If `monit` detects an error with a service or peripheral device, it sets the system status LED to fault status. When a fault condition is fixed, the system status returns to normal status.

Before the switch finishes booting up, the system health monitoring daemon knows that the switch is in boot up status.

The switch enters a fault condition when any of the following events occur:

- The `monit` service is not available.
- A fan, PSU or ASIC data is not available.
- Incomplete data in the state database. For example, PSU voltage data is there but threshold data is not available.

`monit`, `thermalctld` and `psud` all raise `syslog` when a fault condition occurs, so the system health monitor only generates some general `syslog` output in these situation to avoid redundancy. For example, when a fault condition is met, "system health status change to fault" can be sent to `syslog`, then "system health status change to normal" can be sent when the system recovers.

The system health monitor service stars after the switch boots up, after the database.service and updategraph.service.

## monit summary Command

To determine the status of the processes and filesystems monitored by `monit`, run:

```
admin@switch:~$ sudo monit summary -B
Monit 5.20.0 uptime: 112d 17h 21m
 Service Name                     Status                      Type          
 mlx-2100-06                      Running                     System        
 rsyslog                          Running                     Process       
 root-overlay                     Accessible                  Filesystem    
 var-log                          Accessible                  Filesystem    
 routeCheck                       Status ok                   Program       
 telemetry|telemetry              Status ok                   Program       
 telemetry|dialout_client         Status ok                   Program       
 teamd|teamsyncd                  Status ok                   Program       
 teamd|teammgrd                   Status ok                   Program       
 syncd|syncd                      Status failed               Program       
 swss|orchagent                   Status failed               Program       
 swss|portsyncd                   Status failed               Program       
 swss|neighsyncd                  Status failed               Program       
 swss|vrfmgrd                     Status failed               Program       
 swss|vlanmgrd                    Status failed               Program       
 swss|intfmgrd                    Status failed               Program       
 swss|portmgrd                    Status failed               Program       
 swss|buffermgrd                  Status failed               Program       
 swss|nbrmgrd                     Status failed               Program       
 swss|vxlanmgrd                   Status failed               Program       
 snmp|snmpd                       Status failed               Program       
 snmp|snmp_subagent               Status failed               Program       
 sflow|sflowmgrd                  Status ok                   Program       
 lldp|lldpd_monitor               Status ok                   Program       
 lldp|lldp_syncd                  Status ok                   Program       
 lldp|lldpmgrd                    Status ok                   Program       
 database|redis_server            Status ok                   Program       
 bgp|zebra                        Status ok                   Program       
 bgp|fpmsyncd                     Status ok                   Program       
 bgp|bgpd                         Status ok                   Program       
 bgp|staticd                      Status ok                   Program       
 bgp|bgpcfgd                      Status ok                   Program       
 bgp|bgpmon                       Status ok                   Program 
```

{{%notice tip%}}

Running `monit summary` without the `-B` option presents the output in a table with the status in different colors depending upon the process state.

<pre>
admin@switch:~$ sudo monit summary
Monit 5.20.0 uptime: 112d 17h 7m
┌─────────────────────────────────┬────────────────────────────┬───────────────┐
│ Service Name                    │ Status                     │ Type          │
├─────────────────────────────────┼────────────────────────────┼───────────────┤
│ mlx-2100-06                     │ <span style="color: green;">Running</span>                    │ System        │
├─────────────────────────────────┼────────────────────────────┼───────────────┤
│ rsyslog                         │ <span style="color: green;">Running</span>                    │ Process       │
├─────────────────────────────────┼────────────────────────────┼───────────────┤
│ root-overlay                    │ <span style="color: green;">Accessible</span>                 │ Filesystem    │
├─────────────────────────────────┼────────────────────────────┼───────────────┤
│ var-log                         │ <span style="color: green;">Accessible</span>                 │ Filesystem    │
├─────────────────────────────────┼────────────────────────────┼───────────────┤
│ routeCheck                      │ <span style="color: green;">Status ok</span>                  │ Program       │
├─────────────────────────────────┼────────────────────────────┼───────────────┤
│ telemetry|telemetry             │ <span style="color: green;">Status ok</span>                  │ Program       │
├─────────────────────────────────┼────────────────────────────┼───────────────┤
│ telemetry|dialout_client        │ <span style="color: green;">Status ok</span>                  │ Program       │
├─────────────────────────────────┼────────────────────────────┼───────────────┤
│ teamd|teamsyncd                 │ <span style="color: green;">Status ok</span>                  │ Program       │
├─────────────────────────────────┼────────────────────────────┼───────────────┤
│ teamd|teammgrd                  │ <span style="color: green;">Status ok</span>                  │ Program       │
├─────────────────────────────────┼────────────────────────────┼───────────────┤
│ syncd|syncd                     │ <span style="color: red;">Status failed</span>              │ Program       │
├─────────────────────────────────┼────────────────────────────┼───────────────┤
│ swss|orchagent                  │ <span style="color: red;">Status failed</span>              │ Program       │
├─────────────────────────────────┼────────────────────────────┼───────────────┤
│ swss|portsyncd                  │ <span style="color: red;">Status failed</span>              │ Program       │
├─────────────────────────────────┼────────────────────────────┼───────────────┤
│ swss|neighsyncd                 │ <span style="color: red;">Status failed</span>              │ Program       │
├─────────────────────────────────┼────────────────────────────┼───────────────┤
│ swss|vrfmgrd                    │ <span style="color: red;">Status failed</span>              │ Program       │
├─────────────────────────────────┼────────────────────────────┼───────────────┤
│ swss|vlanmgrd                   │ <span style="color: red;">Status failed</span>              │ Program       │
├─────────────────────────────────┼────────────────────────────┼───────────────┤
│ swss|intfmgrd                   │ <span style="color: red;">Status failed</span>              │ Program       │
├─────────────────────────────────┼────────────────────────────┼───────────────┤
│ swss|portmgrd                   │ <span style="color: red;">Status failed</span>              │ Program       │
├─────────────────────────────────┼────────────────────────────┼───────────────┤
│ swss|buffermgrd                 │ <span style="color: red;">Status failed</span>              │ Program       │
├─────────────────────────────────┼────────────────────────────┼───────────────┤
│ swss|nbrmgrd                    │ <span style="color: red;">Status failed</span>              │ Program       │
├─────────────────────────────────┼────────────────────────────┼───────────────┤
│ swss|vxlanmgrd                  │ <span style="color: red;">Status failed</span>              │ Program       │
├─────────────────────────────────┼────────────────────────────┼───────────────┤
│ snmp|snmpd                      │ <span style="color: red;">Status failed</span>              │ Program       │
├─────────────────────────────────┼────────────────────────────┼───────────────┤
│ snmp|snmp_subagent              │ <span style="color: red;">Status failed</span>              │ Program       │
├─────────────────────────────────┼────────────────────────────┼───────────────┤
│ sflow|sflowmgrd                 │ <span style="color: green;">Status ok</span>                  │ Program       │
├─────────────────────────────────┼────────────────────────────┼───────────────┤
│ lldp|lldpd_monitor              │ <span style="color: green;">Status ok</span>                  │ Program       │
├─────────────────────────────────┼────────────────────────────┼───────────────┤
│ lldp|lldp_syncd                 │ <span style="color: green;">Status ok</span>                  │ Program       │
├─────────────────────────────────┼────────────────────────────┼───────────────┤
│ lldp|lldpmgrd                   │ <span style="color: green;">Status ok</span>                  │ Program       │
├─────────────────────────────────┼────────────────────────────┼───────────────┤
│ database|redis_server           │ <span style="color: green;">Status ok</span>                  │ Program       │
├─────────────────────────────────┼────────────────────────────┼───────────────┤
│ bgp|zebra                       │ <span style="color: green;">Status ok</span>                  │ Program       │
├─────────────────────────────────┼────────────────────────────┼───────────────┤
│ bgp|fpmsyncd                    │ <span style="color: green;">Status ok</span>                  │ Program       │
├─────────────────────────────────┼────────────────────────────┼───────────────┤
│ bgp|bgpd                        │ <span style="color: green;">Status ok</span>                  │ Program       │
├─────────────────────────────────┼────────────────────────────┼───────────────┤
│ bgp|staticd                     │ <span style="color: green;">Status ok</span>                  │ Program       │
├─────────────────────────────────┼────────────────────────────┼───────────────┤
│ bgp|bgpcfgd                     │ <span style="color: green;">Status ok</span>                  │ Program       │
├─────────────────────────────────┼────────────────────────────┼───────────────┤
│ bgp|bgpmon                      │ <span style="color: green;">Status ok</span>                  │ Program       │
└─────────────────────────────────┴────────────────────────────┴───────────────┘
</pre>

{{%/notice%}}

## Exclude Devices or Services from Monitoring

You can exclude some services or devices from being monitored. To do so create a file called `system_health_monitoring_config.json` in the `/usr/share/sonic/device/<platform_name>/` directory. The `device` directory lists all supported switches, so you can press *Tab* to display all the switches, then type ahead to select your switch model.

The JSON array in the file takes two arguments: `services_to_ignore` and `devices_to_ignore` for the services or processes you do not want to monitor and for the hardware you do not want to monitor, respectively.

For example:

```
{
  "services_to_ignore": ["snmpd","snmp_subagent"],
  "devices_to_ignore": ["psu","fan.speed","fan1", "fan2.speed"],
}
```

You can ignore any processes (such as `orchagent`, `snmpd` or `telemetry`) as well as the following devices:

- asic: Ignore all ASIC checks.
- fan: Ignore all fan checks.
- fan.speed: Ignore fan speed checks.
- &lt;fan_name>: Ignore checks for a specific fan.
- &lt;fan_name>.speed: Ignore speed checks for a specific fan.
- psu: Ignore all PSU checks.
- psu.temperature: Ignore temperature checks for all PSUs.
- psu.voltage: Ignore voltage checks for all PSUs.
- &lt;psu_name>: Ignore checks for a specific PSU.
- &lt;psu_name>.temperature: Ignore temperature checks for a specific PSU.
- &lt;psu_name>.voltage: Ignore voltage checks for a specific PSU.

## Modify System LED Settings

By default, the system LEDs behave as follows:

| Color | Status | Description |
| ----- | ------ | ----------- |
| Off | off | Switch is powered down. |
| Blinking amber | boot up | Switch is booting up. |
| Red | fault | Switch is in fault status. |
| Green | Normal | Switch in normal status. |

Some switch vendors may have different LED color capabilities, so you can configure the LED colors for various system statuses. Add the following JSON to `/usr/share/sonic/device/<platform_name>/system_health_monitoring_config.json`:

```
{
  "led_color": {
    "fault": "amber",
    "normal": "green",
    "booting": "orange_blink"
  }
}
```
