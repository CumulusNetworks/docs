---
title: What Just Happened (WJH)
author: NVIDIA
weight: 1130
toc: 4
---
*What Just Happened* (WJH) provides real time visibility into network problems and has two components:
- The WJH agent enables you to stream detailed and contextual telemetry for off-switch analysis with tools, such as [NVIDIA NetQ]({{<ref "/cumulus-netq-41" >}}).
- The WJH service (`what-just-happened`) enables you to diagnose network problems by looking at dropped packets. WJH can monitor layer 1, layer 2, layer 3, tunnel, ACL, and buffer related issues.

## Configure WJH

WJH can monitor layer 1, layer 2, layer 3, tunnel, acl and buffer packet drops. You can choose which packet drops you want to monitor by creating channels and setting the packet drop categories you want to monitor.

{{< tabs "TabID24 ">}}
{{< tab "NVUE Commands ">}}

The following example configures three separate channels:
- The `forwarding` channel monitors layer 2, layer 3, and tunnel packet drops.
- The `acl-and-buffer` channel monitors ACL and buffer packet drops.
- The `layer-one` channel monitors layer 1 packet drops.

```
cumulus@switch:~$ nv set service wjh channel forwarding trigger l2
cumulus@switch:~$ nv set service wjh channel forwarding trigger l3
cumulus@switch:~$ nv set service wjh channel forwarding trigger tunnel
cumulus@switch:~$ nv set service wjh channel acl-and-buffer trigger acl
cumulus@switch:~$ nv set service wjh channel acl-and-buffer trigger buffer
cumulus@switch:~$ nv set service wjh channel layer-one trigger l1
cumulus@switch:~$ nv config apply
```

You can stop monitoring specific packet drops by unsetting the channel or unsetting a category in the channel list.

To stop monitoring all packet drop categories listed in the `forwarding` channel (layer, 2, layer 3, and tunnel) and remove the channel:

```
cumulus@switch:~$ nv unset service wjh channel forwarding
cumulus@switch:~$ nv config apply
```

To stop monitoring ACL packet drops in the `acl-and-buffer` channel:

```
cumulus@switch:~$ nv unset service wjh channel acl-and-buffer trigger acl
cumulus@switch:~$ nv config apply
```

{{< /tab >}}
{{< tab "Linux Commands ">}}

Edit the `/etc/what-just-happened/what-just-happened.json` file:
- For each drop category you want to monitor, include the drop category value inside the square brackets ([]). 
- For each drop category you do **not** want to monitor, remove the drop category value from inside the square brackets ([]).

After you edit the file, you must restart the WJH service with the `sudo systemctl restart what-just-happened` command.

The following example configures three separate channels:
- The `forwarding` channel monitors layer 2, layer 3, and tunnel packet drops.
- The `acl-and-buffer` channel monitors ACL and buffer packet drops.
- The `layer-one` channel monitors layer 1 packet drops.

```
cumulus@switch:~$ sudo nano /etc/what-just-happened/what-just-happened.json
{
    "what-just-happened": {
        "channels": {
            "acl-and-buffer": {
                "drop_category_list": [
                    "buffer",
                    "acl"
                ]
            },
            "layer-one": {
                "drop_category_list": [
                    "l1"
                ]
            },
            "forwarding": {
                "drop_category_list": [
                    "l2",
                    "l3",
                    "tunnel"
                ]
            }
        }
    }
}
```

After you configure which packet drops to monitor, you must restart the `what-just-happened` service:

```
cumulus@switch:~$ sudo systemctl restart what-just-happened
```

{{< /tab >}}
{{< /tabs >}}

## Show Information about Dropped Packets

You can run the following commands to show information about dropped packets and diagnose problems.

{{< tabs "TabID76 ">}}
{{< tab "NVUE Commands ">}}

```
cumulus@switch:~$ nv show service wjh packet-buffer 
#    Timestamp              sPort  dPort  VLAN  sMAC               dMAC               EthType  Src IP:Port  Dst IP:Port  IP Proto  Drop   Severity  Drop reason - Recommended action
                                                                                                                                   Group
---- ---------------------- ------ ------ ----- ------------------ ------------------ -------- ------------ ------------ --------- ------ --------- -----------------------------------------------
1    21/06/16 12:02:42.052  swp1   N/A    N/A   44:38:39:00:a4:84  44:38:39:00:a4:84  IPv4     N/A          N/A          N/A       L2     Error     Source MAC equals destination MAC - Bad packet was received from peer
2    21/06/16 12:02:42.052  swp1   N/A    N/A   44:38:39:00:a4:84  44:38:39:00:a4:84  IPv4     N/A          N/A          N/A       L2     Error     Source MAC equals destination MAC - Bad packet was received from peer
3    21/06/16 12:02:42.052  swp1   N/A    N/A   44:38:39:00:a4:84  44:38:39:00:a4:84  IPv4     N/A          N/A          N/A       L2     Error     Source MAC equals destination MAC - Bad packet was received from peer
4    21/06/16 12:02:42.069  swp1   N/A    N/A   44:38:39:00:a4:84  44:38:39:00:a4:84  IPv4     N/A          N/A          N/A       L2     Error     Source MAC equals destination MAC - Bad packet was received from peer
```

{{< /tab >}}
{{< tab "Linux Commands ">}}

You can run the following commands from the command line.

| <div style="width:450px">Command  | Description |
| -------  | ----------- |
| `what-just-happened poll` | Shows information about layer 1, layer 2, layer 3, and tunnel packet drops. The output includes the reason for the drop and the recommended action to take.<br><br>The `what-just-happened poll forwarding` command shows the same information. |
| `what-just-happened poll --aggregate` | Shows information about dropped packets aggregated by the reason for the drop. This command also shows the number of times the dropped packet occurs.<br><br>The `what-just-happened poll forwarding --aggregate` command shows the same information. |
| `what-just-happened poll --export` | Saves information about dropped packets to a file in PCAP format.<br><br>The `what-just-happened poll forwarding --export` command shows the same information. |
| `what-just-happened poll --export --no_metadata` | Saves information about dropped packets to a file in PCAP format without metadata.<br><br> The `what-just-happened poll forwarding --export --no_metadata` command shows the same information.|
| `what-just-happened dump` | Displays all diagnostic information on the command line. |

Run the `what-just-happened -h` command to see all the WJH command options.

{{< /tab >}}
{{< /tabs >}}

## Command Examples

To show all dropped packets and the reason for the drop, run the NVUE `nv show service wjh packet-buffer` command or the `what-just-happened poll` command.

```
cumulus@switch:~$ nv show service wjh packet-buffer
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
cumulus@switch:~$ what-just-happened poll --aggregate
Sample Window : 2021/06/16 12:57:23.046 - 2021/06/16 14:46:17.701

#  sPort  VLAN  sMAC               dMAC               EthType  Src IP:Port  Dst IP:Port  IP Proto  Count  Severity  Drop reason - Recommended action
-- ------ ----- ------------------ ------------------ -------- ------------ ------------ --------- ------ --------- -----------------------------------------------
1  swp4   N/A   44:38:39:00:a4:87  44:38:39:00:a4:87  IPv4     0.0.0.0:0    0.0.0.0:0    ip        100    Error     Source MAC equals destination MAC - Bad packet was received from peer
2  swp1   N/A   44:38:39:00:a4:80  44:38:39:00:a4:80  IPv4     0.0.0.0:0    0.0.0.0:0    ip        100    Error     Source MAC equals destination MAC - Bad packet was received from peer
```

The following command saves dropped packets to a file in PCAP format

```
cumulus@switch:~$ what-just-happened poll --export
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

### Cumulus Linux and Docker

WJH runs in a Docker container. By default, when Docker starts, it creates a bridge called `docker0`. However, for compatibility reasons Cumulus Linux disables the `docker0` bridge in the `/etc/docker/daemon.json` file with the attribute `"bridge: none"`.

### WJH and the NVIDIA NetQ Agent

When you enable the NVIDIA NetQ agent on the switch, the WJH service stops and does not run. If you disable the NVIDIA NetQ service and want to use WJH, run the following commands to enable and start the WJH service:

{{< tabs "TabID14 ">}}
{{< tab "NVUE Commands">}}

```
cumulus@switch:~$ nv set service wjh enable on
cumulus@switch:~$ nv config apply
```

{{< /tab >}}
{{< tab "Linux Commands ">}}

```
cumulus@switch:~$ sudo systemctl enable what-just-happened
cumulus@switch:~$ sudo systemctl start what-just-happened
```

{{< /tab >}}
{{< /tabs >}}
