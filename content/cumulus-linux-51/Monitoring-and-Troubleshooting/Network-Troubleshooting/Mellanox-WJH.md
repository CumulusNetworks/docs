---
title: What Just Happened (WJH)
author: NVIDIA
weight: 1130
toc: 4
---
*What Just Happened* (WJH) provides real time visibility into network problems and has two components:
- The WJH agent enables you to stream detailed and contextual telemetry for off-switch analysis with tools, such as {{<exlink url="https://docs.nvidia.com/networking-ethernet-software/cumulus-netq" text="NVIDIA NetQ" >}}.
- The WJH service (`what-just-happened`) enables you to diagnose network problems by looking at dropped packets. WJH monitors forwarding (layer 2, layer 3, and tunnel) related issues. Cumulus Linux enables the WJH service by default.

  {{%notice note%}}
When you enable the NVIDIA NetQ agent on the switch, the WJH service stops and does not run. If you disable the NVIDIA NetQ service and want to use WJH, run the following commands to enable and start the WJH service:

```
cumulus@switch:~$ sudo systemctl enable what-just-happened
cumulus@switch:~$ sudo systemctl start what-just-happened
```
{{%/notice%}}

## Run WJH Commands

You can run the following commands from the command line.

| <div style="width:450px">Command  | Description |
| -------  | ----------- |
| `what-just-happened poll` | Shows information about dropped packets due to forwarding-related issues (layer 2, layer 3, and tunnel only). The output includes the reason for the drop and the recommended action to take.<br><br>The `what-just-happened poll forwarding` command shows the same information. |
| `what-just-happened poll --aggregate` | Shows information about dropped packets due to forwarding-related issues aggregated by the reason for the drop. This command also shows the number of times the dropped packet occurs.<br><br>The `what-just-happened poll forwarding --aggregate` command shows the same information. |
| `what-just-happened poll --export` | Saves information about dropped packets due to forwarding-related issues into a file in PCAP format.<br><br>The `what-just-happened poll forwarding --export` command shows the same information. |
| `what-just-happened poll --export --no_metadata` | Saves information about dropped packets due to forwarding-related issues into a file in PCAP format without metadata.<br><br> The `what-just-happened poll forwarding --export --no_metadata` command shows the same information.|
| `what-just-happened dump` | Displays all diagnostic information on the command line. |

Run the `what-just-happened -h` command to see all the WJH command options. (WJH only supports the forwarding *channel*.)

## Command Examples

The following example shows all dropped packets and the reason for the drop:

```
root@switch:~# what-just-happened poll
#    Timestamp              sPort  dPort  VLAN  sMAC               dMAC               EthType  Src IP:Port  Dst IP:Port  IP Proto  Drop   Severity  Drop reason - Recommended action
                                                                                                                                   Group
---- ---------------------- ------ ------ ----- ------------------ ------------------ -------- ------------ ------------ --------- ------ --------- -----------------------------------------------
1    21/06/16 12:02:42.052  swp1   N/A    N/A   44:38:39:00:a4:84  44:38:39:00:a4:84  IPv4     N/A          N/A          N/A       L2     Error     Source MAC equals destination MAC - Bad packet was received from peer
2    21/06/16 12:02:42.052  swp1   N/A    N/A   44:38:39:00:a4:84  44:38:39:00:a4:84  IPv4     N/A          N/A          N/A       L2     Error     Source MAC equals destination MAC - Bad packet was received from peer
3    21/06/16 12:02:42.052  swp1   N/A    N/A   44:38:39:00:a4:84  44:38:39:00:a4:84  IPv4     N/A          N/A          N/A       L2     Error     Source MAC equals destination MAC - Bad packet was received from peer
4    21/06/16 12:02:42.069  swp1   N/A    N/A   44:38:39:00:a4:84  44:38:39:00:a4:84  IPv4     N/A          N/A          N/A       L2     Error     Source MAC equals destination MAC - Bad packet was received from peer
```

The following example shows that packets drop five times because the source MAC address equals the destination MAC address:

```
root@switch:~# what-just-happened poll --aggregate
Sample Window : 2021/06/16 12:57:23.046 - 2021/06/16 14:46:17.701

#  sPort  VLAN  sMAC               dMAC               EthType  Src IP:Port  Dst IP:Port  IP Proto  Count  Severity  Drop reason - Recommended action
-- ------ ----- ------------------ ------------------ -------- ------------ ------------ --------- ------ --------- -----------------------------------------------
1  swp4   N/A   44:38:39:00:a4:87  44:38:39:00:a4:87  IPv4     0.0.0.0:0    0.0.0.0:0    ip        100    Error     Source MAC equals destination MAC - Bad packet was received from peer
2  swp1   N/A   44:38:39:00:a4:80  44:38:39:00:a4:80  IPv4     0.0.0.0:0    0.0.0.0:0    ip        100    Error     Source MAC equals destination MAC - Bad packet was received from peer
```

The following command saves dropped packets to a file in PCAP format

```
root@switch:~# what-just-happened poll --export
PCAP file path : /var/log/mellanox/wjh/wjh_user_2021_06_16_12_03_15.pcap

#    Timestamp              sPort  dPort  VLAN  sMAC               dMAC               EthType  Src IP:Port  Dst IP:Port  IP Proto  Drop   Severity  Drop reason - Recommended action
                                                                                                                                   Group
---- ---------------------- ------ ------ ----- ------------------ ------------------ -------- ------------ ------------ --------- ------ --------- -----------------------------------------------
1    21/06/16 12:03:12.728  swp1   N/A    N/A   44:38:39:00:a4:84  44:38:39:00:a4:84  IPv4     N/A          N/A          N/A       L2     Error     Source MAC equals destination MAC - Bad packet as received from peer
2    21/06/16 12:03:12.728  swp1   N/A    N/A   44:38:39:00:a4:84  44:38:39:00:a4:84  IPv4     N/A          N/A          N/A       L2     Error     Source MAC equals destination MAC - Bad packet was received from peer
3    21/06/16 12:03:12.745  swp1   N/A    N/A   44:38:39:00:a4:84  44:38:39:00:a4:84  IPv4     N/A          N/A          N/A       L2     Error     Source MAC equals destination MAC - Bad packet was received from peer
4    21/06/16 12:03:12.745  swp1   N/A    N/A   44:38:39:00:a4:84  44:38:39:00:a4:84  IPv4     N/A          N/A          N/A       L2     Error     Source MAC equals destination MAC - Bad packet was received from peer
```

## Considerations

WJH runs in a Docker container. By default, when Docker starts, it creates a bridge called `docker0`. However, for compatibility reasons Cumulus Linux disables the `docker0` bridge in the `/etc/docker/daemon.json` file with the attribute `"bridge: none"`.
