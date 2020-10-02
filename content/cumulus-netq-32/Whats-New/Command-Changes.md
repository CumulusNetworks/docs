---
title: NetQ CLI Changes
author: Cumulus Networks
weight: 20
toc: 4
---

A number of commands have changed in this release to accommodate the addition of new options or to simplify their syntax. Additionally, new commands have been added and others have been removed. A summary of those changes is provided here.

## New Commands

The following table summarizes the new commands available with this release. They include history for IP address and neighbors, selecting a premise and MAC commentary.

| Command | Summary | Version |
| ------- | ------- | ------- |
| netq [&lt;hostname>] show address-history &lt;text-prefix> [ifname &lt;text-ifname>] [vrf &lt;text-vrf>] [diff] [between &lt;text-time> and &lt;text-endtime>] [listby &lt;text-list-by>] [json] | Shows the history for a given IP address and prefix. | 3.2.0 |
| netq [&lt;hostname>] show neighbor-history &lt;text-ipaddress> [ifname &lt;text-ifname>] [diff] [between &lt;text-time> and &lt;text-endtime>] [listby &lt;text-list-by>] [json] | Shows the neighbor history for a given IP address. | 3.2.0 |
|  netq [&lt;hostname>] show mac-commentary &lt;mac> vlan &lt;1-4096> [between &lt;text-time> and &lt;text-endtime>] [json] | Shows commentary information for a given MAC address. | 3.2.0 |
| netq config add agent wjh-threshold (latency\|congestion) &lt;text-tc-list> &lt;text-port-list> &lt;text-th-hi> &lt;text-th-lo> | Configures latency and congestion thresholds for Mellanox What Just Happened (WJH). | 3.2.0 |
| netq config del agent wjh-threshold (latency\|congestion) &lt;text-tc-list>  | Removes a Mellanox WJH threshold configuration. | 3.2.0 |
| netq config select cli premise &lt;text-premise> | Specifies which premise to use. | 3.2.0 |

## Modified Commands

The following table summarizes the commands that have been changed with this release.

| Updated Command | Old Command | What Changed | Version |
| --------------- | ----------- | ------------ | ------- |
| netq add tca [event_id &lt;text-event-id-anchor>] [tca_id &lt;text-tca-id-anchor>] [scope &lt;text-scope-anchor>] [severity info \| severity critical] [is_active true \| is_active false] [suppress_until &lt;text-suppress-ts>] [threshold_type user_set \| threshold_type vendor_set] [ threshold &lt;text-threshold-value> ] [channel &lt;text-channel-name-anchor> \| channel drop &lt;text-drop-channel-name>] |  netq add tca [event_id &lt;text-event-id-anchor>]  [scope &lt;text-scope-anchor>] [tca_id &lt;text-tca-id-anchor>]  [severity info \| severity critical] [is_active true \| is_active false] [suppress_until &lt;text-suppress-ts>] [ threshold &lt;text-threshold-value> ] [channel &lt;text-channel-name-anchor> \| channel drop &lt;text-drop-channel-name>] | Added the `threshold_type` option, to indicate user-configured or vendor-configured thresholds. Also switched the positions of the `tca_id` and `scope` options. | 3.2.0 |
| netq config show agent [kubernetes-monitor\|loglevel\|stats\|sensors\|frr-monitor\|wjh\|wjh-threshold\|cpu-limit] [json]  |  netq config show agent [kubernetes-monitor\|loglevel\|stats\|sensors\|frr-monitor\|wjh\|cpu-limit] [json] | The command now shows Mellanox WJH latency and congestion thresholds. | 3.2.0 |
| netq [&lt;hostname>] show events [level info \| level error \| level warning \| level critical \| level debug] [type clsupport \| type ntp \| type mtu \| type configdiff \| type vlan \| type trace \| type vxlan \| type clag \| type bgp \| type interfaces \| type interfaces-physical \| type agents \| type ospf \| type evpn \| type macs \| type services \| type lldp \| type license \| type os \| type sensors \| type btrfsinfo \| type lcm] [between &lt;text-time> and &lt;text-endtime>] [json] | netq [&lt;hostname>] show events [level info \| level error \| level warning \| level critical \| level debug] [type clsupport \| type ntp \| type mtu \| type configdiff \| type vlan \| type trace \| type vxlan \| type clag \| type bgp \| type interfaces \| type interfaces-physical \| type agents \| type ospf \| type evpn \| type macs \| type services \| type lldp \| type license \| type os \| type sensors \| type btrfsinfo] [between &lt;text-time> and &lt;text-endtime>] [json] | Added the `type lcm` option for lifecycle management event information. | 3.2.0 |
| netq bootstrap master (interface &lt;text-opta-ifname>\|ip-addr &lt;text-ip-addr>) tarball &lt;text-tarball-name> [pod-ip-range &lt;text-pod-ip-range>] | netq bootstrap master (interface &lt;text-opta-ifname>\|ip-addr &lt;text-ip-addr>) tarball &lt;text-tarball-name> | Added the `pod-ip-range <text-pod-ip-range>` option, enabling you to specify a range of IP addresses for the pod. | 3.2.0 |
| netq [&lt;hostname>] show dom type (module_temp\|module_voltage) [interface &lt;text-dom-port-anchor>] [around &lt;text-time>] [json] | netq [&lt;hostname>] show dom type (module_temperature\|module_voltage) [interface &lt;text-dom-port-anchor>] [around &lt;text-time>] [json] | Renamed the `module_temperature` variable to `module_temp`. | 3.2.0 |
| netq [&lt;hostname>] show wjh-drop &lt;text-drop-type> [ingress-port &lt;text-ingress-port>] [severity &lt;text-severity>] [reason &lt;text-reason>] [src-ip &lt;text-src-ip>] [dst-ip &lt;text-dst-ip>] [proto &lt;text-proto>] [src-port &lt;text-src-port>] [dst-port &lt;text-dst-port>] [src-mac &lt;text-src-mac>] [dst-mac &lt;text-dst-mac>] [egress-port &lt;text-egress-port>] [traffic-class &lt;text-traffic-class>] [rule-id-acl &lt;text-rule-id-acl>] [between &lt;text-time> and &lt;text-endtime>] [around &lt;text-time>] [json] | netq [&lt;hostname>] show wjh-drop &lt;text-drop-type> [ingress-port &lt;text-ingress-port>] [reason &lt;text-reason>] [src-ip &lt;text-src-ip>] [dst-ip &lt;text-dst-ip>] [proto &lt;text-proto>] [src-port &lt;text-src-port>] [dst-port &lt;text-dst-port>] [src-mac &lt;text-src-mac>] [dst-mac &lt;text-dst-mac>] [egress-port &lt;text-egress-port>] [traffic-class &lt;text-traffic-class>] [rule-id-acl &lt;text-rule-id-acl>] [between &lt;text-time> and &lt;text-endtime>] [around &lt;text-time>] [json] | Added the `severity <text-severity>` option. | 3.2.0 |
| netq [&lt;hostname>] show wjh-drop [ingress-port &lt;text-ingress-port>] [severity &lt;text-severity>] [details] [between &lt;text-time> and &lt;text-endtime>] [around &lt;text-time>] [json]  | netq [&lt;hostname>] show wjh-drop [ingress-port &lt;text-ingress-port>] [details] [between &lt;text-time> and &lt;text-endtime>] [around &lt;text-time>] [json] | Added the `severity <text-severity>` option. | 3.2.0 |
