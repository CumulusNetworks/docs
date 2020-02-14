---
title: Events Reference
author: Cumulus Networks
weight: 328
aliases:
 - /display/NETQ/Monitor+Events
 - /pages/viewpage.action?pageId=12321771
pageID: 12321771
product: Cumulus NetQ
version: 2.4
imgData: cumulus-netq
siteSlug: cumulus-netq
toc: 4
---
The following table lists all event messages organized by type.

The messages can be viewed through third-party notification
applications. For details about configuring notifications using the NetQ
CLI, refer to [Integrate NetQ with Notification Applications](../../../Cumulus-NetQ-Integration-Guide/Integrate-NetQ-with-Notification-Applications).

For information about configuring threshold-based events (TCAs), refer to [Configure Threshold-based Events](../../Monitor-Events/Config-TCA-Events/).

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 30%" />
<col style="width: 10%" />
<col style="width: 20%" />
<col style="width: 20%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Type</p></th>
<th><p>Trigger</p></th>
<th><p>Severity</p></th>
<th><p>Message Format</p></th>
<th><p>Example</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>agent</p></td>
<td><p>NetQ Agent state changed to Rotten (not heard from in over 15 seconds)</p></td>
<td><p>Critical</p></td>
<td><p>Agent state changed to rotten</p></td>
<td><p>Agent state changed to rotten</p></td>
</tr>
<tr class="even">
<td><p>agent</p></td>
<td><p>NetQ Agent rebooted</p></td>
<td><p>Critical</p></td>
<td><p>Netq-agent rebooted at (@last_boot)</p></td>
<td><p>Netq-agent rebooted at 1573166417</p></td>
</tr>
<tr class="odd">
<td><p>agent</p></td>
<td><p>Node running NetQ Agent rebooted</p></td>
<td><p>Critical</p></td>
<td><p>Switch rebooted at (@sys_uptime)</p></td>
<td><p>Switch rebooted at 1573166131</p></td>
</tr>
<tr class="even">
<td><p>agent</p></td>
<td><p>NetQ Agent state changed to Fresh</p></td>
<td><p>Info</p></td>
<td><p>Agent state changed to fresh</p></td>
<td><p>Agent state changed to fresh</p></td>
</tr>
<tr class="odd">
<td><p>agent</p></td>
<td><p>NetQ Agent state was reset</p></td>
<td><p>Info</p></td>
<td><p>Agent state was paused and resumed at (@last_reinit)</p></td>
<td><p>Agent state was paused and resumed at 1573166125</p></td>
</tr>
<tr class="even">
<td><p>agent</p></td>
<td><p>Version of NetQ Agent has changed</p></td>
<td><p>Info</p></td>
<td><p>Agent version has been changed old_version:@old_version  and new_version:@new_version. Agent reset at @sys_uptime</p></td>
<td><p>Agent version has been changed old_version:2.1.2  and new_version:2.3.1. Agent reset at 1573079725</p></td>
</tr>
<tr class="odd">
<td><p>bgp</p></td>
<td><p>BGP Session state changed</p></td>
<td><p>Critical</p></td>
<td><p>BGP session with peer @peer @neighbor vrf @vrf state changed from @old_state to @new_state</p></td>
<td><p>BGP session with peer leaf03 leaf04 vrf mgmt state changed from Established to Failed</p></td>
</tr>
<tr class="even">
<td><p>bgp</p></td>
<td><p>BGP Session state changed from Failed to Established</p></td>
<td><p>Info</p></td>
<td><p>BGP session with peer @peer @peerhost @neighbor vrf @vrf session state changed from Failed to Established</p></td>
<td><p>BGP session with peer swp5 spine02 spine03 vrf default session state changed from Failed to Established</p></td>
</tr>
<tr class="odd">
<td><p>bgp</p></td>
<td><p>BGP Session state changed from Established to Failed</p></td>
<td><p>Info</p></td>
<td><p>BGP session with peer @peer @neighbor vrf @vrf state changed from established to failed</p></td>
<td><p>BGP session with peer leaf03 leaf04 vrf mgmt state changed from down to up</p></td>
</tr>
<tr class="even">
<td><p>bgp</p></td>
<td><p>The reset time for a BGP session changed</p></td>
<td><p>Info</p></td>
<td><p>BGP session with peer @peer @neighbor vrf @vrf reset time changed from @old_last_reset_time to @new_last_reset_time</p></td>
<td><p>BGP session with peer spine03 swp9 vrf vrf2 reset time changed from 1559427694 to 1559837484</p></td>
</tr>
<tr class="odd">
<td><p>btrfsinfo</p></td>
<td><p>Disk space available after BTRFS allocation is less than 80% of partition size or only 2 GB remain.</p></td>
<td><p>Critical</p></td>
<td><p>@info : @details</p></td>
<td><p>high btrfs allocation space : greater than 80% of partition size, 61708420</p></td>
</tr>
<tr class="even">
<td><p>btrfsinfo</p></td>
<td><p>Indicates if space would be freed by a rebalance operation on the disk</p></td>
<td><p>Critical</p></td>
<td><p>@info : @details</p></td>
<td><p>data storage efficiency : space left after allocation greater than chunk size 6170849.2","</p></td>
</tr>
<tr class="odd">
<td><p>cable</p></td>
<td><p>Link speed is not the same on both ends of the link</p></td>
<td><p>Critical</p></td>
<td><p>@ifname speed @speed, mismatched with peer @peer @peer_if speed @peer_speed</p></td>
<td><p>swp2 speed 10, mismatched with peer server02 swp8 speed 40</p></td>
</tr>
<tr class="even">
<td><p>cable</p></td>
<td><p>The speed setting for a given port changed</p></td>
<td><p>Info</p></td>
<td><p>@ifname speed changed from @old_speed to @new_speed</p></td>
<td><p>swp9 speed changed from 10 to 40</p></td>
</tr>
<tr class="odd">
<td><p>cable</p></td>
<td><p>The transceiver status for a given port changed</p></td>
<td><p>Info</p></td>
<td><p>@ifname transceiver changed from @old_transceiver to @new_transceiver</p></td>
<td><p>swp4 transceiver changed from disabled to enabled</p></td>
</tr>
<tr class="even">
<td><p>cable</p></td>
<td><p>The vendor of a given transceiver changed</p></td>
<td><p>Info</p></td>
<td><p>@ifname vendor name changed from @old_vendor_name to @new_vendor_name</p></td>
<td><p>swp23 vendor name changed from Broadcom to Mellanox</p></td>
</tr>
<tr class="odd">
<td><p>cable</p></td>
<td><p>The part number of a given transceiver changed</p></td>
<td><p>Info</p></td>
<td><p>@ifname part number changed from @old_part_number to @new_part_number</p></td>
<td><p>swp7 part number changed from FP1ZZ5654002A to MSN2700-CS2F0</p></td>
</tr>
<tr class="even">
<td><p>cable</p></td>
<td><p>The serial number of a given transceiver changed</p></td>
<td><p>Info</p></td>
<td><p>@ifname serial number changed from @old_serial_number to @new_serial_number</p></td>
<td><p>swp4 serial number changed from 571254X1507020 to MT1552X12041</p></td>
</tr>
<tr class="odd">
<td><p>cable</p></td>
<td><p>The status of forward error correction (FEC) support for a given port changed</p></td>
<td><p>Info</p></td>
<td><p>@ifname supported fec changed from @old_supported_fec to @new_supported_fec</p></td>
<td><p>swp12 supported fec changed from supported to unsupported</p>
<p>swp12 supported fec changed from unsupported to supported</p></td>
</tr>
<tr class="even">
<td><p>cable</p></td>
<td><p>The advertised support for FEC for a given port changed</p></td>
<td><p>Info</p></td>
<td><p>@ifname supported fec changed from @old_advertised_fec to @new_advertised_fec</p></td>
<td><p>swp24 supported FEC changed from advertised to not advertised</p></td>
</tr>
<tr class="odd">
<td><p>cable</p></td>
<td><p>The FEC status for a given port changed</p></td>
<td><p>Info</p></td>
<td><p>@ifname fec changed from @old_fec to @new_fec</p></td>
<td><p>swp15 fec changed from disabled to enabled</p></td>
</tr>
<tr class="even">
<td><p>clag</p></td>
<td><p>CLAG remote peer state changed from up to down</p></td>
<td><p>Critical</p></td>
<td><p>Peer state changed to down</p></td>
<td><p>Peer state changed to down</p></td>
</tr>
<tr class="odd">
<td><p>clag</p></td>
<td><p>Local CLAG host MTU does not match its remote peer MTU</p></td>
<td><p>Critical</p></td>
<td><p>SVI @svi1 on vlan @vlan mtu @mtu1 mismatched with peer mtu @mtu2</p></td>
<td><p>SVI svi7 on vlan 4 mtu 1592 mistmatched with peer mtu 1680</p></td>
</tr>
<tr class="even">
<td><p>clag</p></td>
<td><p>CLAG SVI on VLAN is missing from remote peer state</p></td>
<td><p>Warning</p></td>
<td><p>SVI on vlan @vlan is missing from peer</p></td>
<td><p>SVI on vlan vlan4 is missing from peer</p></td>
</tr>
<tr class="odd">
<td><p>clag</p></td>
<td><p>CLAG peerlink is not opperating at full capacity. At least one link is down.</p></td>
<td><p>Warning</p></td>
<td><p>Clag peerlink not at full redundancy, member link @slave is down</p></td>
<td><p>Clag peerlink not at full redundancy, member link swp40 is down</p></td>
</tr>
<tr class="even">
<td><p>clag</p></td>
<td><p>CLAG remote peer state changed from down to up</p></td>
<td><p>Info</p></td>
<td><p>Peer state changed to up</p></td>
<td><p>Peer state changed to up</p></td>
</tr>
<tr class="odd">
<td><p>clag</p></td>
<td><p>Local CLAG host state changed from down to up</p></td>
<td><p>Info</p></td>
<td><p>Clag state changed from down to up</p></td>
<td><p>Clag state changed from down to up</p></td>
</tr>
<tr class="even">
<td><p>clag</p></td>
<td><p>CLAG bond in Conflicted state was updated with new bonds</p></td>
<td><p>Info</p></td>
<td><p>Clag conflicted bond changed from @old_conflicted_bonds to @new_conflicted_bonds</p></td>
<td><p>Clag conflicted bond changed from swp7 swp8 to @swp9 swp10</p></td>
</tr>
<tr class="odd">
<td><p>clag</p></td>
<td><p>CLAG bond changed state from protodown to up state</p></td>
<td><p>Info</p></td>
<td><p>Clag conflicted bond changed from @old_state_protodownbond to @new_state_protodownbond</p></td>
<td><p>Clag conflicted bond changed from protodown to up</p></td>
</tr>
<tr class="even">
<td><p>clsupport</p></td>
<td><p>A new CL Support file has been created for the given node</p></td>
<td><p>Critical</p></td>
<td><p>HostName @hostname has new CL SUPPORT file</p></td>
<td><p>HostName leaf01 has new CL SUPPORT file</p></td>
</tr>
<tr class="odd">
<td><p>configdiff</p></td>
<td><p>Configuration file deleted on a device</p></td>
<td><p>Critical</p></td>
<td><p>@hostname config file @type was deleted</p></td>
<td><p>spine03 config file /etc/frr/frr.conf was deleted</p></td>
</tr>
<tr class="even">
<td><p>configdiff</p></td>
<td><p>Configuration file has been created</p></td>
<td><p>Info</p></td>
<td><p>@hostname config file @type was created</p></td>
<td><p>leaf12 config file /etc/lldp.d/README.conf was created</p></td>
</tr>
<tr class="odd">
<td><p>configdiff</p></td>
<td><p>Configuration file has been modified</p></td>
<td><p>Info</p></td>
<td><p>@hostname config file @type was modified</p></td>
<td><p>spine03 config file /etc/frr/frr.conf was modified</p></td>
</tr>
<tr class="even">
<td><p>evpn</p></td>
<td><p>A VNI was configured and moved from the up state to the down state</p></td>
<td><p>Critical</p></td>
<td><p>VNI @vni state changed from up to down</p></td>
<td><p>VNI 36 state changed from up to down</p></td>
</tr>
<tr class="odd">
<td><p>evpn</p></td>
<td><p>A VNI was configured and moved from the down state to the up state</p></td>
<td><p>Info</p></td>
<td><p>VNI @vni state changed from down to up</p></td>
<td><p>VNI 36 state changed from down to up</p></td>
</tr>
<tr class="even">
<td><p>evpn</p></td>
<td><p>The kernel state changed on a VNI</p></td>
<td><p>Info</p></td>
<td><p>VNI @vni kernel state changed from @old_in_kernel_state to @new_in_kernel_state</p></td>
<td><p>VNI 3 kernel state changed from down to up</p></td>
</tr>
<tr class="odd">
<td><p>evpn</p></td>
<td><p>A VNI state changed from not advertising all VNIs to advertising all VNIs</p></td>
<td><p>Info</p></td>
<td><p>VNI @vni vni state changed from @old_adv_all_vni_state to @new_adv_all_vni_state</p></td>
<td><p>VNI 11 vni state changed from false to true</p></td>
</tr>
<tr class="even">
<td><p>license</p></td>
<td><p>License state is missing or invalid</p></td>
<td><p>Critical</p></td>
<td><p>License check failed, name @lic_name state @state</p></td>
<td><p>License check failed, name agent.lic state invalid</p></td>
</tr>
<tr class="odd">
<td><p>license</p></td>
<td><p>License state is missing or invalid on a particular device</p></td>
<td><p>Critical</p></td>
<td><p>License check failed on @hostname</p></td>
<td><p>License check failed on leaf03</p></td>
</tr>
<tr class="even">
<td><p>link</p></td>
<td><p>Link operational state changed from up to down</p></td>
<td><p>Critical</p></td>
<td><p>HostName @hostname changed state from @old_state to @new_state Interface:@ifname</p></td>
<td><p>HostName leaf01 changed state from up to down Interface:swp34</p></td>
</tr>
<tr class="odd">
<td><p>link</p></td>
<td><p>Link operational state changed from down to up</p></td>
<td><p>Info</p></td>
<td><p>HostName @hostname changed state from @old_state to @new_state Interface:@ifname</p></td>
<td><p>HostName leaf04 changed state from down to up Interface:swp11</p></td>
</tr>
<tr class="even">
<td><p>lldp</p></td>
<td><p>Local LLDP host has new neighbor information</p></td>
<td><p>Info</p></td>
<td><p>LLDP Session with host @hostname and @ifname modified fields @changed_fields</p></td>
<td><p>LLDP Session with host leaf02 swp6 modified fields leaf06 swp21</p></td>
</tr>
<tr class="odd">
<td><p>lldp</p></td>
<td><p>Local LLDP host has new peer interface name</p></td>
<td><p>Info</p></td>
<td><p>LLDP Session with host @hostname and @ifname @old_peer_ifname changed to @new_peer_ifname</p></td>
<td><p>LLDP Session with host spine01 and swp5 swp12 changed to port12</p></td>
</tr>
<tr class="even">
<td><p>lldp</p></td>
<td><p>Local LLDP host has new peer hostname</p></td>
<td><p>Info</p></td>
<td><p>LLDP Session with host @hostname and @ifname @old_peer_hostname changed to @new_peer_hostname</p></td>
<td><p>LLDP Session with host leaf03 and swp2 leaf07 changed to exit01</p></td>
</tr>
<tr class="odd">
<td><p>lnv</p></td>
<td><p>VXLAN registration daemon, vxrd, is not running</p></td>
<td><p>Critical</p></td>
<td><p>vxrd service not running</p></td>
<td><p>vxrd service not running</p></td>
</tr>
<tr class="even">
<td><p>mtu</p></td>
<td><p>VLAN interface link MTU is smaller than that of its parent MTU</p></td>
<td><p>Warning</p></td>
<td><p>vlan interface @link mtu @mtu is smaller than parent @parent mtu @parent_mtu</p></td>
<td><p>vlan interface swp3 mtu 1500 is smaller than parent peerlink-1 mtu 1690</p></td>
</tr>
<tr class="odd">
<td><p>mtu</p></td>
<td><p>Bridge interface MTU is smaller than the member interface with the smallest MTU</p></td>
<td><p>Warning</p></td>
<td><p>bridge @link mtu @mtu is smaller than least of member interface mtu @min</p></td>
<td><p>bridge swp0 mtu 1280 is smaller than least of member interface mtu 1500</p></td>
</tr>
<tr class="even">
<td><p>ntp</p></td>
<td><p>NTP sync state changed from in sync to not in sync</p></td>
<td><p>Critical</p></td>
<td><p>Sync state changed from @old_state to @new_state for @hostname</p></td>
<td><p>Sync state changed from in sync to not sync for leaf06</p></td>
</tr>
<tr class="odd">
<td><p>ntp</p></td>
<td><p>NTP sync state changed from not in sync to in sync</p></td>
<td><p>Info</p></td>
<td><p>Sync state changed from @old_state to @new_state for @hostname</p></td>
<td><p>Sync state changed from not sync to in sync for leaf06</p></td>
</tr>
<tr class="even">
<td><p>ospf</p></td>
<td><p>OSPF session state on a given interface changed from Full to a down state</p></td>
<td><p>Critical</p></td>
<td><p>OSPF session @ifname with @peer_address changed from Full to @down_state</p></td>
<td><p>OSPF session swp7 with 27.0.0.18 state changed from Full to Fail</p>
<p>OSPF session swp7 with 27.0.0.18 state changed from Full to ExStart</p></td>
</tr><tr class="odd">
<td><p>ospf</p></td>
<td><p>OSPF session state on a given interface changed from a down state to full</p></td>
<td><p>Info</p></td>
<td><p>OSPF session @ifname with @peer_address changed from @down_state to Full</p></td>
<td><p>OSPF session swp7 with 27.0.0.18 state changed from Down to Full</p>
<p>OSPF session swp7 with 27.0.0.18 state changed from Init to Full</p>
<p>OSPF session swp7 with 27.0.0.18 state changed from Fail to Full</p></td>
</tr>
<tr class="even">
<td><p>packageinfo</p></td>
<td><p>Package version on device does not match the version identified in the existing manifest</p></td>
<td><p>Critical</p></td>
<td><p>@package_name manifest version mismatch</p></td>
<td><p>netq-apps manifest version mismatch</p></td>
</tr>
<tr class="odd">
<td><p>ptm</p></td>
<td><p>Physical interface cabling does not match configuration specified in <em>topology.dot</em> file</p></td>
<td><p>Critical</p></td>
<td><p>PTM cable status failed</p></td>
<td><p>PTM cable status failed</p></td>
</tr>
<tr class="even">
<td><p>ptm</p></td>
<td><p>Physical interface cabling matches configuration specified in <em>topology.dot</em> file</p></td>
<td><p>Critical</p></td>
<td><p>PTM cable status passed</p></td>
<td><p>PTM cable status passed</p></td>
</tr>
<tr class="odd">
<td><p>resource</p></td>
<td><p>A physical resource has been deleted from a device</p></td>
<td><p>Critical</p></td>
<td><p>Resource Utils deleted for @hostname</p></td>
<td><p>Resource Utils deleted for spine02</p></td>
</tr>
<tr class="even">
<td><p>resource</p></td>
<td><p>Root file system access on a device has changed from Read/Write to Read Only</p></td>
<td><p>Critical</p></td>
<td><p>@hostname root file system access mode set to Read Only</p></td>
<td><p>server03 root file system access mode set to Read Only</p></td>
</tr>
<tr class="odd">
<td><p>resource</p></td>
<td><p>Root file system access on a device has changed from Read Only to Read/Write</p></td>
<td><p>Info</p></td>
<td><p>@hostname root file system access mode set to Read/Write</p></td>
<td><p>leaf11 root file system access mode set to Read/Write</p></td>
</tr>
<tr class="even">
<td><p>resource</p></td>
<td><p>A physical resource has been added to a device</p></td>
<td><p>Info</p></td>
<td><p>Resource Utils added for @hostname</p></td>
<td><p>Resource Utils added for spine04</p></td>
</tr>
<tr class="odd">
<td><p>runningconfigdiff</p></td>
<td><p>Running configuration file has been modified</p></td>
<td><p>Info</p></td>
<td><p>@commandname config result was modified</p></td>
<td><p>@commandname config result was modified</p></td>
</tr>
<tr class="even">
<td><p>sensor</p></td>
<td><p>A fan or power supply unit sensor has changed state</p></td>
<td><p>Critical</p></td>
<td><p>Sensor @sensor state changed from @old_s_state to @new_s_state</p></td>
<td><p>Sensor fan state changed from up to down</p></td>
</tr>
<tr class="odd">
<td><p>sensor</p></td>
<td><p>A temperature sensor has crossed the maximum threshold for that sensor</p></td>
<td><p>Critical</p></td>
<td><p>Sensor @sensor max value @new_s_max exceeds threshold @new_s_crit</p></td>
<td><p>Sensor temp max value 110 exceeds the threshold 95</p></td>
</tr>
<tr class="even">
<td><p>sensor</p></td>
<td><p>A temperature sensor has crossed the minimum threshold for that sensor</p></td>
<td><p>Critical</p></td>
<td><p>Sensor @sensor min value @new_s_lcrit fall behind threshold @new_s_min</p></td>
<td><p>Sensor psu min value 10 fell below threshold 25</p></td>
</tr>
<tr class="odd">
<td><p>sensor</p></td>
<td><p>A temperature, fan, or power supply sensor state changed</p></td>
<td><p>Info</p></td>
<td><p>Sensor @sensor state changed from @old_state to @new_state</p></td>
<td><p>Sensor temperature state changed from critical to ok</p>
<p>Sensor fan state changed from absent to ok</p>
<p>Sensor psu state changed from bad to ok</p></td>
</tr>
<tr class="even">
<td><p>sensor</p></td>
<td><p>A fan or power supply sensor state changed</p></td>
<td><p>Info</p></td>
<td><p>Sensor @sensor state changed from @old_s_state to @new_s_state</p></td>
<td><p>Sensor fan state changed from down to up</p>
<p>Sensor psu state changed from down to up</p></td>
</tr>
<tr class="odd">
<td><p>services</p></td>
<td><p>A service status changed from down to up</p></td>
<td><p>Critical</p></td>
<td><p>Service @name status changed from @old_status to @new_status</p></td>
<td><p>Service bgp status changed from down to up</p></td>
</tr>
<tr class="even">
<td><p>services</p></td>
<td><p>A service status changed from up to down</p></td>
<td><p>Critical</p></td>
<td><p>Service @name status changed from @old_status to @new_status</p></td>
<td><p>Service lldp status changed from up to down</p></td>
</tr>
<tr class="odd">
<td><p>services</p></td>
<td><p>A service changed state from inactive to active</p></td>
<td><p>Info</p></td>
<td><p>Service @name changed state from inactive to active</p></td>
<td><p>Service bgp changed state from inactive to active</p>
<p>Service lldp changed state from inactive to active</p></td>
</tr>
<tr class="even">
<td><p>ssdutil</p></td>
<td><p>3ME3 disk health has dropped below 10%</p></td>
<td><p>Critical</p></td>
<td><p>@info: @details</p></td>
<td><p>low health : 5.0%</p></td>
</tr>
<tr class="odd">
<td><p>ssdutil</p></td>
<td><p>A dip in 3ME3 disk health of more than 2% has occured within the last 24 hours</p></td>
<td><p>Critical</p></td>
<td><p>@info: @details</p></td>
<td><p>significant health drop : 3.0%</p></td>
</tr>
<tr class="even">
<td><p>tca</p></td>
<td><p>Percentage of CPU utilization exceeded user-defined maximum threshold on a switch</p></td>
<td><p>Critical</p></td>
<td><p>CPU Utilization for host @hostname exceed configured mark @cpu_utilization</p></td>
<td><p>CPU Utilization for host leaf11 exceed configured mark 85</p></td>
</tr>
<tr class="odd">
<td><p>tca</p></td>
<td><p>Percentage of disk utilization exceeded user-defined maximum threshold on a switch</p></td>
<td><p>Critical</p></td>
<td><p>Disk Utilization for host @hostname exceed configured mark @disk_utilization</p></td>
<td><p>Disk Utilization for host leaf11 exceed configured mark 90</p></td>
</tr>
<tr class="even">
<td><p>tca</p></td>
<td><p>Percentage of memory utilization exceeded user-defined maximum threshold on a switch</p></td>
<td><p>Critical</p></td>
<td><p>Memory Utilization for host @hostname exceed configured mark @mem_utilization</p></td>
<td><p>Memory Utilization for host leaf11 exceed configured mark 95</p></td>
</tr>
<tr class="odd">
<td><p>tca</p></td>
<td><p>Number of transmit bytes exceeded user-defined maximum threshold on a switch interface</p></td>
<td><p>Critical</p></td>
<td><p>TX bytes upper threshold breached for host @hostname ifname:@ifname value: @tx_bytes</p></td>
<td><p>TX bytes upper threshold breached for host spine02 ifname:swp4 value: 20000</p></td>
</tr>
<tr class="even">
<td><p>tca</p></td>
<td><p>Number of broadcast transmit bytes exceeded user-defined maximum threshold on a switch interface</p></td>
<td><p>Critical</p></td>
<td><p>TX broadcast upper threshold breached for host @hostname ifname:@ifname value: @rx_broadcast</p></td>
<td><p>TX broadcast upper threshold breached for host leaf04 ifname:swp45 value: 40200</p></td>
</tr>
<tr class="odd">
<td><p>tca</p></td>
<td><p>Number of multicast transmit bytes exceeded user-defined maximum threshold on a switch interface</p></td>
<td><p>Critical</p></td>
<td><p>TX multicast upper threshold breached for host @hostname ifname:@ifname value: @rx_broadcast</p></td>
<td><p>TX multicast upper threshold breached for host leaf04 ifname:swp45 value: 30000</p></td>
</tr>
<tr class="even">
<td><p>tca</p></td>
<td><p>Number of receive bytes exceeded user-defined maximum threshold on a switch interface</p></td>
<td><p>Critical</p></td>
<td><p>RX bytes upper threshold breached for host @hostname ifname:@ifname value: @tx_bytes</p></td>
<td><p>RX bytes upper threshold breached for host spine02 ifname:swp4 value: 20000</p></td>
</tr>
<tr class="odd">
<td><p>tca</p></td>
<td><p>Number of broadcast receive bytes exceeded user-defined maximum threshold on a switch interface</p></td>
<td><p>Critical</p></td>
<td><p>RX broadcast upper threshold breached for host @hostname ifname:@ifname value: @rx_broadcast</p></td>
<td><p>RX broadcast upper threshold breached for host leaf04 ifname:swp45 value: 40200</p></td>
</tr>
<tr class="even">
<td><p>tca</p></td>
<td><p>Number of multicast receive bytes exceeded user-defined maximum threshold on a switch interface</p></td>
<td><p>Critical</p></td>
<td><p>RX multicast upper threshold breached for host @hostname ifname:@ifname value: @rx_broadcast</p></td>
<td><p>RX multicast upper threshold breached for host leaf04 ifname:swp45 value: 30000</p></td>
</tr>
<tr class="odd">
<td><p>tca</p></td>
<td><p>Fan speed exceeded user-defined maximum threshold on a switch</p></td>
<td><p>Critical</p></td>
<td><p>Sensor for @hostname exceeded threshold fan speed @s_input for sensor @s_name</p></td>
<td><p>Sensor for spine03 exceeded threshold fan speed 700 for sensor fan2</p></td>
</tr>
<tr class="even">
<td><p>tca</p></td>
<td><p>Power supply output exceeded user-defined maximum threshold on a switch</p></td>
<td><p>Critical</p></td>
<td><p>Sensor for @hostname exceeded threshold power @s_input watts for sensor @s_name</p></td>
<td><p>Sensor for leaf14 exceeded threshold power 120 watts for sensor psu1</p></td>
</tr>
<tr class="odd">
<td><p>tca</p></td>
<td><p>Temperature (&#176 C) exceeded user-defined maximum threshold on a switch</p></td>
<td><p>Critical</p></td>
<td><p>Sensor for @hostname exceeded threshold temperature @s_input for sensor @s_name</p></td>
<td><p>Sensor for leaf14 exceeded threshold temperature 90 for sensor temp1</p></td>
</tr>
<tr class="even">
<td><p>tca</p></td>
<td><p>Power supply voltage exceeded user-defined maximum threshold on a switch</p></td>
<td><p>Critical</p></td>
<td><p>Sensor for @hostname exceeded threshold voltage @s_input volts for sensor @s_name</p></td>
<td><p>Sensor for leaf14 exceeded threshold voltage 12 volts for sensor psu2</p></td>
</tr>
<tr class="odd">
<td><p>version</p></td>
<td><p>An unknown version of the operating system was detected</p></td>
<td><p>Critical</p></td>
<td><p>unexpected os version @my_ver</p></td>
<td><p>unexpected os version cl3.2</p></td>
</tr>
<tr class="even">
<td><p>version</p></td>
<td><p>Desired version of the operating system is not available</p></td>
<td><p>Critical</p></td>
<td><p>os version @ver</p></td>
<td><p>os version cl3.7.9</p></td>
</tr>
<tr class="odd">
<td><p>version</p></td>
<td><p>An unknown version of a software package was detected</p></td>
<td><p>Critical</p></td>
<td><p>expected release version @ver</p></td>
<td><p>expected release version cl3.6.2</p></td>
</tr>
<tr class="even">
<td><p>version</p></td>
<td><p>Desired version of a software package is not available</p></td>
<td><p>Critical</p></td>
<td><p>different from version @ver</p></td>
<td><p>different from version cl4.0</p></td>
</tr>
<tr class="odd">
<td><p>vxlan</p></td>
<td><p>Replication list is contains an inconsistent set of nodes</p></td>
<td><p>Critical</p></td>
<td><p>VNI @vni replication list inconsistent with @conflicts diff:@diff</p></td>
<td><p>VNI 14 replication list inconsistent with ["leaf03","leaf04"] diff:+:["leaf03","leaf04"] -:["leaf07","leaf08"]</p></td>
</tr>
</tbody>
</table>
