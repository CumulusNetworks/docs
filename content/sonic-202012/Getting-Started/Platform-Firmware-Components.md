---
title: Platform Firmware Components
author: Cumulus Networks
weight: 130
product: SONiC
version: 202012
siteSlug: sonic
---

A network switch consists of many auxiliary components which are responsible for managing different subsystems (e.g., PSU/FAN/QSFP/EEPROM/THERMAL) and providing necessary interfaces (e.g., I2C/SPI/JTAG). These components are a complex of programmable logic devices with their own hardware architecture and software.

{{%notice info%}}

It is very important to always have the latest recommended software version to improve device stability, security and performance. Also, software updates can add new features and remove outdated ones.

{{%/notice%}}

## User Interface

```
fwutil
|--- show
|    |--- version
|    |--- status
|    |--- updates -i|--image=<current|next>
|
|--- install
|    |--- chassis
|    |    |--- component <component_name>
|    |         |--- fw -y|--yes <fw_path>
|    |
|    |--- module <module_name>
|         |--- component <component_name>
|              |--- fw -y|--yes <fw_path>
|
|--- update
     |--- chassis
     |    |--- component <component_name>
     |         |--- fw -y|--yes -f|--force -i|--image=<current|next>
     |
     |--- module <module_name>
          |--- component <component_name>
               |--- fw -y|--yes -f|--force -i|--image=<current|next>
```

### Show Commands

The purpose of the show commands is to provide information on:

- Firmware utility related information (such as version)
- Platform components related information (such as version, description)
- Available firmware updates related information (such as firmware, version, status)

To display firmware utility version:

```
root@sonic:~# fwutil show version
fwutil version 1.0.0.0
```

To displays platform components and firmware versions:

- Non modular chassis platform

      root@sonic:~# fwutil show status
      Chassis   Module   Component   Version             Description
      --------  -------  ----------  ------------------  ------------
      Chassis1  N/A      BIOS        0ACLH003_02.02.007  Chassis BIOS
                         CPLD        5                   Chassis CPLD
                         FPGA        5                   Chassis FPGA
- Modular chassis platform

  Not relevant for NVIDIA® Mellanox® switch products.

To displays available firmware updates:

- Non modular chassis platform

      root@sonic:~# fwutil show updates --image=next
      Chassis   Module   Component   Firmware               Version (current/available)              Status
      --------  -------  ----------  ---------------------  ---------------------------------------  ------------------
      Chassis1  N/A      BIOS        <image_path>/bios.bin  0ACLH004_02.02.007 / 0ACLH004_02.02.010  update is required
                         CPLD        <image_path>/cpld.bin  5 / 10                                   update is required
                         FPGA        <image_path>/fpga.bin  5 / 5                                    up-to-date
- Modular chassis platform

  Not relevant for NVIDIA® Mellanox® switch products.

#### Additional Supported Options

-i\|–image: Shows updates using current/next SONiC image.

The default option is --image=current.

### Install Commands

The purpose of the install commands is to provide an interface for manual firmware installation of various platform components.
 To install the firmware:
- Non modular chassis platform

      root@sonic:~# fwutil install chassis component BIOS fw <image_path>/bios.bin
      Warning: <firmware_update_notification>
      New FW will be installed, continue? [y/N]: N
      Aborted!
      root@sonic:~# fwutil install chassis component CPLD fw <image_path>/cpld.bin
      Warning: <firmware_update_notification>
      New FW will be installed, continue? [y/N]: N
      Aborted!
      root@sonic:~# fwutil install chassis component FPGA fw <image_path>/fpga.bin
      Warning: <firmware_update_notification>
      New FW will be installed, continue? [y/N]: N
      Aborted!
- Modular chassis platform

  Not relevant for NVIDIA® Mellanox® switch products.

#### Additional Supported Options

-y\|–yes: Automatic yes to prompts. Assumes "yes" as answer to all prompts and runs non-interactively

### Update Commands

The purpose of the update commands is to provide an interface for automatic firmware installation of various platform components. Automatic firmware update requires platform_components.json to be created and placed at: sonic-buildimage/device/<platform_name>/<onie_platform>/platform_components.json

- Non modular chassis platform
      {
          "chassis": {
              "Chassis1": {
                  "component": {
                      "BIOS": {
                          "firmware": "/etc/<platform_name>/fw/<onie_platform>/chassis1/bios.bin",
                          "version": "0ACLH003_02.02.010"
                      },
                      "CPLD": {
                          "firmware": "/etc/<platform_name>/fw/<onie_platform>/chassis1/cpld.bin",
                          "version": "10"
                      },
                      "FPGA": {
                          "firmware": "/etc/<platform_name>/fw/<onie_platform>/chassis1/fpga.bin",
                          "version": "5"
                      }
                  }
              }
          }
      }
- Modular chassis platform

  Not relevant for NVIDIA® Mellanox® switch products.

**Notes:**

- Firmware update will be disabled if a component definition is not provided (e.g., 'BIOS': { })
- Firmware version will be read from the image if the version field is not provided

To update firmware:

- Non modular chassis platform

      root@sonic:~# fwutil update chassis component BIOS fw --image=next
      Warning: <firmware_update_notification>
      New FW will be installed, continue? [y/N]: N
      Aborted!
      root@sonic:~# fwutil update chassis component CPLD fw --image=next
      Warning: <firmware_update_notification>
      New FW will be installed, continue? [y/N]: N
      Aborted!
      root@sonic:~# fwutil update chassis component FPGA fw --image=next
      Warning: <firmware_update_notification>
      New FW will be installed, continue? [y/N]: N
      Aborted!
- Modular chassis platform

  Not relevant for NVIDIA® Mellanox® switch products.

#### Additional Supported Options

- -y\|--yes: Automatic yes to prompts. Assumes "yes" as answer to all prompts and run non-interactively
- -f\|--force: Installs the firmware regardless of the current version
- -i\|--image: Updates the firmware using the current/next SONiC image

The default option is --image=current.

## Platform Firmware

### Mellanox Platform Firmware Archive (MPFA)

Some of the platform components require a set of images/tools to complete the firmware update. These images/tools come in a bundle and distribute as a single file in a special file format.

#### Structure

MPFA is a very flexible format and supports an arbitrary internal file structure. The mandatory element is metadata.ini which contains a description of what firmware files/versions are available.

**Example:**

```
root@sonic:/tmp/sn3800_cpld.mpfa# tree
.
├── FUI000093_Burn_Tigris_CPLD000120_REV0700_CPLD000165_REV0400_CPLD000166_REV0300_CPLD000167_REV0100.vme
├── FUI000093_Refresh_Tigris_CPLD000120_REV0700_CPLD000165_REV0400_CPLD000166_REV0300_CPLD000167_REV0100.vme
└── metadata.ini
 
0 directories, 3 files
 
root@sonic:/tmp/sn3800_cpld.mpfa# cat metadata.ini
; Firmware files
[firmware]
BURN=FUI000093_Burn_Tigris_CPLD000120_REV0700_CPLD000165_REV0400_CPLD000166_REV0300_CPLD000167_REV0100.vme
REFRESH=FUI000093_Refresh_Tigris_CPLD000120_REV0700_CPLD000165_REV0400_CPLD000166_REV0300_CPLD000167_REV0100.vme
; Component versions
[version]
CPLD1=CPLD000120_REV0700
CPLD2=CPLD000165_REV0400
CPLD3=CPLD000166_REV0300
CPLD4=CPLD000167_REV0100
```

{{%notice info%}}

Section version is optional and can be used in case firmware doesn't support available version query

{{%/notice%}}

## How TOs

### How to Check Available Firmware Updates?

```
root@sonic:/home/admin# show platform firmware updates
Chassis                 Module    Component    Firmware                                             Version (Current/Available)                        Status
----------------------  --------  -----------  ---------------------------------------------------  -------------------------------------------------  ----------
x86_64-mlnx_msn3800-r0  N/A       ONIE         /etc/mlnx/fw/sn3800/onie-updater-x86_64-mlnx_x86-r0  2020.02-5.2.0021-9600 / 2020.02-5.2.0021-9600      up-to-date
                                  SSD          /etc/mlnx/fw/sn3800/mlnx_ssd_fw_package.pkg          0202-000 / 0202-000                                up-to-date
                                  BIOS         /etc/mlnx/fw/sn3800/0ACLH004.rom                     0ACLH004_02.02.007_9600 / 0ACLH004_02.02.007_9600  up-to-date
                                  CPLD1        /etc/mlnx/fw/sn3800/sn3800_cpld.mpfa                 CPLD000120_REV0700 / CPLD000120_REV0700            up-to-date
                                  CPLD2        /etc/mlnx/fw/sn3800/sn3800_cpld.mpfa                 CPLD000165_REV0400 / CPLD000165_REV0400            up-to-date
                                  CPLD3        /etc/mlnx/fw/sn3800/sn3800_cpld.mpfa                 CPLD000166_REV0300 / CPLD000166_REV0300            up-to-date
                                  CPLD4        /etc/mlnx/fw/sn3800/sn3800_cpld.mpfa                 CPLD000167_REV0100 / CPLD000167_REV0100            up-to-date
```

### How to Install Firmware for Chassis Component?

1. Using local firmware path.

       root@sonic:/home/admin# config platform firmware install chassis component CPLD1 fw /home/admin/FUI000093_Burn_Tigris_CPLD000120_REV0700_CPLD000165_REV0400_CPLD000166_REV0300_CPLD000167_REV0100.vme
       Warning: Power cycle (with 30 sec delay) or refresh image is required to complete CPLD1 firmware update.
       New firmware will be installed, continue? [y/N]: y
       Installing firmware:
           /home/admin/FUI000093_Burn_Tigris_CPLD000120_REV0700_CPLD000165_REV0400_CPLD000166_REV0300_CPLD000167_REV0100.vme
       INFO: Installing CPLD1 firmware update: path=/home/admin/FUI000093_Burn_Tigris_CPLD000120_REV0700_CPLD000165_REV0400_CPLD000166_REV0300_CPLD000167_REV0100.vme
                        Lattice Semiconductor Corp.
 
                    ispVME(tm) V12.2 Copyright 1998-2012.
 
                      Customized for Mellanox products.

       Using GPIO update!
       Processing virtual machine file (/home/admin/FUI000093_Burn_Tigris_CPLD000120_REV0700_CPLD000165_REV0400_CPLD000166_REV0300_CPLD000167_REV0100.vme)......

       +=======+
       | PASS! |
       +=======+

       root@sonic:/home/admin# config platform firmware install chassis component CPLD1 fw /home/admin/FUI000093_Refresh_Tigris_CPLD000120_REV0700_CPLD000165_REV0400_CPLD000166_REV0300_CPLD000167_REV0100.vme
       Warning: Power cycle (with 30 sec delay) or refresh image is required to complete CPLD1 firmware update.
       New firmware will be installed, continue? [y/N]: y
       Installing firmware:
           /home/admin/FUI000093_Refresh_Tigris_CPLD000120_REV0700_CPLD000165_REV0400_CPLD000166_REV0300_CPLD000167_REV0100.vme
       INFO: Installing CPLD1 firmware update: path=/home/admin/FUI000093_Refresh_Tigris_CPLD000120_REV0700_CPLD000165_REV0400_CPLD000166_REV0300_CPLD000167_REV0100.vme
                        Lattice Semiconductor Corp.
 
                    ispVME(tm) V12.2 Copyright 1998-2012.
 
                      Customized for Mellanox products.

       Using GPIO update!
       Processing virtual machine file (/home/admin/FUI000093_Refresh_Tigris_CPLD000120_REV0700_CPLD000165_REV0400_CPLD000166_REV0300_CPLD000167_REV0100.vme)......
2. Using remote network firmware path.

       root@sonic:/home/admin# config platform firmware install chassis component CPLD1 fw http://arc-build-server/fwutil/FUI000093_Burn_Tigris_CPLD000120_REV0700_CPLD000165_REV0400_CPLD000166_REV0300_CPLD000167_REV0100.vme
       Downloading firmware:
           [#####################################################################################################################]  100%
       Warning: Power cycle (with 30 sec delay) or refresh image is required to complete CPLD1 firmware update.
       New firmware will be installed, continue? [y/N]: y
       Installing firmware:
           /tmp/FUI000093_Burn_Tigris_CPLD000120_REV0700_CPLD000165_REV0400_CPLD000166_REV0300_CPLD000167_REV0100.vme
       INFO: Installing CPLD1 firmware update: path=/tmp/FUI000093_Burn_Tigris_CPLD000120_REV0700_CPLD000165_REV0400_CPLD000166_REV0300_CPLD000167_REV0100.vme
                 Lattice Semiconductor Corp.

                    ispVME(tm) V12.2 Copyright 1998-2012.
 
                      Customized for Mellanox products.

       Using GPIO update!
       Processing virtual machine file (/tmp/FUI000093_Burn_Tigris_CPLD000120_REV0700_CPLD000165_REV0400_CPLD000166_REV0300_CPLD000167_REV0100.vme)......


       +=======+
       | PASS! |
       +=======+

       root@sonic:/home/admin# config platform firmware install chassis component CPLD1 fw http://arc-build-server/fwutil/FUI000093_Refresh_Tigris_CPLD000120_REV0700_CPLD000165_REV0400_CPLD000166_REV0300_CPLD000167_REV0100.vme
       Downloading firmware:
           [######################################################################################################################]  100%
       Warning: Power cycle (with 30 sec delay) or refresh image is required to complete CPLD1 firmware update.
       New firmware will be installed, continue? [y/N]: y
       Installing firmware:
           /tmp/FUI000093_Refresh_Tigris_CPLD000120_REV0700_CPLD000165_REV0400_CPLD000166_REV0300_CPLD000167_REV0100.vme
       INFO: Installing CPLD1 firmware update: path=/tmp/FUI000093_Refresh_Tigris_CPLD000120_REV0700_CPLD000165_REV0400_CPLD000166_REV0300_CPLD000167_REV0100.vme
                        Lattice Semiconductor Corp.
 
             ispVME(tm) V12.2 Copyright 1998-2012.

                      Customized for Mellanox products.

       Using GPIO update!
       Processing virtual machine file (/tmp/FUI000093_Refresh_Tigris_CPLD000120_REV0700_CPLD000165_REV0400_CPLD000166_REV0300_CPLD000167_REV0100.vme)......

### How to Update Firmware for Chassis Component?

1. Get available platform components.

       root@sonic:/home/admin# show platform firmware status
       Chassis                 Module    Component    Version                  Description
       ----------------------  --------  -----------  -----------------------  ----------------------------------------
       x86_64-mlnx_msn3800-r0  N/A       ONIE         2020.02-5.2.0021-9600    ONIE - Open Network Install Environment
                                         SSD          0202-000                 SSD - Solid-State Drive
                                         BIOS         0ACLH004_02.02.007_9600  BIOS - Basic Input/Output System
                                         CPLD1        CPLD000120_REV0600       CPLD - Complex Programmable Logic Device
                                         CPLD2        CPLD000165_REV0400       CPLD - Complex Programmable Logic Device
                                         CPLD3        CPLD000166_REV0300       CPLD - Complex Programmable Logic Device
                                         CPLD4        CPLD000167_REV0100       CPLD - Complex Programmable Logic Device

2. Get platform type.

       root@sonic:/home/admin# show platform summary
       Platform: x86_64-mlnx_msn3800-r0
       HwSKU: ACS-MSN3800
       ASIC: mellanox
3. Make a configuration file.

       root@sonic:/home/admin# vim /usr/share/sonic/device/x86_64-mlnx_msn3800-r0/platform_components.json
       {
           "chassis": {
               "x86_64-mlnx_msn3800-r0": {
                   "component": {
                       "ONIE": {
                           "firmware": "/etc/mlnx/fw/sn3800/onie-updater-x86_64-mlnx_x86-r0"
                       },
                       "SSD": {
                           "firmware": "/etc/mlnx/fw/sn3800/mlnx_ssd_fw_package.pkg"
                       },
                       "BIOS": { 
                           "firmware": "/etc/mlnx/fw/sn3800/0ACLH004.rom",
                           "version": "0ACLH004_02.02.007_9600"
                        },
                       "CPLD1": {
                           "firmware": "/etc/mlnx/fw/sn3800/sn3800_cpld.mpfa"
                        },
                       "CPLD2": {
                           "firmware": "/etc/mlnx/fw/sn3800/sn3800_cpld.mpfa"
                        },
                       "CPLD3": {
                           "firmware": "/etc/mlnx/fw/sn3800/sn3800_cpld.mpfa"
                        },
                       "CPLD4": {
                           "firmware": "/etc/mlnx/fw/sn3800/sn3800_cpld.mpfa"
                        }
                   }
               }
           }
       }
4. Get the available firmware updates.

       root@sonic:/home/admin# show platform firmware updates
       Chassis                 Module    Component    Firmware                                             Version (Current/Available)                        Status
       ----------------------  --------  -----------  ---------------------------------------------------  -------------------------------------------------  ------------------
       x86_64-mlnx_msn3800-r0  N/A       ONIE         /etc/mlnx/fw/sn3800/onie-updater-x86_64-mlnx_x86-r0  2020.02-5.2.0021-9600 / 2020.02-5.2.0021-9600      up-to-date
                                         SSD          /etc/mlnx/fw/sn3800/mlnx_ssd_fw_package.pkg          0202-000 / 0202-000                                up-to-date
                                         BIOS         /etc/mlnx/fw/sn3800/0ACLH004.rom                     0ACLH004_02.02.007_9600 / 0ACLH004_02.02.007_9600  up-to-date
                                         CPLD1        /etc/mlnx/fw/sn3800/sn3800_cpld.mpfa                 CPLD000120_REV0600 / CPLD000120_REV0700            update is required
                                         CPLD2        /etc/mlnx/fw/sn3800/sn3800_cpld.mpfa                 CPLD000165_REV0400 / CPLD000165_REV0400            up-to-date
                                         CPLD3        /etc/mlnx/fw/sn3800/sn3800_cpld.mpfa                 CPLD000166_REV0300 / CPLD000166_REV0300            up-to-date
                                         CPLD4        /etc/mlnx/fw/sn3800/sn3800_cpld.mpfa                 CPLD000167_REV0100 / CPLD000167_REV0100            up-to-date
5. Run update.

       root@sonic:/home/admin# config platform firmware update chassis component CPLD1 fw
       Warning: Immediate power cycle is required to complete CPLD1 firmware update.
       New firmware will be installed, continue? [y/N]: y
       Updating firmware:
           /etc/mlnx/fw/sn3800/sn3800_cpld.mpfa
       INFO: Processing CPLD1 burn file: firmware install
       INFO: Installing CPLD1 firmware update: path=/tmp/mpfa-zRSyCC/FUI000093_Burn_Tigris_CPLD000120_REV0700_CPLD000165_REV0400_CPLD000166_REV0300_CPLD000167_REV0100.vme
                        Lattice Semiconductor Corp.
 
                    ispVME(tm) V12.2 Copyright 1998-2012.
 
                      Customized for Mellanox products.

       Using GPIO update!
       Processing virtual machine file (/tmp/mpfa-zRSyCC/FUI000093_Burn_Tigris_CPLD000120_REV0700_CPLD000165_REV0400_CPLD000166_REV0300_CPLD000167_REV0100.vme)......

       +=======+
       | PASS! |
       +=======+

       INFO: Processing CPLD1 refresh file: firmware update
       INFO: Installing CPLD1 firmware update: path=/tmp/mpfa-zRSyCC/FUI000093_Refresh_Tigris_CPLD000120_REV0700_CPLD000165_REV0400_CPLD000166_REV0300_CPLD000167_REV0100.vme
                        Lattice Semiconductor Corp.
 
                    ispVME(tm) V12.2 Copyright 1998-2012.
 
                      Customized for Mellanox products.

       Using GPIO update!
       Processing virtual machine file (/tmp/mpfa-zRSyCC/FUI000093_Refresh_Tigris_CPLD000120_REV0700_CPLD000165_REV0400_CPLD000166_REV0300_CPLD000167_REV0100.vme)......


