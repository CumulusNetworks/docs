---
title: SONiC Management Utilities
author: NVIDIA
weight: 630
product: SONiC
version: 202012
siteSlug: sonic
---

NVIDIA switch hardware management interfaces are implemented by using a virtual file system provided by the Linux kernel called `sysfs`. The `sysfs` file system enumerates the devices and buses attached to the system in a file system hierarchy that can be accessed from user space.

The major advantage of working with `sysfs` is that it makes the hardware hierarchy easy to understand and control without having to learn about a hardware component's location, and the buses through which they are connected. The `sysfs` attributes are exposed as symbolic links in the `/var/run/hw-management` directory at system boot time. This directory contains this structure:

| Node Path | Purpose |
| --------- | ------- |
| /alarm | Critical alarm symbolic links for CPU core temperature readings. |
| /config | Configuration of related files. It includes information about fan minimum, maximum allowed speed, some default settings, configured delays for different purposes. |
| /eeprom | EEPROM-related symbolic links to system, PSU, fan and CPU. |
| /environment | Environment (voltage, current, A2D) related symbolic links. |
| /led | LED related symbolic links. |
| /power | Power-related symbolic links. |
| /sfp | Helper scripts that get the current status of SFP and QSFP modules from `ethtool`. |
| /system | System-related symbolic links for ASIC health, power settings (reset, power on and down, power cycle), CPLD version. |
| /thermal | Thermal-related links, including thermal zones. `/mlxsw` contains ASIC ambient temperature and thermal zone symbolic links. The `/mlxsw-moduleX` subdirectories contain QSFP module temperature and thermal zone symbolic links. |
| /watchdog | Standard watchdog `sysfs` attributes. |

## Platform API/Plugins

NVIDIA switches support both Platform API v2.0 and legacy platform device plugins. The platform APIs or the plugins provide the interfaces access or operate the peripheral devices.

### Plugins Supported by NVIDIA Switches

Plugins are implemented for each peripheral device type. SONiC defines base classes, and NVIDIA implements these classes in various plugins including `sfputil.py`, `psuutil.py`, `eeprom.py` and `fanutil.py`.

All platform-specific plugins live on a disk in the SONiC image. The appropriate plugin is loaded at runtime after determining the running platform.

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

Platform API v2.0 is a standardized, unified API to interface with all combinations of the devices specified below. The APIs are organized in a hierarchy based on the physical connection of the devices. Peripheral control logic is implemented in user space.

The platform API v2.0 covers these devices:

- Chassis
- EEPROM
- FAN
- LED
- Module component
- PSU
- SFP
- SSD
- Thermal
- Watchdog

## ethtool

`ethtool` is used to query and control network device driver and hardware settings, particularly for wired Ethernet devices. `ethtool` leverages the `mlxsw_minimal` driver in the Linux kernel to provide a more convenient way to read QSFP/SFP module information on NVIDIA switches. NVIDIA platform SFP APIs leverage `ethtool` to get raw data and parse the module related data accordingly.

```
admin@switch:~$ sudo ethtool -m sfp1
	Identifier                                : 0x0d (QSFP+)
	Extended identifier                       : 0x00
	Extended identifier description           : 1.5W max. Power consumption
	Extended identifier description           : No CDR in TX, No CDR in RX
	Extended identifier description           : High Power Class (> 3.5 W) not enabled
	Connector                                 : 0x23 (No separable connector)
	Transceiver codes                         : 0x08 0x00 0x00 0x00 0x00 0x00 0x00 0x00
	Transceiver type                          : 40G Ethernet: 40G Base-CR4
	Encoding                                  : 0x05 (64B/66B)
	BR, Nominal                               : 10300Mbps
	Rate identifier                           : 0x00
	Length (SMF,km)                           : 0km
	Length (OM3 50um)                         : 0m
	Length (OM2 50um)                         : 0m
	Length (OM1 62.5um)                       : 0m
	Length (Copper or Active cable)           : 1m
	Transmitter technology                    : 0xa0 (Copper cable unequalized)
	Attenuation at 2.5GHz                     : 0db
	Attenuation at 5.0GHz                     : 0db
	Attenuation at 7.0GHz                     : 0db
	Attenuation at 12.9GHz                    : 0db
	Vendor name                               : 10Gtek
	Vendor OUI                                : 00:00:00
	Vendor PN                                 : CAB-Q10/Q10-P1M
	Vendor rev                                : 01
	Vendor SN                                 : WTQ11K10044
	Revision Compliance                       : Revision not specified
	Module temperature                        : 0.00 degrees C / 32.00 degrees F
	Module voltage                            : 0.0000 V
```

## Switch Base MAC Address

NVIDIA switches are assigned with a set of MAC address and the base MAC address is burned to the `syseeprom`.

The first time a switch boots up, the base MAC address is read from the `/host/machine.conf` file, which is fed by ONIE and put into config_DB, and the MAC address works as the system's MAC address of the switch.

{{%notice info%}}

For NVIDIA Spectrum 1-based switches, the lowest 6 bits of the base MAC address must be *0*. For NVIDIA Spectrum-2 and later switches, the lowest 7 bits must be *0*. Keep this value in mind if you customize the switch's base MAC address for any reason.

{{%/notice%}}
