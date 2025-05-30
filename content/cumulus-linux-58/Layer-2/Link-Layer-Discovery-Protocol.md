---
title: Link Layer Discovery Protocol
author: NVIDIA
weight: 400
toc: 3
---
<span class="a-tooltip">[LLDP](## "Link Layer Discovery Protocol")</span> shows information about connected devices. The `lldpd` daemon implements the IEEE802.1AB LLDP standard and starts at system boot.

LLDP in Cumulus Linux supports CDP (Cisco Discovery Protocol v1 and v2) and logs by default into `/var/log/daemon.log` with an `lldpd` prefix.

## Configure LLDP Timers

You can configure the frequency of LLDP updates (between 5 and 32768 seconds) and the amount of time (between 1 and 8192 seconds) to hold the information before discarding it. The hold time interval is a multiple of the `tx-interval`.

The following example commands configure the frequency of LLDP updates to 100 and the hold time to 3.

{{< tabs "TabID67 ">}}
{{< tab "NVUE Commands ">}}

```
cumulus@switch:~$ nv set service lldp tx-interval 100
cumulus@switch:~$ nv set service lldp tx-hold-multiplier 3
cumulus@switch:~$ nv config apply
```

{{< /tab >}}
{{< tab "Linux Commands ">}}

Create the `/etc/lldpd.conf` file or create a file in the `/etc/lldpd.d/` directory with a `.conf` suffix and add the timers:

```
cumulus@switch:~$ sudo nano /etc/lldpd.conf
configure lldp tx-interval 100
configure lldp tx-hold 3
...
```

Restart the `lldpd` service for the changes to take effect:

```
cumulus@switch:~$ sudo systemctl restart lldpd
```

{{< /tab >}}
{{< /tabs >}}

## Disable LLDP on an Interface

To disable LLDP on an interface:

{{< tabs "TabID51 ">}}
{{< tab "NVUE Commands ">}}

NVUE does not provide commands to disable LLDP on an interface. However, you can create an NVUE flexible snippet. See {{<link url="NVUE-Snippets/#flexible-snippet-examples" text="Flexible Snippets">}}.

{{< /tab >}}
{{< tab "Linux Commands ">}}

{{< tabs "TabID59 ">}}
{{< tab "Persistent Configuration ">}}

Create the `/etc/lldp.d/lldp-interfaces.conf` file and add the `configure system interface pattern-blacklist` option. The following example disables LLDP on swp1 and swp2:

```
cumulus@leaf01:~$ sudo nano /etc/lldpd.d/lldp-interfaces.conf
configure system interface pattern-blacklist swp1,swp2
```

An alternative method is to use the `system interface pattern` keyword to send LLDP on all interfaces except for swp1 and swp2:

```
cumulus@leaf01:~$ sudo nano /etc/lldpd.d/lldp-interfaces.conf
configure system interface pattern eth*,swp*,!swp1,!swp2
```

Restart the `lldpd` service for the changes to take effect:

```
cumulus@leaf01:~$ sudo systemctl restart lldpd
```

{{< /tab >}}
{{< tab "Runtime Configuration (Advanced)">}}

{{%notice warning%}}
A runtime configuration does not persist when you reboot the switch; you lose all changes.
{{%/notice%}}

To configure active interfaces:

```
cumulus@leaf01:~$ sudo lldpcli configure system interface pattern "swp*"
```

To configure inactive interfaces:

```
cumulus@leaf01:~$ sudo lldpcli configure system interface pattern *,!eth0,swp*
```

{{%notice note%}}
The active interface list always overrides the inactive interface list.
{{%/notice%}}

To reset any interface list to none:

```
cumulus@leaf01:~$ sudo lldpcli configure system interface pattern ""
```

{{< /tab >}}
{{< /tabs >}}

{{< /tab >}}
{{< /tabs >}}

The following example show that swp1 through swp4 are up and advertising LLDP between leaf01 and leaf02:

```
cumulus@leaf01:~$ sudo lldpctl | egrep 'Inter|Port|SysName'
Interface:    eth0, via: LLDP, RID: 1, Time: 1 day, 03:07:48
    SysName:      oob-mgmt-switch
  Port:
    PortID:       ifname swp2
    PortDescr:    swp2
Interface:    swp3, via: LLDP, RID: 2, Time: 0 day, 06:52:48
    SysName:      leaf02
  Port:
    PortID:       ifname swp3
    PortDescr:    swp3
Interface:    swp4, via: LLDP, RID: 2, Time: 0 day, 00:07:38
    SysName:      leaf02
  Port:
    PortID:       ifname swp4
    PortDescr:    swp4
```

The following example shows that after disabling LLDP on swp1 and swp2, only swp3 and swp4 are generating and receiving LLDP on leaf01. leaf02 is only receiving LLDP on swp3 and swp4 from leaf01:

```
cumulus@leaf02:~$ sudo lldpctl | egrep 'Inter|Port|SysName'
Interface:    eth0, via: LLDP, RID: 2, Time: 0 day, 00:09:16
    SysName:      oob-mgmt-switch
  Port:
    PortID:       ifname swp3
    PortDescr:    swp3
Interface:    swp3, via: LLDP, RID: 1, Time: 0 day, 00:08:47
    SysName:      leaf01
  Port:
    PortID:       ifname swp3
    PortDescr:    swp3
Interface:    swp4, via: LLDP, RID: 1, Time: 0 day, 00:09:16
    SysName:      leaf01
  Port:
    PortID:       ifname swp4
    PortDescr:    swp4
```

## SNMP Subagent

The <span class="a-tooltip">[SNMP](## "Simple Network Management Protocol")</span> subagent allows SNMP queries to retrieve LLDP information from the `lldpd` service.

If you enable SNMP with NVUE commands, NVUE enables the SNMP subagent automatically. To disable the SNMP subagent, disable SNMP with the NVUE `nv set service snmp-server enable off` command.

If you use Linux commands to configure the switch, Cumulus Linux does not enable the SNMP subagent by default. To enable the SNMP subagent, edit the `/etc/default/lldpd` file and add the `-x` option:

```
cumulus@switch:~$ sudo nano /etc/default/lldpd

# Add "-x" to DAEMON_ARGS to start SNMP subagent

# Enable CDP by default
DAEMON_ARGS="-c -x -M 4"
```

Restart the `lldpd` service for the changes to take effect:

```
cumulus@switch:~$ sudo systemctl restart lldpd
```

{{%notice note%}}
- The `-c` option enables backwards compatibility with CDP. See {{<link url="#change-cdp-settings" text="Change CDP Settings">}} below.
- The `-M 4` option sends a field in discovery packets to indicate that the switch is a network device.
{{%/notice%}}

## Change CDP Settings

Cumulus Linux provides support for <span class="a-tooltip">[CDP](## "Cisco Discovery Protocol ")</span> so that the switch can advertise information about itself with Cisco routers that do not support LLDP. By default, the Cumulus Linux switch sends CDP packets only if the peer sends CDP packets. You can change this setting by replacing `-c` in the `/etc/default/lldpd` file with one of the following options:

| Option | Description |
|--------|-------------|
| -cc    | The Cumulus Linux switch sends CDPv1 packets even when there is no detected CDP peer. |
| -ccc   | The Cumulus Linux switch sends CDPv2 packets even when there is no detected CDP peer. |
| -cccc  | The Cumulus Linux switch disables CDPv1 and enables CDPv2. |
| -ccccc | The Cumulus Linux switch disables CDPv1 and forces CDPv2. |

The following example changes the CDP setting to `-ccc` so that the switch sends CDPv2 packets even when there is no detected CDP peer:

```
cumulus@switch:~$ sudo nano /etc/default/lldpd
...
# Enable CDP by default
DAEMON_ARGS="-ccc -x -M 4"
```

You must restart the `lldpd` service for the changes to take effect.

```
cumulus@switch:~$ sudo systemctl restart lldpd
```

## Set LLDP Mode

By default, the `lldpd` service sends LLDP frames unless it detects a CDP peer, then it sends CDP frames. You can change this behavior and configure the `lldpd` service to send only CDP frames or only LLDP frames.

{{%notice note%}}
- You configure the `lldpd` service to send only CDP or only LLDP frames globally for all interfaces; you cannot configure these settings for specific interfaces.
- If you configure the `lldpd` service to send only CDP frames (CDPv1 or CDPv2), {{<link url="#lldp-dcbx-tlvs" text="LLDP DCBX TLV transmission for QOS ROCE" >}} is not supported.
{{%/notice%}}

{{< tabs "TabID156 ">}}
{{< tab "NVUE Commands ">}}

To send only CDPv1 frames:

```
cumulus@switch:~$ nv set service lldp mode force-send-cdpv1
cumulus@switch:~$ nv config apply
```

To send only CDPv2 frames:

```
cumulus@switch:~$ nv set service lldp mode force-send-cdpv2
cumulus@switch:~$ nv config apply
```

To send only LLDP frames:

```
cumulus@switch:~$ nv set service lldp mode force-send-lldp
cumulus@switch:~$ nv config apply
```

To reset to the default setting (to send both CDP and LLDP frames):

```
cumulus@switch:~$ nv set service lldp mode default
cumulus@switch:~$ nv config apply
```

{{< /tab >}}
{{< tab "Linux Commands ">}}

Edit the `/etc/default/lldpd` file and add one of the following options to the `DAEMON_ARGS` section:

To send only CDPv1 frames:

```
cumulus@switch:~$ sudo nano /etc/default/lldpd
...
DAEMON_ARGS="-cc -ll -M 4"
```

To send only CDPv2 frames:

```
cumulus@switch:~$ sudo nano /etc/default/lldpd
...
DAEMON_ARGS="-cccc -ll -M 4"
```

To send only LLDP frames:

```
cumulus@switch:~$ sudo nano /etc/default/lldpd
...
DAEMON_ARGS="-l -M 4"
```

To reset to the default setting (to send both CDP and LLDP frames):

```
cumulus@switch:~$ sudo nano /etc/default/lldpd
...
DAEMON_ARGS="-c -M 4"
```

You must restart the `lldpd` service for the changes to take effect.

```
cumulus@switch:~$ sudo systemctl restart lldpd
```

{{< /tab >}}
{{< /tabs >}}

To show the current LLDP mode, run the `nv show service lldp` command. The following example shows that the `lldpd` service sends CDPv2 frames only.

```
cumulus@leaf02:mgmt:~$ nv show service lldp
                    operational       applied
------------------  ----------------  ----------------
dot1-tlv            off               off
mode                force-send-cdpv2  force-send-cdpv2
tx-hold-multiplier  4                 4
tx-interval         30                30
```

## CDP PortID Behavior

LLDP emulates CDP by default on interfaces where it detects a CDP neighbor. CDP only supports the `PortID` value (TLV) in the protocol; however, LLDP has a separate `PortID` and `PortDescription` field.

By default, when the switch sends a CDP packet, if there is an alias (description) on the interface, LLDP sends the alias in the CDP `PortID` field. When an LLDP neighbor receives a CDP packet, the receiving switch displays the CDP Port ID in both the `PortID` and `PortDescription` fields.

If you want LLDP to send the `portID` (`ifname`) value to a CDP neighbor instead of the interface alias, you can configure the following options:
- To transmit both the `PortID` and `PortDescription` in the same `PortID` field, insert the interface name in the interface `alias` field.
- To send the `ifname` instead of the interface alias over CDP, configure the `configure lldp portidsubtype macaddress` option in the `/etc/lldpd.d/lldp_global.conf` file. The default configuration is `portidsubtype ifname`.

The following table shows the TLVs sent for each configuration.

| LLDP Configuration | LLDP PortID Value Sent | LLDP Port Description Value Sent | CDP PortID Value Sent |
| ------------------ | ---------------------- | -------------------------------- | --------------------- |
| `configure lldp portidsubtype ifname` (default)| interface `ifname` | interface `alias` | interface `alias` |
| `configure lldp portidsubtype macaddress` MAC address | interface `mac address` | interface `ifname` | interface `ifname` |

Use CDP only or LLDP only to get the desired behavior of `PortID`, `Description`, or `MacAddress` (LLDP only) across all neighbors. For more information, see {{<link url="#set-lldp-mode" text="LLDP Mode">}}.

## LLDP DCBX TLVs

<span class="a-tooltip">[DCBX](## "Data Center Bridging Capability Exchange protocol ")</span> is an extension of LLDP. Cumulus Linux supports DCBX <span class="a-tooltip">[TLVs](## "Type-Length-Value ")</span> to provide additional information in LLDP packets to peers, such as VLAN information and <span class="a-tooltip">[QoS](## "Quality of Service ")</span>. Adding QoS configuration as part of the DCBX TLVs allows automated configuration on hosts and switches that connect to the switch.

{{%notice info%}}
- Cumulus Linux can send a maximum of 250 VLANS per switch port in one LLDP frame.
- Cumulus Linux does not support CEE DCBX TLVs.
- Cumulus Linux limits DCBX support to enabling DCBX TLVs (either with ROCE global configuration or per interface) as documented in the {{<exlink url="https://ieeexplore.ieee.org/document/8403927" text="IEEE 802.1Q standard">}}.
{{%/notice%}}

Cumulus Linux supports the following TLVs:
<!-- vale off -->
### IEEE 802.1 TLVs
<!-- vale on -->
| Name             | Subtype | Description |
|----------------- | ------- | ----------- |
| Port VLAN ID     | 1       | The port VLAN identifier. |
| VLAN Name        | 3       | The name of any VLAN to which the port belongs. |
| Link Aggregation | 7       | Indicates if the port supports link aggregation and if it is on. |

### QoS TLVs

| Name               | Subtype | Description |
|------------------- | ------- | ----------- |
| ETS Configuration  | 9       | The <span class="a-tooltip">[ETS](## "Enhanced Transmission Selection ")</span> configuration settings on the switch.|
| ETS Recommendation | A       | The recommended <span class="a-tooltip">[ETS](## "Enhanced Transmission Selection ")</span> settings that the switch wants the connected peer interface to use. |
| PFC Configuration  | B       | The <span class="a-tooltip">[PFC](## "Priority-based Flow Control ")</span> configuration settings on the switch. |
<!-- vale off -->
### IEEE 802.3 TLVs
<!-- vale on -->
Cumulus Linux transmits the following 802.3 TLVs by default. You do not need to enable them.

| Name                | Subtype | Description |
|-------------------- | ------- | ----------- |
| Link Aggregation    | 3       | Indicates if the port supports link aggregation and if it is on.  |
| Maximum Frame Size  | 4       | The MTU configuration on the port. The MTU on the port is the <span class="a-tooltip">[MFS](## "Maximum Frame Size ")</span>. |
<!-- vale off -->
### Transmit IEEE 802.1 TLVs
<!-- vale on -->
You can transmit the 802.1 TLV types (VLAN name, Port VLAN ID, and IEEE 802.1 Link Aggregation) when exchanging LLDP messages. By default, 802.1 TLV transmission is off and the switch sends all LLDP frames without 802.1 TLVs.

To enable 802.1 TLV transmission, run the `nv set service lldp dot1-tlv on` command:

```
cumulus@switch:~$ nv set service lldp dot1-tlv on
cumulus@switch:~$ nv config apply
```

### Transmit QoS TLVs

You can enable QoS TLV transmission (ETS Configuration, ETS Recommendation, PFC Configuration) on an interface. By default, all QoS TLV transmission is off on all interfaces.

{{%notice info%}}
Adding the QoS TLVs to LLDP packets on an interface relies on PFC and ETS configuration from `switchd`. Refer to {{<link url="Quality-of-Service" text="Quality of Service">}} for information on configuring PFC and ETS.

When you enable {{<link url="RDMA-over-Converged-Ethernet-RoCE" text="ROCE">}} on the switch:
- QoS TLV transmission (PFC Configuration, ETS Configuration, and ETS Recommendation) is on globally for all ports, which overrides any QoS TLV transmission setting on a switch port interface.
- LLDP frames for all switch port interfaces carry PFC configuration, ETS configuration, ETS recommendation, and APP Priority TLVs. The ETS configuration and PFC configuration TLV payloads are the same for all interfaces.
{{%/notice%}}

To enable PFC Configuration TLV transmission, run the `nv set interface <interface> lldp dcbx-pfc-tlv on` command:

```
cumulus@switch:~$ nv set interface swp1 lldp dcbx-pfc-tlv on
cumulus@switch:~$ nv config apply
```

To enable ETS Configuration TLV transmission, run the `nv set interface <interface> lldp dcbx-ets-config-tlv on` command:

```
cumulus@switch:~$ nv set interface swp1 lldp dcbx-ets-config-tlv on
cumulus@switch:~$ nv config apply 
```

To enable ETS Recommendation TLV transmission, run the `nv set interface <interface> lldp dcbx-ets-recomm-tlv on` command:

```
cumulus@switch:~$ nv set interface swp1 lldp dcbx-ets-recomm-tlv on
cumulus@switch:~$ nv config apply
```

{{%notice note%}}
The interface must be a physical interface; you cannot enable TLVs on bonds.  
{{%/notice%}}

### Transmit LLDP-MED Inventory TLVs

<span class="a-tooltip">[LLDP-MED](## "LLDP for Media Endpoint Devices")</span> is an extension to LLDP that operates between endpoint devices, such as IP phones and switches. Inventory management TLV enables an endpoint to transmit detailed inventory information about itself to the switch, such as the manufacturer, model, firmware, and serial number.

To enable LLDP-MED inventory TLVs on the switch, run the `nv set service lldp lldp-med-inventory-tlv on` command:

```
cumulus@switch:~$ nv set service lldp lldp-med-inventory-tlv on
cumulus@switch:~$ nv config apply
```

### Show DCBX TLV Settings

To show if IEEE 802.1 TLV or LLDP-MED Inventory TLV transmission is on, run the NVUE `nv show service lldp` command:

```
cumulus@leaf01:mgmt:~$ nv show service lldp
                        operational  applied
----------------------  -----------  -------
tx-interval             30           30     
tx-hold-multiplier      4            4      
dot1-tlv                off          off    
lldp-med-inventory-tlv  on           on     
mode                    default      default
```

To show if Qos TLV transmission is on for an interface, run the NVUE `nv show interface <interface>` command:

```
cumulus@leaf01:mgmt:~$ nv show interface swp1
                          operational        applied      description
------------------------  -----------------  -----------  ---------------------------------------------------
...
lldp
  dcbx-ets-config-tlv                        on           DCBX ETS config TLV flag
  dcbx-ets-recomm-tlv                        off          DCBX ETS recommendation TLV flag
  dcbx-pfc-tlv                               on           DCBX PFC TLV flag
... 
```

## Troubleshooting

You can use the `lldpcli` tool to query the `lldpd` daemon for neighbors, statistics, and other running configuration information. See `man lldpcli(8)` for details.

To show all neighbors on all ports and interfaces:

```
cumulus@switch:~$ sudo lldpcli show neighbors
-------------------------------------------------------------------------------
LLDP neighbors:
-------------------------------------------------------------------------------
Interface:    eth0, via: LLDP, RID: 1, Time: 0 day, 17:38:08
  Chassis:
    ChassisID:    mac 08:9e:01:e9:66:5a
    SysName:      PIONEERMS22
    SysDescr:     Cumulus Linux version 4.1.0 running on quanta lb9
    MgmtIP:       192.168.0.22
    Capability:   Bridge, on
    Capability:   Router, on
  Port:
    PortID:       ifname swp47
    PortDescr:    swp47
-------------------------------------------------------------------------------
Interface:    swp1, via: LLDP, RID: 10, Time: 0 day, 17:08:27
  Chassis:
    ChassisID:    mac 00:01:00:00:09:00
    SysName:      MSP-1
    SysDescr:     Cumulus Linux version 4.1.0 running on QEMU Standard PC (i440FX + PIIX, 1996)
    MgmtIP:       192.0.2.9
    MgmtIP:       fe80::201:ff:fe00:900
    Capability:   Bridge, off
    Capability:   Router, on
  Port:
    PortID:       ifname swp1
    PortDescr:    swp1
-------------------------------------------------------------------------------
Interface:    swp2, via: LLDP, RID: 10, Time: 0 day, 17:08:27
  Chassis:
    ChassisID:    mac 00:01:00:00:09:00
    SysName:      MSP-1
    SysDescr:     Cumulus Linux version 4.1.0 running on QEMU Standard PC (i440FX + PIIX, 1996)
    MgmtIP:       192.0.2.9
    MgmtIP:       fe80::201:ff:fe00:900
    Capability:   Bridge, off
    Capability:   Router, on
  Port:
    PortID:       ifname swp2
    PortDescr:    swp2
-------------------------------------------------------------------------------
Interface:    swp3, via: LLDP, RID: 11, Time: 0 day, 17:08:27
  Chassis:
    ChassisID:    mac 00:01:00:00:0a:00
    SysName:      MSP-2
    SysDescr:     Cumulus Linux version 4.1.0 running on QEMU Standard PC (i440FX + PIIX, 1996)
    MgmtIP:       192.0.2.10
    MgmtIP:       fe80::201:ff:fe00:a00
    Capability:   Bridge, off
    Capability:   Router, on
  Port:
    PortID:       ifname swp1
    PortDescr:    swp1
...
```

To show `lldpd` statistics for all ports:

```
cumulus@switch:~$ sudo lldpcli show statistics
----------------------------------------------------------------------
LLDP statistics:
----------------------------------------------------------------------
Interface:    eth0
  Transmitted:  9423
  Received:     17634
  Discarded:    0
  Unrecognized: 0
  Ageout:       10
  Inserted:     20
  Deleted:      10
--------------------------------------------------------------------
Interface:    swp1
  Transmitted:  9423
  Received:     6264
  Discarded:    0
  Unrecognized: 0
  Ageout:       0
  Inserted:     2
  Deleted:      0
---------------------------------------------------------------------
Interface:    swp2
  Transmitted:  9423
  Received:     6264
  Discarded:    0
  Unrecognized: 0
  Ageout:       0
  Inserted:     2
  Deleted:      0
---------------------------------------------------------------------
Interface:    swp3
  Transmitted:  9423
  Received:     6265
  Discarded:    0
  Unrecognized: 0
  Ageout:       0
  Inserted:     2
  Deleted:      0
----------------------------------------------------------------------
...
```

To show a summary of `lldpd` statistics for all ports:

```
cumulus@switch:~$ sudo lldpcli show statistics summary
---------------------------------------------------------------------
LLDP Global statistics:
---------------------------------------------------------------------
Summary of stats:
  Transmitted:  648186
  Received:     437557
  Discarded:    0
  Unrecognized: 0
  Ageout:       10
  Inserted:     38
  Deleted:      10
```

To show the running LLDP configuration:

```
cumulus@switch:~$ sudo lldpcli show running-configuration
--------------------------------------------------------------------
Global configuration:
--------------------------------------------------------------------
Configuration:
  Transmit delay: 30
  Transmit hold: 4
  Receive mode: no
  Pattern for management addresses: (none)
  Interface pattern: (none)
  Interface pattern blacklist: (none)
  Interface pattern for chassis ID: (none)
  Override description with: (none)
  Override platform with: Linux
  Override system name with: (none)
  Advertise version: yes
  Update interface descriptions: no
  Promiscuous mode on managed interfaces: no
  Disable LLDP-MED inventory: yes
  LLDP-MED fast start mechanism: yes
  LLDP-MED fast start interval: 1
  Source MAC for LLDP frames on bond slaves: local
  Portid TLV Subtype for lldp frames: ifname
--------------------------------------------------------------------
```

## Considerations

- Cumulus Linux does not support LLDP Annex E (and Annex D).
- If you configure both an eth0 IP address and a loopback IP address on the switch, LLDP advertises the loopback IP address as the management IP address. In this case, the Cumulus Linux switch behaves more like a typical Linux host than a networking appliance.

## Related Information

- {{<exlink url="http://vincentbernat.github.io/lldpd/" text="GitHub - lldpd project">}}
- {{<exlink url="http://en.wikipedia.org/wiki/Link_Layer_Discovery_Protocol" text="Wikipedia - Link Layer Discovery Protocol">}}
