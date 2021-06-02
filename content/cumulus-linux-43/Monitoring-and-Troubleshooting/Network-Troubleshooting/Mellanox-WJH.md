---
title: Mellanox What Just Happened (WJH)
author: NVIDIA
weight: 1130
toc: 4
---
Cumulus Linux supports *What Just Happened* (WJH) for Mellanox switches, which provides real time visibility into network problems.

WJH has two components:
- The WJH agent is installed and enabled by default in Cumulus Linux so that you can stream detailed and contextual telemetry for off-box analysis with tools, such as [Cumulus NetQ]({{<ref "/cumulus-netq-33" >}}). 
- The WJH service is an optional package that you can install and run in Cumulus Linux to help diagnose network problems by looking at dropped packets. Currently, only forwarding (layer 2, layer 3, and tunnel) related issues are shown.

## Install the WJH Service

To install and run the WJH service, run the following commands:

```
cumulus@switch:~$ sudo -E apt-get update
cumulus@switch:~$ sudo -E apt-get install what-just-happened
cumulus@switch:~$ sudo systemctl start what-just-happened
```

## Run WJH Commands

After you install and start the WJH service, you can run the following commands from the command line.

| <div style="width:450px">Command  | Description |
| -------  | ----------- |
| `what-just-happened poll` | Shows information about dropped packets due to forwarding-related issues (layer 2, layer 3, and tunnel only). The output includes the reason for the drop and the recommended action to take.<br><br>The `what-just-happened poll forwarding` command shows the same information. |
| `what-just-happened poll --aggregate` | Shows information about dropped packets due to forwarding-related issues aggregated by the reason for the drop. The number of times the dropped packet occurred is also shown.<br><br>The `what-just-happened poll forwarding --aggregate` command shows the same information. |
| `what-just-happened poll --export` | Saves information about dropped packets due to forwarding-related issues into a file in PCAP format.<br><br>The `what-just-happened poll forwarding --export` command shows the same information. |
| `what-just-happened poll  --no_metadata` | Saves information about dropped packets due to forwarding-related issues into a file in PCAP format without metadata.<br><br> The `what-just-happened poll forwarding --no_metadata` command shows the same information.|
| `what-just-happened configuration global` | Shows WJH configuration for forwarding-related issues.<br><br>The `what-just-happened configuration forwarding` command shows the same information. |
| `what-just-happened dump` | Displays all diagnostic information on the command line. |

Run the `what-just-happened -h` command to see all the WJH command options. (Forwarding is the only *channel* currently supported.)

## Command Examples

The following command example shows all dropped packets and the reason for the drop:

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

The following example shows that packets were dropped five times because the source MAC address equals the destination MAC address:

```
cumulus@switch:~$ what-just-happened poll --aggregate
Sample Window : 2020/11/06 16:12:54.032 - 2020/11/06 16:12:59.381
#  sPort  VLAN  sMAC               dMAC               EthType  Src IP:Port  Dst IP:Port  IP Proto  Count  Severity  Drop reason - Recommended action
-- ------ ----- ------------------ ------------------ -------- ------------ ------------ --------- ------ --------- -----------------------------------------------
1  -1     N/A   44:38:39:00:a4:80  44:38:39:00:a4:80  IPv4     0.0.0.0:0    0.0.0.0:0    ip        5      Error     Source MAC equals destination MAC - Bad packet
```

The following command saves dropped packets to a file in PCAP format:
```
cumulus@switch:~$ what-just-happened --export
PCAP file path : /var/log/mellanox/wjh/wjh_user_2020_11_06_16_13_37.pcap
#  Timestamp              sPort  dPort  VLAN  sMAC               dMAC               EthType  Src IP:Port  Dst IP:Port  IP Proto  Drop   Severity  Drop reason - Recommended action
                                                                                                                                 Group
-- ---------------------- ------ ------ ----- ------------------ ------------------ -------- ------------ ------------ --------- ------ --------- -----------------------------------------------
1  20/11/06 16:13:30.644  -1     N/A    N/A   44:38:39:00:a4:80  44:38:39:00:a4:80  IPv4     N/A          N/A          N/A       L2     Error     Source MAC equals destination MAC - Bad packet
                                                                                                                                                  was received from peer
2  20/11/06 16:13:31.063  -1     N/A    N/A   44:38:39:00:a4:80  44:38:39:00:a4:80  IPv4     N/A          N/A          N/A       L2     Error     Source MAC equals destination MAC - Bad packet
                                                                                                                                                  was received from peer
```
