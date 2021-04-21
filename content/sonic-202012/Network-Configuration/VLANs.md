---
title: VLANs
author: NVIDIA
weight: 420
product: SONiC
version: 202012
siteSlug: sonic
---

A *VLAN* (virtual local area network) is a logical interface that enables hosts to communicate through layer 2 by connecting any physical and logical interface that is a member of the VLAN into a single layer 2 domain.

{{<tabs "VLANs">}}

{{<tab "SONiC CLI">}}

Create Vlan100 and add physical interfaces Ethernet8 and Ethernet12 as members:

    admin@switch:~$ sudo config vlan add 100
    admin@switch:~$ sudo config vlan member add 100 Ethernet8
    admin@switch:~$ sudo config vlan member add 100 Ethernet12

If you are not tagging the VLAN members, use the `-u` option when adding a member to the VLAN:

    admin@switch:~$ sudo config vlan member add -u 100 Ethernet4

{{</tab>}}

{{<tab "config_db.json">}}

Create Vlan100 and add physical interfaces Ethernet8 and Ethernet12 as members. Configure the VLAN in the VLAN, VLAN_INTERFACE and VLAN_MEMBER tables in `/etc/sonic/config_db.json`. If you are not tagging the VLAN members, specify *untagged* for `tagging_mode`.

```
admin@switch:~$ sudo vi /etc/sonic/config_db.json

      "VLAN": {
        "Vlan100": {
            "members": [
                "Ethernet8",
                "Ethernet12"
            ],
            "vlanid": "100"
        },
    },
    "VLAN_INTERFACE": {
        "Vlan100": {},
        "Vlan100|10.0.100.1/24": {}
    },
    "VLAN_MEMBER": {
        "Vlan100|Ethernet8": {
            "tagging_mode": "tagged"
        },
        "Vlan100|Ethernet12": {
            "tagging_mode": "untagged"
        },
    }
```

{{</tab>}}

{{</tabs>}}

Save your changes to the configuration:

    admin@switch:~$ sudo config save -y

### DHCP Relays

You can add one or more DHCP relay destination IP addresses to a VLAN.

{{<tabs "DHCPrelay">}}

{{<tab "SONiC CLI">}}

    admin@leaf01:~$ sudo config vlan dhcp_relay add 100 10.0.100.1
    Added DHCP relay destination address 10.0.100.1 to Vlan100
    Restarting DHCP relay service...

{{</tab>}}

{{<tab "config_db.json">}}

Configure the DHCP relay in the VLAN table in `/etc/sonic/config_db.json`.

```
admin@switch:~$ sudo vi /etc/sonic/config_db.json
    "VLAN": {
        "Vlan100": {
            "dhcp_servers": [
                "10.0.100.1"
            ],
            "members": [
                "Ethernet8",
                "Ethernet12"
            ],
            "vlanid": "100"
        },
```

{{</tab>}}

{{</tabs>}}

Save your changes to the configuration:

    admin@switch:~$ sudo config save -y

## Configure SVIs

A *switch virtual interface* is a layer 3 interface that serves to route traffic from a switch on one VLAN to another switch on another VLAN.

Bridges can be included as part of a routing topology after being assigned an IP address. This enables hosts within the bridge to communicate with other hosts outside of the bridge through a switch virtual interface (SVI), which provides layer 3 routing. The IP address of the bridge is typically from the same subnet as the member hosts of the bridge.

{{<tabs "SVI">}}

{{<tab "SONiC CLI">}}

Configure the SVI using the `config interface ip add` command (not the config vlan command)

    admin@switch:~$ sudo config interface ip add Vlan100 10.0.100.1/24

{{</tab>}}

{{<tab "config_db.json">}}

Configure the SVI in the VLAN_INTERFACE tables in `/etc/sonic/config_db.json`.

```
admin@switch:~$ sudo vi /etc/sonic/config_db.json
    ...
    "VLAN_INTERFACE": {
        "Vlan100": {},
        "Vlan100|10.0.100.1/24": {}
    },
    ...
```

{{</tab>}}

{{</tabs>}}

Save your changes to the configuration:

    admin@switch:~$ sudo config save -y

<!-- 
{{<tabs "TITLE">}}

{{<tab "SONiC CLI">}}


{{</tab>}}

{{<tab "config_db.json">}}

```
admin@switch:~$ sudo vi /etc/sonic/config_db.json

```

{{</tab>}}

{{</tabs>}}

Save your changes to the configuration:

    admin@switch:~$ sudo config save -y

-->


