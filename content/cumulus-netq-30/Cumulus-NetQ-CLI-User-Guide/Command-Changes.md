---
title: NetQ CLI Changes
author: Cumulus Networks
weight: 490
aliases:
 - /display/NETQ/NetQ+Command+Line+Overview
 - /pages/viewpage.action?pageId=12321059
pageID: 12321059
toc: 3
---

A number of commands have changed in this release to accommodate the addition of new keywords and options or to simplify their syntax. Additionally, new commands have been added and others have been removed. A summary of those changes is provided here.

## New Commands

The following table summarizes the new commands available with this release. They are grouped into the following categories: new `netq show` commands, What Just Happened feature, clustering deployment, detailed validation commands, and threshold-based events.

| Command | Summary | Version |
| ------- | ------- | ------- |
| netq lcm add credentials (username &lt;text-switch-username> password &lt;text-switch-password> \| ssh-key &lt;text-ssh-key>) | Creates credentials (either SSH key or basic username/password auth) to perform life cycle management (LCM). | 3.0.0 |
| netq lcm add image &lt;text-image-path> | Uploads a Cumulus Linux install image to the LCM repository. | 3.0.0 |
| netq lcm add role (superspine \| spine \| leaf \| exit) switches &lt;text-switch-hostnames> | Adds a switch role to one or more switches. | 3.0.0 |
| netq lcm del credentials | Removes a set of LCM credentials. | 3.0.0 |
| netq lcm del image &lt;text-image-id> | Deletes a Cumulus Linux install image from the LCM repository. | 3.0.0 |
| netq lcm show credentials [json] | Displays configured LCM credentials. | 3.0.0 |
| netq lcm show images [&lt;text-image-id>] [json] | Displays Cumulus Linux install images that have been added to the LCM repository. | 3.0.0 |
| netq lcm show status &lt;text-lcm-job-id> [json] | Displays the status of an LCM upgrade task. | 3.0.0 |
| netq lcm show switches [version &lt;text-cumulus-linux-version>] [json] | Displays all the switches running Cumulus Linux that are managed under LCM. | 3.0.0 |
| netq lcm show upgrade-jobs [json] | Displays all the LCM upgrade jobs and their status. | 3.0.0 |
| netq lcm upgrade name &lt;text-job-name> image-id &lt;text-image-id> license &lt;text-cumulus-license> hostnames &lt;text-switch-hostnames> [order &lt;text-upgrade-order>] [run-before-after] | Creates and runs a new upgrade job. | 3.0.0 |
| netq config add agent command service-key &lt;text-service-key-anchor> [poll-period &lt;text-cmd-periodicity>] [command &lt;text-cmd-text>] [enable True \| enable False] | Configures, enables and disables commands that the NetQ agent runs at preset intervals. | 3.0.0 |
| netq config agent factory-reset commands | Restores NetQ agent commands to their defaults. | 3.0.0 |
| netq config del agent command service-key &lt;text-service-key-anchor> | Deletes a NetQ agent command. | 3.0.0 |
| netq config show agent commands [service-key &lt;text-service-key-anchor>] [json] | Displays the NetQ agent commands. | 3.0.0 |

## Modified Commands

The following table summarizes the commands that have been changed with
this release.

| Updated Command | Old Command | What Changed | Version |
| --------------- | ----------- | ------------ | ------- |
| netq [&lt;hostname>] show ethtool-stats port &lt;physical-port> (rx \| tx) [extended] [around &lt;text-time>] [json] | netq [&lt;hostname>] show ethtool-stats [&lt;physical-port>] [rx \| tx \| min]  [around &lt;text-time>] [json] | The `port`, `rx` and `tx` keywords are now required. Removed the `min` keyword. Added the `extended` keyword to show more statistics. | 3.0.0 |
| netq [&lt;hostname>] show events [level info \| level error \| level warning \| level critical \| level debug] [type clsupport \| type ntp \| type mtu \| type configdiff \| type vlan \| type trace \| type vxlan \| type clag \| type bgp \| type interfaces \| type interfaces-physical \| type agents \| type ospf \| type evpn \| type macs \| type services \| type lldp \| type license \| type os \| type sensors \| type btrfsinfo] [between &lt;text-time> and &lt;text-endtime>] [json] | netq [&lt;hostname>] show events [level info \| level error \| level warning \| level critical \| level debug] [type clsupport \| type ntp \| type mtu \| type configdiff \| type vlan \| type trace \| type vxlan \| type clag \| type bgp \| type interfaces \| type interfaces-physical \| type agents \| type ospf \| type evpn \| type lnv \| type macs \| type services \| type lldp \| type license \| type os \| type sensors \| type btrfsinfo] [between &lt;text-time> and &lt;text-endtime>] [json] | Removed `type lnv` since LNV is no longer supported in Cumulus Linux. | 3.0.0 |
| netq [&lt;hostname>] show interface-utilization [&lt;text-port>] [tx\|rx] [around &lt;text-time>] [json] | netq [&lt;hostname>] show interface-utils [&lt;text-port>] [tx\|rx] [around &lt;text-time>] [json] | Changed `interface-utils` keyword to `interface-utilization`. | 3.0.0 |
| netq check agents [label &lt;text-label-name> \| hostnames &lt;text-list-hostnames>] [include &lt;agent-number-range-list> \| exclude &lt;agent-number-range-list>] [around &lt;text-time>] [json] | netq check agents [label &lt;text-label-name>] [include &lt;agent-number-range-list> \| exclude &lt;agent-number-range-list>] [around &lt;text-time>] [json] | Added ability to specify a list of hostnames using the `hostnames <text-list-hostnames>]` option. | 3.0.0 |
| netq check bgp [label &lt;text-label-name> \| hostnames &lt;text-list-hostnames>] [vrf &lt;vrf>] [include &lt;bgp-number-range-list> \| exclude &lt;bgp-number-range-list>] [around &lt;text-time>] [json \| summary] | netq check bgp [label &lt;text-label-name>] [vrf &lt;vrf>] [include &lt;bgp-number-range-list> \| exclude &lt;bgp-number-range-list>] [around &lt;text-time>] [json \| summary] | Added ability to specify a list of hostnames using the `hostnames <text-list-hostnames>]` option. | 3.0.0 |
| netq check cl-version [label &lt;text-label-name> \| hostnames &lt;text-list-hostnames>] [match-version &lt;cl-ver> \| min-version &lt;cl-ver>] [include &lt;version-number-range-list> \| exclude &lt;version-number-range-list>] [around &lt;text-time>] [json \| summary] | netq check cl-version [label &lt;text-label-name>] [match-version &lt;cl-ver> \| min-version &lt;cl-ver>] [include &lt;version-number-range-list> \| exclude &lt;version-number-range-list>] [around &lt;text-time>] [json \| summary] | Added ability to specify a list of hostnames using the `hostnames <text-list-hostnames>]` option. | 3.0.0 |
| netq check clag [label &lt;text-label-name> \| hostnames &lt;text-list-hostnames> ] [include &lt;clag-number-range-list> \| exclude &lt;clag-number-range-list>] [around &lt;text-time>] [json \| summary] | netq check clag [label &lt;text-label-name>] [include &lt;clag-number-range-list> \| exclude &lt;clag-number-range-list>] [around &lt;text-time>] [json \| summary] | Added ability to specify a list of hostnames using the `hostnames <text-list-hostnames>]` option. | 3.0.0 |
| netq check evpn [mac-consistency] [label &lt;text-label-name> \| hostnames &lt;text-list-hostnames>] [include &lt;evpn-number-range-list> \| exclude &lt;evpn-number-range-list>] [around &lt;text-time>] [json \| summary] | netq check evpn [mac-consistency] [label &lt;text-label-name>] [include &lt;evpn-number-range-list> \| exclude &lt;evpn-number-range-list>] [around &lt;text-time>] [json \| summary] | Added ability to specify a list of hostnames using the `hostnames <text-list-hostnames>]` option. | 3.0.0 |
| netq check interfaces [label &lt;text-label-name> \| hostnames &lt;text-list-hostnames>] [include &lt;interface-number-range-list> \| exclude &lt;interface-number-range-list>] [around &lt;text-time>] [json \| summary] | netq check interfaces [label &lt;text-label-name>] [include &lt;interface-number-range-list> \| exclude &lt;interface-number-range-list>] [around &lt;text-time>] [json \| summary] | Added ability to specify a list of hostnames using the `hostnames <text-list-hostnames>]` option. | 3.0.0 |
| netq check license [label &lt;text-label-name> \| hostnames &lt;text-list-hostnames>] [include &lt;license-number-range-list> \| exclude &lt;license-number-range-list>] [around &lt;text-time>] [json \| summary] | netq check license [label &lt;text-label-name>] [include &lt;license-number-range-list> \| exclude &lt;license-number-range-list>] [around &lt;text-time>] [json \| summary] | Added ability to specify a list of hostnames using the `hostnames <text-list-hostnames>]` option. | 3.0.0 |
| netq check mlag [label &lt;text-label-name> \| hostnames &lt;text-list-hostnames> ] [include &lt;mlag-number-range-list> \| exclude &lt;mlag-number-range-list>] [around &lt;text-time>] [json \| summary]| netq check mlag [label &lt;text-label-name>] [include &lt;mlag-number-range-list> \| exclude &lt;mlag-number-range-list>] [around &lt;text-time>] [json \| summary] | Added ability to specify a list of hostnames using the `hostnames <text-list-hostnames>]` option. | 3.0.0 |
| netq check mtu [label &lt;text-label-name> \| hostnames &lt;text-list-hostnames>] [unverified] [include &lt;mtu-number-range-list> \| exclude &lt;mtu-number-range-list>] [around &lt;text-time>] [json \| summary] | netq check mtu [label &lt;text-label-name>] [unverified] [include &lt;mtu-number-range-list> \| exclude &lt;mtu-number-range-list>] [around &lt;text-time>] [json \| summary] | Added ability to specify a list of hostnames using the `hostnames <text-list-hostnames>]` option. | 3.0.0 |
| netq check ntp [label &lt;text-label-name> \| hostnames &lt;text-list-hostnames>] [include &lt;ntp-number-range-list> \| exclude &lt;ntp-number-range-list>] [around &lt;text-time>] [json \| summary] | netq check ntp [label &lt;text-label-name>] [include &lt;ntp-number-range-list> \| exclude &lt;ntp-number-range-list>] [around &lt;text-time>] [json \| summary] | Added ability to specify a list of hostnames using the `hostnames <text-list-hostnames>]` option. | 3.0.0 |
| netq check ospf [label &lt;text-label-name> \| hostnames &lt;text-list-hostnames>] [include &lt;ospf-number-range-list> \| exclude &lt;ospf-number-range-list>] [around &lt;text-time>] [json \| summary] | netq check ospf [label &lt;text-label-name>] [include &lt;ospf-number-range-list> \| exclude &lt;ospf-number-range-list>] [around &lt;text-time>] [json \| summary] | Added ability to specify a list of hostnames using the `hostnames <text-list-hostnames>]` option. | 3.0.0 |
| netq check sensors [label &lt;text-label-name> \| hostnames &lt;text-list-hostnames>] [include &lt;sensors-number-range-list> \| exclude &lt;sensors-number-range-list>] [around &lt;text-time>] [json \| summary] | netq check sensors [label &lt;text-label-name>] [include &lt;sensors-number-range-list> \| exclude &lt;sensors-number-range-list>] [around &lt;text-time>] [json \| summary] | Added ability to specify a list of hostnames using the `hostnames <text-list-hostnames>]` option. | 3.0.0 |
| netq check vlan [label &lt;text-label-name> \| hostnames &lt;text-list-hostnames>] [unverified] [include &lt;vlan-number-range-list> \| exclude &lt;vlan-number-range-list>] [around &lt;text-time>] [json \| summary] | netq check vlan [label &lt;text-label-name>] [unverified] [include &lt;vlan-number-range-list> \| exclude &lt;vlan-number-range-list>] [around &lt;text-time>] [json \| summary] | Added ability to specify a list of hostnames using the `hostnames <text-list-hostnames>]` option. | 3.0.0 |
| netq check vxlan [label &lt;text-label-name> \| hostnames &lt;text-list-hostnames>] [include &lt;vxlan-number-range-list> \| exclude &lt;vxlan-number-range-list>] [around &lt;text-time>] [json \| summary] | netq check vxlan [label &lt;text-label-name>] [include &lt;vxlan-number-range-list> \| exclude &lt;vxlan-number-range-list>] [around &lt;text-time>] [json \| summary] | Added ability to specify a list of hostnames using the `hostnames <text-list-hostnames>]` option. | 3.0.0 |
| netq show ip addresses [&lt;remote-interface>] [&lt;ipv4>\|&lt;ipv4/prefixlen>] [vrf &lt;vrf>] [subnet\|supernet\|gateway] [around &lt;text-time>] [json] | netq show ip addresses [&lt;remote-interface>] [&lt;ipv4>\|&lt;ipv4/prefixlen>] [vrf &lt;vrf>] [around &lt;text-time>] [json] | Added the ability to display all addresses in a subnet or supernet or the layer 3 gateway of an address. | 3.0.0 |
| netq show ipv6 addresses [&lt;remote-interface>] [&lt;ipv6>\|&lt;ipv6/prefixlen>] [vrf &lt;vrf>] [subnet\|supernet\|gateway] [around &lt;text-time>] [json] | netq show ipv6 addresses [&lt;remote-interface>] [&lt;ipv6>\|&lt;ipv6/prefixlen>] [vrf &lt;vrf>] [around &lt;text-time>] [json] | Added the ability to display all addresses in a subnet or supernet or the layer 3 gateway of an address. | 3.0.0 |

## Removed Commands

The following table summarizes the previously deprecated commands that have been removed from Cumulus NetQ.

| Command | Summary | Version |
| ------- | ------- | ------- |
| netq [&lt;hostname>] show lnv [around &lt;text-time>] [json] | LNV is no longer supported in Cumulus Linux. | 3.0.0 |
| netq check lnv [around &lt;text-time>] [json] | LNV is no longer supported in Cumulus Linux. | 3.0.0 |
