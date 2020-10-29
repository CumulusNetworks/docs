---
title: Verify Network Connectivity
author: Cumulus Networks
weight: 1030
toc: 2
---
It is helpful to verify that communications are freely flowing between the various devices in your network. You can verify the connectivity between two devices in both an adhoc fashion and by defining connectivity checks to occur on a scheduled basis. NetQ provides three NetQ UI card workflows and several NetQ CLI trace commands to view connectivity:

- Trace Request card
    - Run a scheduled trace on demand or create new on-demand or scheduled trace request
    - View a preview of all scheduled traces
- On-demand Trace Results card
    - View source and destination devices, status, paths found, and number/distribution of MTU and hops
    - View job configuration
- Scheduled Trace Results card
    - View source and destination devices, status, distribution of paths, bad nodes, MTU and hops
    - View job configuration
- `netq trace` command
    - Create and run a trace on demand
    - View source and destination devices, status, paths found, MTU, and hops in terminal window
- `netq add trace` command
    - Create an on-demand or scheduled trace
    - Results viewed on On-demand and Scheduled Trace Results cards

## NetQ CLI Considerations

When creating and running traces using the NetQ CLI, consider the following items.

### Time Values

When entering a time value, you must include a numeric value *and* the unit of measure:

- **w**: week(s)
- **d**: day(s)
- **h**: hour(s)
- **m**: minute(s)
- **s**: second(s)
- **now**

When using the `between` option, the start time (`text-time`) and end time (`text-endtime`) values can be entered as most recent first and least recent second, or vice versa. The values do not have to have the same unit of measure.

### Result Display Options

Three output formats are available for the on-demand trace with results in a terminal window.

- **JSON**: Results are listed in a .json file, good for exporting to other applications or software.
- **Pretty**: Results are lined up by paths in a pseudo-graphical manner to help visualize the multiple paths.
- **Detail**: Results are displayed in a tabular format with a row per hop and a set of rows per path, useful for traces with higher hop counts where the pretty output wraps lines,
making it harder to interpret the results. This is the default output when not specified.

### Known Addresses

The tracing function only knows about addresses that have already been learned. If you find that a path is invalid or incomplete, you may need to ping the identified device so that its address becomes known.

## Create a Trace Request

Two types of connectivity checks can be run in NetQ: an immediate (on-demand) trace and a scheduled trace.

### Create a Layer 3 On-demand Trace Request

It is helpful to verify the connectivity between two devices when you suspect an issue is preventing proper communication between them. If you cannot find a layer 3 path, you might also try checking connectivity through a layer 2 path.

{{< tabs "TabID33" >}}

{{< tab "NetQ UI" >}}

1. Open the medium Trace Request card.

    {{<figure src="/images/netq/trace-request-medium-320.png" width="200">}}

2. In the **Source** field, enter the hostname or IP address of the device where you want to start the trace.

3. In the **Destination** field, enter the IP address of the device where you want to end the trace.  

    {{<figure src="/images/netq/trace-request-medium-l3-example-222.png" width="200">}}

<div style="padding-left: 18px;">In this example, we are starting our trace at *server02* and ending it at *10.1.3.103*.</div>

<div style="padding-left: 18px;"><div class="notices tip"><p>If you mistype an address, you must double-click it, or backspace over the error, and retype the address. You cannot select the address by dragging over it as this action attempts to move the card to another location.</p></div></div>

4. Click **Run Now**. A corresponding Trace Results card is opened on your workbench. Refer to {{<link title="#View Layer 3 Trace Results" text="View Layer 3 Trace Results">}} for details.

{{< /tab >}}

{{< tab "NetQ CLI" >}}

Use the `netq trace` command to view the results in the terminal window. Use the `netq add trace` command to view the results in the NetQ UI.

{{< tabs "TabID59" >}}

{{< tab "netq trace" >}}

To create a layer 3 on-demand trace and see the results in the terminal window, run:

```
netq trace <ip> from (<src-hostname>|<ip-src>) [json|detail|pretty]
```

Note the syntax requires the *destination* device address first and then the *source* device address or hostname.

This example shows a trace from x (source) to y (destination) in pretty output. identify the addresses for the source and
destination devices using the `netq show ip addresses` command 

```
```

{{< /tab >}}

{{< tab "netq add trace" >}}

{{< /tab >}}

{{< /tabs >}}

{{< /tab >}}

{{< /tabs >}}

## Validate Paths between Devices

If you have VLANs configured, you can view the available paths between two devices on the VLAN currently and at a time in the past using their MAC addresses  . You can view the output in one of three formats (*json*, *pretty*, and *detail*). JSON output provides the output in a JSON file format for ease of importing to other applications or software. Pretty output lines up the paths in a pseudo-graphical manner to help visualize multiple paths. Detail output is useful for traces with higher hop counts where the pretty output wraps lines, making it harder to interpret the results. The detail output displays a table with a row for each path.

To view the paths:

1.  Identify the MAC address and VLAN ID for the destination device

2.  Identify the IP address or hostname for the source device

3.  Use the `netq trace` command to see the available paths between
    those devices.

The trace command syntax is:

    netq trace <mac> [vlan <1-4096>] from (<src-hostname>|<ip-src>) [vrf <vrf>] [around <text-time>] [json|detail|pretty] [debug]

{{%notice note%}}

The syntax requires the destination device address first, `mac`, and
then the source device address or hostname. Additionally, the `vlan`
keyword-value pair is required for layer 2 traces even though the syntax
indicates it is optional.

The tracing function only knows about addresses that have already been
learned. If you find that a path is invalid or incomplete, you may need
to ping the identified device so that its address becomes known.

{{%/notice%}}

### View Paths between Two Switches with Pretty Output

This example shows the available paths between a top of rack switch,
*tor-1*, and a server, *server11*. The request is to go through VLAN
*1001* from the VRF *vrf1*. The results include a summary of the trace,
including the total number of paths available, those with errors and
warnings, and the MTU of the paths. In this case, the results are
displayed in pseudo-graphical output.

```
cumulus@switch:~$ netq trace 00:02:00:00:00:02 vlan 1001 from leaf01 vrf vrf1 pretty
Number of Paths: 4
Number of Paths with Errors: 0
Number of Paths with Warnings: 0
Path MTU: 9152
 leaf01 vni: 34 uplink-2 -- downlink-5 spine02 downlink-2 -- uplink-2 vni: 34 leaf12 hostbond4 -- swp2 server11  
               uplink-2 -- downlink-5 spine02 downlink-1 -- uplink-2 vni: 34 leaf11 hostbond4 -- swp1 server11  
 leaf01 vni: 34 uplink-1 -- downlink-5 spine01 downlink-2 -- uplink-1 vni: 34 leaf12 hostbond4 -- swp2 server11  
               uplink-1 -- downlink-5 spine01 downlink-1 -- uplink-1 vni: 34 leaf11 hostbond4 -- swp1 server11    
```

Alternately, you can use the IP address of the source device, as shown
in this example.

    cumulus@redis-1:~$  netq trace 00:02:00:00:00:02 vlan 1001 from 10.0.0.8 vrf vrf1 pretty
    Number of Paths: 4
    Number of Paths with Errors: 0
    Number of Paths with Warnings: 0
    Path MTU: 9152
     server11 swp1 -- swp5 <vlan1000> tor-1 <vlan1001> vni: 34 uplink-2 -- downlink-5 spine02 downlink-2 -- uplink-2 vni: 34 <vlan1001> leaf12 hostbond4 -- swp2 server11  
                                                               uplink-2 -- downlink-5 spine02 downlink-1 -- uplink-2 vni: 34 <vlan1001> leaf11 hostbond4 -- swp1 server11  
              swp1 -- swp5 <vlan1000> tor-1 <vlan1001> vni: 34 uplink-1 -- downlink-5 spine01 downlink-2 -- uplink-1 vni: 34 <vlan1001> leaf12 hostbond4 -- swp2 server11  
                                                               uplink-1 -- downlink-5 spine01 downlink-1 -- uplink-1 vni: 34 <vlan1001> leaf11 hostbond4 -- swp1 server11

### View Paths between Two Switches with Detailed Output

This example provides the same path information as the pretty output,
but displays the information in a tabular output.

    cumulus@switch:~$ netq trace 00:02:00:00:00:02 vlan 1001 from 10.0.0.8 vrf vrf1 detail
    Number of Paths: 4
    Number of Paths with Errors: 0
    Number of Paths with Warnings: 0
    Path MTU: 9152
    Id  Hop Hostname        InPort          InVlan InTunnel              InRtrIf         InVRF           OutRtrIf        OutVRF          OutTunnel             OutPort         OutVlan
    --- --- --------------- --------------- ------ --------------------- --------------- --------------- --------------- --------------- --------------------- --------------- -------
    1   1   server11                                                                                                                                           swp1            1000
        2   leaf01          swp5            1000                         vlan1000        vrf1            vlan1001        vrf1            vni: 34               uplink-2
        3   spine02         downlink-5                                   downlink-5      default         downlink-2      default                               downlink-2
        4   leaf12          uplink-2               vni: 34               vlan1001        vrf1                                                                  hostbond4       1001
        5   server11        swp2
    --- --- --------------- --------------- ------ --------------------- --------------- --------------- --------------- --------------- --------------------- --------------- -------
    2   1   server11                                                                                                                                           swp1            1000
        2   leaf01          swp5            1000                         vlan1000        vrf1            vlan1001        vrf1            vni: 34               uplink-2
        3   spine02         downlink-5                                   downlink-5      default         downlink-1      default                               downlink-1
        4   leaf11          uplink-2               vni: 34               vlan1001        vrf1                                                                  hostbond4       1001
        5   server11        swp1
    --- --- --------------- --------------- ------ --------------------- --------------- --------------- --------------- --------------- --------------------- --------------- -------
    3   1   server11                                                                                                                                           swp1            1000
        2   leaf01          swp5            1000                         vlan1000        vrf1            vlan1001        vrf1            vni: 34               uplink-1
        3   spine01         downlink-5                                   downlink-5      default         downlink-2      default                               downlink-2
        4   leaf12          uplink-1               vni: 34               vlan1001        vrf1                                                                  hostbond4       1001
        5   server11        swp2
    --- --- --------------- --------------- ------ --------------------- --------------- --------------- --------------- --------------- --------------------- --------------- -------
    4   1   server11                                                                                                                                           swp1            1000
        2   leaf01          swp5            1000                         vlan1000        vrf1            vlan1001        vrf1            vni: 34               uplink-1
        3   spine01         downlink-5                                   downlink-5      default         downlink-1      default                               downlink-1
        4   leaf11          uplink-1               vni: 34               vlan1001        vrf1                                                                  hostbond4       1001
        5   server11        swp1
    --- --- --------------- --------------- ------ --------------------- --------------- --------------- --------------- --------------- --------------------- --------------- -------

