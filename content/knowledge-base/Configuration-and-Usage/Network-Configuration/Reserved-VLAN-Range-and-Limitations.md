---
title: Reserved VLAN Range and Limitations
author: NVIDIA
weight: 394
toc: 4
---
Cumulus reserves a single contiguous set of VLAN IDs (the reserved VLAN range) for internal data plane operations. If you configure VLAN IDs that are within the reserved VLAN range, a scenario called *reserved VLAN overlap* occurs, which can result in unexpected traffic patterns.

To prevent a reserved VLAN overlap, you might need to change the reserved VLAN range.

{{%notice note%}}
Use caution when configuring VLANs; Cumulus Linux does not prevent reserved VLAN overlap.
{{%/notice%}}

## Reserved VLAN Count

The minimum number of VLAN IDs required in the reserved VLAN range depends on the Cumulus Linux version and the feature you configure. You might need to change the reserved VLAN range to increase the number of VLANs reserved for certain features.

{{%notice note%}}
- The reserved VLAN range is a single contiguous set of VLAN IDs that you cannot use when configuring the switch.
- NVIDIA does not recommend you change the number of reserved VLANs unless absolutely necessary.
- Do not reduce the number of VLANs below the defaults.
- The reserved VLAN range requirements, based on your platform, Cumulus Linux release and configuration, must not exceed the total count of reserved VLANs configured. The {{<link url="#default-reserved-VLAN-ranges" text="table">}} below shows the default range for each Cumulus Linux release.
- Use caution when changing the number of reserved VLANs: Cumulus Linux does not prevent you from configuring features that might exceed the number of reserved VLANs.
- Changing the reserved VLAN range requires a `switchd` restart.

{{%/notice%}}

## Default Reserved VLAN Ranges

| Version | Default Range | Default Reserved Count |
| ------- | ------------- | ---------------------- |
| 5.x     | 3725-3999     | 275  |
| 4.4.x   | 3725-3999     | 275  |
| 4.3.x   | 3600-3999     | 400  |

## Determine the Reserved VLAN Range

- NVIDIA Spectrum switches running Cumulus Linux 5.0 and later require a reserved VLAN for every bridge and QinQ bridge, plus 2.
- NVIDIA Spectrum switches running Cumulus Linux 4.4 and earlier require a reserved VLAN for every bridge, physical interface, layer 3 sub interface, and QinQ bridge, plus 1.
- Broadcom switches running Cumulus Linux 4.3 and earlier require a reserved VLAN for every bridge, physical interface, layer 3 sub interface, and QinQ bridge, plus 1.

The example below provides Linux-type shell commands to help you determine the in-use and configured VLAN counts and values. These commands are only a guide. Follow the guidelines below to determine how to best calculate the values.

1. If your switch is running Cumulus Linux 5.0 or later, go to step 2. If your switch is running Cumulus Linux 4.4 or earlier, determine the total number of physical interfaces that your platform supports. For example, the NVIDIA SN2700 switch has a total of 32 QSFP ports that you can break out into 2x or 4x.

   At the maximum breakout (4x), there are 128 physical ports. Cumulus Linux **always** uses this number of reserved VLANs regardless of configuration:
   - 32 x 1 = 32 Reserved VLAN IDs on the switch with no breakout
   - 32 x 2 = 64 Reserved VLAN IDs on the switch with all ports broken out in 2x mode
   - 16 x 4 = 64 Reserved VLAN IDs on the switch with all ports broken out in 4x mode

2. Determine the total number of bridges in the configuration. The example below uses the `bridge-ports` statement as a counting key.

```
cumulus@switch:~$ sudo cat /etc/network/interfaces | grep "bridge-ports" | wc -l
cumulus@switch:~$ sudo cat /etc/network/interfaces.d/*.intf | grep "bridge-ports" | wc -l
cumulus@switch:~$ sudo cat /etc/network/interfaces | grep "bridge-ports" | wc -l
cumulus@switch:~$ sudo cat /etc/network/interfaces.d/*.intf | grep "bridge-ports" | wc -l
```

3. If you use double-tagged Q-in-Q, determine the total number of implicit bridges not defined in the configuration. The example below uses a unique interfaces+inner tag (swpX.Y) as a counting key.

```
cumulus@switch:~$ sudo grep -o -h "iface swp.*\.[[:digit:]]*\." /etc/network/interfaces | sort -u | wc -l
cumulus@switch:~$ sudo grep -o -h "iface swp.*\.[[:digit:]]*\." /etc/network/interfaces.d/*.intf | sort -u | wc -l
```

4. If your switch is running Cumulus Linux 5.0 or later, go to step 5. If your switch is running Cumulus Linux 4.4 or earlier, determine the total number of layer 3 sub interfaces in the configuration. The example below uses the `vlan-raw-device` statement as a counting key.

```
cumulus@switch:~$ sudo cat /etc/network/interfaces | grep "vlan-raw-device" | wc -l
cumulus@switch:~$ sudo cat /etc/network/interfaces.d/*.intf | grep "vlan-raw-device" | wc -l
```

5. Add the totals from step 1 through step 4.
   - For NVIDIA Spectrum switches running 5.0 and later: Bridges + (implied QinQ bridges) + 2 = MINIMUM for configuration.
   - For NVIDIA Spectrum switches running 4.4 and earlier: Interfaces + bridges + (implied QinQ bridges) + layer 3 sub interfaces + 1 = MINIMUM for configuration.
   - For Broadcom switches running 4.3 and earlier: Interfaces + bridges + (implied QinQ bridges) + layer 3 sub interfaces + 1 = MINIMUM for configuration.

Never exceed this count, even temporarily, so that you have room for future expansion, in-process operations, and automation. For example, an automation system can modify a bridge by adding, then removing the old bridge. Cumulus does not guarantee minimal usage of reserved VLANs when doing multi-step operations.

6. Select a contiguous range of VLANs that covers the desired count from step 5 and does not overlap with VLAN IDs in the configuration. The example below determines which VLAN IDs are in the configuration:

```
cumulus@switch:~$ grep -h "iface swp" /etc/network/interfaces | grep -iv "\#" | cut -s -d '.' -f 2- | tr '.' '\n' | sort -u | sort -n
cumulus@switch:~$ grep -h "iface swp" /etc/network/interfaces.d/*.intf | grep -iv "\#" | cut -s -d '.' -f 2- | tr '.' '\n' | sort -u | sort -n
```

## Change the Reserved VLAN Range

To change the reserved VLAN range, run the commands below.
- For Cumulus Linux 5.3 and later, you can run NVUE or Linux commands.
- For Cumulus Linux 5.2 and earlier, you must run Linux commands.

The following example changes the reserved VLAN range to be between 4064 and 4094.

{{< tabs "TabID177 ">}}
{{< tab "NVUE Commands ">}}

```
cumulus@switch:~$ nv set system global reserved vlan internal range 4064-4094
cumulus@switch:~$ nv config apply
```

NVUE restarts the `switchd` service.

{{< /tab >}}
{{< tab "Linux Commands ">}}

1. Edit the `/etc/cumulus/switchd.conf` file to uncomment the `resv_vlan_range` line and specify a new range.

   ```
   cumulus@switch:~$ sudo nano /etc/cumulus/switchd.conf
   ...
   # global reserved vlan internal range
   resv_vlan_range = 4064-4094
   ```

2. After you save the file, you must restart `switchd`:

   ```
   cumulus@switch:~$ sudo systemctl restart switchd.service
   ```

{{< /tab >}}
{{< /tabs >}}
