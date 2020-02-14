---
title: NetQ CLI Changes
author: Cumulus Networks
weight: 32
aliases:
 - /display/NETQ/NetQ+Command+Line+Overview
 - /pages/viewpage.action?pageId=12321059
pageID: 12321059
product: Cumulus NetQ
version: 2.4
imgData: cumulus-netq
siteSlug: cumulus-netq
---
A number of commands have changed in this release to accommodate the addition of new keywords and options or to simplify their syntax. Additionally, new commands have been added and others have been removed. A summary of those changes is provided here.

## New Commands

The following table summarizes the new commands available with this release. They are grouped into the following categories: new `netq show` commands, What Just Happened feature, clustering deployment, detailed validation commands, and threshold-based events.

<table>
<colgroup>
<col style="width: 42.5%" />
<col style="width: 42.5%" />
<col style="width: 15%" />
</colgroup>
<tbody>
<tr>
  <th>Command</th>
  <th>Summary</th>
  <th>Version</th>
</tr>
<tr>
  <td>netq [&lt;hostname&gt;] show cl-manifest [json]</td>
  <td>Lists installed software packages one or all devices</td>
  <td>2.4.0</td>
</tr>
<tr>
  <td>netq [&lt;hostname&gt;] show cl-resource acl [ingress|egress] [around &lt;text-time&gt;] [json]</td>
  <td>Displays incoming and outgoing access control lists (ACLs) configured on one or all devices, currently or at a time in the past</td>
  <td>2.4.0</td>
</tr>
<tr>
  <td>netq [&lt;hostname&gt;] show cl-resource forwarding [around &lt;text-time&gt;] [json]</td>
  <td>Displays xxx on one or all devices, currently or at a time in the past</td>
  <td>2.4.0</td>
</tr>
<tr>
  <td>netq [&lt;hostname&gt;] show recommended-pkg-verison [release-id &lt;test-release-id&gt;] [package-name &lt;text-package-name&gt;] [json]</td>
  <td>Displays list of recommended packages to install/upgrade on one or all devices</td>
  <td>2.4.0</td>
</tr>
<tr>
  <td>netq [&lt;hostname&gt;] show cl-resource-util [cpu|memory] [around &lt;text-time&gt;] [json]</td>
  <td>Displays the CPU or memory utilization for a given device or all devices, currently or at a time in the past/td>
  <td>2.4.0</td>
</tr>
<tr>
  <td>netq [&lt;hostname&gt;] show show-resource-util disk [&lt;text-diskname&gt;] [around &lt;text-time&gt;] [json]</td>
  <td>Displays the disk utilization for a given device or all devices, currently or at a time in the past</td>
  <td>2.4.0</td>
</tr>
<tr>
  <td>netq [&lt;hostname&gt;] show wjh-drop [&lt;text-drop-type&gt;] [ingress-port &lt;text-ingress-port&gt;] [reason &lt;text-reason&gt;] [src-ip &lt;text-src-ip&gt;] [dst-ip &lt;text-dst-ip&gt;] [proto &lt;text-proto&gt;] [src-port &lt;text-src-port&gt;] [dst-port &lt;text-dst-port&gt;] [src-mac &lt;text-src-mac&gt;] [dst-mac &lt;text-dst-mac&gt;] [egress-port &lt;text-egress-port&gt;] [traffic-class &lt;text-traffic-class&gt;] [rule-id-acl &lt;text-rule-id-acl&gt;] [between &lt;text-time&gt; and &lt;text-endtime&gt;] [around &lt;text-time&gt;] [json]</td>
  <td>Displays status of various resource, interface, and sensor-related drops, the reason for the drop, and where they have occurred in the last 24 hours, between a set of times, or at a time in the past</td>
  <td>2.4.0</td>
</tr>
<tr>
  <td>netq [&lt;hostname&gt;] show (agent| unit-tests [json]</td>
  <td>Displays the CPU or memory utilization for a given device or all devices, currently or at a time in the past/td>
  <td>2.4.0</td>
</tr>
<tr>
  <td>netq [&lt;hostname&gt;] show show-resource-util disk [&lt;text-diskname&gt;] [around &lt;text-time&gt;] [json]</td>
  <td>Displays the disk utilization for a given device or all devices, currently or at a time in the past</td>
  <td>2.4.0</td>
</tr>
<tr>
  <td>netq bootstrap master interface &lt;text-opta-ifname&gt;] tarball &lt;text-tarball-name&gt;</td>
  <td>Loads master node with the NetQ installer in a server cluster deployment</td>
  <td>2.4.0</td>
</tr>
<tr>
  <td>netq bootstrap master upgrade &lt;text-tarball-name&gt;</td>
  <td>Loads master node with a new NetQ installer in a server cluster deployment</td>
  <td>2.4.0</td>
</tr>
<tr>
  <td>netq bootstrap reset</td>
  <td>Resets the NetQ installer to default settings on nodes in a server cluster deployment</td>
  <td>2.4.0</td>
</tr>
<tr>
  <td>netq bootstrap worker tarball &lt;text-tarball-name&gt; master-ip &lt;text-master-ip&gt;</td>
  <td>Loads a worker node with the NetQ installer in a server cluster deployment</td>
  <td>2.4.0</td>
</tr>
<!-- <tr>
  <td>netq install cluster activate-job config-key &lt;text-opta-key&gt;</td>
  <td>Activates NetQ, the last step of installation</td>
  <td>2.4.0</td>
</tr>
<tr>
  <td>netq install [standalone|cluster] infra-job</td>
  <td>Sets up and configures the standalone or server cluster infrastructure</td>
  <td>2.4.0</td>
</tr>
<tr>
  <td>netq install [standalone|cluster] init-job</td>
  <td>Initalizes standalone or server cluster </td>
  <td>2.4.0</td>
</tr>
<tr>
  <td>netq install [standalone|cluster] install-job bundle &lt;text-bundle-url&gt;</td>
  <td>Installs installation files on the standalone or master server</td>
  <td>2.4.0</td>
</tr>
<tr> -->
  <td>netq install cluster join-workers &lt;text-worker-01&gt; [&lt;text-worker-02&gt;]</td>
  <td>Adds worker node(s) to the server cluster</td>
  <td>2.4.0</td>
</tr>
<tr>
  <td>netq show job-status &lt;text-opta-ip&gt; [json]</td>
  <td>Displays the status of running jobs on the standalone or cluster servers</td>
  <td>2.4.0</td>
</tr>
<tr>
  <td>netq config add agent cluster-servers &lt;text-opta-ip-list&gt; [port &lt;text-opta-port&gt;] [vrf &lt;text-vrf-name&gt;]
[json]</td>
  <td>Configures the agent on monitored switches and hosts to send data to the cluster nodes. You can also provide a specific port or VRF to use for the communication.</td>
  <td>2.4.0</td>
</tr>
<tr>
  <td>netq check &lt;protocol-or-service&gt; <br>[include &lt;proto-or-srvc-number-range-list&gt; | <br>exclude &lt;proto-or-srvc-number-range-list&gt;] <br>[around &lt;text-time&gt;] [json | summary]<br><br>where &lt;protocol-or-service&gt; is one of the following:
  <ul><li>bgp [vrf <vrf>]</li>
  <li>cl-version [match-version <cl-ver> | min-version <cl-ver>]</li>
  <li>clag</li>
  <li> evpn [mac-consistency]</li>
  <li>interfaces</li>
  <li>license</li>
  <li>mtu [unverified]</li>
  <li>ntp</li>
  <li>ospf</li>
  <li>sensors</li>
  <li>vlan [unverified]</li>
  <li>vxlan</li></td>
  <td>Validates the specified protocol or service, running all tests or selected tests.</td>
  <td>2.4.0</td>
</tr>
<tr>
  <td>netq show (agent|bgp|cl-version|clag|<br>evpn|interfaces|license|mtu|ntp|ospf|sensors|<br>vlan|vxlan) unit-tests [json]</td>
  <td>Displays the validation tests that can be run for each protocol and service accordingly.</td>
  <td>2.4.0</td>
</tr>
<tr>
  <td>netq add tca [event_id &lt;text-event-id-anchor&gt;]  [scope &lt;text-scope-anchor&gt;] [tca_id &lt;text-tca-id-anchor&gt;]  [severity info | severity critical] [is_active true | is_active false] [suppress_until &lt;text-suppress-ts&gt;] [ threshold &lt;text-threshold-value&gt; ] [channel &lt;text-channel-name-anchor&gt; | channel drop &lt;text-drop-channel-name&gt;] </td>
  <td>Configures a threshold-based event notification. Also used to set the severity of the event, disable the event temporarily or indefinitely, and remove a receiving channel.</td>
  <td>2.4.0</td>
</tr>
<tr>
  <td>netq del tca tca_id &lt;text-tca-id-anchor&gt;</td>
  <td>Removes a threshold-based event rule</td>
  <td>2.4.0</td>
</tr>
<tr>
  <td>netq show tca [tca_id &lt;text-tca-id-anchor&gt;] [json]</td>
  <td>Displays all or a given threshold-based event rules</td>
  <td>2.4.0</td>
</tr>
</tbody>
</table>

## Modified Commands

The following table summarizes the commands that have been changed with
this release.

<table>
 <colgroup>
  <col style="width: 30%" />
  <col style="width: 30%" />
  <col style="width: 30%" />
  <col style="width: 10%" />
 </colgroup>
 <thead>
 <tr class="header">
 <th>Updated Command</th>
 <th>Old Command</th>
 <th>What Changed</th>
 <th>Version</th>
 </tr>
 </thead>
 <tbody>
  <tr>
    <td>netq install cluster full interface &lt;text-opta-ifname&gt; bundle &lt;text-bundle-url&gt; config-key &lt;text-opta-key&gt;  workers &lt;text-worker-01&gt; &lt;text-worker-02&gt; <br>and <br>netq install standalone full interface &lt;text-opta-ifname&gt;  bundle &lt;text-bundle-url&gt; config-key &lt;text-opta-key&gt; [proxy-host &lt;text-proxy-host&gt; proxy-port &lt;text-proxy-port&gt;]</td>
    <td>netq install interface &lt;text-opta-ifname&gt; tarball (&lt;text-tarball-name&gt; | download | download &lt;text-opta-version&gt;) config-key &lt;text-opta-key&gt; [proxy-host &lt;text-proxy-host&gt; proxy-port &lt;text-proxy-port&gt;] [file &lt;text-config-file&gt;] [force]</td>
    <td>Separated single command into two commands to support the new clustering feature for on-premises deployments. Removed <em>download</em>, <em>file</em>, and <em>force</em> options.</td>
    <td>2.4.0</td>
  </tr>
  <tr>
    <td>netq install opta cluster full interface &lt;text-opta-ifname&gt; bundle &lt;text-bundle-url&gt; config-key &lt;text-opta-key&gt;  workers &lt;text-worker-01&gt; &lt;text-worker-02&gt; [proxy-host &lt;text-proxy-host&gt; proxy-port &lt;text-proxy-port&gt;]<br>*and*<br>netq install opta standalone full interface &lt;text-opta-ifname&gt; bundle &lt;text-bundle-url&gt; config-key &lt;text-opta-key&gt;</td>
    <td>netq install opta interface &lt;text-opta-ifname&gt; tarball (&lt;text-tarball-name&gt; | download | download &lt;text-opta-version&gt;) config-key &lt;text-opta-key&gt; [proxy-host &lt;text-proxy-host&gt; proxy-port &lt;text-proxy-port&gt;] [file &lt;text-config-file&gt;] [force]</td>
    <td>Separated single command into two commands to support the new clustering feature for cloud deployments. Removed <em>download</em>, <em>file</em>, and <em>force</em> options.</td>
    <td>2.4.0</td>
  </tr>
  <tr>
  <td>netq config del agent (server|agent-url|cluster-servers)</td>
  <td>netq config del agent (server|agent-url)</td>
  <td>Added the ability to remove the agent from servers in a clustered deployment.</td>
  <td>2.4.0</td>
  </tr>
</tbody>
</table>

## Deprecated Commands

The following table summarizes the commands that are present, but no longer active.  A recommended alternative is provided, if appropriate.

<table>
 <colgroup>
  <col style="width: 30%" />
  <col style="width: 40%" />
  <col style="width: 20%" />
  <col style="width: 10%" />
 </colgroup>
 <thead>
 <tr class="header">
 <th>Command</th>
 <th>Status</th>
 <th>Alternate Command</th>
 <th>Version</th>
 </tr>
 </thead>
 <tbody>
  <tr>
    <td>netq [check|show] lnv</td>
    <td>LNV was deprecated in Cumulus Linux 3.7.4 and has been removed from Cumulus Linux 4.0.0. Cumulus NetQ will continue to support and return LNV data as long as you are running a supported version of Cumulus Linux (earlier than 4.0.0) and Cumulus NetQ 2.4.x or earlier. To use these commands with Cumulus NetQ 2.4.x you must enable LNV in the <code>netq.yml</code> configuration file, as it is disabled by default.</td>
    <td>N/A</td>
    <td>2.4.0</td>
  </tr>
  </body>
  </table>
