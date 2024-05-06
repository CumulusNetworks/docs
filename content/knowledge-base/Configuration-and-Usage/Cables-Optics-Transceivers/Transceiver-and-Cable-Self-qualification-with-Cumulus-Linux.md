---
title: Transceiver and Cable Self-qualification with Cumulus Linux
author: NVIDIA
weight: 331
toc: 4
---

NVIDIA provides this document as a suggested procedure for qualifying a transceiver module or cable as a recommended pluggable. NVIDIA does not actively prevent any non-recommended pluggable from functioning and does not restrict the use of self-qualified pluggables. Customers who wish to use a non-recommended pluggable can follow the suggested procedure outlined in this document. For concerns about pluggables that are not listed, {{<exlink url="https://www.nvidia.com/en-us/contact/sales/" text="contact your NVIDIA">}} sales team.

## Example Connections

This procedure is valid for qualifying all types of transceivers and cables in a device undergoing testing. Customers can choose the same types or a combination of different transceivers for this test.

The following diagram illustrates an example where the top and bottom ports connect with a cable as a loopback. The example includes cabling and configuration for the testing of both 40G QSFP and 10/1G SFP. NVIDIA recommends that you test different speed components independently. The example includes both to simplify the presentation.

{{<img src="/images/knowledge-base/transceiver-cable-self-qual.png" alt="Loopback cable port connections" width="600px">}}

TG-1/TG-2 are either networking traffic generators (IXIA/Spirent or equivalent) or two servers with a Linux OS installed and `iperf3` free traffic generator tool or an equivalent.

## Cumulus Linux Configuration

Modify the `/etc/network/interfaces` file with the following bridge configuration:

    auto trg_1
    iface trg_1 inet manual
        bridge_ageing 150
        bridge_stp off
        bridge_ports swp41 swp52
        up ip link set trg_1 up
    
    auto trg_2
    iface trg_2 inet manual
        bridge_ageing 150
        bridge_stp off
        bridge_ports swp42 swp43
        up ip link set trg_2 up
    
    auto l_1
    iface l_1 inet manual
        bridge_ageing 150
        bridge_stp off
        bridge_ports swp51 swp50
        up ip link set l_1 up
    
    auto l_2
    iface l_2 inet manual
        bridge_ageing 150
        bridge_stp off
        bridge_ports swp49 swp48
        up ip link set l_2 up
    
    auto l_3
    iface l_3 inet manual
        bridge_ageing 150
        bridge_stp off
        bridge_ports swp47 swp46
        up ip link set l_3 up
    
    auto l_4
    iface l_4 inet manual
        bridge_ageing 150
        bridge_stp off
        bridge_ports swp45 swp44
        up ip link set l_4 up

You should expect to see the following bridge configuration after you reboot the switch you are testing. Rebooting instead of reloading the configuration ensures that the system detects and properly configures all optics when the it starts up.

    cumulus@switch~$ sudo brctl show
    bridge name    bridge id                 STP enabled       interfaces
    l_1            8000.443839002076         no                swp50
                                                               swp51
    l_2            8000.443839002071         no                swp48
                                                               swp49
    l_3            8000.44383900206f         no                swp46
                                                               swp47
    L_4            8000.44383900206e         no                swp44
                                                               swp45
    trg_1          8000.44383900206c         no                swp43
                                                               swp52
    trg_2          8000.44383900206d         no                swp44
                                                               swp45

## Verifying Link Status

Run the following Cumulus Linux command to verify that all loopback links are up:

    ~$ sudo ethtool swp50
    Settings for swp50:
                   Supported ports: [ FIBRE ]
                   Supported link modes:   10000baseT/Full
                                        40000baseT/Full
                   Supported pause frame use: Symmetric Receive-only
                   Supports auto-negotiation: Yes
                   Advertised link modes:  1000baseT/Full
                                        10000baseT/Full
                                        40000baseT/Full
                   Advertised pause frame use: Symmetric
                   Advertised auto-negotiation: No
                   Speed: 40000Mb/s
                   Duplex: Full
                   Port: FIBRE
                   PHYAD: 0
                   Transceiver: external
                   Auto-negotiation: off
                   Current message level: 0x00000000 (0)
                                                          
                   Link detected: yes

## Activating Data Traffic from Linux Servers

Configure the server interfaces connected to traffic ingress/egress
ports to set IPv4 addresses in the same IP subnet. For example:

    TG1$ sudo ifconfig eth1 101.0.1.1/24 up
    TG2$ sudo ifconfig eth1 101.0.1.2/24 up

You can try `ping` or `ping –f` (flood) between these interfaces.

For generating `iperf` traffic, use options like the following (for example):

    TG1$ sudo iperf -s -B 101.0.1.1 -p 9000
    TG2$ sudo iperf -c 101.0.1.1 -i 3 -t 600 -p 9000 –d

Where:
<!-- vale off -->
- \-B is bound to an interface
- \-p is the TCP port number
- \-c is the iperf destination
- \-i is the print to screen interval
- \-t is the duration of the test in seconds
- \-d is bidirectional traffic
<!-- vale on -->
Confirm that `ping` and `iperf` traffic reach the destination and the
bandwidth matches the expected rate (subject to the transceiver's
supported speed and the server CPU). Connect two servers back-to-back
first to capture baseline server performance characteristics.

## Transceivers Module Information (EEPROM & DOM)

Use the following Cumulus Linux command to check each transceiver's EEPROM and Digital Optical Monitoring (DOM) information:

    cumulus@switch~$ sudo ethtool –m swp<id>
<!-- vale off -->
## Cumulus Linux-based Error Counters Check
<!-- vale on -->
The following commands indicate error and drop counters occurred during and after the test:

    cumulus@switch~$ sudo ethtool -S swp<id> | grep -i error
         HwIfInDot3LengthErrors: 0
         HwIfInErrors: 0
         SoftInErrors: 0
         SoftInFrameErrors: 0
         HwIfOutErrors: 0
         SoftOutErrors: 0

## PASS/FAIL Criteria

The following checklist and test plan comprise successful results.

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p><strong>Test/Check</strong></p></td>
<td><p><strong>Expected Result</strong></p></td>
<td><p><strong>Comment</strong></p></td>
</tr>
<tr class="even">
<td><pre><code>$ ping –f &lt;dest IP&gt;</code></pre></td>
<td><pre><code>% packets drop</code></pre></td>
<td><p>Source and destination IP of TG1 &amp; TG2</p></td>
</tr>
<tr class="odd">
<td><pre><code>$ iperf TCP stream</code></pre></td>
<td><p>Bidirectional traffic with Cumulus Linux snake test matches transfer rate of two traffic generators' endpoints when connected back-to-back.</p></td>
<td> </td>
</tr>
<tr class="even">
<td><pre><code>$ ethtool -S swp&lt;id&gt; | grep -i error</code></pre></td>
<td><p>All error counters return null.</p></td>
<td><p>To detects drops or errors, collect output from <code>ethtool -S</code> before sending traffic, then again afterwards and compare to see if the counters increase.</p></td>
</tr>
<tr class="odd">
<td><pre><code>$ ethtool swp&lt;id&gt;</code></pre></td>
<td><p>Link up</p></td>
<td> </td>
</tr>
<tr class="even">
<td><pre><code>$ ethtool -m swp&lt;id&gt;</code></pre></td>
<td><p>Returns EEPROM information, such as vendor and equipment type.</p></td>
<td><p>DOM information is optional for successful self-qualification of transceivers. In some cases ODM vendors elect to restrict information programmed for DOM.</p></td>
</tr>
<tr class="odd">
<td><pre><code>$ sudo systemctl reset-failed switchd.service
$ sudo systemctl restart switchd.service</code></pre></td>
<td><p>After the <code>switchd</code> service restarts, all links are back up and traffic recovers.</p></td>
<td><p>This test confirms that a <code>switchd</code> daemon restart does correctly program all required transceiver settings.</p></td>
</tr>
<tr class="even">
<td><p>Reboot the switch and repeat same tests and checkpoints again.</p></td>
<td><p>All checks/tests iterations are successful.</p></td>
<td><p>During the qualification cycle for some transceivers, NVIDIA observed that marginal and disqualified transceivers exhibited failures with 10-25% failure rates across switch reboots.</p></td>
</tr>
</tbody>
</table>
