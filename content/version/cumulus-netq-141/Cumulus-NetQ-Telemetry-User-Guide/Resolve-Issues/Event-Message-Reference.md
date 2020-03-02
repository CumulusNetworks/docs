---
title: Event Message Reference
author: Cumulus Networks
weight: 123
aliases:
 - /display/NETQ141/Event+Message+Reference
 - /pages/viewpage.action?pageId=10453533
pageID: 10453533
---
NetQ presents messages at four levels of severity: Critical, Warning,
Info, and Debug. Recommended actions suggest NetQ CLI commands and NCLU
commands for further investigation. The following table lists event
messages organized by message type and then severity.

{{%notice note%}}

The messages can be viewed in syslog or through third-party notification
applications using the NetQ Notifier. For details about configuring NetQ
Notifier, refer to the [Configure Optional NetQ Capabilities](/version/cumulus-netq-141/Cumulus-NetQ-Deployment-Guide/Configure-Optional-NetQ-Capabilities).

{{%/notice%}}

<table style="width:100%;">
<colgroup>
<col style="width: 16%" />
<col style="width: 16%" />
<col style="width: 16%" />
<col style="width: 16%" />
<col style="width: 16%" />
<col style="width: 16%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Type</p></th>
<th><p>Trigger</p></th>
<th><p>Severity</p></th>
<th><p>Message Format</p></th>
<th><p>Example</p></th>
<th><p>Recommended Action</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>BgpSession</p></td>
<td><p>BGP session state changed from &lt;old state&gt; to established state</p></td>
<td><p>INFO</p></td>
<td><p>&lt;hostname&gt; &lt;peer_name&gt; [&lt;description&gt;] : session state changed from &lt;old state&gt; to &lt;new state&gt;</p></td>
<td><p>torc-12 peerlink-1.4094: session state changed from failed to established</p></td>
<td><p>No action required.</p></td>
</tr>
<tr class="even">
<td><p>BgpSession</p></td>
<td><p>BGP session state is not in established state</p></td>
<td><p>WARNING</p></td>
<td><p>&lt;hostname&gt; &lt;peer_name&gt; [&lt;description&gt;] : session state is &lt;curr_state&gt;</p></td>
<td><p>torc-12 peerlink-1.4094: session state is failed</p></td>
<td><p>Investigate reason for current state:</p>
<p><code>netq &lt;hostname&gt; show bgp</code></p>
<p><code>net show bgp summary</code></p>
<p><code>net show bgp neigh &lt;peer&gt;</code></p></td>
</tr>
<tr class="odd">
<td><p>BgpSession</p></td>
<td><p>BGP session state changed from &lt;old state&gt; to &lt;new state&gt;</p></td>
<td><p>WARNING</p></td>
<td><p>&lt;hostname&gt; &lt;peer_name&gt; [&lt;description&gt;] : session state changed from &lt;old state&gt; to &lt;new state != established&gt;</p></td>
<td><p>torc-12 peerlink-1.4094: session state changed from established to failed</p></td>
<td><p>Investigate reason for state change:</p>
<p><code>netq &lt;hostname&gt; show bgp</code></p>
<p><code>net show bgp summary</code></p>
<p><code>net show bgp neigh &lt;peer&gt;</code></p></td>
</tr>
<tr class="even">
<td><p>ClagSession</p></td>
<td><p>CLAG role AND/OR peer role changed from secondary to primary, AND/OR peer state changed from down to up</p></td>
<td><p>INFO</p></td>
<td><p>&lt;hostname&gt;: Role changed [from &lt;old role&gt;] to &lt;new role&gt;, Peer Role changed [from &lt;old role&gt;] to &lt;new role&gt;, Peer state changed from &lt;old state&gt; to up</p></td>
<td><p>torc-12: Role changed from secondary to primary Peer state changed from down to up</p></td>
<td><p>No action required.</p></td>
</tr>
<tr class="odd">
<td><p>ClagSession</p></td>
<td><p>CLAG role AND/OR peer role changed from primary to secondary AND/OR peer state changed from up to down</p></td>
<td><p>WARNING</p></td>
<td><p>&lt;hostname&gt;: Role change [from &lt;old role&gt;] to &lt;new role&gt;, Peer Role changed [from &lt;old role&gt;] to &lt;new role&gt;, Peer state changed from &lt;old state&gt; to down</p></td>
<td><p>torc-12: Role changed from primary to secondary Peer state changed from up to down</p></td>
<td><p>Check CLAG status of peer:</p>
<p><code>netq &lt;hostname&gt; show clag</code></p>
<p><code>net show clag</code></p>
<p>Check logs for reason for transition:</p>
<p><code>less /var/log/clagd.log</code></p></td>
</tr>
<tr class="even">
<td><p>LnvSession</p></td>
<td><p>LNV session state changed state from bad to up</p></td>
<td><p>INFO</p></td>
<td><p>&lt;hostname&gt; &lt;role&gt;: session state changed from &lt;old state != up&gt; to &lt;new state != 'bad'&gt;</p></td>
<td><p>Torc-11 vxsnd: session state changed from bad to up</p></td>
<td><p>No user action required.</p></td>
</tr>
<tr class="odd">
<td><p>LnvSession</p></td>
<td><p>LNV session state changed from up to bad</p></td>
<td><p>WARNING</p></td>
<td><p>&lt;hostname&gt; &lt;role&gt;: session state changed from up to bad</p></td>
<td><p>Torc-11 vxsnd: session state changed from up to bad</p></td>
<td><p>Investigate reason for state change:</p>
<p><code>netq &lt;hostname&gt; show lnv</code></p></td>
</tr>
<tr class="even">
<td><p>LnvSession</p></td>
<td><p>LNV session state is bad</p></td>
<td><p>WARNING</p></td>
<td><p>&lt;hostname&gt; &lt;role&gt;: session state is &lt;state != 'up'&gt;</p></td>
<td><p>Torc-11 vxrd: session state is down</p></td>
<td><p>Investigate reason for current state:</p>
<p><code>netq &lt;hostname&gt; show lnv</code></p></td>
</tr>
<tr class="odd">
<td><p>Link</p></td>
<td><p>Link operational state changed from down to up</p></td>
<td><p>INFO</p></td>
<td><p>&lt;hostname&gt; &lt;ifname&gt; [&lt;ifname description&gt;] [vni:&lt;vni&gt; | master:&lt;master&gt;]: state changed from &lt;old operstate&gt; to &lt;new operstate&gt;</p></td>
<td><p>dell-s4048t-03 swp50: link state changed from down to up</p></td>
<td><p>No user action required.</p></td>
</tr>
<tr class="even">
<td><p>Link</p></td>
<td><p>Link operational state changed from up to down</p></td>
<td><p>WARNING</p></td>
<td><p>&lt;hostname&gt; &lt;ifname&gt; [&lt;ifname description&gt;] [vni:&lt;vni&gt; | master:&lt;master&gt;]: state changed from &lt;old operstate&gt; to DOWN</p></td>
<td><p>dell-s4048t-03 swp50: link state changed from up to down</p></td>
<td><p>Check link status:</p>
<p><code>netq check interfaces</code></p>
<p><code>ip link show &lt;ifname&gt;</code></p>
<p>Verify physical cabling.</p></td>
</tr>
<tr class="odd">
<td><p>Port</p></td>
<td><p>Serial number is different AND port did not change state</p></td>
<td><p>INFO</p></td>
<td><p>&lt;hostname &lt;ifname&gt;: port module changed</p></td>
<td><p>qct-ly8-04 swp44: port module changed</p></td>
<td><p>No user action required.</p></td>
</tr>
<tr class="even">
<td><p>Port</p></td>
<td><p>Serial number is different AND port changed state from empty to plugged</p></td>
<td><p>INFO</p></td>
<td><p>&lt;hostname &lt;ifname&gt;: port is now plugged</p></td>
<td><p>qct-ly8-04 swp44: port is now plugged</p></td>
<td><p>No user action required.</p></td>
</tr>
<tr class="odd">
<td><p>Port</p></td>
<td><p>Serial number is different AND port changed state from plugged to empty</p></td>
<td><p>WARNING</p></td>
<td><p>&lt;hostname &lt;ifname&gt;: port is now empty</p></td>
<td><p>torc-11 swp44: port is now empty</p></td>
<td><p>Verify physical cabling.</p></td>
</tr>
<tr class="even">
<td><p>Services</p></td>
<td><p>A service changed state from previous state to ok</p></td>
<td><p>INFO</p></td>
<td><p>&lt;hostname&gt; &lt;service name&gt; (vrf &lt;vrf&gt;): state changed from &lt;prev state&gt; to ok</p></td>
<td><p>dell-s4048t-03 ledmgrd (vrf default): state changed from fail to ok</p></td>
<td><p>No user action required.</p></td>
</tr>
<tr class="odd">
<td><p>Services</p></td>
<td><p>A service changed state from previous state to warning, error, or fail state</p></td>
<td><p>WARNING</p></td>
<td><p>&lt;hostname&gt; &lt;service name&gt; (vrf &lt;vrf&gt;): state changed from &lt;prev state&gt; to &lt;curr state&gt;</p></td>
<td><p>dell-s4048t-03 ledmgrd (vrf default): state changed from ok to fail</p></td>
<td><p>Check status of the service:</p>
<p><code>netq [&lt;hostname&gt;] show services [&lt;service-name&gt;]</code></p>
<p><code>sudo systemctl status &lt;service&gt;</code></p></td>
</tr>
<tr class="even">
<td><p>Services</p></td>
<td><p>A service enters the warning, error, or fail state</p></td>
<td><p>WARNING</p></td>
<td><p>&lt;hostname&gt; &lt;service name&gt; (vrf &lt;vrf&gt;): state is &lt;curr state&gt;</p></td>
<td><p>dell-s4048t-03 ledmgrd (vrf default): state is fail</p></td>
<td><p>Check status of the service:</p>
<p><code>netq [&lt;hostname&gt;] show services [&lt;service-name&gt;]</code></p>
<p><code>sudo systemctl status &lt;service&gt;</code></p></td>
</tr>
<tr class="odd">
<td><p>Services</p></td>
<td><p>A service PID changed AND state is ok</p></td>
<td><p>INFO</p></td>
<td><p>&lt;hostname&gt; &lt;service name&gt; (vrf &lt;vrf&gt;): service restarted</p></td>
<td><p>dell-s4048t-03 lldpd (vrf default): service restarted</p></td>
<td><p>No user action required.</p></td>
</tr>
<tr class="even">
<td><p>Services</p></td>
<td><p>A service PID changed AND state is warning, error, or fail</p></td>
<td><p>WARNING</p></td>
<td><p>&lt;hostname&gt; &lt;service name&gt; (vrf &lt;vrf&gt;): service restarted</p></td>
<td><p>dell-s4048t-03 lldpd (vrf default): service restarted</p></td>
<td><p>Check status of the service:</p>
<p><code>netq [&lt;hostname&gt;] show services [&lt;service-name&gt;]</code></p>
<p><code>sudo systemctl status &lt;service&gt;</code></p></td>
</tr>
<tr class="odd">
<td><p>OS</p></td>
<td><p>OS version changed in /etc/os-release output</p></td>
<td><p>INFO</p></td>
<td><p>&lt;hostname&gt; &lt;name&gt;: version changed from &lt;prev version&gt; to &lt;new version&gt;</p></td>
<td><p>dell-s4048t-03 Cumulus Linux: version changed from 3.3.1 to 3.4.0</p></td>
<td><p>No user action required.</p></td>
</tr>
<tr class="even">
<td><p>Temp/Fan/PSU (sensors)</p></td>
<td><p>Sensor s_state is ok AND no previous state</p></td>
<td><p>INFO</p></td>
<td><p>&lt;hostname&gt; &lt;sensor name&gt;: status is ok</p></td>
<td><p>vx-1 temp1: status is ok</p></td>
<td><p>No user action required.</p></td>
</tr>
<tr class="odd">
<td><p>Temp/Fan/PSU (sensors)</p></td>
<td><p>Sensor s_state is high, low, or unknown AND no previous state</p></td>
<td><p>WARNING</p></td>
<td><p>&lt;hostname&gt; &lt;sensor name&gt;: status is (high, low, unknown)</p></td>
<td><p>vx-1 temp1: status is low</p></td>
<td><p>Check sensor status:</p>
<p><code>netq &lt;hostname&gt; show sensors</code></p>
<p><code>sudo smonctl -v</code></p></td>
</tr>
<tr class="even">
<td><p>Temp/Fan/PSU (sensors)</p></td>
<td><p>Sensor s_state is critical, l_critical, bad, or absent AND no previous state</p></td>
<td><p>CRITICAL</p></td>
<td><p>&lt;hostname&gt; &lt;sensor name&gt;: status is (critical, l_critical, bad, absent)</p></td>
<td><p>vx-1 temp1: status is bad</p></td>
<td><p>Check sensor status:</p>
<p><code>netq &lt;hostname&gt; show sensors</code></p>
<p><code>sudo smonctl -v</code></p></td>
</tr>
<tr class="odd">
<td><p>Temp/Fan/PSU (sensors)</p></td>
<td><p>Sensor s_state changed from previous state to ok</p></td>
<td><p>INFO</p></td>
<td><p>&lt;hostname&gt; &lt;sensor name&gt;: state changed from &lt;prev state&gt; to ok</p></td>
<td><p>vx-1 temp1: state changed from high to ok</p></td>
<td><p>No user action required.</p></td>
</tr>
<tr class="even">
<td><p>Temp/Fan/PSU (sensors)</p></td>
<td><p>Sensor s_state changed from previous state to high, low, or unknown</p></td>
<td><p>WARNING</p></td>
<td><p>&lt;hostname&gt; &lt;sensor name&gt;: state changed from &lt;prev state&gt; to (high, low, unknown)</p></td>
<td><p>vx-1 temp1: state changed from high to low</p></td>
<td><p>Check sensor status:</p>
<p><code>netq &lt;hostname&gt; show sensors</code></p>
<p><code>sudo smonctl -v</code></p></td>
</tr>
<tr class="odd">
<td><p>Temp/Fan/PSU (sensors)</p></td>
<td><p>Sensor s_state changed from previous state to critical, l_critical, bad, or absent</p></td>
<td><p>CRITICAL</p></td>
<td><p>&lt;hostname&gt; &lt;sensor name&gt;: state changed from &lt;prev state&gt; to (critical, l_critical, bad, absent)</p></td>
<td><p>vx-1 temp1: state changed from ok to bad</p></td>
<td><p>Check sensor status:</p>
<p><code>netq &lt;hostname&gt; show sensors</code></p>
<p><code>sudo smonctl -v</code></p></td>
</tr>
<tr class="even">
<td><p>License</p></td>
<td><p>License state changed to ok</p></td>
<td><p>INFO</p></td>
<td><p>&lt;hostname&gt; cumulus: license changed from &lt;prev state&gt; to ok</p></td>
<td><p>Dell-s4048t-03 cumulus: license changed from missing to ok</p></td>
<td><p>No user action required.</p></td>
</tr>
<tr class="odd">
<td><p>License</p></td>
<td><p>License state changed to missing or invalid</p></td>
<td><p>WARNING</p></td>
<td><p>&lt;hostname&gt; cumulus: license changed from &lt;prev state&gt; to &lt;curr state&gt;</p></td>
<td><p>Dell-s4048t-03 cumulus: license changed from ok to missing</p></td>
<td><p>Re-install license on switch:</p>
<p><code>sudo cl-license -i</code></p></td>
</tr>
<tr class="even">
<td><p>License</p></td>
<td><p>License state is missing or invalid</p></td>
<td><p>WARNING</p></td>
<td><p>&lt;hostname&gt; cumulus: license is &lt;curr state&gt;</p></td>
<td><p>Dell-s4048t-03 cumulus: license is missing</p></td>
<td><p>Re-install license on switch:</p>
<p><code>sudo cl-license -i</code></p></td>
</tr>
<tr class="odd">
<td><p>NTP</p></td>
<td><p>NTP sync state changed from out of sync (no) to in sync (yes)</p></td>
<td><p>INFO</p></td>
<td><p>&lt;hostname&gt;: NTP sync state changed from no to yes</p></td>
<td><p>dell-s4048t-03: NTP sync state changed from no to yes</p></td>
<td><p>No user action required.</p></td>
</tr>
<tr class="even">
<td><p>NTP</p></td>
<td><p>NTP sync state changed from in sync (yes) to out of sync (no)</p></td>
<td><p>WARNING</p></td>
<td><p>&lt;hostname&gt;: NTP sync state changed from yes to no</p></td>
<td><p>dell-s4048t-03: NTP sync state changed from yes to no</p></td>
<td><p>Verify NTP state:</p>
<p><code>netq &lt;hostname&gt; show ntp</code></p>
<p><code>sudo ntpq -p</code></p></td>
</tr>
<tr class="odd">
<td><p>NTP</p></td>
<td><p>NTP is not synchronized AND no previous state known</p></td>
<td><p>WARNING</p></td>
<td><p>&lt;hostname&gt;: NTP is not synced</p></td>
<td><p>dell-s4048t-03: NTP is not synced</p></td>
<td><p>Verify NTP state:</p>
<p><code>netq &lt;hostname&gt; show ntp</code></p>
<p><code>sudo ntpq -p</code></p></td>
</tr>
</tbody>
</table>

