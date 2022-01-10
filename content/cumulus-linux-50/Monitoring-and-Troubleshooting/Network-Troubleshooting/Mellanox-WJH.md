---
title: What Just Happened (WJH)
author: NVIDIA
weight: 1130
toc: 4
---
*What Just Happened* (WJH) provides real time visibility into network problems and has two components:
- Cumulus Linux includes the WJH agent by default so that you can stream detailed and contextual telemetry for off-switch analysis with tools, such as [NVIDIA NetQ]({{<ref "/cumulus-netq-41" >}}). 
- Cumulus Linux includes the WJH service so that you can diagnose network problems by looking at dropped packets. WJH shows layer 1, layer 2, layer 3, buffer, tunnel, and ACL related issues.

## Enable the WJH Service

WJH is disabled by default. To enable the WJH service:

```
cumulus@switch:~$ sudo systemctl start what-just-happened
```

## Configure WJH

By default, WJH shows all layer 1, layer 2, layer 3, buffer, tunnel, and ACL related issues. You can configure WJH to show specific types of dropped packets only.

Edit the `/etc/what-just-happened/what-just-happened.json` file and remove the drop category value from inside the square brackets ([]). You must restart the WJH service after you edit the file.

The following example configures WJH to not show layer 1 and buffer packet drops:

```
root@switch:~# sudo nano /etc/what-just-happened/what-just-happened.json
{
  "what-just-happened": {
    "channels": {
      "forwarding": {
        "drop_category_list": ["L2", "L3", "tunnel"]
      },
      "layer-1": {
        "drop_category_list": []
      },
      "buffer": {
        "drop_category_list": []
      },
      "tunnel": {
        "drop_category_list": ["tunnel"]
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

## Run WJH Commands

After you start the WJH service, you can run the following commands from the command line.

| <div style="width:450px">Command  | Description |
| -------  | ----------- |
| `what-just-happened poll` | Shows information about all dropped packets. The output includes the reason for the drop and the recommended action to take. |
| `what-just-happened poll forwarding` | Shows information about dropped packets due to forwarding-related issues (layer 2, layer 3, and tunnel). The output includes the reason for the drop and the recommended action to take.  |
| `what-just-happened poll --aggregate` | Shows information about dropped packets aggregated by the reason for the drop. This command also shows the number of times the dropped packet occurs. |
| `what-just-happened poll forwarding --aggregate` | Shows information about dropped packets due to forwarding-related issues (layer 2, layer 3, and tunnel) aggregated by the reason for the drop. This command also shows the number of times the dropped packet occurs. |
| `what-just-happened poll --export` | Saves information about dropped packets in a file in PCAP format. |
| `what-just-happened poll forwarding --export` | Saves information about dropped packets due to forwarding-related issues (layer 2, layer 3, and tunnel) in a file in PCAP format. |
| `what-just-happened poll --export --no_metadata` | Saves information about dropped packets in a file in PCAP format without metadata. |
| `what-just-happened poll forwarding --export --no_metadata` | Saves information about dropped packets due to forwarding-related issues (layer 2, layer 3, and tunnel) in a file in PCAP format without metadata.|
| `what-just-happened dump` | Displays all diagnostic information on the command line. |

Run the `what-just-happened -h` command to see all the WJH command options.

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
