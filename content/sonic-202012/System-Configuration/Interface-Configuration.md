---
title: Interface Configuration
author: Cumulus Networks
weight: 310
product: SONiC
version: 201911_MUR5
siteSlug: sonic
---

This topic discusses configuring various interfaces:

- Loopback interface
- Management interface
- Network interfaces
- VLAN interfaces

## Configure the Loopback Interface

Like other network operating systems, SONiC includes a loopback interface for traffic that originates and terminates on the same switch.

{{<tabs "Loopback Interface">}}

The following example configures the IP address and subnet for Loopback0:

{{<tab "SONiC CLI">}}

```
admin@switch:~$ sudo config interface ip add Loopback0 10.255.255.1/32
```

{{</tab>}}

{{<tab "config_db.json">}}

Configure the loopback in the LOOPBACK_INTERFACE table in `/etc/sonic/config_db.json`.

```
admin@switch:~$ sudo vi /etc/sonic/config_db.json

{
"LOOPBACK_INTERFACE": {
        "Loopback0": {},
        "Loopback0|10.255.255.1/32": {}
    }
}
```

{{</tab>}}

{{</tabs>}}

Save your changes to the configuration:

    admin@switch:~$ sudo config save -y

## Configure the Management Interface

The management interface (eth0) in SONiC is configured by default to use the DHCP client to get the IP address from the DHCP server. Connect the management interface to the same network in which your DHCP server is connected and get the IP address from DHCP server. The IP address received from DHCP server can be verified using the /sbin/ifconfig eth0 Linux command.

{{<tabs "Management Interface">}}

{{<tab "SONiC CLI">}}

SONiC does not provide a CLI to configure the static IP for the management interface. To configure a static IP address for the management interface, use the `config_db.json` file and reload the configuration.

{{</tab>}}

{{<tab "config_db.json">}}

Configure the management interface (eth0) in the MGMT_INTERFACE table in `/etc/sonic/config_db.json`.

The management interface can be configured with either or both of these attributes:

| Attribute | Description |
| --------- | ----------- |
| gwaddr | The gateway address of the prefix. |
| forced_mgmt_routes | Traffic sent to the addresses and prefixes specified here are forced to go through management network instead of data network. |

```
admin@switch:~$ sudo vi /etc/sonic/config_db.json

{
"MGMT_INTERFACE": {
        "eth0|10.11.150.11/16": {
        "gwaddr": "10.11.0.1"
    },
    "eth0|FC00:2::32/64": {
        "forced_mgmt_routes": [
            "10.0.0.100/31",
            "10.255.0.8",
                "10.255.0.0/28"
        ],
        "gwaddr": "2001:DB8::1"
    }
  }
}
```

{{</tab>}}

{{</tabs>}}

Save your changes to the configuration:

    admin@switch:~$ sudo config save -y

## Configure Network Interfaces


{{<tabs "Network Interfaces">}}

Configure the network interfaces in the INTERFACE table in `/etc/sonic/config_db.json`.

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

## Configure VLANs

Configure the VLAN interfaces in the VLAN_INTERFACE table in `/etc/sonic/config_db.json`.

{{<tabs "VLANs">}}

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

{{<tabs "TITLE">}}

{{<tab "SONiC CLI">}}


{{</tab>}}

{{<tab "config_db.json">}}

```
admin@switch:~$ sudo vi /etc/sonic/config_db.json

```

{{</tab>}}

{{</tabs>}}
