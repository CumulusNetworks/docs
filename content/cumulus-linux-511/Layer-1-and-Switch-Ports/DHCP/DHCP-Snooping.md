---
title: DHCP Snooping
author: NVIDIA
weight: 355
toc: 3
---
DHCP snooping is a network security feature that prevents unauthorized DHCP servers from assigning IP addresses, protects against DHCP spoofing and IP address conflicts, and enhances overall network security. By ensuring that only trusted DHCP servers can assign IP addresses and maintaining a binding table of IP address to MAC address mappings, DHCP snooping helps safeguard network integrity and reliability.

Cumulus Linux acts as a middle layer between the DHCP infrastructure and DHCP clients by scanning DHCP control packets and building an IP-MAC database. Cumulus Linux accepts DHCP offers from only trusted interfaces and can rate limit packets.

When DHCP snooping detects a violation, Cumulus Linux drops the packet and logs a message in the `/var/log/dhcpsnoop.log` file.

{{%notice note%}}
- Cumulus Linux does not support DHCP option 82 processing.
- DHCP snooping support single bridge mode only.
{{%/notice%}}

## Configure DHCP Snooping

To configure DHCP snooping:
- Enable DHCP snooping on a VLAN under a bridge.
- Add a trusted interface. Cumulus Linux allows DHCP offers from only trusted interfaces to prevent malicious DHCP servers from assigning IP addresses inside the network. The interface must be a member of the bridge you specify.

{{< tabs "TabID17 ">}}
{{< tab "NVUE Commands ">}}

The following example enables DHCP snooping on VLAN 10 and the trusted interface to swp3. swp3 is a member of the bridge `br_default`:

```
cumulus@leaf01:~$ nv set bridge domain br_default dhcp-snoop vlan 10 
cumulus@leaf01:~$ nv set bridge domain br_default dhcp-snoop vlan 10 trust swp3
```

{{< /tab >}}
{{< tab "Linux Commands ">}}

Create the `/etc/dhcpsnoop/dhcp_snoop.json` file, then add DHCP snooping configuration under the bridge.

The following example enables DHCP snooping for IPv4 on VLAN 10 and the trusted interface to swp3. swp3 is a member of the bridge `br_default`:

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

The following example enables DHCP snooping for IPv6 on VLAN 10 and the trusted interface to swp6. swp6 is a member of the bridge `br_default`:

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

{{< /tab >}}
{{< /tabs >}}

## Show the DHCP Binding Table

To show the DHCP binding table, run the `nv show bridge domain <bridge> dhcp-snoop` command for IPv4 or the `nv show bridge domain <bridge> dhcp-snoop6` command for IPv6.

The following example command shows the DHCP binding table for IPv4:

```
cumulus@leaf01:~$ nv show bridge domain br_default dhcp-snoop
DHCP Snooping Table 
====================== 
VLAN  Port  IP        MAC                      Lease     State   Bridge 
----  ----  ------    -----------------        -----     -----   ------ 
10    swp3  10.0.0.4  00:02:00:00:00:04        7200      ACK     br_default
      swp6  10.0.0.6  00:02:00:00:00:06        7200      ACK     br_default
```

To show the DHCP binding table for a specific VLAN, run the `nv show bridge domain <bridge> dhcp-snoop vlan <vlan-ID>` command for IPv4 or the `nv show bridge domain <bridge> dhcp-snoop6 vlan <vlan-id>` command for IPv6.

The following example command shows the DHCP binding table for IPv6 for VLAN 10:

```
cumulus@leaf01:~$ nv show bridge domain br_default dhcp-snoop6 vlan 10
DHCP Snooping Vlan Table 
======================== 
Port   IP           MAC                            Lease      State  
----   ------       -----------------              -----      -----     
swp6   128::1/64    00:02:00:00:00:04              7200       ACK 
```

To show information in the DHCP binding table for a specific trusted port, run the `nv show bridge domain <bridge> dhcp-snoop vlan <vlan-ID> trust <interface-id>` command for IPv4 or the `nv show bridge domain <bridge> dhcp-snoop6 vlan <vlan-id> trust <interface-id>` command for IPv6.

The following example command shows information in the DHCP binding table for IPv4 for trusted port swp6:

```
cumulus@leaf01:~$ nv show bridge domain br_default dhcp-snoop vlan 10 trust swp6
DHCP Snooping Table 
====================== 
IP    : 20.0.0.1 
Mac   : 00:02:00:00:00:04 
Lease : 7200    
State : ACK  
```
