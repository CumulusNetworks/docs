---
title: DHCP Snooping
author: NVIDIA
weight: 355
toc: 3
---
DHCP snooping is a network security feature that prevents unauthorized DHCP servers from assigning IP addresses, protects against DHCP spoofing and IP address conflicts, and enhances overall network security. By ensuring that only trusted DHCP servers can assign IP addresses and maintaining a binding table of IP address to MAC address mappings, DHCP snooping helps safeguard network integrity and reliability.

Cumulus Linux acts as a middle layer between the DHCP infrastructure and DHCP clients by scanning DHCP control packets and building an IP-MAC database. Cumulus Linux accepts DHCP offers from trusted interfaces only.

{{%notice note%}}
- Cumulus Linux does not support DHCP option 82 processing.
- You must add the DHCP snooping VLAN to a bridge.
- DHCP snooping supports single bridge mode only.
{{%/notice%}}

## Configure DHCP Snooping

To configure DHCP snooping:
- Add the DHCP snooping VLAN to a bridge.
- Enable DHCP snooping on the VLAN under the bridge.
- Add a trusted interface. Cumulus Linux allows DHCP offers from only trusted interfaces to prevent malicious DHCP servers from assigning IP addresses inside the network. The interface must be a member of the bridge you specify.

{{< tabs "TabID17 ">}}
{{< tab "NVUE Commands ">}}

The following example enables DHCP snooping on VLAN 10 and sets the trusted interface to swp3. swp3 is a member of the bridge `br_default`:

```
cumulus@switch:~$ nv set bridge domain br_default vlan 10
cumulus@switch:~$ nv set bridge domain br_default dhcp-snoop vlan 10 
cumulus@switch:~$ nv set bridge domain br_default dhcp-snoop vlan 10 trust swp3
cumulus@switch:~$ nv config apply
```

For IPv6, run the `nv set bridge domain <bridge> dhcp-snoop6 vlan <vlan>` command.

To disable DHCP snooping on a VLAN under a bridge, run the `nv unset bridge domain <bridge> dhcp-snoop vlan <vlan>` command for IPv4 or the `nv unset bridge domain <bridge> dhcp-snoop6 vlan <vlan>` command for IPv6.

{{< /tab >}}
{{< tab "Linux Commands ">}}

Create the `/etc/dhcpsnoop/dhcp_snoop.json` file, then add DHCP snooping configuration under the bridge.

The following example enables DHCP snooping for IPv4 on VLAN 10 and sets the trusted interface to swp3. swp3 is a member of the bridge `br_default`:

```
cumulus@switch:~$ sudo nano /etc/dhcpsnoop/dhcp_snoop.json
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

The following example enables DHCP snooping for IPv6 on VLAN 10 and sets the trusted interface to swp6. swp6 is a member of the bridge `br_default`:

```
cumulus@switch:~$ sudo nano /etc/dhcpsnoop/dhcp_snoop.json
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

## Show the DHCP Snooping Table

To show the DHCP snooping table, run the `nv show bridge domain <bridge> dhcp-snoop` command for IPv4 or the `nv show bridge domain <bridge> dhcp-snoop6` command for IPv6.

The following example shows the DHCP snooping table for IPv4:

```
cumulus@switch:~$ nv show bridge domain br_default dhcp-snoop
DHCP Snooping Table
======================
    Vlan  Port  IP           MAC                State  Lease  Bridge    
    ----  ----  -----------  -----------------  -----  -----  ----------
    10    swp1  10.1.10.100  48:b0:2d:fa:6b:a1  ACK    3600   br_default
```

To show the DHCP snooping table for a specific VLAN, run the `nv show bridge domain <bridge> dhcp-snoop vlan <vlan-ID>` command for IPv4 or the `nv show bridge domain <bridge> dhcp-snoop6 vlan <vlan-id>` command for IPv6.

The following example shows the IPv4 DHCP snooping table for VLAN 10:

```
cumulus@switch:~$ nv show bridge domain br_default dhcp-snoop vlan 10
DHCP Snooping Vlan Trust Ports Table
=======================================
    Port 
    -----
    swp51

DHCP Snooping Vlan Bind Table
================================
    Port  IP           MAC                State  Lease  Bridge    
    ----  -----------  -----------------  -----  -----  ----------
    swp1  10.1.10.100  48:b0:2d:fa:6b:a1  ACK    3300   br_default
```

To show trusted port information in the DHCP snooping table, run the `nv show bridge domain <bridge-id> dhcp-snoop trust-ports` command for IPv4 or the `nv show bridge domain <bridge> dhcp-snoop6 trust-ports` command for IPv6.

The following example shows the trusted port information in the IPv4 DHCP snooping table:

```
cumulus@switch:~$ show bridge domain br_default dhcp-snoop trust-ports
Vlan               Ports
----------    --------------------
100           swp1, swp2
200           swp3, swp4
```
