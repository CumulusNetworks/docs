---
title: Fluentd Reference
author: NVIDIA
weight: 1154
toc: 3
bookhidden: true

---

## Enable Fluentd Streaming

To enable Fluentd streaming from NVlink4 switches to your Fluent collector, use the `netq_telemetry_agent_handler` tool to configure streaming parameters. The `netq_telemetry_agent_handler` application can be downloaded from {{<exlink url="https://apps.nvidia.com/pid/contentlibraries/detail?id=1097442" text="NVIDIA Product Information Delivery Portal">}}. The syntax for the command can be reviewed on the command line with the `netq_telemetry_agent_handler -h` command:

```
$ ./netq_telemetry_agent_handler -h
Usage of ./netq_telemetry_agent_handler:
  -add
        Append a new destination collector
  -address value
        List of addresses for discovery
  -delete
        Delete destination collectors
  -delete_all
        Delete all destination collectors
  -destination value
        List of fluent collectors (format <ip_addr>,<port>,<tcp/tls>)
  -domain string
        Domain name (optional)
  -domain_id string
        Domain identifier (optional)
  -password string
        NVOS http password (default "admin")
  -replace
        Replace destination collectors
  -user string
        NVOS http user (default "admin")
Examples for configuring one switch to append a fluent destination:
        ./netq_telemetry_agent_handler -add -address 192.168.0.17 -destination 10.188.44.17,30001,tcp -user admin -password admin -domain test -domain_id 1 -domain my_domain
Examples for configuring one switch to append two fluent destinations:
        ./netq_telemetry_agent_handler -add -address 192.168.0.17 -destination 10.188.44.17,30001,tcp -destination 10.188.44.43,30001,tcp -user admin -password admin -domain_id 1 -domain my_domain
Examples for configuring two switches to replace with one fluent destination:
        ./netq_telemetry_agent_handler -replace -address 192.168.0.17 -address 192.168.0.21 -destination 10.188.44.17,30001,tcp -user admin -password admin -domain_id 1 -domain my_domain
Examples for configuring one switche to delete a fluent destination:
        ./netq_telemetry_agent_handler -delete -address 192.168.0.17 -destination 10.188.44.17,30001,tcp -user admin -password admin -domain_id 1 -domain my_domain
Examples for configuring one switch to delete all fluent destinations:
        ./netq_telemetry_agent_handler -delete_all -address 192.168.0.17 -user admin -password admin -domain_id 1 -domain my_domain
```
## NVLink4 Fluentd Message Examples

Expand the dropdown menu to view NVLink4 Fluentd message output in JSON format: 

{{< expand "JSON examples" >}}
```
ResourceUtil
{
  "aid": "s-a14-ou20-ch1-evt-kg4.nvidia.com",
  "message_type": "ResourceUtil",
  "ts": 1698784259506,
  "trans_mode": 1,
  "message": [
    {
      "active": true,
      "cpu_utilization": 132,
      "deleted": false,
      "disk_utilization": {
        "/dev/sda10": {
          "percent": 10.61,
          "total": 50950307840,
          "used": 5406457856
        },
        "/dev/sda8": {
          "percent": 1.65,
          "total": 190840832,
          "used": 3145728
        }
      },
      "domain": "",
      "hostname": "s-a14-ou20-ch1-evt-kg4.nvidia.com",
      "is_disk_read_only": true,
      "mem_utilization": 12.34,
      "message_type": "ResourceUtil",
      "timestamp": 1698784259506
    }
  ]
}

Port
{
  "aid": "s-a14-ou20-ch1-evt-kg4.nvidia.com",
  "message_type": "Port",
  "ts": 1698784259506,
  "trans_mode": 1,
  "message": [
    {
      "active": true,
      "connector": "Optical module",
      "deleted": false,
      "domain": "",
      "hostname": "s-a14-ou20-ch1-evt-kg4.nvidia.com",
      "identifier": "OSFP",
      "ifname": "NVL1/14/2/1",
      "length": "30m OM3 ,50m OM4 ,50m OM5",
      "message_type": "Port",
      "part_number": "MMA4Z00-NS",
      "serial_number": "MT2306FT11744",
      "speed": "106.250 Gbps",
      "state": "active",
      "timestamp": 1698784259506,
      "transceiver": "2 x NDR, 2 x 400G-SR4",
      "vendor_name": "NVIDIA"
    }
  ]
}

Power
{
  "aid": "s-a14-ou20-ch1-evt-kg4.nvidia.com",
  "message_type": "Power",
  "ts": 1698784259506,
  "trans_mode": 1,
  "message": [
    {
      "active": true,
      "deleted": false,
      "domain": "",
      "hostname": "s-a14-ou20-ch1-evt-kg4.nvidia.com",
      "message_type": "Power",
      "s_adapter_name": "PS1",
      "s_power_in_input": 582.65,
      "s_power_out_input": 536,
      "s_voltage_in_input": 200.5,
      "s_voltage_in_max": 13.8,
      "s_voltage_in_min": 10.2,
      "s_voltage_out_input": 12.02,
      "timestamp": 1698784259506
    }
  ]
}

PSU
{
  "aid": "s-a14-ou20-ch1-evt-kg4.nvidia.com",
  "message_type": "PSU",
  "ts": 1698784259506,
  "trans_mode": 1,
  "message": [
    {
      "active": true,
      "deleted": false,
      "domain": "",
      "hostname": "s-a14-ou20-ch1-evt-kg4.nvidia.com",
      "message_type": "PSU",
      "s_name": "PS1",
      "s_prev_state": "ok",
      "s_state": "ok",
      "timestamp": 1698784259506
    }
  ]
}

Fan
{
  "aid": "s-a14-ou20-ch1-evt-kg4.nvidia.com",
  "message_type": "Fan",
  "ts": 1698784259506,
  "trans_mode": 1,
  "message": [
    {
      "active": true,
      "deleted": false,
      "domain": "",
      "hostname": "s-a14-ou20-ch1-evt-kg4.nvidia.com",
      "message_type": "Fan",
      "s_input": 29446,
      "s_name": "FAN3-F1",
      "s_prev_state": "OK",
      "s_state": "ok",
      "timestamp": 1698784259506
    }
  ]
}

Temp
{
  "aid": "s-a14-ou20-ch1-evt-kg4.nvidia.com",
  "message_type": "Temp",
  "ts": 1698784259506,
  "trans_mode": 1,
  "message": [
    {
      "active": true,
      "deleted": false,
      "domain": "",
      "hostname": "s-a14-ou20-ch1-evt-kg4.nvidia.com",
      "message_type": "Temp",
      "s_desc": "PS2 power-mon T1",
      "s_input": 54,
      "s_name": "temp1",
      "s_prev_state": "ok",
      "s_state": "ok",
      "timestamp": 1698784259506
    }
  ]
}

Address
{
  "aid": "s-a14-ou20-ch1-evt-kg4.nvidia.com",
  "message_type": "Address",
  "ts": 1698784259506,
  "trans_mode": 1,
  "message": [
    {
      "active": true,
      "deleted": false,
      "domain": "",
      "hostname": "s-a14-ou20-ch1-evt-kg4.nvidia.com",
      "ifname": "mgmt0",
      "is_ipv6": false,
      "mask": 32,
      "message_type": "Address",
      "prefix": "10.137.20.77",
      "timestamp": 1698784259506,
      "vrf": "default"
    }
  ]
}

Inventory
{
  "aid": "s-a14-ou20-ch1-evt-kg4.nvidia.com",
  "message_type": "Inventory",
  "ts": 1698784259506,
  "trans_mode": 1,
  "message": [
    {
      "active": true,
      "agent_version": "N/A",
      "asic_core_bw": "N/A",
      "asic_data": "[]",
      "asic_model": "N/A",
      "asic_model_id": "SGXLS10-NS2F",
      "asic_ports": "NVL4-1,NVL4-2,EROT-1,EROT-2",
      "asic_vendor": "NVIDIA",
      "cpu_arch": "x86_64",
      "cpu_data": "[]",
      "cpu_max_freq": "",
      "cpu_model": "",
      "cpu_nos": "4",
      "deleted": false,
      "disk_data": "[{\"firmware_version\":\"0202-000\",\"model\":\"StorFly VSFBM4XI060G-MLX\",\"serial_number\":\"58247-0059\"}]",
      "disk_total_size": "60.0 GB",
      "domain": "",
      "hostname": "s-a14-ou20-ch1-evt-kg4.nvidia.com",
      "license_data": "[{\"license\":\"LK2-RESTRICTED_CMDS_GEN2-43A5-Q7Y9-1X1U-888A-2B7M-9JLR-E0\",\"name\":\"B8:3F:D2:1F:07:68 (ok)\"}]",
      "license_state": "ok",
      "memory_data": "[]",
      "memory_total_size": "15779 MB total",
      "message_type": "Inventory",
      "os_name": "NVOS",
      "os_version": "20231009-190322",
      "os_version_id": "X86_64 20231009-190322 2023-10-09 16:08:03 x86_64",
      "platform_base_mac": "B8:3F:D2:1F:07:68",
      "platform_label_revision": "A4",
      "platform_mfg_date": "N/A",
      "platform_model": "unknown",
      "platform_part_number": "N/A",
      "platform_serial_number": "MT2243XZ0C2L",
      "platform_vendor": "NVIDIA",
      "timestamp": 1698784259506
    }
  ]
}

Node
{
  "aid": "s-a14-ou20-ch1-evt-kg4.nvidia.com",
  "message_type": "Node",
  "ts": 1698784259506,
  "trans_mode": 1,
  "message": [
    {
      "active": true,
      "deleted": false,
      "domain": "",
      "hostname": "s-a14-ou20-ch1-evt-kg4.nvidia.com",
      "last_reinit": 1698784661,
      "lastboot": 1698784661,
      "message_type": "Node",
      "ntp_state": "yes",
      "sys_uptime": 1698351073,
      "timestamp": 1698784661,
      "version": "N/A"
    }
  ]
}
Link
{
  "aid": "s-a14-ou20-ch1-evt-kg4.nvidia.com",
  "message_type": "Link",
  "ts": 1698784259506,
  "trans_mode": 1,
  "message": [
    {
      "active": true,
      "admin_state": "Enabled",
      "deleted": false,
      "domain": "",
      "down_reason": "",
      "hostname": "s-a14-ou20-ch1-evt-kg4.nvidia.com",
      "ifalias": "",
      "ifname": "NVL2/28/1/2",
      "kind": "nvl",
      "managed": true,
      "master": "",
      "message_type": "Link",
      "mtu": 256,
      "oper_state": "active",
      "pre_failure": "no",
      "recovery_count": 0,
      "timestamp": 1698784259506,
      "vrf": "default"
    }
  ]
}

NvlStats
{
  "aid": "s-a14-ou20-ch1-evt-kg4.nvidia.com",
  "message_type": "NvlStats",
  "ts": 1698784259506,
  "trans_mode": 1,
  "message": [
    {
      "active": true,
      "crc_errors": 358,
      "deleted": false,
      "domain": "",
      "hostname": "s-a14-ou20-ch1-evt-kg4.nvidia.com",
      "ifname": "NVL1/6/2/2",
      "message_type": "NvlStats",
      "rx_all_flits": 0,
      "rx_crc_bit_error_rate": 0,
      "rx_data_flits": 0,
      "rx_physical_bit_error_rate": 0,
      "rx_physical_errors_per_lane_0": 0,
      "rx_physical_errors_per_lane_1": 0,
      "rx_replay_rate": 0,
      "timestamp": 1698784259506,
      "tx_all_flits": 0,
      "tx_data_flits": 0,
      "tx_replay_rate": 0,
      "wait": 0
    }
  ]
}

Dom
{
  "aid": "s-a14-ou20-ch1-evt-kg4.nvidia.com",
  "message_type": "Dom",
  "ts": 1698784259506,
  "trans_mode": 1,
  "message": [
    {
      "active": true,
      "deleted": false,
      "domain": "",
      "hostname": "s-a14-ou20-ch1-evt-kg4.nvidia.com",
      "identifier": "",
      "ifname": "NVL1/5/2/1",
      "laser_bias_current": {
        "Channel 1": "9.07200 mA",
        "Channel 2": "8.96600 mA",
        "Channel 3": "9.14200 mA",
        "Channel 4": "9.50800 mA",
        "Channel 5": "9.22800 mA",
        "Channel 6": "9.42000 mA",
        "Channel 7": "9.28000 mA",
        "Channel 8": "9.05400 mA"
      },
      "laser_bias_current_high_alarm_th": "11.00000 mA",
      "laser_bias_current_high_warning_th": "131 mA",
      "laser_bias_current_low_alarm_th": "7.00000 mA",
      "laser_bias_current_low_warning_th": "0 mA",
      "laser_output_power": {
        "Channel 1": "1.18400 mW / 0.73352 dBm",
        "Channel 2": "1.22080 mW / 0.86645 dBm",
        "Channel 3": "1.18750 mW / 0.74634 dBm",
        "Channel 4": "1.22320 mW / 0.87497 dBm",
        "Channel 5": "1.19420 mW / 0.77077 dBm",
        "Channel 6": "1.23460 mW / 0.91526 dBm",
        "Channel 7": "1.17860 mW / 0.71366 dBm",
        "Channel 8": "1.23960 mW / 0.93282 dBm"
      },
      "laser_output_power_high_alarm_th": "2.51190 mW / 4.00002 dBm",
      "laser_output_power_high_warning_th": "6.5535 mW",
      "laser_output_power_low_alarm_th": "0.45000 mW / -3.46788 dBm",
      "laser_output_power_low_warning_th": "0 mW",
      "laser_rx_power": {
        "Channel 1": "1.17770 mW / 0.71035 dBm",
        "Channel 2": "1.21720 mW / 0.85362 dBm",
        "Channel 3": "1.15860 mW / 0.63934 dBm",
        "Channel 4": "1.20620 mW / 0.81419 dBm",
        "Channel 5": "1.16100 mW / 0.64832 dBm",
        "Channel 6": "1.21460 mW / 0.84433 dBm",
        "Channel 7": "1.16280 mW / 0.65505 dBm",
        "Channel 8": "1.14250 mW / 0.57856 dBm"
      },
      "laser_rx_power_high_alarm_th": "2.51190 mW / 4.00002 dBm",
      "laser_rx_power_high_warning_th": "6.5535 mW",
      "laser_rx_power_low_alarm_th": "0.31620 mW / -5.00038 dBm",
      "laser_rx_power_low_warning_th": "0 mW",
      "message_type": "Dom",
      "module_temp": "66.000000 degrees C/150.800003 degrees F",
      "module_temp_high_alarm_th": "80.000000 degrees C/176.000000 degrees F",
      "module_temp_high_warning_th": "127.000000 degrees C/260.600006 degrees F",
      "module_temp_low_alarm_th": "-10.000000 degrees C/14.000000 degrees F",
      "module_temp_low_warning_th": "-127.000000 degrees C/-196.599991 degrees F",
      "module_voltage": "3.23440 V",
      "module_voltage_high_alarm_th": "3.50000 V",
      "module_voltage_high_warning_th": "0 V",
      "module_voltage_low_alarm_th": "3.10000 V",
      "module_voltage_low_warning_th": "6.5535 V",
      "timestamp": 1698784259506
    }
  ]
}

NvlDeviceInfo
{
  "aid": "s-a14-ou20-ch1-evt-kg4.nvidia.com",
  "message_type": "NvlDeviceInfo",
  "ts": 1698784259506,
  "trans_mode": 1,
  "message": [
    {
      "active": true,
      "bind_interface_ip": "10.137.20.77",
      "deleted": false,
      "domain": "",
      "hostname": "s-a14-ou20-ch1-evt-kg4.nvidia.com",
      "log_append_to_log": "enabled",
      "log_level": "info",
      "message_type": "NvlDeviceInfo",
      "shutdown": "no",
      "starting_tcp_port": "16000",
      "state": "running",
      "timestamp": 1698784259506,
      "uid_led_status": "Off"
    }
  ]
}

NvlEvents
{
  "aid": "s-a14-ou20-ch1-evt-kg4.nvidia.com",
  "message_type": "NvlEvents",
  "ts": 1698784259506,
  "trans_mode": 1,
  "message": [
    {
      "ASIC": "NVL4-1",
      "Description": "-",
      "DomainName": "",
      "InstanceLink": "1/5/1/2 (44)",
      "SXID": "-",
      "Severity": "Non-fatal",
      "Subinstance": "-",
      "Time": 1698350778,
      "Type": "Port up",
      "active": true,
      "deleted": false,
      "domain": "",
      "hostname": "s-a14-ou20-ch1-evt-kg4.nvidia.com",
      "message_type": "NvlEvents",
      "timestamp": 1698784259506
    },
  ]
}
```
{{< /expand >}}
<br>
## Fluentd Message Reference

{{< expand "Fluentd message reference" >}}

**General**

 | Field Name |Type | Description |
 |--- | --- | --- | 
 | date | Double | Message timestamp by fluent-bit | 
 | aid | String | Agent ID/hostname | 
 | domain | String | Domain name | 
 | message_type | String | Message type (node, inventory, link, etc.) | 
 | ts | Long | Message timestamp | 
 | trans_mode | String | Transition mode (full, partial, first segment, mid segment, last segment) | 
 | message | Object | Message content for the message type | 

 **Node**
 | Field Name |Type | Description |
 |--- | --- | --- | 
 | domain | String | Domain name | 
 | deleted | Boolean | Record deletion status | 
 | hostname | String | Hostname | 
 | last_reinit | Long | Last system initialization | 
 | lastboot | Long | Last system reboot | 
 | ntp_state | String | NTP daemon state | 
 | sys_uptime | Long | System uptime | 
 | timestamp | Long | Inner message timestamp | 
 | version | String | Agent version | 


**Inventory**
 | Field Name |Type | Description |
 |--- | --- | --- | 
 | active | Boolean | Record activity status | 
 | agent_version | String | Agent version | 
 | asic_core_bw | String | (not supported) | 
 | asic_data | String | Additional ASIC data (not supported) | 
 | asic_model | String | ASIC model | 
 | asic_model_id | String | ASIC model ID (system type) | 
 | asic_ports | String | ASIC ports | 
 | asic_vendor | String | ASIC vendor (hard-coded NVIDIA) | 
 | cpu_arch | String | CPU architecture | 
 | cpu_data | String | (not supported) | 
 | cpu_max_freq | String | CPU max frequency | 
 | cpu_model | String | CPU model | 
 | cpu_nos | String | Number of CPU nos | 
 | deleted | Boolean | Record deletion status | 
 | disk_data | String | Additional disk data information | 
 | disk_total_size | String | Disk total size | 
 | domain | String | Domain name | 
 | hostname | String | Hostname | 
 | license_data | String | License information | 
 | license_state | String | License state | 
 | memory_data | String | Additional memory data information (not supported) | 
 | memory_total_size | String | Memory total size on the switch | 
 | message_type | String | Message type | 
 | os_name | String | Operating system name | 
 | os_version | String | Operating system version | 
 | os_version_id | String | Operating system version summary | 
 | platform_base_mac | String | Platform management MAC address | 
 | platform_label_revision | String | Platform label revision (not supported) | 
 | platform_mfg_date | String | Platform manufacture data (not supported) | 
 | platform_model | String | Platform model | 
 | platform_part_number | String | Platform part number (not supported) | 
 | platform_serial_number | String | Platform serial number (not supported) | 
 | platform_vendor | String | Platform vendor (hard-coded NVIDIA) | 
 | timestamp | Long | Message timestamp | 

 **ResourceUtil**
 | Field Name |Type | Description |
 |--- | --- | --- | 
 | active | Boolean | Record activity status | 
 | cpu_utilization | String | Total CPU utilization as a percentage | 
 | deleted | Boolean | Record deletion status | 
 | mem_utilization | String | Show memory utilization as a percentage | 
 | message_type | String | Message type | 
 | timestamp | Long | Message timestamp | 
 | disk_utilization | List | Show disk utilization as a percentage | 
 | "disk_utilization" Item start |  |  | 
 | percent | Double | Percentage of used disk space | 
 | total | Long | Total disk utilization in bytes | 
 | used | Long | Used disk utilization in bytes | 
 | is_disk_read_only | Boolean | Read-only status (always true) | 

 **Port**
 | Field Name |Type | Description |
 |--- | --- | --- | 
 | active | Boolean | Record activity status | 
 | connector | String | Interface connector (not supported) | 
 | deleted | Boolean | Record deletion status | 
 | hostname | String | Hostname | 
 | identifier | String | Interface identifier (not supported) | 
 | length | String |  | 
 | ifname | String | Interface name | 
 | message_type | String | Message type | 
 | part_number | String | Interface part number (not supported) | 
 | serial_number | String | Interface serial number (not supported) | 
 | speed | String | Interface port speed | 
 | state | String | Interface operational state | 
 | timestamp | Long | Message timestamp | 
 | transceiver | String | Transceiver information (not supported) | 
 | vendor_name | String | Interface vendor (not supported) | 


 **Fan**
  | Field Name |Type | Description |
 |--- | --- | --- | 
 | active | Boolean | Record activity status | 
 | deleted | Boolean | Record deletion status | 
 | hostname | String | Hostname | 
 | message_type | String | Message type | 
 | s_input | String | Fan source input | 
 | s_name | String | Fan source name | 
 | s_prev_state | String | Fan previous state | 
 | s_state | String | Fan current state | 
 | timestamp | Long | Message timestamp | 
 | Temp |  |  | 
 | active | Boolean | Record activity status | 
 | deleted | Boolean | Record deletion status | 
 | hostname | String | Hostname | 
 | message_type | String | Message type | 
 | s_desc | String | Temperature description | 
 | s_input | String | Temperature input | 
 | s_name | String | Temperature name | 
 | s_prev_state | String | Temperature previous state | 
 | s_state | String | Temperature current state | 
 | timestamp | Long | Message timestamp | 


 **Power**
  | Field Name |Type | Description |
 |--- | --- | --- | 
 | active | Boolean | Record activity status | 
 | deleted | Boolean | Record deletion status | 
 | hostname | String | Hostname | 
 | message_type | String | Message type | 
 | s_adapter_name | String | Message adapter name | 
 | timestamp | Long | Message timestamp | 

 **PSU**
 | Field Name |Type | Description |
 |--- | --- | --- | 
 | active | Boolean | Record activity status | 
 | deleted | Boolean | Record deletion status | 
 | hostname | String | Hostname | 
 | message_type | String | Message type | 
 | s_name | String | PSU name | 
 | s_prev_state | String | PSU previous state | 
 | s_state | String | PSU current state | 
 | timestamp | Long | Message timestamp | 


 **Link**
  | Field Name |Type | Description |
 |--- | --- | --- | 
 | active | Boolean | Record activity status | 
 | admin_state | String | Interface admin state | 
 | deleted | Boolean | Record deletion status | 
 | down_reason | String | Interface down reason | 
 | hostname | String | Hostname | 
 | ifalias | String | Interface description | 
 | ifname | String | Interface name | 
 | kind | String | Interface type | 
 | managed | String | Interface device is managed | 
 | master | String | Interface parent device | 
 | message_type | String | Message type | 
 | mtu | String | Interface MTU | 
 | oper_state | String | Interface operational state | 
 | timestamp | Long | Message timestamp | 

**NvlStats**
 | Field Name |Type | Description |
 |--- | --- | --- | 
 | active | Boolean | Record activity status | 
 | crc_errors | Long | CRC errors counter | 
 | deleted | Boolean | Record deletion status | 
 | hostname | String | Hostname | 
 | ifname | String | Interface name | 
 | message_type | String | Message type | 
 | rx_all_flits | Long | RX all flits counter | 
 | rx_data_flits | Long | RX data flits counter | 
 | timestamp | Long | Message timestamp | 
 | tx_all_flits | Long | TX all flits counter | 
 | tx_data_flits | Long | TX data flits counter | 
 | rx_physical_bit_error_rate | Double | RX physical bit error rate | 
 | rx_physical_errors_per_lane_0 | Long | RX physical errors lane 0 | 
 | rx_physical_errors_per_lane_1 | Long | RX physical errors lane 1 | 
 | rx_crc_bit_error_rate | Double | RX CRC but error rate | 
 | tx_replay_rate | Double | TX replay rate | 
 | rx_replay_rate | Double | RX replay rate | 
 | wait | Long | TX wait counter | 

**NVL device info**
 | Field Name |Type |Short Description |
 |--- | --- | --- | 
 | active | Boolean | Record activity status | 
 | bind_interface_ip | String | Binded interface IP | 
 | deleted | Boolean | Record deletion status | 
 | hostname | String | Hostname | 
 | log_append_to_log | Boolean | Log appended to log | 
 | log_level | String | Log level | 
 | message_type | String | Message type | 
 | shutdown | String | Shutdown state | 
 | starting_tcp_port | String | Starting TCP port | 
 | uid_led_status | String | Current switch LED status | 
 | state | String | LFM state | 
 | timestamp | Long | Message timestamp |

 **DOM**
  | Field Name |Type |Short Description |
 |--- | --- | --- |  
 | active | Boolean | Record activity status | 
 | deleted | Boolean | Record deletion status | 
 | hostname | String | Hostname | 
 | identifier | String | Identifier (not supported) | 
 | ifname | String | Interface name | 
 | laser_bias_current | Object |  | 
 | "laser_bias_current" start |  |  | 
 | Channel 1 | String | Channel 1 | 
 | Channel 2 | String | Channel 2 | 
 | Channel 3 | String | Channel 3 | 
 | Channel 4 | String | Channel 4 | 
 | Channel 5 | String | Channel 5 | 
 | Channel 6 | String | Channel 6 | 
 | Channel 7 | String | Channel 7 | 
 | Channel 8 | String | Channel 8 | 
 | "laser_bias_current" end |  |  | 
 | laser_bias_current_high_alarm_th | String | Laser bias current high alarm threshold | 
 | laser_bias_current_high_warning_th | String | Laser bias current high warning threshold | 
 | laser_bias_current_low_alarm_th | String | Laser bias current low alarm threshold | 
 | laser_bias_current_low_warning_th | String | Laser bias current low warning threshold | 
 | laser_output_power | Object |  | 
 | "laser_output_power" start |  |  | 
 | Channel 1 | String | Channel 1 | 
 | Channel 2 | String | Channel 2 | 
 | Channel 3 | String | Channel 3 | 
 | Channel 4 | String | Channel 4 | 
 | Channel 5 | String | Channel 5 | 
 | Channel 6 | String | Channel 6 | 
 | Channel 7 | String | Channel 7 | 
 | Channel 8 | String | Channel 8 | 
 | "laser_output_power" end |  |  | 
 | laser_output_power_high_alarm_th | String | Laser output power high alarm threshold | 
 | laser_output_power_high_warning_th | String | Laser output power high warning threshold | 
 | laser_output_power_low_alarm_th | String | Laser output power low alarm threshold | 
 | laser_output_power_low_warning_th | String | Laser output power low warning threshold | 
 | laser_rx_power | Object |  | 
 | "laser_rx_power" start |  |  | 
 | Channel 1 | String | Channel 1 | 
 | Channel 2 | String | Channel 2 | 
 | Channel 3 | String | Channel 3 | 
 | Channel 4 | String | Channel 4 | 
 | Channel 5 | String | Channel 5 | 
 | Channel 6 | String | Channel 6 | 
 | Channel 7 | String | Channel 7 | 
 | Channel 8 | String | Channel 8 | 
 | "laser_rx_power" end |  |  | 
 | laser_rx_power_high_alarm_th | String | Laser RX power high alarm threshold | 
 | laser_rx_power_high_warning_th | String | Laser RX power high warning threshold | 
 | laser_rx_power_low_alarm_th | String | Laser RX power low alarm threshold | 
 | laser_rx_power_low_warning_th | String | Laser RX power low warning threshold | 
 | message_type | String | Message type | 
 | module_temp | String | Module temperature | 
 | module_temp_high_alarm_th | String | Module temperature high alarm threshold | 
 | module_temp_high_warning_th | String | Module temperature high warning threshold | 
 | module_temp_low_alarm_th | String | Module temperature low alarm threshold | 
 | module_temp_low_warning_th | String | Module temperature low warning threshold | 
 | module_voltage | String | Module voltage | 
 | module_voltage_high_alarm_th | String | Module voltage high alarm threshold | 
 | module_voltage_high_warning_th | String | Module voltage high warning threshold | 
 | module_voltage_low_alarm_th | String | Module voltage low alarm threshold | 
 | module_voltage_low_warning_th | String | Module voltage low warning threshold | 
 | timestamp | Long |  | 

**MGMT address**
 | Field Name |Type |Short Description |
 |--- | --- | --- | 
 | ifname | String | Interface attached to mgmt address | 
 | prefix | String | IP address for mgmt address | 
 | mask | String | Mask for mgmt address | 
 | vrf | String | VRF for mgmt address | 
 | is_ipv6 | Boolean | IPv6 address status | 

 **NVL events**
  | Field Name |Type |Short Description |
 |--- | --- | --- | 
 | ASIC | String | ASIC source | 
 | SXID | String |  | 
 | Description | String | Event description | 
 | Severity | String | Event severity | 
 | InstanceLink | String |  | 
 | Subinstance | String |  | 
 | DomainName | String | Domain name | 
 | timestamp | Long | Event timestamp | 

{{< /expand >}}
## Fluentd Collection

You can use your own Fluent collector, or use {{<exlink url="https://fluentbit.io" text="Fluent Bit">}}:

```
$ /opt/fluent-bit/bin/fluent-bit -i forward -p port=30001 -o stdout -p format=json_lines -m '*'
Fluent Bit v2.0.5
* Copyright (C) 2015-2022 The Fluent Bit Authors
* Fluent Bit is a CNCF sub-project under the umbrella of Fluentd
* https://fluentbit.io


[2023/01/19 03:15:40] [ info] [fluent bit] version=2.0.5, commit=, pid=2341886
[2023/01/19 03:15:40] [ info] [storage] ver=1.3.0, type=memory, sync=normal, checksum=off, max_chunks_up=128
[2023/01/19 03:15:40] [ info] [cmetrics] version=0.5.7
[2023/01/19 03:15:40] [ info] [ctraces ] version=0.2.5
[2023/01/19 03:15:40] [ info] [input:forward:forward.0] initializing
[2023/01/19 03:15:40] [ info] [input:forward:forward.0] storage_strategy='memory' (memory only)
[2023/01/19 03:15:40] [ info] [input:forward:forward.0] listening on 0.0.0.0:30001
[2023/01/19 03:15:40] [ info] [sp] stream processor started
[2023/01/19 03:15:40] [ info] [output:stdout:stdout.0] worker #0 started
{"date":1674090930.626897,"aid":"<hostname>","message_type":"Link","ts":1674090926111,"trans_mode":1,"domain":"my_domain","message":[{"active":true,"admin_state":"Enabled","deleted":false,"down_reason":"","hostname":"<hostname>","ifalias":"","ifname":"NVL1/2/1/2","kind":"nvl","managed":true,"master":"test","message_type":"Link","mtu":256,"oper_state":"active","timestamp":1674090926111,"vrf":"default"},{"active":true,"admin_state":"Enabled","deleted":false,"down_reason":"","hostname":"<hostname>","ifalias":"","ifname":"NVL1/12/2/1","kind":"nvl","managed":true,"master":"test","message_type":"Link","mtu":256,"oper_state":"init","timestamp":1674090926111,"vrf":"default"},{"active":true,"admin_state":"Enabled","deleted":false,"down_reason":"","hostname":"<hostname>","ifalias":"","ifname":"NVL1/13/2/2","kind":"nvl","managed":true,"master":"test","message_type":"Link","mtu":256,"oper_state":"init","timestamp":1674090926111,"vrf":"default"},{"active":true,"admin_state":"Enabled","deleted":false,"down_reason":"","hostname":"<hostname>","ifalias":"","ifname":"NVL2/29/2/2","kind":"nvl","managed":true,"master":"test","message_type":"Link","mtu":256,"oper_state":"init","timestamp":1674090926111,"vrf":"default"},{"active":true,"admin_state":"Enabled","deleted":false,"down_reason":"","hostname":"<hostname>","ifalias":"","ifname":"NVL2/32/1/2","kind":"nvl","managed":true,"master":"test","message_type":"Link","mtu":256,"oper_state":"init","timestamp":1674090926111,"vrf":"default"},{"active":true,"admin_state":"Enabled","deleted":false,"down_reason":"","hostname":"<hostname>","ifalias":"","ifname":"NVL1/7/1/1","kind":"nvl","managed":true,"master":"test","message_type":"Link","mtu":256,"oper_state":"init","timestamp":1674090926111,"vrf":"default"},{"active":true,"admin_state":"Enabled","deleted":false,"down_reason":"","hostname":"<hostname>","ifalias":"","ifname":"NVL1/9/1/2","kind":"nvl","managed":true,"master":"test","message_type":"Link","mtu":256,"oper_state":"init","timestamp":1674090926111,"vrf":"default"},{"active":true,"admin_state":"Enabled","deleted":false,"down_reason":"","hostname":"<hostname>","ifalias":"","ifname":"NVL2/30/1/1","kind":"nvl","managed":true,"master":"test","message_type":"Link","mtu":256,"oper_state":"init","timestamp":1674090926111,"vrf":"default"},{"active":true,"admin_state":"Enabled","deleted":false,"down_reason":"","hostname":"<hostname>","ifalias":"","ifname":"NVL1/16/2/2","kind":"nvl","managed":true,"master":"test","message_type":"Link","mtu":256,"oper_state":"init","timestamp":1674090926111,"vrf":"default"},{"active":true,"admin_state":"Enabled","deleted":false,"down_reason":"","hostname":"<hostname>","ifalias":"","ifname":"NVL2/17/2/1","kind":"nvl","managed":true,"master":"test","message_type":"Link","mtu":256,"oper_state":"init","timestamp":1674090926111,"vrf":"default"}]}
```
