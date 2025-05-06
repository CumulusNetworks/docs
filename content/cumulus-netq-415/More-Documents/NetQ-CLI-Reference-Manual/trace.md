---
title: trace
author: Cumulus Networks
weight: 1107
toc: 3
right_toc_levels: 1
pdfhidden: true
type: nojsscroll
---

## netq trace

Verifies network connectivity between two devices at layer 2 or layer 3. Results appear in the terminal window.

{{<notice tip>}}

The tracing function only knows about already learned addresses. If you find that a path is invalid or incomplete, ping the identified device so that its address becomes known.

{{</notice>}}

You can improve the readability of the output using color. Run `netq config add color` to turn color on or `netq config del color` to turn it off.

### Syntax

Three forms of this command are available: one for layer 3 and two for layer 2 traces.

```
netq trace
	<ip>
	from (<src-hostname>|<ip-src>)
	[vrf <vrf>]
	[around <text-time>]
	[json|detail|pretty]
        [debug]
```
```
netq trace
	(<mac> vlan <1-4096>)
	from (<src-hostname>|<ip-src>)
	[vrf <vrf>]
	[around <text-time>]
	[json|detail|pretty]
        [debug]
```
```	
netq trace
	(<mac> vlan <1-4096>)
	from <mac-src>
	[around <text-time>]
	[json|detail|pretty]
        [debug]
```

### Required Arguments

| Argument | Value | Description |
| ---- | ---- | ---- |
| NA | \<ip\> | End trace at the device with this IPv4 or IPv6 address (no mask). IPv6 addresses must be the complete, non-truncated address. |
| NA | \<mac\> | End trace at the device with this MAC address |
| vlan | \<1-4096\> | End trace at the device with this VLAN identifier |
| NA | \<src-hostname\> | Start trace at the device with this hostname |
| NA | \<ip-src\> | Start trace at the device with this IPv4 or IPv6 address. IPv6 addresses must be the complete, non-truncated address. |
| NA | \<mac-src\> | Start trace at the device with this MAC address |

### Options

| Option | Value | Description |
| ---- | ---- | ---- |
| vrf | \<vrf\> | Only use paths through this VRF |
| around | \<text-time\> | <p>Indicates how far to go back in time for the network state information. Write the value using text (versus a UTP representation for example). Note there is no space between the number and unit of time. </p><p>Valid values include:<ul><li><1-xx>s: number of seconds</li><li><1-xx>m: number of minutes</li><li><1-xx>h: number of hours</li><li><1-xx>d: number of days</li></ul></p> |
| json | NA | Display results in JSON format |
| detail | NA | Display results in a tabular format with a row per hop and a set of rows per path, useful for traces with higher hop counts where the pretty output wraps lines, making it harder to interpret the results. This is the default output when not specified. |
| pretty | NA | Display results lined up by paths in a pseudo-graphical manner to help visualize the multiple paths |
| debug | NA | Log all events |

### Sample Usage

```
cumulus@switch:~$ netq trace 10.10.10.63 from  10.10.10.1 pretty
Number of Paths: 12
Number of Paths with Errors: 0
Number of Paths with Warnings: 0
Path MTU: 9216

 leaf01 swp54 -- swp1 spine04 swp6 -- swp54 border02 peerlink.4094 -- peerlink.4094 border01 lo
                                                     peerlink.4094 -- peerlink.4094 border01 lo
 leaf01 swp53 -- swp1 spine03 swp6 -- swp53 border02 peerlink.4094 -- peerlink.4094 border01 lo
                                                     peerlink.4094 -- peerlink.4094 border01 lo
 leaf01 swp52 -- swp1 spine02 swp6 -- swp52 border02 peerlink.4094 -- peerlink.4094 border01 lo
                                                     peerlink.4094 -- peerlink.4094 border01 lo
 leaf01 swp51 -- swp1 spine01 swp6 -- swp51 border02 peerlink.4094 -- peerlink.4094 border01 lo
                                                     peerlink.4094 -- peerlink.4094 border01 lo
 leaf01 swp54 -- swp1 spine04 swp5 -- swp54 border01 lo
 leaf01 swp53 -- swp1 spine03 swp5 -- swp53 border01 lo
 leaf01 swp52 -- swp1 spine02 swp5 -- swp52 border01 lo
 leaf01 swp51 -- swp1 spine01 swp5 -- swp51 border01 lo
 ```

 ```
 cumulus@switch:~$ netq trace 10.10.10.63 from  10.10.10.1
Number of Paths: 12
Number of Paths with Errors: 0
Number of Paths with Warnings: 0
Path MTU: 9216

Id  Hop Hostname    InPort          InTun, RtrIf    OutRtrIf, Tun   OutPort
--- --- ----------- --------------- --------------- --------------- ---------------
1   1   leaf01                                      swp54           swp54
    2   spine04     swp1            swp1            swp6            swp6
    3   border02    swp54           swp54           peerlink.4094   peerlink.4094
    4   border01    peerlink.4094                                   lo
--- --- ----------- --------------- --------------- --------------- ---------------
2   1   leaf01                                      swp54           swp54
    2   spine04     swp1            swp1            swp6            swp6
    3   border02    swp54           swp54           peerlink.4094   peerlink.4094
    4   border01    peerlink.4094                                   lo
--- --- ----------- --------------- --------------- --------------- ---------------
3   1   leaf01                                      swp53           swp53
    2   spine03     swp1            swp1            swp6            swp6
    3   border02    swp53           swp53           peerlink.4094   peerlink.4094
    4   border01    peerlink.4094                                   lo
--- --- ----------- --------------- --------------- --------------- ---------------
4   1   leaf01                                      swp53           swp53
    2   spine03     swp1            swp1            swp6            swp6
    3   border02    swp53           swp53           peerlink.4094   peerlink.4094
    4   border01    peerlink.4094                                   lo
--- --- ----------- --------------- --------------- --------------- ---------------
...
 ```

 ```
 cumulus@switch:~$ netq trace 44:38:39:00:00:3e vlan 10 from 44:38:39:00:00:32
Number of Paths: 16
Number of Paths with Errors: 0
Number of Paths with Warnings: 0
Path MTU: 9000

Id  Hop Hostname    InPort          InTun, RtrIf    OutRtrIf, Tun   OutPort
--- --- ----------- --------------- --------------- --------------- ---------------
1   1   server01                                                    mac:44:38:39:00
                                                                    :00:38
    2   leaf02      swp1                            vni: 10         swp54
    3   spine04     swp2            swp2            swp4            swp4
    4   leaf04      swp54           vni: 10                         bond1
    5   server04    uplink
--- --- ----------- --------------- --------------- --------------- ---------------
2   1   server01                                                    mac:44:38:39:00
                                                                    :00:38
    2   leaf02      swp1                            vni: 10         swp54
    3   spine04     swp2            swp2            swp3            swp3
    4   leaf03      swp54           vni: 10                         bond1
    5   server04    uplink
--- --- ----------- --------------- --------------- --------------- ---------------
3   1   server01                                                    mac:44:38:39:00
                                                                    :00:38
    2   leaf02      swp1                            vni: 10         swp53
    3   spine03     swp2            swp2            swp4            swp4
    4   leaf04      swp53           vni: 10                         bond1
    5   server04    uplink
--- --- ----------- --------------- --------------- --------------- ---------------
4   1   server01                                                    mac:44:38:39:00
                                                                    :00:38
    2   leaf02      swp1                            vni: 10         swp53
    3   spine03     swp2            swp2            swp3            swp3
    4   leaf03      swp53           vni: 10                         bond1
    5   server04    uplink
--- --- ----------- --------------- --------------- --------------- ---------------
...
 ```

### Related Commands

- ```netq add trace```

