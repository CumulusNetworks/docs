---
title: SONiC Debug Tools
author: Cumulus Networks
weight: 610
product: SONiC
version: 201911_MUR5
siteSlug: sonic
---

## SDK Utilities

Each SDK API has a correlated python script which allows calling the SDK API from the SONiC shell. It can be found under the /usr/bin folder of the syncd container. It is recommended to use only the "get" options to prevent miss configuration and miss alignment with the SAI who is the only control application.

Below you can find a set demonstrating various Switch/Router SDK features usage. The debug utilities do include the "dump" keyword in their names.

A list of some of the provided examples:

- sx_api_bridge_dump.py
- sx_api_bridge_iter_get.py
- sx_api_cos_shared_buffers_dump.py
- sx_api_dbg_generate_dump.py
- sx_api_fdb_dump.py
- sx_api_flex_acl_dump.py
- sx_api_flex_acl_key_attr_get.py
- sx_api_host_ifc_counters_get.py

```
root@sonic:/home/admin# docker exec -it syncd bash
root@sonic:/usr/bin# ls sx_* -l
-rwxr-xr-x 1 root root    3445 Mar 23 16:16 sx_api_bridge_dump.py
-rwxr-xr-x 1 root root    8632 Mar 23 16:16 sx_api_bridge_iter_get.py
-rwxr-xr-x 1 root root   20471 Mar 23 16:16 sx_api_bridge_lag_redirect.py
-rwxr-xr-x 1 root root   10786 Mar 23 16:16 sx_api_bridge_vport.py
-rwxr-xr-x 1 root root    2759 Mar 23 16:16 sx_api_cos_default_prio.py
-rwxr-xr-x 1 root root    7939 Mar 23 16:16 sx_api_cos_ets.py
-rwxr-xr-x 1 root root   18616 Mar 23 16:16 sx_api_cos_port_buff_type.py
-rwxr-xr-x 1 root root    3794 Mar 23 16:16 sx_api_cos_port_ptp_params.py
…
…
```

With these python interfaces, you can easily dump the information in SDK to have a view of the SDK data and facilitate you are troubleshooting.

An example of such usage can be seen below in the "sx_api_ports_dump.py" ports information dump:

```
root@sonic:/usr/bin# sx_api_ports_dump.py
=====================================================================================================
|  log_port|local_port|label_port|       mtu| admin_s|  oper_s|       module_s|  pvid|     oper_speed|  fec_mode|
=================================================================================================================
|   0x10100|         1|        33|      9238|    DOWN|    DOWN|      UNPLUGGED|     1|            N/A|      None|
|   0x10200|         2|        34|      9238|    DOWN|    DOWN|      UNPLUGGED|     1|            N/A|      None|
|   0x10300|         3|        35|      9238|    DOWN|    DOWN|      UNPLUGGED|     1|            N/A|      None|
|   0x10400|         4|        36|      9238|    DOWN|    DOWN|      UNPLUGGED|     1|            N/A|      None|
…………..
…………..
|   0x13d00|        61|         1|      9238|    DOWN|    DOWN|        PLUGGED|     1|            N/A|      None|
|   0x13e00|        62|         2|      9122|      UP|      UP|        PLUGGED|  1000|        25GB_CR|        FC|
|   0x13f00|        63|         3|      9122|      UP|      UP|        PLUGGED|  1000|        25GB_CR|        FC|
|   0x14000|        64|         4|      9122|      UP|      UP|        PLUGGED|  1000|        25GB_CR|        FC|
=====================================================================================================
```

### SDK Debug Dump

SDK Debug Dump is the API that can export all the debug information modules to a user defined file name or the console. The internal debug information is exported per module:

- Databases dump parsed into tables
- List of current processes
- ASIC type and revision
- MST dump – useful for FW debug
- dmesg
- lsmod
- lspci
- uname –a
- sx_status_t sx_api_dbg_generate_dump (const sx_api_handle_t handle, const char *dump_file_path)

To generate full SDK configuration dump:

    # docker exec –it syncd sx_api_dbg_generate_dump.py

## SDK API Sniffer

SDK API Sniffer provides a way to record the RPC calls from the SDK user API library to the sx_sdk in a .pcap file, which can be used to get the exact same state in SDK and firmware to reproduce and investigate issues.

{{<img src="/images/sonic/sdk-api-sniffer.png" width="600px">}}

Below are examples for how to enable and disable the sniffer. In the enable command output, you will see the sniffer file name which the sniffer content will be stored.

```
admin@sonic:~# sudo config platform mlnx sniffer sdk enable 
Swss service will be restarted, continue? [y/N]: y
Enabling SDK sniffer
SDK sniffer is Enabled, recording file is /var/log/mellanox/sniffer/sx_sdk_sniffer_20200622072855.pcap.
Note: the sniffer file may exhaust the space on /var/log, please disable it when you are done with this sniffering.
 
admin@sonic:~# sudo config platform mlnx sniffer sdk disable
Swss service will be restarted, continue? [y/N]: y
Disabling SDK sniffer
SDK sniffer is Disabled.
```

For the CLI configuration, refer: https://github.com/Azure/sonic-utilities/blob/201911/doc/Command-Reference.md.

## NVIDIA® Mellanox® Firmware Tools (MFT)

NVIDIA® Mellanox® Firmware Tools (MFT) package is integrated in SONiC and provides a set of firmware management and debug tools.

For NVIDIA® Mellanox® devices. MFT can be used for:

- Generating a standard or customized Mellanox firmware image
- Querying for firmware information
- Burning a firmware image to a single Mellanox device

All MFT tools address the target hardware device using an mst device name. This name is assigned by running the command ‘mst start’ for PCI and I2C access (enabled by default). To list the available mst device names on the local machine, run "mst status’.

### mlxcables - Mellanox Cables Tool

The mlxcables tool allows users to access the cables and do the following:

- Query the cable and get its IDs
- Read specific addresses in the EEPROM
- Read a specific register by its name. Supported registers are received by the tool (depends on the cable type)
- Dump all the cable EEPROM bytes in RAW format
- Upgrade the FW image on the cable uC (Only on cables that support ISFU)

To query the cable:

1. Discover the mst cable devices.

       admin@sonic:~$ sudo mst cable add

       -I- Added 33 cable devices ..
2. Show the mst devices.

   Each MFT tool requires specifying the device (-d), and each ASIC has a different device (for example: Mellanox Spectrum - /dev/mst/mt52100_pci_cr0).

       admin@sonic:~$ sudo mst status

       MST modules:
       ------------

           MST PCI module loaded

           MST PCI configuration module loaded

       MST devices:
       ------------
       /dev/mst/mt52100_pciconf0        - PCI configuration cycles access.
 
                                          domain:bus:dev.fn=0000:03:00.0 addr.reg=88 data.reg=92 cr_bar.gw_offset=-1
 
                                          Chip revision is: 01

       /dev/mst/mt52100_pci_cr0         - PCI direct access.
 
                                          domain:bus:dev.fn=0000:03:00.0 bar=0xf5000000 size=0x400000
 
                                          Chip revision is: 01

       Cables:
       -------------------
       mt52100_pciconf0_cable_0

       mt52100_pciconf0_cable_1

       mt52100_pciconf0_cable_10

       mt52100_pciconf0_cable_11

       .........
       .........
       mt52100_pciconf0_cable_36

       mt52100_pciconf0_cable_4

       mt52100_pciconf0_cable_5

       mt52100_pciconf0_cable_6

       mt52100_pciconf0_cable_7

       mt52100_pciconf0_cable_8

       mt52100_pciconf0_cable_9

3. Query and display the cable related information.

   mlxcable numbering is from: 0 - (Number of ports-1)

       admin@sonic:~$ sudo mlxcables -d /dev/mst/mt52100_pci_cr0_cable_0

       Querying Cables ....

       Cable #1:
       ---------
       Cable name    : /dev/mst/mt52100_pci_cr0_cable_0
       
       >> No FW data to show

       -------- Cable EEPROM --------

       Identifier    : SFP/SFP+/SFP28 (03h)

       Technology    : AOC (Active Optical Cable)

       Compliance    : Unspecified, 100G AOC or 25GAUI C2M AOC. Providing a worst BER of 10^(-12) or below

       OUI           : 0x0002c9

       Vendor        : Mellanox

       Serial number : MT1834FT03899

       Part number   : MFA7A50-C003

       Revision      : A3

       Temperature   : 40 C

       Length        : 3 m

For detailed parameters and instructions, please refer to latest MFT User Manual.

### mlxlink - Mellanox Link Tool

The mlxlink tool is used to check and debug link status and issues related to them. The tool can be used on different links and cables (passive, active, transceiver and backplane).

The following operations could be performed using this tool.

- In order for mlxlink to function properly, make sure to update the firmware version to the latest version.
- mlxlink is intended for advanced users with appropriate technical background.
- Do not use mlxlink to disable the port connecting between the host and the unmanaged switch using (“--port_state dn”) flag.
- mlxlink errors, warnings and notes are printed on stderr console.
- Setting the speeds (50GbE and 100GbE) requires specifying the number of lanes for the speed: mlxlink -d <dev> --speeds [50G_2X | 50G_1X | 100G_2X | 100G_4X]
- mlxlink numbering is from: 1 - (Number of ports)

- Queries:
  - Transmitter
  - Receiver
  - BER monitor
  - External PHY
  - Eye Opening
  - FEC Capabilities
  - Module information
- Commands:
  - Configure speeds
  - Loopback
  - FEC override
  - RX/TX PRBS mode
  - More

For example:

```
admin@sonic:~$ sudo mlxlink -d /dev/mst/mt52100_pci_cr0 -p 0x2
 
Operational Info
----------------
State                           : Active
Physical state                  : LinkUp
Speed                           : 25GbE
Width                           : 1x
FEC                             : Firecode FEC
Loopback Mode                   : No Loopback
Auto Negotiation                : ON
 
Supported Info
--------------
Enabled Link Speed              : 0x38000000 (25G)
Supported Cable Speed           : 0x3c007011 (25G,10G,1G)
 
Troubleshooting Info
--------------------
Status Opcode                   : 0
Group Opcode                    : N/A
Recommendation                  : No issue was observed.
```

For detailed parameters and instructions, please refer to latest MFT User Manual.

### mstdump - Mellanox Dump Tool

The mstdump utility dumps device internal configuration registers. The dump file is used by Mellanox Support for hardware troubleshooting purposes. It can be applied on all Mellanox devices.

When debugging a link issue, it is recommended to execute the command 3 times with 1 sec interval to help track the state machine changes.

Examples:

Dumps internal registers of a SN2700 device:

```
admin@sonic:~$ sudo mstdump /dev/mst/mt52100_pci_cr0
...
0x0015a884 0x40000000
0x0015a888 0x00000024
0x0015a88c 0x11000900
0x0015a890 0x00000000
0x0015a894 0x40000000
0x0015a898 0x00000024
0x0015a89c 0x11000900
0x0015a8a0 0x00000000
0x0015a8a4 0x40000000
0x0015a8a8 0x00000024
0x0015a8ac 0x11000900
0x0015a8b0 0x00000144
0x0015a8b4 0x00700080
0x0015a8b8 0x00000000
0x0015a8bc 0x00000000
0x0015a8c0 0x00000000
0x0015a8c4 0x00000000
0x0015a8c8 0x00000000
0x0015a8cc 0x00000000
0x0015a8d0 0x00000000
0x0015a8d4 0x00000000
0x0015a8d8 0x00000000
0x0015a8e0 0x01006000
...
```

mstdump is also executed as part of the ‘show techsupport’.

For detailed parameters and instructions, please refer to latest {{<exlink url="https://docs.mellanox.com/category/mft" text="MFT User Manual">}}.

## System Dump

System Dump is used to generate system dump for debugging purposes. Once the command is executed, it compresses all the information into an archive file. Resulting archive file is saved as /var/dump/<DEVICE_HOST_NAME>_YYYYMMDD_HHMMSS.tar.gz

Each issue reported must include system dump. The information can assist in reproducing the issue and having an offline analyse.

To generate system dump:

    #show techsupport \[--since '2 days ago'\]

System dump includes the following info:

- State of /proc FS
- Platform info (version, name, etc.)
- Configuration (routes, BGP, etc.)
- System info (running processes, memory utilization, etc.)
- Redis DB instances dump
- SAI attributes dump
- Log files
- Core dump files
- Platform specific files.

*For Mellanox it also includes SDK dump, firmware trace and MST dump.

## Logs

All SONiC logs are available at /var/log/syslog. To change log level, use the swssloglevel utility:

To set orchagent severity level to NOTICE:

    # swssloglevel -l NOTICE -c orchagent

To set SAI_API_SWITCH severity to ERROR:

    # swssloglevel -l SAI_LOG_LEVEL_ERROR -s -c SWITCH

To set all SAI_API_* severity to DEBUG:

    # swssloglevel -l SAI_LOG_LEVEL_DEBUG -s -a

## Docker Status

To verify that all docker containers are running:

    # docker ps

To verify that all processes are running in a container:

    # docker exec -it swss supervisorctl status

Containers are started by systemd, so it is possible to use systemctl to get the status. 

    # systemctl status swss.service

In case some docker containers are not running:

1. Check whether all services are running.

       # systemctl status
2. Check /var/log/syslog for errors.
3. Restart SONiC service which failed, for example swss: # systemctl restart swss.
