---
title: Mellanox What Just Happened (WJH)
author: NVIDIA
weight: 1130
toc: 4
---
Cumulus Linux supports *What Just Happened* (WJH) for Mellanox switches, which provides real time visibility into network problems.

WJH has two components:
- The WJH agent is installed and enabled by default in Cumulus Linux so that you can stream detailed and contextual telemetry for off-box analysis with tools, such as {{<exlink url="https://docs.cumulusnetworks.com/cumulus-netq/" text="Cumulus NetQ">}}. 
- The WJH service is an optional package that you can install and run in Cumulus Linux to help diagnose network problems by looking at dropped packets due to layer 1, layer 2, layer 3, tunnel, ACL, and buffer related issues.

## Install the WJH Service

To install and run the WJH service, run the following commands:

```
cumulus@switch:~$ sudo apt-get install what-just-happened
cumulus@switch:~$ sudo systemctl start what-just-happened
```

## Command Options

| Command  | Description |
| -------  | ----------- |
| `what-just-happened poll` | Shows information about all dropped packets, including the reason for the drop and the recommended action to take. |
| `what-just-happened poll --aggregate` | Shows all aggregated counters. |
| `what-just-happened poll --export` | Saves dropped packets into a file in PCAP format. |
| `what-just-happened poll --export --no_metadata` | Saves dropped packets into a file in PCAP format without metadata. |
| `what-just-happened configuration channels` | Shows what-just-happened channel configuration. |
| `what-just-happened global` | Shows global what-just-happened configuration. |
| `what-just-happened dump` | Displays what-just-happened diagnostic information on the command line. |

## Command Examples

The following command example shows all dropped packets:

```
cumulus@switch:~$ what-just-happened poll
#  Timestamp              sPort  dPort  VLAN  sMAC               dMAC               EthType  Src IP:Port  Dst IP:Port  IP Proto  Drop   Severity  Drop reason - Recommended action
                                                                                                                                 Group
-- ---------------------- ------ ------ ----- ------------------ ------------------ -------- ------------ ------------ --------- ------ --------- -----------------------------------------------
1  20/11/06 16:10:24.594  -1     N/A    N/A   44:38:39:00:a4:80  44:38:39:00:a4:80  IPv4     N/A          N/A          N/A       L2     Error     Source MAC equals destination MAC - Bad packet
                                                                                                                                                  was received from peer
2  20/11/06 16:10:25.106  -1     N/A    N/A   44:38:39:00:a4:80  44:38:39:00:a4:80  IPv4     N/A          N/A          N/A       L2     Error     Source MAC equals destination MAC - Bad packet
                                                                                                                                                  was received from peer
```

The following command example shows aggregated counters in the default channel (forwarding):

```
cumulus@switch:~$ what-just-happened poll --aggregate
Sample Window : 2020/11/06 16:12:54.032 - 2020/11/06 16:12:59.381
#  sPort  VLAN  sMAC               dMAC               EthType  Src IP:Port  Dst IP:Port  IP Proto  Count  Severity  Drop reason - Recommended action
-- ------ ----- ------------------ ------------------ -------- ------------ ------------ --------- ------ --------- -----------------------------------------------
1  -1     N/A   44:38:39:00:a4:80  44:38:39:00:a4:80  IPv4     0.0.0.0:0    0.0.0.0:0    ip        5      Error     Source MAC equals destination MAC - Bad packet
```

The following command example saves dropped packets in the forwarding channel into a file in PCAP format:
```
cumulus@switch:~$ what-just-happened forwarding --export
PCAP file path : /var/log/mellanox/wjh/wjh_user_2020_11_06_16_13_37.pcap
#  Timestamp              sPort  dPort  VLAN  sMAC               dMAC               EthType  Src IP:Port  Dst IP:Port  IP Proto  Drop   Severity  Drop reason - Recommended action
                                                                                                                                 Group
-- ---------------------- ------ ------ ----- ------------------ ------------------ -------- ------------ ------------ --------- ------ --------- -----------------------------------------------
1  20/11/06 16:13:30.644  -1     N/A    N/A   44:38:39:00:a4:80  44:38:39:00:a4:80  IPv4     N/A          N/A          N/A       L2     Error     Source MAC equals destination MAC - Bad packet
                                                                                                                                                  was received from peer
2  20/11/06 16:13:31.063  -1     N/A    N/A   44:38:39:00:a4:80  44:38:39:00:a4:80  IPv4     N/A          N/A          N/A       L2     Error     Source MAC equals destination MAC - Bad packet
                                                                                                                                                  was received from peer
```

You can also run commands from the docker CLI with `wjhcli` commands.
