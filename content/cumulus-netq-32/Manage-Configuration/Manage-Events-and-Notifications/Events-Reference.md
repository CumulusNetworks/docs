---
title: System Event Messages Reference
author: Cumulus Networks
weight: 810
toc: 4
---
The following table lists all system (including threshold-based) event messages organized by type. These messages can be viewed through third-party notification applications. For details about configuring notifications, refer to {{<link title="Configure Notifications">}}.

For a list of What Just Happened events supported, refer to {{<link title="Configure and Monitor What Just Happened Metrics/#view-what-just-happened-metrics" text="WJH Supported Events">}}.

## Agent Events

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 25%" />
<col style="width: 10%" />
<col style="width: 25%" />
<col style="width: 25%" />
</colgroup>
<thead>
<tr class="header">
<th>Type</th>
<th>Trigger</th>
<th>Severity</th>
<th>Message Format</th>
<th>Example</th>
</tr>
</thead>
<tbody>
<tr>
<td>agent</td>
<td>NetQ Agent state changed to Rotten (not heard from within two minutes)</td>
<td>Critical</td>
<td>Agent state changed to rotten</td>
<td>Agent state changed to rotten</td>
</tr>
<tr>
<td>agent</td>
<td>NetQ Agent state changed to Dead (user has decomissioned the agent using NetQ CLI)</td>
<td>Critical</td>
<td>Agent state changed to rotten</td>
<td>Agent state changed to rotten</td>
</tr>
<tr>
<td>agent</td>
<td>NetQ Agent rebooted</td>
<td>Critical</td>
<td>Netq-agent rebooted at (@last_boot)</td>
<td>Netq-agent rebooted at 1573166417</td>
</tr>
<tr>
<td>agent</td>
<td>Node running NetQ Agent rebooted</td>
<td>Critical</td>
<td>Switch rebooted at (@sys_uptime)</td>
<td>Switch rebooted at 1573166131</td>
</tr>
<tr>
<td>agent</td>
<td>NetQ Agent state changed to Fresh</td>
<td>Info</td>
<td>Agent state changed to fresh</td>
<td>Agent state changed to fresh</td>
</tr>
<tr>
<td>agent</td>
<td>NetQ Agent state was reset</td>
<td>Info</td>
<td>Agent state was paused and resumed at (@last_reinit)</td>
<td>Agent state was paused and resumed at 1573166125</td>
</tr>
<tr>
<td>agent</td>
<td>Version of NetQ Agent has changed</td>
<td>Info</td>
<td>Agent version has been changed old_version:@old_version  and new_version:@new_version. Agent reset at @sys_uptime</td>
<td>Agent version has been changed old_version:2.1.2  and new_version:2.3.1. Agent reset at 1573079725</td>
</tr>
</tbody>
</table>

## BGP Events

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 25%" />
<col style="width: 10%" />
<col style="width: 25%" />
<col style="width: 25%" />
</colgroup>
<thead>
<tr class="header">
<th>Type</th>
<th>Trigger</th>
<th>Severity</th>
<th>Message Format</th>
<th>Example</th>
</tr>
</thead>
<tbody>
<tr>
<td>bgp</td>
<td>BGP Session state changed</td>
<td>Critical</td>
<td>BGP session with peer @peer @neighbor vrf @vrf state changed from @old_state to @new_state</td>
<td>BGP session with peer leaf03 leaf04 vrf mgmt state changed from Established to Failed</td>
</tr>
<tr>
<td>bgp</td>
<td>BGP Session state changed from Failed to Established</td>
<td>Info</td>
<td>BGP session with peer @peer @peerhost @neighbor vrf @vrf session state changed from Failed to Established</td>
<td>BGP session with peer swp5 spine02 spine03 vrf default session state changed from Failed to Established</td>
</tr>
<tr>
<td>bgp</td>
<td>BGP Session state changed from Established to Failed</td>
<td>Info</td>
<td>BGP session with peer @peer @neighbor vrf @vrf state changed from established to failed</td>
<td>BGP session with peer leaf03 leaf04 vrf mgmt state changed from down to up</td>
</tr>
<tr>
<td>bgp</td>
<td>The reset time for a BGP session changed</td>
<td>Info</td>
<td>BGP session with peer @peer @neighbor vrf @vrf reset time changed from @old_last_reset_time to @new_last_reset_time</td>
<td>BGP session with peer spine03 swp9 vrf vrf2 reset time changed from 1559427694 to 1559837484</td>
</tr>
</body>
</table>

## BTRFS Events

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 25%" />
<col style="width: 10%" />
<col style="width: 25%" />
<col style="width: 25%" />
</colgroup>
<thead>
<tr class="header">
<th>Type</th>
<th>Trigger</th>
<th>Severity</th>
<th>Message Format</th>
<th>Example</th>
</tr>
</thead>
<tbody>
<tr>
<td>btrfsinfo</td>
<td>Disk space available after BTRFS allocation is less than 80% of partition size or only 2 GB remain.</td>
<td>Critical</td>
<td>@info : @details</td>
<td>high btrfs allocation space : greater than 80% of partition size, 61708420</td>
</tr>
<! -- remove this second event? -->
<tr>
<td>btrfsinfo</td>
<td>Indicates if space would be freed by a rebalance operation on the disk</td>
<td>Critical</td>
<td>@info : @details</td>
<td>data storage efficiency : space left after allocation greater than chunk size 6170849.2","</td>
</tr>
</body>
</table>

## Cable Events

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 25%" />
<col style="width: 10%" />
<col style="width: 25%" />
<col style="width: 25%" />
</colgroup>
<thead>
<tr class="header">
<th>Type</th>
<th>Trigger</th>
<th>Severity</th>
<th>Message Format</th>
<th>Example</th>
</tr>
</thead>
<tbody>
<tr>
<td>cable</td>
<td>Link speed is not the same on both ends of the link</td>
<td>Critical</td>
<td>@ifname speed @speed, mismatched with peer @peer @peer_if speed @peer_speed</td>
<td>swp2 speed 10, mismatched with peer server02 swp8 speed 40</td>
</tr>
<tr>
<td>cable</td>
<td>The speed setting for a given port changed</td>
<td>Info</td>
<td>@ifname speed changed from @old_speed to @new_speed</td>
<td>swp9 speed changed from 10 to 40</td>
</tr>
<tr>
<td>cable</td>
<td>The transceiver status for a given port changed</td>
<td>Info</td>
<td>@ifname transceiver changed from @old_transceiver to @new_transceiver</td>
<td>swp4 transceiver changed from disabled to enabled</td>
</tr>
<tr>
<td>cable</td>
<td>The vendor of a given transceiver changed</td>
<td>Info</td>
<td>@ifname vendor name changed from @old_vendor_name to @new_vendor_name</td>
<td>swp23 vendor name changed from Broadcom to Mellanox</td>
</tr>
<tr>
<td>cable</td>
<td>The part number of a given transceiver changed</td>
<td>Info</td>
<td>@ifname part number changed from @old_part_number to @new_part_number</td>
<td>swp7 part number changed from FP1ZZ5654002A to MSN2700-CS2F0</td>
</tr>
<tr>
<td>cable</td>
<td>The serial number of a given transceiver changed</td>
<td>Info</td>
<td>@ifname serial number changed from @old_serial_number to @new_serial_number</td>
<td>swp4 serial number changed from 571254X1507020 to MT1552X12041</td>
</tr>
<tr>
<td>cable</td>
<td>The status of forward error correction (FEC) support for a given port changed</td>
<td>Info</td>
<td>@ifname supported fec changed from @old_supported_fec to @new_supported_fec</td>
<td>swp12 supported fec changed from supported to unsupported
<p>swp12 supported fec changed from unsupported to supported</td>
</tr>
<tr>
<td>cable</td>
<td>The advertised support for FEC for a given port changed</td>
<td>Info</td>
<td>@ifname supported fec changed from @old_advertised_fec to @new_advertised_fec</td>
<td>swp24 supported FEC changed from advertised to not advertised</td>
</tr>
<tr>
<td>cable</td>
<td>The FEC status for a given port changed</td>
<td>Info</td>
<td>@ifname fec changed from @old_fec to @new_fec</td>
<td>swp15 fec changed from disabled to enabled</td>
</tr>
</body>
</table>

## CLAG/MLAG Events

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 25%" />
<col style="width: 10%" />
<col style="width: 25%" />
<col style="width: 25%" />
</colgroup>
<thead>
<tr class="header">
<th>Type</th>
<th>Trigger</th>
<th>Severity</th>
<th>Message Format</th>
<th>Example</th>
</tr>
</thead>
<tbody>
<tr>
<td>clag</td>
<td>CLAG remote peer state changed from up to down</td>
<td>Critical</td>
<td>Peer state changed to down</td>
<td>Peer state changed to down</td>
</tr>
<! -- <tr>
<td>clag</td>
<td>Local CLAG host MTU does not match its remote peer MTU</td>
<td>Critical</td>
<td>SVI @svi1 on vlan @vlan mtu @mtu1 mismatched with peer mtu @mtu2</td>
<td>SVI svi7 on vlan 4 mtu 1592 mistmatched with peer mtu 1680</td>
</tr>
<tr>
<td>clag</td>
<td>CLAG SVI on VLAN is missing from remote peer state</td>
<td>Warning</td>
<td>SVI on vlan @vlan is missing from peer</td>
<td>SVI on vlan vlan4 is missing from peer</td>
</tr>
<tr>
<td>clag</td>
<td>CLAG peerlink is not opperating at full capacity. At least one link is down.</td>
<td>Warning</p></td>
<td>Clag peerlink not at full redundancy, member link @slave is down</td>
<td>Clag peerlink not at full redundancy, member link swp40 is down</td>
</tr> -->
<tr>
<td>clag</td>
<td>CLAG remote peer state changed from down to up</td>
<td>Info</td>
<td>Peer state changed to up</td>
<td>Peer state changed to up</td>
</tr>
<tr>
<td>clag</td>
<td>Local CLAG host state changed from down to up</td>
<td>Info</td>
<td>Clag state changed from down to up</td>
<td>Clag state changed from down to up</td>
</tr>
<tr>
<td>clag</td>
<td>CLAG bond in Conflicted state was updated with new bonds</td>
<td>Info</td>
<td>Clag conflicted bond changed from @old_conflicted_bonds to @new_conflicted_bonds</td>
<td>Clag conflicted bond changed from swp7 swp8 to @swp9 swp10</td>
</tr>
<tr>
<td>clag</td>
<td>CLAG bond changed state from protodown to up state</td>
<td>Info</td>
<td>Clag conflicted bond changed from @old_state_protodownbond to @new_state_protodownbond</td>
<td>Clag conflicted bond changed from protodown to up</td>
</tr>
</body>
</table>

## CL Support Evemts

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 25%" />
<col style="width: 10%" />
<col style="width: 25%" />
<col style="width: 25%" />
</colgroup>
<thead>
<tr class="header">
<th>Type</th>
<th>Trigger</th>
<th>Severity</th>
<th>Message Format</th>
<th>Example</th>
</tr>
</thead>
<tbody>
<tr>
<td>clsupport</td>
<td>A new CL Support file has been created for the given node</td>
<td>Critical</td>
<td>HostName @hostname has new CL SUPPORT file</td>
<td>HostName leaf01 has new CL SUPPORT file</td>
</tr>
</body>
</table>

## Config Diff Events

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 25%" />
<col style="width: 10%" />
<col style="width: 25%" />
<col style="width: 25%" />
</colgroup>
<thead>
<tr class="header">
<th>Type</th>
<th>Trigger</th>
<th>Severity</th>
<th>Message Format</th>
<th>Example</th>
</tr>
</thead>
<tbody>
<tr>
<td>configdiff</td>
<td>Configuration file deleted on a device</td>
<td>Critical</td>
<td>@hostname config file @type was deleted</td>
<td>spine03 config file /etc/frr/frr.conf was deleted</td>
</tr>
<tr>
<td>configdiff</td>
<td>Configuration file has been created</td>
<td>Info</td>
<td>@hostname config file @type was created</td>
<td>leaf12 config file /etc/lldp.d/README.conf was created</td>
</tr>
<tr>
<td>configdiff</td>
<td>Configuration file has been modified</td>
<td>Info</td>
<td>@hostname config file @type was modified</td>
<td>spine03 config file /etc/frr/frr.conf was modified</td>
</tr>
</body>
</table>

## EVPN Events

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 25%" />
<col style="width: 10%" />
<col style="width: 25%" />
<col style="width: 25%" />
</colgroup>
<thead>
<tr class="header">
<th>Type</th>
<th>Trigger</th>
<th>Severity</th>
<th>Message Format</th>
<th>Example</th>
</tr>
</thead>
<tbody>
<tr>
<td>evpn</td>
<td>A VNI was configured and moved from the up state to the down state</td>
<td>Critical</td>
<td>VNI @vni state changed from up to down</td>
<td>VNI 36 state changed from up to down</td>
</tr>
<tr>
<td>evpn</td>
<td>A VNI was configured and moved from the down state to the up state</td>
<td>Info</td>
<td>VNI @vni state changed from down to up</td>
<td>VNI 36 state changed from down to up</td>
</tr>
<tr>
<td>evpn</td>
<td>The kernel state changed on a VNI</td>
<td>Info</td>
<td>VNI @vni kernel state changed from @old_in_kernel_state to @new_in_kernel_state</td>
<td>VNI 3 kernel state changed from down to up</td>
</tr>
<tr>
<td>evpn</td>
<td>A VNI state changed from not advertising all VNIs to advertising all VNIs</td>
<td>Info</td>
<td>VNI @vni vni state changed from @old_adv_all_vni_state to @new_adv_all_vni_state</td>
<td>VNI 11 vni state changed from false to true</td>
</tr>
</body>
</table>

## Lifecycle Management Events

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 25%" />
<col style="width: 10%" />
<col style="width: 25%" />
<col style="width: 25%" />
</colgroup>
<thead>
<tr class="header">
<th>Type</th>
<th>Trigger</th>
<th>Severity</th>
<th>Message Format</th>
<th>Example</th>
</tr>
</thead>
<tbody>
<tr>
<td>lcm</td>
<td>Cumulus Linux backup started for a switch or host</td>
<td>Info</td>
<td>CL configuration backup started for hostname @hostname</td>
<td>CL configuration backup started for hostname spine01</td>
</tr>
<tr>
<td>lcm</td>
<td>Cumulus Linux backup completed for a switch or host</td>
<td>Info</td>
<td>CL configuration backup completed for hostname @hostname</td>
<td>CL configuration backup completed for hostname spine01</td>
</tr>
<tr>
<td>lcm</td>
<td>Cumulus Linux backup failed for a switch or host</td>
<td>Critical</td>
<td>CL configuration backup failed for hostname @hostname</td>
<td>CL configuration backup failed for hostname spine01</td>
</tr>
<tr>
<td>lcm</td>
<td>Cumulus Linux upgrade from one version to a newer version has started for a switch or host</td>
<td>Critical</td>
<td>CL Image upgrade from version @old_cl_version to version @new_cl_version started for hostname @hostname</td>
<td>CL Image upgrade from version 4.1.0 to version 4.2.1 started for hostname server01</td>
</tr>
<tr>
<td>lcm</td>
<td>Cumulus Linux upgrade from one version to a newer version has completed successfully for a switch or host</td>
<td>Info</td>
<td>CL Image upgrade from version @old_cl_version to version @new_cl_version completed for hostname @hostname</td>
<td>CL Image upgrade from version 4.1.0 to version 4.2.1 completed for hostname server01</td>
</tr>
<tr>
<td>lcm</td>
<td>Cumulus Linux upgrade from one version to a newer version has failed for a switch or host</td>
<td>Critical</td>
<td>CL Image upgrade from version @old_cl_version to version @new_cl_version failed for hostname @hostname</td>
<td>CL Image upgrade from version 4.1.0 to version 4.2.1 failed for hostname server01</td>
</tr>
<tr>
<td>lcm</td>
<td>Restoration of a Cumulus Linux configuration started for a switch or host</td>
<td>Info</td>
<td>CL configuration restore started for hostname @hostname</td>
<td>CL configuration restore started for hostname leaf01</td>
</tr>
<tr>
<td>lcm</td>
<td>Restoration of a Cumulus Linux configuration completed successfully for a switch or host</td>
<td>Info</td>
<td>CL configuration restore completed for hostname @hostname</td>
<td>CL configuration restore completed for hostname leaf01</td>
</tr>
<tr>
<td>lcm</td>
<td>Restoration of a Cumulus Linux configuration failed for a switch or host</td>
<td>Critical</td>
<td>CL configuration restore failed for hostname @hostname</td>
<td>CL configuration restore failed for hostname leaf01</td>
</tr>
<tr>
<td>lcm</td>
<td>Rollback of a Cumulus Linux image has started for a switch or host</td>
<td>Critical</td>
<td>CL Image rollback from version @old_cl_version to version @new_cl_version started for hostname @hostname</td>
<td>CL Image rollback from version 4.2.1 to version 4.1.0 started for hostname leaf01</td>
</tr>
<tr>
<td>lcm</td>
<td>Rollback of a Cumulus Linux image has completed successfully for a switch or host</td>
<td>Info</td>
<td>CL Image rollback from version @old_cl_version to version @new_cl_version completed for hostname @hostname</td>
<td>CL Image rollback from version 4.2.1 to version 4.1.0 completed for hostname leaf01</td>
</tr>
<tr>
<td>lcm</td>
<td>Rollback of a Cumulus Linux image has failed for a switch or host</td>
<td>Critical</td>
<td>CL Image rollback from version @old_cl_version to version @new_cl_version failed for hostname @hostname</td>
<td>CL Image rollback from version 4.2.1 to version 4.1.0 failed for hostname leaf01</td>
</tr>
<tr>
<td>lcm</td>
<td>Installation of a Cumulus NetQ image has started for a switch or host</td>
<td>Info</td>
<td>NetQ Image version @netq_version installation started for hostname @hostname</td>
<td>NetQ Image version 3.2.0 installation started for hostname spine02</td>
</tr>
<tr>
<td>lcm</td>
<td>Installation of a Cumulus NetQ image has completed successfully for a switch or host</td>
<td>Info</td>
<td>NetQ Image version @netq_version installation completed for hostname @hostname</td>
<td>NetQ Image version 3.2.0 installation completed for hostname spine02</td>
</tr>
<tr>
<td>lcm</td>
<td>Installation of a Cumulus NetQ image has failed for a switch or host</td>
<td>Critical</td>
<td>NetQ Image version @netq_version installation failed for hostname @hostname</td>
<td>NetQ Image version 3.2.0 installation failed for hostname spine02</td>
</tr>
<tr>
<td>lcm</td>
<td>Upgrade of a Cumulus NetQ image has started for a switch or host</td>
<td>Info</td>
<td>NetQ Image upgrade from version @old_netq_version to version @netq_version started for hostname @hostname</td>
<td>NetQ Image upgrade from version 3.1.0 to version 3.2.0 started for hostname spine02</td>
</tr>
<tr>
<td>lcm</td>
<td>Upgrade of a Cumulus NetQ image has completed successfully for a switch or host</td>
<td>Info</td>
<td>NetQ Image upgrade from version @old_netq_version to version @netq_version completed for hostname @hostname</td>
<td>NetQ Image upgrade from version 3.1.0 to version 3.2.0 completed for hostname spine02</td>
</tr>
<tr>
<td>lcm</td>
<td>Upgrade of a Cumulus NetQ image has failed for a switch or host</td>
<td>Critical</td>
<td>NetQ Image upgrade from version @old_netq_version to version @netq_version failed for hostname @hostname</td>
<td>NetQ Image upgrade from version 3.1.0 to version 3.2.0 failed for hostname spine02</td>
</tr>
</body>
</table>

## Cumulus Linux License Events

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 25%" />
<col style="width: 10%" />
<col style="width: 25%" />
<col style="width: 25%" />
</colgroup>
<thead>
<tr class="header">
<th>Type</th>
<th>Trigger</th>
<th>Severity</th>
<th>Message Format</th>
<th>Example</th>
</tr>
</thead>
<tbody>
<tr>
<td>license</td>
<td>License state is missing or invalid</td>
<td>Critical</td>
<td>License check failed, name @lic_name state @state</td>
<td>License check failed, name agent.lic state invalid</td>
</tr>
<tr>
<td>license</td>
<td>License state is missing or invalid on a particular device</td>
<td>Critical</td>
<td>License check failed on @hostname</td>
<td>License check failed on leaf03</td>
</tr>
</body>
</table>

## Link Events

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 25%" />
<col style="width: 10%" />
<col style="width: 25%" />
<col style="width: 25%" />
</colgroup>
<thead>
<tr class="header">
<th>Type</th>
<th>Trigger</th>
<th>Severity</th>
<th>Message Format</th>
<th>Example</th>
</tr>
</thead>
<tbody>
<tr>
<td>link</td>
<td>Link operational state changed from up to down</td>
<td>Critical</td>
<td>HostName @hostname changed state from @old_state to @new_state Interface:@ifname</td>
<td>HostName leaf01 changed state from up to down Interface:swp34</td>
</tr>
<tr>
<td>link</td>
<td>Link operational state changed from down to up</td>
<td>Info</td>
<td>HostName @hostname changed state from @old_state to @new_state Interface:@ifname</td>
<td>HostName leaf04 changed state from down to up Interface:swp11</td>
</tr>
</body>
</table>

## LLDP Events

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 25%" />
<col style="width: 10%" />
<col style="width: 25%" />
<col style="width: 25%" />
</colgroup>
<thead>
<tr class="header">
<th>Type</th>
<th>Trigger</th>
<th>Severity</th>
<th>Message Format</th>
<th>Example</th>
</tr>
</thead>
<tbody>
<tr>
<td>lldp</td>
<td>Local LLDP host has new neighbor information</td>
<td>Info</td>
<td>LLDP Session with host @hostname and @ifname modified fields @changed_fields</td>
<td>LLDP Session with host leaf02 swp6 modified fields leaf06 swp21</td>
</tr>
<tr>
<td>lldp</td>
<td>Local LLDP host has new peer interface name</td>
<td>Info</td>
<td>LLDP Session with host @hostname and @ifname @old_peer_ifname changed to @new_peer_ifname</td>
<td>LLDP Session with host spine01 and swp5 swp12 changed to port12</td>
</tr>
<tr>
<td>lldp</td>
<td>Local LLDP host has new peer hostname</td>
<td>Info</td>
<td>LLDP Session with host @hostname and @ifname @old_peer_hostname changed to @new_peer_hostname</td>
<td>LLDP Session with host leaf03 and swp2 leaf07 changed to exit01</td>
</tr>
</body>
</table>

## MTU Events

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 25%" />
<col style="width: 10%" />
<col style="width: 25%" />
<col style="width: 25%" />
</colgroup>
<thead>
<tr class="header">
<th>Type</th>
<th>Trigger</th>
<th>Severity</th>
<th>Message Format</th>
<th>Example</th>
</tr>
</thead>
<tbody>
<tr>
<td>mtu</td>
<td>VLAN interface link MTU is smaller than that of its parent MTU</td>
<td>Warning</td>
<td>vlan interface @link mtu @mtu is smaller than parent @parent mtu @parent_mtu</td>
<td>vlan interface swp3 mtu 1500 is smaller than parent peerlink-1 mtu 1690</td>
</tr>
<tr>
<td>mtu</td>
<td>Bridge interface MTU is smaller than the member interface with the smallest MTU</td>
<td>Warning</td>
<td>bridge @link mtu @mtu is smaller than least of member interface mtu @min</td>
<td>bridge swp0 mtu 1280 is smaller than least of member interface mtu 1500</td>
</tr>
</body>
</table>

## NTP Events

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 25%" />
<col style="width: 10%" />
<col style="width: 25%" />
<col style="width: 25%" />
</colgroup>
<thead>
<tr class="header">
<th>Type</th>
<th>Trigger</th>
<th>Severity</th>
<th>Message Format</th>
<th>Example</th>
</tr>
</thead>
<tbody>
<tr>
<td>ntp</td>
<td>NTP sync state changed from in sync to not in sync</td>
<td>Critical</td>
<td>Sync state changed from @old_state to @new_state for @hostname</td>
<td>Sync state changed from in sync to not sync for leaf06</td>
</tr>
<tr>
<td>ntp</td>
<td>NTP sync state changed from not in sync to in sync</td>
<td>Info</td>
<td>Sync state changed from @old_state to @new_state for @hostname</td>
<td>Sync state changed from not sync to in sync for leaf06</td>
</tr>
</body>
</table>

## OSPF Events

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 25%" />
<col style="width: 10%" />
<col style="width: 25%" />
<col style="width: 25%" />
</colgroup>
<thead>
<tr class="header">
<th>Type</th>
<th>Trigger</th>
<th>Severity</th>
<th>Message Format</th>
<th>Example</th>
</tr>
</thead>
<tbody>
<tr>
<td>ospf</td>
<td>OSPF session state on a given interface changed from Full to a down state</td>
<td>Critical</td>
<td>OSPF session @ifname with @peer_address changed from Full to @down_state</td>
<td><p>OSPF session swp7 with 27.0.0.18 state changed from Full to Fail</p>
<p>OSPF session swp7 with 27.0.0.18 state changed from Full to ExStart</p></td>
</tr><tr>
<td>ospf</td>
<td>OSPF session state on a given interface changed from a down state to full</td>
<td>Info</td>
<td>OSPF session @ifname with @peer_address changed from @down_state to Full</td>
<td><p>OSPF session swp7 with 27.0.0.18 state changed from Down to Full</p>
<p>OSPF session swp7 with 27.0.0.18 state changed from Init to Full</p>
<p>OSPF session swp7 with 27.0.0.18 state changed from Fail to Full</p></td>
</tr>
</body>
</table>

## Package Information Events

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 25%" />
<col style="width: 10%" />
<col style="width: 25%" />
<col style="width: 25%" />
</colgroup>
<thead>
<tr class="header">
<th>Type</th>
<th>Trigger</th>
<th>Severity</th>
<th>Message Format</th>
<th>Example</th>
</tr>
</thead>
<tbody>
<tr>
<td>packageinfo</td>
<td>Package version on device does not match the version identified in the existing manifest</td>
<td>Critical</td>
<td>@package_name manifest version mismatch</td>
<td>netq-apps manifest version mismatch</td>
</tr>
</body>
</table>

## PTM Events

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 25%" />
<col style="width: 10%" />
<col style="width: 25%" />
<col style="width: 25%" />
</colgroup>
<thead>
<tr class="header">
<th>Type</th>
<th>Trigger</th>
<th>Severity</th>
<th>Message Format</th>
<th>Example</th>
</tr>
</thead>
<tbody>
<tr>
<td>ptm</td>
<td>Physical interface cabling does not match configuration specified in <em>topology.dot</em> file</td>
<td>Critical</td>
<td>PTM cable status failed</td>
<td>PTM cable status failed</td>
</tr>
<tr>
<td>ptm</td>
<td>Physical interface cabling matches configuration specified in <em>topology.dot</em> file</td>
<td>Critical</td>
<td>PTM cable status passed</td>
<td>PTM cable status passed</td>
</tr>
</body>
</table>

## Resource Events

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 25%" />
<col style="width: 10%" />
<col style="width: 25%" />
<col style="width: 25%" />
</colgroup>
<thead>
<tr class="header">
<th>Type</th>
<th>Trigger</th>
<th>Severity</th>
<th>Message Format</th>
<th>Example</th>
</tr>
</thead>
<tbody>
<tr>
<td>resource</td>
<td>A physical resource has been deleted from a device</td>
<td>Critical</td>
<td>Resource Utils deleted for @hostname</td>
<td>Resource Utils deleted for spine02</td>
</tr>
<tr>
<td>resource</td>
<td>Root file system access on a device has changed from Read/Write to Read Only</td>
<td>Critical</td>
<td>@hostname root file system access mode set to Read Only</td>
<td>server03 root file system access mode set to Read Only</td>
</tr>
<tr>
<td>resource</td>
<td>Root file system access on a device has changed from Read Only to Read/Write</td>
<td>Info</td>
<td>@hostname root file system access mode set to Read/Write</td>
<td>leaf11 root file system access mode set to Read/Write</td>
</tr>
<tr>
<td>resource</td>
<td>A physical resource has been added to a device</td>
<td>Info</td>
<td>Resource Utils added for @hostname</td>
<td>Resource Utils added for spine04</td>
</tr>
</body>
</table>

## Running Config Diff Events

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 25%" />
<col style="width: 10%" />
<col style="width: 25%" />
<col style="width: 25%" />
</colgroup>
<thead>
<tr class="header">
<th>Type</th>
<th>Trigger</th>
<th>Severity</th>
<th>Message Format</th>
<th>Example</th>
</tr>
</thead>
<tbody>
<tr>
<td>runningconfigdiff</td>
<td>Running configuration file has been modified</td>
<td>Info</td>
<td>@commandname config result was modified</td>
<td>@commandname config result was modified</td>
</tr>
</body>
</table>

## Sensor Events

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 25%" />
<col style="width: 10%" />
<col style="width: 25%" />
<col style="width: 25%" />
</colgroup>
<thead>
<tr class="header">
<th>Type</th>
<th>Trigger</th>
<th>Severity</th>
<th>Message Format</th>
<th>Example</th>
</tr>
</thead>
<tbody>
<tr>
<td>sensor</td>
<td>A fan or power supply unit sensor has changed state</td>
<td>Critical</td>
<td>Sensor @sensor state changed from @old_s_state to @new_s_state</td>
<td>Sensor fan state changed from up to down</td>
</tr>
<tr>
<td>sensor</td>
<td>A temperature sensor has crossed the maximum threshold for that sensor</td>
<td>Critical</td>
<td>Sensor @sensor max value @new_s_max exceeds threshold @new_s_crit</td>
<td>Sensor temp max value 110 exceeds the threshold 95</td>
</tr>
<tr>
<td>sensor</td>
<td>A temperature sensor has crossed the minimum threshold for that sensor</td>
<td>Critical</td>
<td>Sensor @sensor min value @new_s_lcrit fall behind threshold @new_s_min</td>
<td>Sensor psu min value 10 fell below threshold 25</td>
</tr>
<tr>
<td>sensor</td>
<td>A temperature, fan, or power supply sensor state changed</td>
<td>Info</td>
<td>Sensor @sensor state changed from @old_state to @new_state</td>
<td><p>Sensor temperature state changed from critical to ok</p>
<p>Sensor fan state changed from absent to ok</p>
<p>Sensor psu state changed from bad to ok</p></td>
</tr>
<tr>
<td>sensor</td>
<td>A fan or power supply sensor state changed</td>
<td>Info</td>
<td>Sensor @sensor state changed from @old_s_state to @new_s_state</td>
<td><p>Sensor fan state changed from down to up</p>
<p>Sensor psu state changed from down to up</p></td>
</tr>
<tr>
<td>sensor</td>
<td>A fan or power supply unit sensor is in a new state</td>
<td>Critical</td>
<td>Sensor @sensor state is @new_s_state</td>
<td>Sensor psu state is bad</td>
</tr>
</body>
</table>

## Services Events

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 25%" />
<col style="width: 10%" />
<col style="width: 25%" />
<col style="width: 25%" />
</colgroup>
<thead>
<tr class="header">
<th>Type</th>
<th>Trigger</th>
<th>Severity</th>
<th>Message Format</th>
<th>Example</th>
</tr>
</thead>
<tbody>
<tr>
<td>services</td>
<td>A service status changed from down to up</td>
<td>Critical</td>
<td>Service @name status changed from @old_status to @new_status</td>
<td>Service bgp status changed from down to up</td>
</tr>
<tr>
<td>services</td>
<td>A service status changed from up to down</td>
<td>Critical</td>
<td>Service @name status changed from @old_status to @new_status</td>
<td>Service lldp status changed from up to down</td>
</tr>
<tr>
<td>services</td>
<td>A service changed state from inactive to active</td>
<td>Info</td>
<td>Service @name changed state from inactive to active</td>
<td><p>Service bgp changed state from inactive to active</p>
<p>Service lldp changed state from inactive to active</p></td>
</tr>
</body>
</table>

## SSD Utilization Events

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 25%" />
<col style="width: 10%" />
<col style="width: 25%" />
<col style="width: 25%" />
</colgroup>
<thead>
<tr class="header">
<th>Type</th>
<th>Trigger</th>
<th>Severity</th>
<th>Message Format</th>
<th>Example</th>
</tr>
</thead>
<tbody>
<tr>
<td>ssdutil</td>
<td>3ME3 disk health has dropped below 10%</td>
<td>Critical</td>
<td>@info: @details</td>
<td>low health : 5.0%</td>
</tr>
<tr>
<td>ssdutil</td>
<td>A dip in 3ME3 disk health of more than 2% has occurred within the last 24 hours</td>
<td>Critical</td>
<td>@info: @details</td>
<td>significant health drop : 3.0%</td>
</tr>
</body>
</table>

## Threshold-based Events

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 25%" />
<col style="width: 10%" />
<col style="width: 25%" />
<col style="width: 25%" />
</colgroup>
<thead>
<tr class="header">
<th>Type</th>
<th>Trigger</th>
<th>Severity</th>
<th>Message Format</th>
<th>Example</th>
</tr>
</thead>
<tbody>
<tr>
<td>tca</td>
<td>Percentage of CPU utilization exceeded user-defined maximum threshold on a switch</td>
<td>Critical</td>
<td>CPU Utilization for host @hostname exceed configured mark @cpu_utilization</td>
<td>CPU Utilization for host leaf11 exceed configured mark 85</td>
</tr>
<tr>
<td>tca</td>
<td>Percentage of disk utilization exceeded user-defined maximum threshold on a switch</td>
<td>Critical</td>
<td>Disk Utilization for host @hostname exceed configured mark @disk_utilization</td>
<td>Disk Utilization for host leaf11 exceed configured mark 90</td>
</tr>
<tr>
<td>tca</td>
<td>Percentage of memory utilization exceeded user-defined maximum threshold on a switch</td>
<td>Critical</td>
<td>Memory Utilization for host @hostname exceed configured mark @mem_utilization</td>
<td>Memory Utilization for host leaf11 exceed configured mark 95</td>
</tr>
<tr>
<td>tca</td>
<td>Number of transmit bytes exceeded user-defined maximum threshold on a switch interface</td>
<td>Critical</td>
<td>TX bytes upper threshold breached for host @hostname ifname:@ifname value: @tx_bytes</td>
<td>TX bytes upper threshold breached for host spine02 ifname:swp4 value: 20000</td>
</tr>
<tr>
<td>tca</td>
<td>Number of broadcast transmit bytes exceeded user-defined maximum threshold on a switch interface</td>
<td>Critical</td>
<td>TX broadcast upper threshold breached for host @hostname ifname:@ifname value: @rx_broadcast</td>
<td>TX broadcast upper threshold breached for host leaf04 ifname:swp45 value: 40200</td>
</tr>
<tr>
<td>tca</td>
<td>Number of multicast transmit bytes exceeded user-defined maximum threshold on a switch interface</td>
<td>Critical</td>
<td>TX multicast upper threshold breached for host @hostname ifname:@ifname value: @rx_broadcast</td>
<td>TX multicast upper threshold breached for host leaf04 ifname:swp45 value: 30000</td>
</tr>
<tr>
<td>tca</td>
<td>Number of receive bytes exceeded user-defined maximum threshold on a switch interface</td>
<td>Critical</td>
<td>RX bytes upper threshold breached for host @hostname ifname:@ifname value: @tx_bytes</td>
<td>RX bytes upper threshold breached for host spine02 ifname:swp4 value: 20000</td>
</tr>
<tr>
<td>tca</td>
<td>Number of broadcast receive bytes exceeded user-defined maximum threshold on a switch interface</td>
<td>Critical</td>
<td>RX broadcast upper threshold breached for host @hostname ifname:@ifname value: @rx_broadcast</td>
<td>RX broadcast upper threshold breached for host leaf04 ifname:swp45 value: 40200</td>
</tr>
<tr>
<td>tca</td>
<td>Number of multicast receive bytes exceeded user-defined maximum threshold on a switch interface</td>
<td>Critical</td>
<td>RX multicast upper threshold breached for host @hostname ifname:@ifname value: @rx_broadcast</td>
<td>RX multicast upper threshold breached for host leaf04 ifname:swp45 value: 30000</td>
</tr>
<tr>
<td>tca</td>
<td>Fan speed exceeded user-defined maximum threshold on a switch</td>
<td>Critical</td>
<td>Sensor for @hostname exceeded threshold fan speed @s_input for sensor @s_name</td>
<td>Sensor for spine03 exceeded threshold fan speed 700 for sensor fan2</td>
</tr>
<tr>
<td>tca</td>
<td>Power supply output exceeded user-defined maximum threshold on a switch</td>
<td>Critical</td>
<td>Sensor for @hostname exceeded threshold power @s_input watts for sensor @s_name</td>
<td>Sensor for leaf14 exceeded threshold power 120 watts for sensor psu1</td>
</tr>
<tr>
<td>tca</td>
<td>Temperature (&#176 C) exceeded user-defined maximum threshold on a switch</td>
<td>Critical</td>
<td>Sensor for @hostname exceeded threshold temperature @s_input for sensor @s_name</td>
<td>Sensor for leaf14 exceeded threshold temperature 90 for sensor temp1</td>
</tr>
<tr>
<td>tca</td>
<td>Power supply voltage exceeded user-defined maximum threshold on a switch</td>
<td>Critical</td>
<td>Sensor for @hostname exceeded threshold voltage @s_input volts for sensor @s_name</td>
<td>Sensor for leaf14 exceeded threshold voltage 12 volts for sensor psu2</td>
</tr>
</body>
</table>

## Version Events

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 25%" />
<col style="width: 10%" />
<col style="width: 25%" />
<col style="width: 25%" />
</colgroup>
<thead>
<tr class="header">
<th>Type</th>
<th>Trigger</th>
<th>Severity</th>
<th>Message Format</th>
<th>Example</th>
</tr>
</thead>
<tbody>
<tr>
<td>version</td>
<td>An unknown version of the operating system was detected</td>
<td>Critical</td>
<td>unexpected os version @my_ver</td>
<td>unexpected os version cl3.2</td>
</tr>
<tr>
<td>version</td>
<td>Desired version of the operating system is not available</td>
<td>Critical</td>
<td>os version @ver</td>
<td>os version cl3.7.9</td>
</tr>
<tr>
<td>version</td>
<td>An unknown version of a software package was detected</td>
<td>Critical</td>
<td>expected release version @ver</td>
<td>expected release version cl3.6.2</td>
</tr>
<tr>
<td>version</td>
<td>Desired version of a software package is not available</td>
<td>Critical</td>
<td>different from version @ver</td>
<td>different from version cl4.0</td>
</tr>
</body>
</table>

## VXLAN Events

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 25%" />
<col style="width: 10%" />
<col style="width: 25%" />
<col style="width: 25%" />
</colgroup>
<thead>
<tr class="header">
<th>Type</th>
<th>Trigger</th>
<th>Severity</th>
<th>Message Format</th>
<th>Example</th>
</tr>
</thead>
<tbody>
<tr>
<td>vxlan</td>
<td>Replication list is contains an inconsistent set of nodes<></td>
<td>Critical<></td>
<td>VNI @vni replication list inconsistent with @conflicts diff:@diff<></td>
<td>VNI 14 replication list inconsistent with ["leaf03","leaf04"] diff:+:["leaf03","leaf04"] -:["leaf07","leaf08"]</td>
</tr>
</tbody>
</table>
