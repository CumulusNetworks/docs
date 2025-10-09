---
title: Interface Configuration
author: NVIDIA
weight: 310
product: SONiC
version: 202012
siteSlug: sonic
---

This topic discusses configuring various interfaces:

- Loopback interface
- Management interface
- Network interfaces
- Switch virtual interfaces (SVIs)
- VLAN interfaces
- VRFs

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

You can configure the following settings for the physical interfaces on the switch:

| Option | Description |
| ------ | ----------- |
| fec | Sets the FEC (forward error correction). FEC options include `rs`, `fc` (*fire code*, AKA base-R) or `none`. |
| ip | Adds or removes an IP address for the interface. |
| mtu | Sets the MTU (maximum transmission unit) size for the interface. |
| pfc | Sets the PFC (priority flow control) configuration for the interface. |
| shutdown | Administratively shuts down the interface. |
| speed | Sets the interface port speed. |
| startup | Administratively brings up the interface. |
| transceiver | Enables or disables low power mode for a transceiver. Also can reset the transceiver. |
| vrf | Binds or unbinds the interface to the specified VRF. |

 <!--   breakout - to set interface breakout mode (how now?) -->

### FEC

{{<exlink url="https://en.wikipedia.org/wiki/Forward_error_correction" text="Forward error correction (FEC)">}} is an encoding and decoding layer that enables the switch to detect and correct bit errors introduced over the cable between two interfaces. The target IEEE bit error rate (BER) on high speed ethernet link is 10-12. Because 25G transmission speeds can introduce a higher than acceptable BER on a link, FEC is often required to correct errors to achieve the target BER at 25G, 4x25G, 100G, and higher link speeds. The type and grade of a cable or module and the medium of transmission will determine which FEC setting is needed.

For the link to come up, the two interfaces on each end must use the same FEC setting.

{{%notice note%}}

There is a very small latency overhead required for FEC. For most applications, this small amount of latency is preferable to error packet retransmission latency.

{{%/notice%}}

SONiC supports these FEC types:

- **RS** (Reed Solomon), IEEE 802.3 Clause 108 (CL108) on individual 25G channels and Clause 91 on 100G (4channels). This is the highest FEC algorithm, providing the best bit-error correction. Use the `rs` option to specify Reed Solomon FEC.
- **FC** (Fire Code, also called Base-R or BaseR), IEEE 802.3 Clause 74 (CL74). Base-R provides less protection from bit errors than RS FEC but adds less latency. Use the `fc` option to specify Fire Code FEC.
- **None**. No error correction is done. Use the `none` option to specify no FEC.

{{<tabs "FEC">}}

{{<tab "SONiC CLI">}}

    admin@leaf01:~$ sudo config interface fec Ethernet4 fc

{{</tab>}}

{{<tab "config_db.json">}}

Configure FEC in the PORT table in `/etc/sonic/config_db.json`.

```
admin@switch:~$ sudo vi /etc/sonic/config_db.json

"PORT": {
    "Ethernet4": {
        ...
        "fec": "fc",
        ...
    },
    ...
}
```

{{</tab>}}

{{</tabs>}}

Save your changes to the configuration:

    admin@switch:~$ sudo config save -y

### MTU

The MTU (*maximum transmission unit*) for an interface applies to traffic traversing the management port, front panel or switch ports, bridge, VLAN subinterfaces, and bonds (both physical and logical interfaces).

The default MTU is 9100.

{{<tabs "MTU">}}

{{<tab "SONiC CLI">}}

    admin@leaf01:~$ sudo config interface mtu Ethernet4 1500

{{</tab>}}

{{<tab "config_db.json">}}

Configure MTU in the PORT table in `/etc/sonic/config_db.json`.

```
admin@switch:~$ sudo vi /etc/sonic/config_db.json

"PORT": {
    "Ethernet4": {
        ...
        "mtu": "1500",
        ...
    },
    ...
}
```

{{</tab>}}

{{</tabs>}}

Save your changes to the configuration:

    admin@switch:~$ sudo config save -y

### IP Address

Use the `ip` command option to configure the IP address for an interface, including a physical interface, port channel, VLAN or loopback.

You can specify an IPv4 or IPv6 address.

{{<tabs "IP">}}

{{<tab "SONiC CLI">}}

    admin@leaf01:~$ sudo config interface ip add Ethernet4 10.255.255.4/32
    admin@leaf01:~$ sudo config interface ip add Ethernet4 2001:DB8::4/32

To remove the IP address, use:

    admin@leaf01:~$ sudo config interface ip remove Ethernet4 10.255.255.4/32

{{</tab>}}

{{<tab "config_db.json">}}

Configure the IP address in the INTERFACE table in `/etc/sonic/config_db.json`.

```
admin@switch:~$ sudo vi /etc/sonic/config_db.json

"INTERFACE": {
    "Ethernet4": {},
    ...
    "Ethernet4|10.255.255.4/32": {},
    "Ethernet4|2001:DB8::4/32": {},
    ...
}
```

{{</tab>}}

{{</tabs>}}

Save your changes to the configuration:

    admin@switch:~$ sudo config save -y

### Port Speed

You configure the port speed in terms of Mbps (megabits per second).

To determine the valid port speeds for your switch, run:

    admin@switch:~$ sudo docker exec -it syncd sx_api_ports_dump.py

{{<tabs "Speed">}}

{{<tab "SONiC CLI">}}

    admin@leaf01:~$ sudo config interface speed Ethernet4 10000

{{</tab>}}

{{<tab "config_db.json">}}

Configure port speed in the PORT table in `/etc/sonic/config_db.json`.

```
admin@switch:~$ sudo vi /etc/sonic/config_db.json

"PORT": {
    "Ethernet4": {
        ...
        "speed": "10000", 
        ...
    },
    ...
}
```

{{</tab>}}

{{</tabs>}}

Save your changes to the configuration:

    admin@switch:~$ sudo config save -y

### Breakout Ports

You can configure the physical ports as breakout ports, splitting each physical port into two or four logical ports.

How you break out a port depends on the physical port's speed and what the switch hardware supports. For example, if Ethernet0 is a 100G port, you can break it out as follows:

- 4 25G ports
- 4 10G ports
- 2 50G ports
- 2 40G ports

{{%notice tip%}}

To see how the port can be broken out, press *Tab* twice when you issue the `config interface breakout` command:

```
admin@sonic:~$ sudo config interface breakout Ethernet0 <tab><tab>

1x100G[40G]  2x50G        4x25G[10G]
```

{{%/notice%}}

{{<tabs "Breakout ports">}}

{{<tab "SONiC CLI">}}

To configure a breakout port, run `config interface <port> breakout <options>`. For example, if Ethernet0 is a 100G port and you want to break it out into four 25G ports, run:

    admin@leaf01:~$ sudo config interface Ethernet0 breakout 4X25G

{{</tab>}}

{{<tab "config_db.json">}}

Configure the breakout ports in the PORT table in `/etc/sonic/config_db.json`. For example, if Ethernet0 is a 100G port and you want to break it out into four 25G ports, edit the file as follows:

```
admin@switch:~$ sudo vi /etc/sonic/config_db.json

    "PORT": {
        "Ethernet0": {
            "admin_status": "up",
            "alias": "Ethernet1/1/1",
            "index": "1",
            "lanes": "0",
            "speed": "25000"
        },
        "Ethernet1": {
            "admin_status": "up",
            "alias": "Ethernet1/1/2",
            "index": "1",
            "lanes": "1",
            "speed": "25000"
        },
        "Ethernet2": {
            "admin_status": "up",
            "alias": "Ethernet1/1/3",
            "index": "1",
            "lanes": "2",
            "speed": "25000"
        },
        "Ethernet3": {
            "admin_status": "up",
            "alias": "Ethernet1/1/4",
            "index": "1",
            "lanes": "3",
            "speed": "25000"
        },
```

{{</tab>}}

{{</tabs>}}

Save your changes to the configuration:

    admin@switch:~$ sudo config save -y


### Asymmetric Priority Flow Control

*Priority flow control* (PFC), as defined in the {{<exlink url="http://www.ieee802.org/1/pages/802.1bb.html" text="IEEE 802.1Qbb">}} standard, provides a link-level flow control mechanism that can be controlled independently for each Class of Service (CoS) with the intention to ensure no data frames are lost when congestion occurs in a bridged network.

Asymmetric PFC provides the Ethernet PAUSE functionality in each direction independently on an interface. The configuration for generating and responding to PAUSE messages can be different at both ends of the link.

{{<tabs "PFC">}}

{{<tab "SONiC CLI">}}

To enable asymmetric PFC, run:

    admin@leaf01:~$ sudo config interface pfc asymmetric Ethernet4 on

To disable asymmetric PFC, run:

    admin@leaf01:~$ sudo config interface pfc asymmetric Ethernet4 off

{{</tab>}}

{{<tab "config_db.json">}}

Configure asymmetric PFC in the PORT table in `/etc/sonic/config_db.json`.

```
admin@switch:~$ sudo vi /etc/sonic/config_db.json

"PORT": {
    "Ethernet4": {
        ...
        "pfc_asym": "on",
        ...
    },
    ...
}
```

To disable it, set it to *off*:

```
admin@switch:~$ sudo vi /etc/sonic/config_db.json

"PORT": {
    "Ethernet4": {
        ...
        "pfc_asym": "off",
        ...
    },
    ...
}
```

{{</tab>}}

{{</tabs>}}

Save your changes to the configuration:

    admin@switch:~$ sudo config save -y

### Bind to a VRF

Read the {{<link url="Virtual-Routing-and-Forwarding-VRF" text="VRF">}} topic for information on creating a VRF.

### Administratively Bring a Port Up or Down

The *administrative state* of an interface determines the state of that interface when the switch boots up; the interface can be up or down.

{{<tabs "AdminUpDown">}}

{{<tab "SONiC CLI">}}

To configure an interface to be administratively up, run:

    admin@leaf01:~$ sudo config interface startup Ethernet4

To configure an interface to be administratively down, run:

    admin@leaf01:~$ sudo config interface shutdown Ethernet4

{{</tab>}}

{{<tab "config_db.json">}}

Configure the port's administrative state in the PORT table in `/etc/sonic/config_db.json`. To set the port to always be administratively up, set the `admin_status` to `up`:

```
admin@switch:~$ sudo vi /etc/sonic/config_db.json

"PORT": {
    "Ethernet4": {
        ...
        "admin_status": "up",
        ...
    },
    ...
}
```

To set the port to always be administratively down, so it doesn't come up after a reboot, set the `admin_status` to `down`:

```
admin@switch:~$ sudo vi /etc/sonic/config_db.json

"PORT": {
    "Ethernet4": {
        ...
        "admin_status": "down",
        ...
    },
    ...
}
```

{{</tab>}}

{{</tabs>}}

Save your changes to the configuration:

    admin@switch:~$ sudo config save -y

### Low Power Mode for a Transceiver

If the interface in question is an SFP transceiver, you can enable or disable low power mode for that interface. You can also can reset it.

{{<tabs "transceiver">}}

{{<tab "SONiC CLI">}}

To enable low power mode, run:

    admin@leaf01:~$ sudo config interface transceiver lpmode Ethernet4 enable

To disable low power mode, run:

    admin@leaf01:~$ sudo config interface transceiver lpmode Ethernet4 disable

To reset the transceiver, run:

    admin@leaf01:~$ sudo config interface transceiver reset Ethernet4

{{</tab>}}

{{<tab "config_db.json">}}

Configure low power mode for the port in the PORT table in `/etc/sonic/config_db.json`.

```
admin@switch:~$ sudo vi /etc/sonic/config_db.json

"PORT": {
    "Ethernet4": {
        ...
        "lpmode": "enabled",
        ...
    },

    ...

}
```

To disable low power mode for the port, set `lpmode` to `disabled`:

```
admin@switch:~$ sudo vi /etc/sonic/config_db.json

"PORT": {
    "Ethernet4": {
        ...
        "lpmode": "disabled",
        ...
    },

    ...

}
```

{{</tab>}}

{{</tabs>}}

Save your changes to the configuration:

    admin@switch:~$ sudo config save -y

## Configure SVIs

Read the {{<link url="VLANs">}} topic for information on creating a switch virtual interface.

## Configure VLANs

Read the {{<link url="VLANs">}} topic for information on creating a VLAN interface.
