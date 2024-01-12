---
title: What Just Happened (WJH)
author: NVIDIA
weight: 1130
toc: 4
---
*What Just Happened* (WJH) provides real time visibility into network problems and has two components:
- The WJH agent enables you to stream detailed and contextual telemetry for off-switch analysis with tools such as [NVIDIA NetQ]({{<ref "/cumulus-netq-48" >}}).
- The WJH service (`what-just-happened`) enables you to diagnose network problems by looking at dropped packets. WJH can monitor layer 1, layer 2, layer 3, tunnel, buffer and ACL related issues. Cumulus Linux enables and runs the WJH service by default.

## Configure WJH

You can choose which packet drops you want to monitor by creating channels and setting the packet drop categories (layer 1, layer 2, layer 3, tunnel, buffer and ACL ) you want to monitor.

NVUE does not provide commands to set the buffer and ACL packet drop categories. You must edit the `/etc/what-just-happened/what-just-happened.json` file. See the Linux Commands tab.

{{< tabs "TabID24 ">}}
{{< tab "NVUE Commands ">}}

The following example configures two separate channels:
- The `forwarding` channel monitors layer 2, layer 3, and tunnel packet drops.
- The `layer-1` channel monitors layer 1 packet drops.

```
cumulus@switch:~$ nv set system wjh channel forwarding trigger l2
cumulus@switch:~$ nv set system wjh channel forwarding trigger l3
cumulus@switch:~$ nv set system wjh channel forwarding trigger tunnel
cumulus@switch:~$ nv set system wjh channel layer-1 trigger l1
cumulus@switch:~$ nv config apply
```

You can stop monitoring specific packet drops by unsetting a category in the channel list. The following command example stops monitoring layer 2 packet drops that are in the `forwarding` channel:

```
cumulus@switch:~$ nv unset system wjh channel forwarding trigger l2
cumulus@switch:~$ nv config apply
```

To remove a channel, run the `nv unset system wjh channel <channel>` command. The following command example removes the `layer-1` channel:

```
cumulus@switch:~$ nv unset system wjh channel layer-1 
cumulus@switch:~$ nv config apply
```

{{< /tab >}}
{{< tab "Linux Commands ">}}

Edit the `/etc/what-just-happened/what-just-happened.json` file:
- For each drop category you want to monitor, include the drop category value inside the square brackets ([]). 
- For each drop category you do **not** want to monitor, remove the drop category value from inside the square brackets.

After you edit the file, you must restart the WJH service with the `sudo systemctl restart what-just-happened` command.

The following example configures a channel to monitor layer 2, layer 3, and tunnel packet drops and a channel to monitor layer 1 packet drops.

```
cumulus@switch:~$ sudo nano /etc/what-just-happened/what-just-happened.json
{
    "what-just-happened": {
        "channels": {
            "forwarding": {
                "drop_category_list": [
                    "l2",
                    "l3",
                    "tunnel"
                ]
            },
            "layer-1": {
                "drop_category_list": [
                    "l1"
                ]
            }
        }
    }
}
```

```
cumulus@switch:~$ sudo systemctl restart what-just-happened
```

The following example configures a channel to monitor buffer packet drops and a channel to monitor ACL packet drops.

```
cumulus@switch:~$ sudo nano /etc/what-just-happened/what-just-happened.json
{
    "what-just-happened": {
        "channels": {
            "buffer": {
                "drop_category_list": ["buffer"]
            },
            "acl": {
                "drop_category_list": ["acl"]
            }
        }
    }
}
```

```
cumulus@switch:~$ sudo systemctl restart what-just-happened
```

{{< /tab >}}
{{< /tabs >}}

## Show Information about Dropped Packets

You can run the following commands to show information about dropped packets and diagnose problems.

{{< tabs "TabID76 ">}}
{{< tab "NVUE Commands ">}}

To show information about packet drops for all the channels you configure, run the `nv show system wjh packet-buffer ` command. The command output includes the reason for the drop and the recommended action to take.

You can also show the WJH configuration on the switch:
- To show the configuration for a channel, run the `nv show system wjh channel <channel>` command. For example, `nv show system wjh channel forwarding`.
- To show the configuration for packet drop categories in a channel, run the `nv show system wjh channel <channel> trigger` command. For example, `nv show system wjh channel forwarding trigger`.

The following example shows information about layer 1 packet drops:

```
cumulus@switch:~$ nv show system wjh packet-buffer
#   dMAC  dPort  Dst IP:Port  EthType  Drop group  IP Proto  Drop reason - Recommended action                         Severity  sMAC  sPort    Src IP:Port  Timestamp              VLAN
--  ----  -----  -----------  -------  ----------  --------  -------------------------------------------------------  --------  ----  -------  -----------  ---------------------  ----
1   N/A   N/A    N/A          N/A      L1          N/A       Generic L1 event - Check layer 1 aggregated information  Warn      N/A   swp17    N/A          22/11/03 01:00:35.458  N/A
2   N/A   N/A    N/A          N/A      L1          N/A       Generic L1 event - Check layer 1 aggregated information  Warn      N/A   swp18    N/A          22/11/03 01:00:35.458  N/A
3   N/A   N/A    N/A          N/A      L1          N/A       Generic L1 event - Check layer 1 aggregated information  Warn      N/A   swp19    N/A          22/11/03 01:00:35.458  N/A
4   N/A   N/A    N/A          N/A      L1          N/A       Generic L1 event - Check layer 1 aggregated information  Warn      N/A   swp20    N/A          22/11/03 01:00:35.458  N/A
```

{{< /tab >}}
{{< tab "Linux Commands ">}}

You can run the following commands from the command line.

| <div style="width:450px">Command  | Description |
| -------  | ----------- |
| `what-just-happened poll` | Shows information about packet drops for all the channels you configure. The output includes the reason for the drop and the recommended action to take.<br><br>The `what-just-happened poll <channel>` command shows information for the channel you specify. |
| `what-just-happened poll --aggregate` | Shows information about dropped packets aggregated by the reason for the drop. This command also shows the number of times the dropped packet occurs.<br><br>The `what-just-happened poll <channel> --aggregate` command shows information for the channel you specify. |
| `what-just-happened poll --export` | Saves information about dropped packets to a file in PCAP format.<br><br>The `what-just-happened poll <channel> --export` command saves information for the channel you specify. |
| `what-just-happened poll --export --no_metadata` | Saves information about dropped packets to a file in PCAP format without metadata.<br><br> The `what-just-happened poll <channel> --export --no_metadata` command saves information for the channel you specify.|
| `what-just-happened dump` | Displays all diagnostic information on the command line. |

Run the `what-just-happened -h` command to see all the WJH command options.

To show all dropped packets and the reason for the drop, run the NVUE `nv show system wjh packet-buffer` command or the `what-just-happened poll` command.


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
cumulus@switch:~$ what-just-happened poll --export --no_metadata
PCAP file path : /var/log/mellanox/wjh/wjh_user_2021_06_16_12_03_15.pcap

#    Timestamp              sPort  dPort  VLAN  sMAC               dMAC               EthType  Src IP:Port  Dst IP:Port  IP Proto  Drop   Severity  Drop reason - Recommended action
                                                                                                                                   Group
---- ---------------------- ------ ------ ----- ------------------ ------------------ -------- ------------ ------------ --------- ------ --------- -----------------------------------------------
1    21/06/16 12:03:12.728  swp1   N/A    N/A   44:38:39:00:a4:84  44:38:39:00:a4:84  IPv4     N/A          N/A          N/A       L2     Error     Source MAC equals destination MAC - Bad packet as received from peer
2    21/06/16 12:03:12.728  swp1   N/A    N/A   44:38:39:00:a4:84  44:38:39:00:a4:84  IPv4     N/A          N/A          N/A       L2     Error     Source MAC equals destination MAC - Bad packet was received from peer
3    21/06/16 12:03:12.745  swp1   N/A    N/A   44:38:39:00:a4:84  44:38:39:00:a4:84  IPv4     N/A          N/A          N/A       L2     Error     Source MAC equals destination MAC - Bad packet was received from peer
4    21/06/16 12:03:12.745  swp1   N/A    N/A   44:38:39:00:a4:84  44:38:39:00:a4:84  IPv4     N/A          N/A          N/A       L2     Error     Source MAC equals destination MAC - Bad packet was received from peer
```

{{< /tab >}}
{{< /tabs >}}

## Considerations

### Buffer Packet Drop Monitoring

- Buffer packet drop monitoring is available on a switch with Spectrum-2 and later.
- Buffer packet drop monitoring uses a SPAN destination. If you configure SPAN, ensure that you do not exceed the total number of SPAN destinations allowed for your switch ASIC type; see {{<link url="SPAN-and-ERSPAN/#limitations" text="SPAN and ERSPAN">}}. If you need to remove the SPAN destination that buffer packet drop monitoring uses, delete the buffer monitoring drop category from the `/etc/what-just-happened/what-just-happened.json` file and reload the `what-just-happened` service.

### Cumulus Linux and Docker

WJH runs in a Docker container. By default, when Docker starts, it creates a bridge called `docker0`. However, for compatibility reasons Cumulus Linux disables the `docker0` bridge in the `/etc/docker/daemon.json` file with the attribute `"bridge: none"`.

### WJH and the NVIDIA NetQ Agent

When you enable the NVIDIA NetQ agent on the switch, the WJH service stops and does not run. If you disable the NVIDIA NetQ service and want to use WJH, run the following commands to enable and start the WJH service:

{{< tabs "TabID14 ">}}
{{< tab "NVUE Commands">}}

```
cumulus@switch:~$ nv set system wjh enable on
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
