---
title: DHCP Snooping
author: NVIDIA
weight: 355
toc: 3
---
DHCP snooping enables Cumulus Linux to act as a middle layer between the DHCP infrastructure and DHCP clients by scanning DHCP control packets and building an IP-MAC database. Cumulus Linux accepts DHCP offers from only trusted interfaces and can rate limit packets.

{{%notice note%}}
DHCP option 82 processing is not supported.
{{%/notice%}}

## Configure DHCP Snooping

To configure DHCP snooping, you need to:

- Enable DHCP snooping on a VLAN.
- Add a trusted interface. Cumulus Linux allows DHCP offers from only trusted interfaces to prevent malicious DHCP servers from assigning IP addresses inside the network. The interface must be a member of the bridge specified.
- Set the rate limit for DHCP requests to avoid DoS attacks. The default value is 100 packets per second.

The following example commands show you how to configure DHCP snooping for IPv4 and IPv6.

{{%notice note%}}
NVUE does not provide commands to configure DHCP Snooping.
{{%/notice%}}

{{< tabs "TabID01 ">}}
{{< tab "IPv4 ">}}

```
cumulus@leaf01:~$ net add bridge br0 dhcp-snoop vlan 100
cumulus@leaf01:~$ net add bridge br0 dhcp-snoop vlan 100 trust swp6
cumulus@leaf01:~$ net add bridge br0 dhcp-snoop vlan 100 rate-limit 50
cumulus@leaf01:~$ net pending
cumulus@leaf01:~$ net commit
```

{{< /tab >}}

{{< tab "IPv6 ">}}

```
cumulus@leaf01:~$ net add bridge br0 dhcp-snoop6 vlan 100
cumulus@leaf01:~$ net add bridge br0 dhcp-snoop6 vlan 100 trust swp6
cumulus@leaf01:~$ net add bridge br0 dhcp-snoop6 vlan 100 rate-limit 50
cumulus@leaf01:~$ net pending
cumulus@leaf01:~$ net commit
```

{{< /tab >}}

{{< /tabs >}}

The NCLU commands save the configuration in the `/etc/dhcpsnoop/dhcp_snoop.json` file. For example:

```
{
  "bridge": [
    {
      "bridge_id": "br0",  <<< Bridge name
      "vlan": [
        {
          "vlan_id": 100,
          "snooping": 1,
          "rate_limit": 50,
          "ip_version": 6,
          "trusted_interface": [
            "swp6"
          ],
        }
      ]
    }
  ]
}
```

To remove all DHCP snooping configuration, run the `net del dhcp-snoop all` command. For example:

```
cumulus@leaf01:~$ net del dhcp-snoop all
cumulus@leaf01:~$ net pending
cumulus@leaf01:~$ net commit
```

When DHCP snooping detects a violation, the packet is dropped and a message is logged to the `/var/log/dhcpsnoop.log` file.

## Show the DHCP Binding Table

To show the DHCP binding table, run the `net show dhcp-snoop table` command for IPv4 or the `net show dhcp-snoop6 table` command for IPv6. The following example command shows the DHCP binding table for IPv4:

```
cumulus@leaf01:~$ net show dhcp-snoop table
Port VLAN IP        MAC               Lease State Bridge
---- ---- --------- ----------------- ----- ----- ------

swp5 1002 10.0.0.3  00:02:00:00:00:04 7200  ACK   br0

swp5 1000 10.0.1.3  00:02:00:00:00:04 7200  ACK   br0
```
