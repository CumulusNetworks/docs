---
title: Link Layer Discovery Protocol
author: NVIDIA
weight: 400
toc: 3
---
<span class="a-tooltip">[LLDP](## "Link Layer Discovery Protocol")</span> shows information about connected devices.

The `lldpd` daemon implements the IEEE802.1AB LLDP standard and starts at system boot. All `lldpd` command line arguments are in the `/etc/default/lldpd` file.

`lldpd` supports CDP (Cisco Discovery Protocol, v1 and v2) and logs by default into `/var/log/daemon.log` with an `lldpd` prefix.

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

To disable LLDP on a single interface, edit the `/etc/default/lldpd` file. This file specifies the default options to present to the `lldpd` service when it starts. The following example uses the `-I` option to disable LLDP on swp43:

```
cumulus@switch:~$ sudo nano /etc/default/lldpd

# Add "-x" to DAEMON_ARGS to start SNMP subagent
# Enable CDP by default
DAEMON_ARGS="-c -I *,!swp43"
```

Restart the `lldpd` service for the changes to take effect:

```
cumulus@switch:~$ sudo systemctl restart lldpd
```

{{< expand "Runtime Configuration (Advanced) "  >}}

{{%notice warning%}}
A runtime configuration does not persist when you reboot the switch; you lose all changes.
{{%/notice%}}

To configure active interfaces:

```
cumulus@switch:~$ sudo lldpcli configure system interface pattern "swp*"
```

To configure inactive interfaces:

```
cumulus@switch:~$ sudo lldpcli configure system interface pattern *,!eth0,swp*
```

{{%notice note%}}
The active interface list always overrides the inactive interface list.
{{%/notice%}}

To reset any interface list to none:

```
cumulus@switch:~$ sudo lldpcli configure system interface pattern ""
```

{{< /expand >}}

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

### LLDP-MED Inventory TLVs

LLDP-MED Inventory TLVs enable an endpoint to transmit detailed inventory information about itself to the switch, such as the manufacturer, model, firmware, and serial number.

### Application Priority TLVs

| Name           | Description |
|----------------| ----------- |
| Priority | The priority of the configured application. |
| Sel | 2 for applications that use TCP, iSCSI, NVME over TCP with port 4420 or 8009.<br>3 for applications that use UDP. |
| Protocol ID | TCP port or UDP port |

### Transmit IEEE 802.1 TLVs
<!-- vale on -->
You can transmit the 802.1 TLV types (VLAN name, Port VLAN ID, and IEEE 802.1 Link Aggregation) when exchanging LLDP messages. By default, 802.1 TLV transmission is off and the switch sends all LLDP frames without 802.1 TLVs.

To enable 802.1 TLV transmission, run the `nv set service lldp dot1-tlv on` command:

```
cumulus@switch:~$ nv set service lldp dot1-tlv on
cumulus@switch:~$ nv config apply
```

To show if IEEE 802.1 TLV Inventory TLV transmission is on, run the NVUE `nv show service lldp` command:

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

### Transmit QoS TLVs

You can enable QoS TLV transmission (ETS Configuration, ETS Recommendation, PFC Configuration) on an interface. By default, all QoS TLV transmission is off on all interfaces.

{{%notice info%}}
Adding the QoS TLVs to LLDP packets on an interface relies on PFC and ETS configuration from `switchd`. Refer to {{<link url="Quality-of-Service" text="Quality of Service">}} for information on configuring PFC and ETS.

When you enable {{<link url="RDMA-over-Converged-Ethernet-RoCE" text="ROCE">}} on the switch:
- QoS TLV transmission (PFC Configuration, ETS Configuration, and ETS Recommendation) is on globally for all ports, which overrides any QoS TLV transmission setting on a switch port interface.
- LLDP frames for all switch port interfaces carry PFC configuration, ETS configuration, ETS recommendation, and APP Priority TLVs. The ETS configuration and PFC configuration TLV payloads are the same for all interfaces.
{{%/notice%}}

#### Enable QoS TLV Transmission

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

#### Show QoS TLV Transmission Settings

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

### Transmit LLDP-MED Inventory TLVs

<span class="a-tooltip">[LLDP-MED](## "LLDP for Media Endpoint Devices")</span> is an extension to LLDP that operates between endpoint devices, such as IP phones and switches. Inventory management TLV enables an endpoint to transmit detailed inventory information about itself to the switch, such as the manufacturer, model, firmware, and serial number.

To enable LLDP-MED inventory TLVs on the switch, run the `nv set service lldp lldp-med-inventory-tlv on` command:

```
cumulus@switch:~$ nv set service lldp lldp-med-inventory-tlv on
cumulus@switch:~$ nv config apply
```

To show if LLDP-MED Inventory TLV transmission is on, run the NVUE `nv show service lldp` command:

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

### Transmit Application Priority TLVs

You can configure the switch to transmit DCBX application priority TLVs so that the network can receive and queue traffic properly.

Cumulus Linux supports sending application priority TLVs for:
- <span class="a-tooltip">[iSCSI](## "Internet Small Computer System Interface")</span> over TCP port 3260.
- <span class="a-tooltip">[NVMe](## "Non-Volatile Memory Express")</span> over TCP port 4420 or 8009.
- Applications over a specific TCP port or UDP port.

#### Enable Application Priority TLV Transmission

To enable application priority TLV transmission, run NVUE commands to set:
- The application, TCP port, or UDP port and the associated application priority. If you do not set an application priority, Cumulus Linux uses the default priority 0.
- The interface from which you want to transmit application priority TLVs. LLDP starts sending PDUs with the application priority TLVs after you apply the configuration on the specified interface.

{{%notice note%}}
Cumulus Linux does not support application priority TLV transmission on bonds.
{{%/notice%}}

The following example associates application priority 3 with iSCSI, then enables transmission of the application priority TLVs on swp1.

```
cumulus@switch:~$ nv set service lldp application-tlv app iSCSI priority 3
cumulus@switch:~$ nv set interface swp1 lldp application-tlv app iSCSI
cumulus@switch:~$ nv config apply
```

The following example associates application priority 5 with NVMe over TCP port 4420, then enables transmission of the application priority TLVs on swp1.

```
cumulus@switch:~$ nv set service lldp application-tlv tcp-port 4420 priority 5
cumulus@switch:~$ nv set interface swp1 lldp application-tlv tcp-port 4420 
cumulus@switch:~$ nv config apply
```

The following example associates application priority 6 with the application using TCP port 4217, then enables transmission of application priority TLVs on swp1:

```
cumulus@switch:~$ nv set service lldp application-tlv tcp-port 4217 priority 6
cumulus@switch:~$ nv set interface swp1 lldp application-tlv tcp-port 4217
cumulus@switch:~$ nv config apply
```

The following example associates application priority with the application using UDP port 4317, then enables transmission of application priority TLVs on swp1:

```
cumulus@switch:~$ nv set service lldp application-tlv udp-port 4317 priority 4
cumulus@switch:~$ nv set interface swp1 lldp application-tlv udp-port 4317
cumulus@switch:~$ nv config apply
```

The following example associates application priority 0 (the default priority) with iSCSI over TCP port 3260, then enables transmission of application TLVs on swp1.

```
cumulus@switch:~$ nv set interface swp1 lldp application-tlv app iSCSI
cumulus@switch:~$ nv config apply
```

#### Disable Application Priority TLV Transmission

To stop LLDP from sending PDUs with application priority TLVs, unset the interface configuration; for example:

```
cumulus@switch:~$ nv unset interface swp1 lldp application-tlv
```

#### Show Application Priority TLV Settings

To show all the application TLVs configured on an interface:

```
cumulus@switch:~$ nv show interface swp1 lldp application-tlv
              operational          applied   
----------     -----------          --------- 
[udp-port]   933                    933
[udp-port]   8721                   8721
[tcp-port]   1209                   1209
[tcp-port]   5933                   5933
[app]        NVME_4420              NVME_4420 
[app]        iSCSI                  iSCSI    
```

To show the priority mapping for UDP ports:

```
cumulus@switch:~$ nv show service lldp application-tlv udp-port
Port              Priority 
---------- ------------- 
4317              3
```

To show the priority mapping for applications:

```
cumulus@switch:~$ nv show service lldp application-tlv app
AppName           Priority 
--------------- ------------ 
iSCSI           2 
```

To show the priority mapping for TCP ports:

```
cumulus@switch:~$ nv show service lldp application-tlv tcp-port
Port              Priority 
----------- ------------ 
3260                  6
4420                  3
```

To show the UDP port numbers for which application priority TLVs transmit on an interface:

```
cumulus@switch:~$ nv show interface swp1 lldp application-tlv udp-port
Ports             
----
4023
4067
```

To show the application names for which application priority TLVs transmit on an interface:

```
cumulus@switch:~$ nv show interface swp1 lldp application-tlv app
AppName            
------------- 
ISCSI  
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
