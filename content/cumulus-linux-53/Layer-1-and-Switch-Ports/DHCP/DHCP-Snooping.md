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

The following example shows you how to configure DHCP snooping for IPv4 and IPv6.

{{%notice note%}}
NVUE does not provide commands to configure DHCP Snooping.
{{%/notice%}}

Create the `/etc/dhcpsnoop/dhcp_snoop.json` file and add DHCP snooping configuration under the bridge.

The following example enables DHCP snooping for IPv4 on VLAN 10, sets the rate limit to 50 and the trusted interface to swp3. swp3 is a member of the bridge `br_default`:

```
cumulus@leaf01:~$ sudo nano /etc/dhcpsnoop/dhcp_snoop.json
{
  "bridge": [
    {
      "bridge_id": "br_default",
      "vlan": [
        {
          "vlan_id": 10,
          "snooping": 1,
          "rate_limit": 50,
          "ip_version": 4,
          "trusted_interface": [
            "swp3"
          ],
        }
      ]
    }
  ]
}
```

The following example enables DHCP snooping for IPv6 on VLAN 10, sets the rate limit to 50 and the trusted interface to swp6. swp6 is a member of the bridge `br_default`:

```
cumulus@leaf01:~$ sudo nano /etc/dhcpsnoop/dhcp_snoop.json
{
  "bridge": [
    {
      "bridge_id": "br_default",
      "vlan": [
        {
          "vlan_id": 10,
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
