---
title: NVLink4 Fluentd Reference
author: NVIDIA
weight: 1150
toc: 3
bookhidden: true
---

## NVLink4 Fluentd Reference

The following examples show NVLink4 fluentd message output in JSON format: 

```Node
{
  "date": 1656408595.780359,
  "aid": "r-ufm191",
  "domain": "r-ufm",
  "message_type": "Node",
  "ts": 1656408595754,
  "trans_mode": 1,
  "message": [
    {
      "active": true,
      "deleted": false,
     "hostname": "r-ufm191",
      "last_reinit": 1656408413,
      "lastboot": 1656408413,
      "message_type": "Node",
      "ntp_state": "yes",
      "sys_uptime": 1656344312,
      "timestamp": 1656408595,
      "version": "1.0"
    }
  ]
}
 

Inventory
{
  "date": 1656408595.780281,
  "aid": "r-ufm191",
  "domain": "r-ufm",
  "message_type": "Inventory",
  "ts": 1656408595754,
  "trans_mode": 1,
  "message": [
    {
      "active": true,
      "agent_version": "1.0",
      "asic_core_bw": "N/A",
      "asic_data": "[]",
      "asic_model": "NVL4",
      "asic_model_id": "P4697",
      "asic_ports": "NVL4-1,NVL4-2",
      "asic_vendor": "NVIDIA",
      "cpu_arch": "x86_64",
      "cpu_data": "[]",
      "cpu_max_freq": "2500.0000",
      "cpu_model": "Intel(R) Xeon(R) CPU E5-2620 0 @ 2.00GHz",
      "cpu_nos": "2",
      "deleted": false,
      "disk_data": "[{\"firmware_version\":\"0202-000\",\"model\":\"StorFly VSF302XC016G-MLX1\",\"serial_number\":\"P1T13004897701140573\"}]",
      "disk_total_size": "15.8 GB",
      "domain": "",
      "hostname": "r-ufm191",
      "license_data": "[{\"license\":\"LK2-RESTRICTED_CMDS_GEN2-43A1-4H83-DSKJ-N88A-52AS-J329-PF\",\"name\":\"24:8A:07:40:05:96 (ok)\"}]",
      "license_state": "ok",
      "memory_data": "[]",
      "memory_total_size": "7789 MB total",
      "message_type": "Inventory",
      "os_name": "Onyx",
      "os_version": "daxia",
      "os_version_id": "X86_64 daxia 2022-05-16 10:35:38 x86_64",
      "platform_base_mac": "24:8A:07:40:09:96",
      "platform_label_revision": "A4",
      "platform_mfg_date": "N/A",
      "platform_model": "nvl4_gpu",
      "platform_part_number": "N/A",
      "platform_serial_number": "MT1632X02710",
      "platform_vendor": "NVIDIA",
      "timestamp": 1656408595754
    }
  ]
}
 
ResourceUtil
{
  "date": 1656408595.758639,
  "aid": "r-ufm191",
  "domain": "r-ufm",
  "message_type": "ResourceUtil",
  "ts": 1656408595754,
  "trans_mode": 1,
  "message": [
    {
      "active": true,
      "cpu_utilization": 13,
      "deleted": false,
      "disk_utilization": {
        "/dev/sda10": {
          "percent": 38.69,
          "total": 10137632768,
          "used": 3922722816
        },
        "/dev/sda8": {
          "percent": 0.55,
          "total": 190840832,
          "used": 1048576
        }
      },
      "hostname": "r-ufm191",
      "is_disk_read_only": true,
      "mem_utilization": 27.04,
      "message_type": "ResourceUtil",
      "timestamp": 1656408595754
    }
  ]
}
 
Port
{
  "date": 1656408595.768998,
  "aid": "r-ufm191",
  "domain": "r-ufm",
  "message_type": "Port",
  "ts": 1656408595754,
  "trans_mode": 1,
  "message": [
    {
      "active": true,
      "connector": "-",
      "deleted": false,
      "hostname": "r-ufm191",
      "identifier": "-",
      "ifname": "NVL4/16/1/2",
      "message_type": "Port",
      "part_number": "-",
      "serial_number": "-",
      "speed": "53.125 Gbps",
      "state": "init",
      "timestamp": 1656408595754,
      "transceiver": "-",
      "vendor_name": "-"
    }
  ]
}
 
Fan
{
  "date": 1656408595.776626,
  "aid": "r-ufm191",
  "domain": "r-ufm",
  "message_type": "Fan",
  "ts": 1656408595754,
  "trans_mode": 1,
  "message": [
    {
      "active": true,
      "deleted": false,
      "hostname": "r-ufm191",
      "message_type": "Fan",
      "s_input": 8287,
      "s_name": "FAN3-F1",
      "s_prev_state": "ok",
      "s_state": "ok",
      "timestamp": 1656408595754
    },
  ]
}
 
Temp
{
  "date": 1656408595.777002,
  "aid": "r-ufm191",
  "domain": "r-ufm",
  "message_type": "Temp",
  "ts": 1656408595754,
  "trans_mode": 1,
  "message": [
    {
      "active": true,
      "deleted": false,
      "hostname": "r-ufm191",
      "message_type": "Temp",
      "s_desc": "PS2 power-mon T1",
      "s_input": 30,
      "s_name": "temp1",
      "s_prev_state": "ok",
      "s_state": "ok",
      "timestamp": 1656408595754
    }
  ]
}
 
Power
{
  "date": 1656409388.77556,
  "aid": "r-ufm191",
  "domain": "r-ufm",
  "message_type": "Power",
  "ts": 1656409388754,
  "trans_mode": 1,
  "message": [
    {
      "active": true,
      "deleted": false,
      "hostname": "r-ufm191",
      "message_type": "Power",
      "s_adapter_name": "PS1",
      "timestamp": 1656409388754
    }
  ]
}

PSU
{
  "date": 1656409327.775926,
  "aid": "r-ufm191",
  "domain": "r-ufm",
  "message_type": "PSU",
  "ts": 1656409327753,
  "trans_mode": 1,
  "message": [
    {
      "active": true,
      "deleted": false,
      "hostname": "r-ufm191",
      "message_type": "PSU",
      "s_name": "PS1",
      "s_prev_state": "fail",
      "s_state": "fail",
      "timestamp": 1656409327753
    }
  ]
}
 
Link
{
  "date": 1656408595.813899,
  "aid": "r-ufm191",
  "domain": "r-ufm",
  "message_type": "Link",
  "ts": 1656408595754,
  "trans_mode": 1,
  "message": [
    {
      "active": true,
      "admin_state": "Enabled",
      "deleted": false,
      "down_reason": "",
      "hostname": "r-ufm191",
      "ifalias": "",
      "ifname": "NVL1/9/2/2",
      "kind": "nvl",
      "managed": true,
      "master": "",
      "message_type": "Link",
      "mtu": 256,
      "oper_state": "init",
      "timestamp": 1656408595754
    }
  ]
}
 
NvlStats
{
  "date": 1656408595.831456,
  "aid": "r-ufm191",
  "domain": "r-ufm",
  "message_type": "NvlStats",
  "ts": 1656408595754,
  "trans_mode": 1,
  "message": [
    {
      "active": true,
      "crc_errors": 0,
      "deleted": false,
      "hostname": "r-ufm191",
      "ifname": "NVL2/30/1/1",
      "message_type": "NvlStats",
      "rx_all_flits": 0,
      "rx_data_flits": 0,
      "timestamp": 1656408595754,
      "tx_all_flits": 0,
      "tx_data_flits": 0,
      "wait": 0
    }
  ]
}

Lfm
[
  {
    "date": 1656409315.771477,
    "aid": "r-ufm191",
     "domain": "r-ufm",
    "message_type": "LfmStatus",
    "ts": 1656409315754,
    "trans_mode": 1,
    "message": [
      {
        "active": true,
        "bind_interface_ip": "10.209.38.181",
        "deleted": false,
        "hostname": "r-ufm191",
        "log_append_to_log": "enabled",
        "log_level": "info",
        "message_type": "LfmStatus",
        "shutdown": "no",
        "starting_tcp_port": "16000",
        "state": "stopped",
        "timestamp": 1656409315754
      }
    ]
  }
]

Dom
{
  "date": 1656410104.058327,
  "aid": "r-ufm191",
  "domain": "r-ufm",
  "message_type": "Dom",
  "ts": 1656410103925,
  "trans_mode": 1,
  "message": [
    {
      "active": true,
      "deleted": false,
      "hostname": "r-ufm191",
      "identifier": "",
      "ifname": "NVL2/5/2/1",
      "laser_bias_current": {
        "Channel 1": "8.73800 mA",
        "Channel 2": "8.73800 mA",
        "Channel 3": "0.00000 mA",
        "Channel 4": "0.00000 mA",
        "Channel 5": "0.00000 mA",
        "Channel 6": "0.00000 mA",
        "Channel 7": "0.00000 mA",
        "Channel 8": "0.00000 mA"
      },
      "laser_bias_current_high_alarm_th": "8.50000 mA",
      "laser_bias_current_high_warning_th": "131 mA",
      "laser_bias_current_low_alarm_th": "5.49200 mA",
      "laser_bias_current_low_warning_th": "0 mA",
      "laser_output_power": {
        "Channel 1": "0.00000 mW / -inf dBm",
        "Channel 2": "0.00000 mW / -inf dBm",
        "Channel 3": "0.00000 mW / -inf dBm",
        "Channel 4": "6.55350 mW / 8.16473 dBm",
        "Channel 5": "0.87370 mW / -0.58638 dBm",
        "Channel 6": "0.87210 mW / -0.59434 dBm",
        "Channel 7": "0.00000 mW / -inf dBm",
        "Channel 8": "0.00000 mW / -inf dBm"
      },
      "laser_output_power_high_alarm_th": "3.46730 mW / 5.39991 dBm",
      "laser_output_power_high_warning_th": "6.5535 mW",
      "laser_output_power_low_alarm_th": "0.07240 mW / -11.40261 dBm",
      "laser_output_power_low_warning_th": "0 mW",
      "laser_rx_power": {
        "Channel 1": "0.00000 mW / -inf dBm",
        "Channel 2": "0.00000 mW / -inf dBm",
        "Channel 3": "0.00000 mW / -inf dBm",
        "Channel 4": "0.00000 mW / -inf dBm",
        "Channel 5": "0.00000 mW / -inf dBm",
        "Channel 6": "0.00000 mW / -inf dBm",
        "Channel 7": "0.00000 mW / -inf dBm",
        "Channel 8": "0.00000 mW / -inf dBm"
      },
      "laser_rx_power_high_alarm_th": "3.46730 mW / 5.39991 dBm",
      "laser_rx_power_high_warning_th": "6.5535 mW",
      "laser_rx_power_low_alarm_th": "0.04670 mW / -13.30683 dBm",
      "laser_rx_power_low_warning_th": "0 mW",
      "message_type": "Dom",
      "module_temp": "46.000000 degrees C/114.799995 degrees F",
      "module_temp_high_alarm_th": "80.000000 degrees C/176.000000 degrees F",
      "module_temp_high_warning_th": "127.000000 degrees C/260.599976 degrees F",
      "module_temp_low_alarm_th": "-10.000000 degrees C/14.000000 degrees F",
      "module_temp_low_warning_th": "-127.000000 degrees C/-196.599991 degrees F",
      "module_voltage": "3.24330 V",
      "module_voltage_high_alarm_th": "3.50000 V",
      "module_voltage_high_warning_th": "0 V",
      "module_voltage_low_alarm_th": "3.10000 V",
      "module_voltage_low_warning_th": "6.5535 V",
      "timestamp": 1656410103925
    }
  ]
}
```