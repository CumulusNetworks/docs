---
title: Mellanox Debug Tools for SONiC
author: NVIDIA
weight: 610
product: SONiC
version: 202012
siteSlug: sonic
---

There are a number of tools you can use to debug SONiC on your switch. Some of the tools described below are available only on NVIDIA Spectrum switches.

## SDK Utilities

Each SDK API has a correlated Python script that can call the SDK API from the SONiC shell. It is located in the `/usr/bin` folder in the `syncd` container. You should only use the `get` options to prevent misconfiguration and misalignment with the SAI, as it is the only control application.

This topic discusses the various switch and router SDK features and their usage. The debug utilities include the *dump* keyword in their names.

Some default debug scripts include:

- sx_api_bridge_dump.py
- sx_api_bridge_iter_get.py
- sx_api_cos_shared_buffers_dump.py
- sx_api_dbg_generate_dump.py
- sx_api_fdb_dump.py
- sx_api_flex_acl_dump.py
- sx_api_flex_acl_key_attr_get.py
- sx_api_host_ifc_counters_get.py

You can get this list when you run this following command:

```
admin@switch:/home/admin$ docker exec -it syncd bash
admin@switch:/usr/bin$ ls sx_* -l
-rwxr-xr-x 1 root root    3445 Mar 23 16:16 sx_api_bridge_dump.py
-rwxr-xr-x 1 root root    8632 Mar 23 16:16 sx_api_bridge_iter_get.py
-rwxr-xr-x 1 root root   20471 Mar 23 16:16 sx_api_bridge_lag_redirect.py
-rwxr-xr-x 1 root root   10786 Mar 23 16:16 sx_api_bridge_vport.py
-rwxr-xr-x 1 root root    2759 Mar 23 16:16 sx_api_cos_default_prio.py
-rwxr-xr-x 1 root root    7939 Mar 23 16:16 sx_api_cos_ets.py
-rwxr-xr-x 1 root root   18616 Mar 23 16:16 sx_api_cos_port_buff_type.py
-rwxr-xr-x 1 root root    3794 Mar 23 16:16 sx_api_cos_port_ptp_params.py
...
```

With these Python interfaces, you can easily dump the information in the SDK to have a view of the SDK data and facilitate your troubleshooting.

An example of such usage can be seen below in the `sx_api_ports_dump.py` port information dump:

```
admin@switch:/usr/bin$ sudo sx_api_ports_dump.py
=================================================================================================================
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
=================================================================================================================
```

### SDK Debug Dump

The SDK debug dump is the API that can export all the debug information modules to a user-defined file name or the console. The internal debug information is exported per module:

- Databases dump parsed into tables
- List of current processes
- ASIC type and revision
- `mstdump` – useful for FW debug
- `dmesg`
- `lsmod`
- `lspci`
- `uname –a`
- sx_status_t sx_api_dbg_generate_dump (const sx_api_handle_t handle, const char *dump_file_path)

To generate the full SDK configuration dump, run:

    admin@switch:~$ sudo docker exec –it syncd sx_api_dbg_generate_dump.py

## SDK API Sniffer

On NVIDIA Spectrum switches, the SDK API sniffer can record the RPC calls from the SDK user API library to the `sx_sdk` in a PCAP file. You can use this to get the same exact state in both the SDK and firmware in order to reproduce and investigate issues.

{{<img src="/images/sonic/sdk-api-sniffer.png" width="600px">}}

To enable the sniffer, run the following command. The command output displays the sniffer file name, which is where the sniffer content is stored.

```
admin@switch:~$ sudo config platform mlnx sniffer sdk enable 
Swss service will be restarted, continue? [y/N]: y
Enabling SDK sniffer
SDK sniffer is Enabled, recording file is /var/log/mellanox/sniffer/sx_sdk_sniffer_20200622072855.pcap.
Note: the sniffer file may exhaust the space on /var/log, please disable it when you are done with this sniffering.
```

To disable the sniffer, run:

```
admin@switch:~$ sudo config platform mlnx sniffer sdk disable
Swss service will be restarted, continue? [y/N]: y
Disabling SDK sniffer
SDK sniffer is Disabled.
```

More information on these platform-specific commands, read the {{<exlink url="https://github.com/Azure/sonic-utilities/blob/master/doc/Command-Reference.md#platform-specific-commands" text="Azure SONiC documentation on GitHub">}}.

## MFT - Mellanox Firmware Tools

On NVIDIA Spectrum switches, the Mellanox Firmware Tools (MFT) package is integrated into SONiC and provides a set of firmware management and debugging tools.

You can use MFT to:

- Generate a standard or customized NVIDIA Spectrum firmware image
- Query for firmware information
- Burn a firmware image to a single NVIDIA Spectrum device

Every MFT addresses the target hardware device using an MST (Mellanox Software Tools) device name. This name is assigned by running the `mst start` command for PCI and I2C access (which is enabled by default). To list the available MST device names on the local machine, run `mst status`.

### mlxcables - Mellanox Cables Tool

On NVIDIA Spectrum switches, the `mlxcables` tool allows users to access the cables and do the following:

- Query the cable and get its IDs.
- Read specific addresses in the EEPROM.
- Read a specific register by its name. Supported registers are received by the tool and depend on the cable type.
- Dump all the cable EEPROM bytes in RAW format.
- Upgrade the firmware image on the cable uC (only on cables that support ISFU).

To query the cable:

1. Discover the MST cable devices.

       admin@switch:~$ sudo mst cable add

       -I- Added 33 cable devices ..
2. Show the MST devices.

   Each MFT command requires specifying the device (using the `-d` option), and each ASIC has a different device. For example, NVIDIA Spectrum: `/dev/mst/mt52100_pci_cr0`.

       admin@switch:~$ sudo mst status

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

       admin@switch:~$ sudo mlxcables -d /dev/mst/mt52100_pci_cr0_cable_0
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

For detailed parameters and instructions, refer to the latest {{<exlink url="https://docs.mellanox.com/category/mft" text="MFT user manual">}}.

### mlxlink - Mellanox Link Tool

The `mlxlink` tool is used to check and debug link status and issues related to them. The tool can be used on different links and cables (passive, active, transceiver and backplane).

{{%notice note%}}

- `mlxlink` is intended for advanced users with appropriate technical background.
- In order for `mlxlink` to function properly, {{<exlink url="https://docs.mellanox.com/display/MFTv4161/Updating+the+Device" text="update the firmware">}} to the latest version.
- Do not use `mlxlink` to disable the port connecting between the host and the unmanaged switch using the `--port_state dn` flag.
- `mlxlink` errors, warnings and notes are printed to the `stderr` console.
- Setting port speeds (50GbE and 100GbE) requires specifying the number of lanes for the speed: `mlxlink -d <dev> --speeds [50G_2X | 50G_1X | 100G_2X | 100G_4X]`
- `mlxlink` port numbering starts at 1.

{{%/notice%}}

You can perform the following operations with `mlxlink`:

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
admin@switch:~$ sudo mlxlink -d /dev/mst/mt52100_pci_cr0 -p 0x2
 
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

For detailed parameters and instructions, refer to the latest {{<exlink url="https://docs.mellanox.com/category/mft" text="MFT user manual">}}.

### mstdump - NVIDIA Spectrum Dump Tool

On NVIDIA Spectrum switches, the `mstdump` utility dumps device internal configuration registers. The dump file is used by NVIDIA support for hardware troubleshooting purposes. It can be run on all NVIDIA Spectrum switches.

When debugging a link issue, you should execute the command 3 times at 1 second intervals to help track the state machine changes.

For example, to dump internal registers of an SN2700 switch, run:

```
admin@switch:~$ sudo mstdump /dev/mst/mt52100_pci_cr0
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

`mstdump` is also executed when you run `show techsupport`.

For detailed parameters and instructions, refer to the latest NVIDIA {{<exlink url="https://docs.mellanox.com/category/mft" text="MFT user manual">}}.
