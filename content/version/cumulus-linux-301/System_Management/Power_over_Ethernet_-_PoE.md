---
title: Power over Ethernet - PoE
author: Cumulus Networks
weight: 67
aliases:
 - /display/CL30/Power+over+Ethernet+-+PoE
 - /pages/viewpage.action?pageId=5118226
pageID: 5118226
product: Cumulus Linux
version: '3.0'
imgData: cumulus-linux-301
siteSlug: cumulus-linux-301
---
Cumulus Linux supports Power over Ethernet (PoE), so certain Cumulus
Linux switches can supply power from Ethernet switch ports to enabled
devices over the Ethernet cables that connect them.

The [currently supported platform](http://cumulusnetworks.com/hcl/)
includes:

  - Accton AS4610-54P, which supports PoE and PoE+ (an [early access
    feature](https://support.cumulusnetworks.com/hc/en-us/articles/202933878))
    and configuration over Ethernet layer 2 LLDP for power negotiation

## <span>How It Works</span>

When a powered device is connected to the switch via an Ethernet cable:

  - If the available power is greater than the power required by the
    connected device, power is supplied to the switch port, and the
    device powers on

  - If available power is less than the power required by the connected
    device and the switch port's priority is less than the port priority
    set on all powered ports, power is **not** supplied to the port

  - If available power is less than the power required by the connected
    device and the switch port's priority is greater than the priority
    of a currently powered port, power is removed from lower priority
    port(s) and power is supplied to the port

  - If the total consumed power exceeds the configured power limit of
    the power source, low priority ports are turned off. In the case of
    a tie, the port with the lower port number gets priority

Power is available as follows:

| PSU 1 | PSU 2 | PoE Power Budget |
| ----- | ----- | ---------------- |
| 920W  | x     | 750W             |
| x     | 920W  | 750W             |
| 920W  | 920W  | 1650W            |

The AS4610-54P has an LED on the front panel to indicate PoE status:

  - Green: The `poed` daemon is running and no errors are detected

  - Yellow: One or more errors are detected or the `poed` daemon is not
    running

### <span>About Link State and PoE State</span>

Link state and PoE state are completely independent of each other. When
a link is brought down on a particular port using `ip link <port> down`,
power on that port is not turned off; however, LLDP negotiation is not
possible.

## <span>Configuring PoE</span>

You use the `poectl` command utility to configure PoE on a [switch that
supports](http://cumulusnetworks.com/hcl/) the feature. You can:

  - Enable or disable PoE for a given switch port

  - Set a switch port's PoE priority to one of three values: *low*,
    *high* or *critical*

By default, PoE is enabled on all Ethernet/1G switch ports, and these
ports are set with a low priority. Switch ports can have low, high or
critical priority.

To change the priority for one or more switch ports, run `poectl -p swp#
[low|high|critical]`. For example:

    cumulus@switch:~$ sudo poectl -p swp1-swp5,swp7 high

To disable PoE for one or more ports, run `poectl -d [port_numbers]`:

    cumulus@switch:~$ sudo poectl -d swp1-swp5,swp7

To display PoE information for a set of switch ports, run `poectl -i
[port_numbers]`:

    cumulus@switch:~$ sudo poectl -i swp10-swp13
    Port          Status               LLDP      Priority PD type       PD class   Voltage   Current   Power 
    -----   --------------------   -----------   -------- -----------   --------   -------   -------   --------- 
    swp10   connected              negotiating   low high-power         4          53.5 V     25 mA    3.9 W 
    swp11   searching              n/a           low none               none        0.0 V      0 mA    0.0 W 
    swp12   connected              n/a           low legacy             2          53.5 V     25 mA    1.4 W 
    swp13   connected              51.0 W        low high-power         4          53.6 V     72 mA    3.8 W 

Or to see all the PoE information for a switch, run `poectl -s`:

    cumulus@switch:~$ poectl -s
    System power:
      Total:      730.0 W
      Used:        11.0 W
      Available:  719.0 W
    Connected ports:
      swp11, swp24, swp27, swp48

The set commands (priority, enable, disable) either succeed silently or
display an error message if the command fails.

### <span id="src-5118226_PoweroverEthernet-PoE-args" class="confluence-anchor-link"></span><span>poectl Arguments</span>

The `poectl` command takes the following arguments:

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Argument</p></th>
<th><p>Description</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>-h, --help</p></td>
<td><p>Show this help message and exit</p></td>
</tr>
<tr class="even">
<td><p>-i, --port-info PORT_LIST</p></td>
<td><p>Returns detailed information for the specified ports. You can specify a range of ports. For example:<br />
<code>-i swp1-swp5,swp10</code></p>
<p>{{%notice note%}}</p>
<p>On an Edge-Core AS4610-54P switch, the voltage reported by the <code>poectl -i</code> command and measured through a power meter connected to the device varies by 5V. The current and power readings are correct and no difference is seen for them.</p>
<p>{{%/notice%}}</p></td>
</tr>
<tr class="odd">
<td><p>-a, --all</p></td>
<td><p>Returns PoE status and detailed information for all ports.</p></td>
</tr>
<tr class="even">
<td><p>-p, --priority PORT_LIST PRIORITY</p></td>
<td><p>Sets priority for the specified ports: low, high, critical.</p></td>
</tr>
<tr class="odd">
<td><p>-d, --disable-ports PORT_LIST</p></td>
<td><p>Disables PoE operation on the specified ports.</p></td>
</tr>
<tr class="even">
<td><p>-e, --enable-ports PORT_LIST</p></td>
<td><p>Enables PoE operation on the specified ports.</p></td>
</tr>
<tr class="odd">
<td><p>-s, --system</p></td>
<td><p>Returns PoE status for the entire switch.</p></td>
</tr>
<tr class="even">
<td><p>-r, --reset PORT_LIST</p></td>
<td><p>Performs a hardware reset on the specified ports. Use this if one or more ports are stuck in an error state. This does not reset any configuration settings for the specified ports.</p></td>
</tr>
<tr class="odd">
<td><p>-v, --version</p></td>
<td><p>Displays version information.</p></td>
</tr>
<tr class="even">
<td><p>-j, --json</p></td>
<td><p>Displays output in JSON format.</p></td>
</tr>
<tr class="odd">
<td><p>--save</p></td>
<td><p>Saves the current configuration. The saved configuration is automatically loaded on system boot.</p></td>
</tr>
<tr class="even">
<td><p>--load</p></td>
<td><p>Loads and applies the saved configuration.</p></td>
</tr>
</tbody>
</table>

## <span>Logging poed Events</span>

The `poed` service logs the following events to syslog:

  - When a switch provides power to a powered device

  - When a device that was receiving power is removed

  - When the power available to the switch changes

  - Errors
