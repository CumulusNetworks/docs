---
title: SONiC Management Utilities
author: Cumulus Networks
weight: 630
product: SONiC
version: 202012
siteSlug: sonic
---

## MLNX Hardware Management and Sysfs

Mellanox hardware management interfaces are implemented by using a virtual file system provided by the Linux kernel called sysfs. The sysfs file system enumerates the devices and buses attached to the system in a file system hierarchy that can be accessed from the user space.

The major advantage of working with sysfs is that it makes hardware hierarchy easy to understand and control without having to learn about hardware component location, and the buses through which they are connected. The sysfs attributes are exposed as symbolic links in the /var/run/hw-management folder at system boot time categorized as in below.

This folder contains the next structure:

| Node Path | Purpose |
| --------- | ------- |
| /config | Configuration of related files. It includes information about FAN minimum, maximum allowed speed, some default settings, configured delays for different purposes |
| /eeprom | EEPROM related symbolic links to System, PSU, FAN, CPU |
| /environment | Environment (voltage, current, A2D) related symbolic links |
| /led | LED related symbolic links |
| /power | Power related symbolic links |
| /system | System related (health, reset, CPLD version. etc.) related symbolic links |
| /thermal | Thermal related links, including thermal zones related subfolders. /mlxsw - ASIC ambient temperature thermal zone related symbolic links. /mlxsw-moduleX - QSFP module X temperature thermal zone related symbolic links |
| /watchdog | Standard watchdog sysfs attributes |

## Platform API/Plugins

NVIDIA switches support both Platform API v2.0 and legacy platform device plugins. The platform APIs or the plugins provide the interfaces access or operate the peripheral devices.

### Plugins Supported by NVIDIA Switches
The plugins have been implemented per peripheral device type. SONiC defines base classes, and we implement these classes in various plugins including sfputil.py, psuutil.py, eeprom.py and fanutil.py.

All Platform-specific plugins live on a disk in the image. The appropriate plugin is loaded at runtime after determining the running platform.

| Defined class/category | APIs | Supported: Yes/No |
| ---------------------- | ---- | ----------------- |
| PsuBase | |
| | PsuUtil.get_num_psus | Y |
| | PsuUtil.get_psu_status | Y |
| | PsuUtil.get_psu_presence | Y |
| SfpUtilBase | |
| | SfpUtil.get_transceiver_info_dict | Y |
| | SfpUtil.get_transceiver_dom_info_dict | Y |
| | SfpUtil.get_presence | Y |
| | SfpUtil.get_low_power_mode | Y |
| | SfpUtil.set_low_power_mode | Y |
| | SfpUtil.reset | Y |
| | SfpUtil.get_transceiver_change_event | Y |
| LedControlBase | |
| | LedControlBase.port_link_state_change | N |
| EepromDecoder | |
| | EepromDecoder.mgmtaddrstr | N |
| | EepromDecoder.switchaddrstr | N |
| | EepromDecoder.switchaddrrange | N |
| TlvInfoDecoder | |
| | TlvInfoDecoder.base_mac_addr | Y |
| | TlvInfoDecoder.modelstr | Y |
| | TlvInfoDecoder.serial_number_str | Y |

### Platform API v2.0

Platform API v2.0 is a standardized, unified API to interface with all combinations of these devices specified below. The APIs are organized in a hierarchy based on the physical connection of the devices. Peripheral control logic is implemented in user-space.

Devices covered by the Platform API v2.0:

- Chassis
- Module component
- LED (Not supported in SONiC 201911)
- SSD
- eeprom
- FAN
- PSU
- SFP
- Thermal
- Watchdog

## ethtool

`ethtool` is used to query and control network device driver and hardware settings, particularly for wired Ethernet devices. ethtool leverages the mlxsw_minimal driver in Linux kernel to provide a more convenient way to read QSFP/SFP module info on NVIDIA switches. Mellanox platform SFP APIs are leveraging the ethtool to get raw data and parse the module related data accordingly.

```
switchadmin@sonicadmin@sonic:/#sudoethtool -m sfp1
        Identifier                                : 0x03 (SFP)
        Extended identifier                       : 0x04 (GBIC/SFP defined by 2-wire interface ID)
        Connector                                 : 0x23 (No separable connector)
        Transceiver codes                         : 0x01 0x00 0x00 0x04 0x00 0x04 0x00 0x00
        Transceiver type                          : Infiniband: 1X Copper Passive
        Transceiver type                          : Ethernet: 1000BASE-CX
        Transceiver type                          : FC: Copper Passive
        Encoding                                  : 0x06 (64B/66B)
        BR, Nominal                               : 25500MBd
        Rate identifier                           : 0x00 (unspecified)
        Length (SMF,km)                           : 0km
        Length (SMF)                              : 0m
        Length (50um)                             : 0m
        Length (62.5um)                           : 0m
        Length (Copper)                           : 2m
        Length (OM3)                              : 0m
        Passive Cu cmplnce.                       : 0x01 (SFF-8431 appendix E) [SFF-8472 rev10.4 only]
        Vendor name                               : Mellanox
        Vendor OUI                                : 00:02:c9
        Vendor PN                                 : MCP7F00-A002R
        Vendor rev                                : A1
        Option values                             : 0x00 0x00
        BR margin, max                            : 103%
        BR margin, min                            : 0%
        Vendor SN                                 : MT1702VS15044
        Date code                                 : 170109
        Optical diagnostics support               : No
```

## Switch Base MAC Address

NVIDIA® Mellanox® switches are assigned with a set of MAC address and the base MAC address is burned to the syseeprom.

For the first time the switch boots up, the base MAC address is read from the host/machine.conf, which is fed by ONIE and put into configdb, and the MAC address works as the system's MAC address of the switch.

{{%notice info%}}

For the Mellanox Spectrum based switches, the lowest 6 bits of the base MAC address must be 0, and for Mellanox Spectrum-2 and above switches, the lowest 7 bits musto be 0. This must be taken into consideration when the base MAC for the switch is customized for any reason.

{{%/notice%}}
