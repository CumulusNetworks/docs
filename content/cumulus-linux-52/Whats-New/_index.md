---
title: What's New
author: NVIDIA
weight: 5
toc: 2
---
This document supports the Cumulus Linux 5.2 release, and lists new platforms, features, and enhancements.
- For a list of open and fixed issues in Cumulus Linux 5.2, see the {{<link title="Cumulus Linux 5.2 Release Notes" text="Cumulus Linux 5.2 Release Notes">}}.
- To upgrade to Cumulus Linux 5.2, follow the steps in {{<link url="Upgrading-Cumulus-Linux">}}.
<!-- vale off -->
## What's New in Cumulus Linux 5.2.1
<!-- vale on -->
Cumulus Linux 5.2.1 provides bug fixes.
<!-- vale off -->
## What's New in Cumulus Linux 5.2.0
<!-- vale on -->
Cumulus Linux 5.2.0 supports new platforms, provides bug fixes, and contains several new features and improvements.

### Platforms

- NVIDIA SN2201 (100G Spectrum-1)

### New Features and Enhancements

- Support for signed images on secured switches and support for SecureApt to update individual packages
- {{<link url="Zero-Touch-Provisioning-ZTP/#dhcp-on-front-panel-ports" text="ZTP on front panel ports">}}
- PTP enhancements include:
   - {{<link url="Precision-Time-Protocol-PTP/#ptp-profiles" text="Pre-defined PTP profiles and custom profiles">}}
   - {{<link url="Precision-Time-Protocol-PTP/#message-mode" text="PTP unicast message mode">}}
- {{<link url="NVUE-Object-Model" text="NVUE">}} enhancements include:
  - {{<link url="NVUE-CLI/#command-abbreviation" text="Command abbreviation">}}
  - {{<link url="NVUE-CLI/#command-question-mark" text="Command question mark (?)">}} to show required information quickly and concisely, such as the command value type, range, and options with a brief description of each. `?` also indicates if you need to provide specific values for the command.
  - {{<link url="Equal-Cost-Multipath-Load-Sharing-Hardware-ECMP/#gtp-hashing" text="TEID-based ECMP hashing">}} and {{<link url="Bonding-Link-Aggregation/#gtp-hashing" text="TEID-based bond hashing">}} configuration commands available
  - {{<link url="Netfilter-ACLs/#install-and-manage-acl-rules-with-nvue" text="Show ACL statistics per interface">}} commands
  - New commands:
   {{< tabs "TabID34 ">}}
{{< tab "show commands ">}}

```
nv show interface <interface-id> acl <acl-id> statistics
nv show interface <interface-id> acl <acl-id> statistics <rule-id>
nv show service ptp <instance-id> unicast-master
nv show service ptp <instance-id> unicast-master <table-id>
nv show service ptp <instance-id> unicast-master <table-id> address
nv show service ptp <instance-id> unicast-master <table-id> address <ip-mac-address-id>
nv show service ptp <instance-id> profile
nv show service ptp <instance-id> profile <profile-id>
nv show system forwarding
nv show system forwarding lag-hash
nv show system forwarding ecmp-hash
```

{{< /tab >}}
{{< tab "set commands ">}}

```
nv set router policy route-map <route-map-id> rule <rule-id> match evpn-default-route (on|off)
nv set router policy route-map <route-map-id> rule <rule-id> set as-path-prepend as 1-4294967295
nv set router policy route-map <route-map-id> rule <rule-id> set as-path-prepend as <asn-range>
nv set router policy route-map <route-map-id> rule <rule-id> set originator-id <ipv4>
nv set router policy route-map <route-map-id> rule <rule-id> set label-index 0-1048560
nv set router policy route-map <route-map-id> rule <rule-id> set forwarding-address <ipv6>
nv set router policy route-map <route-map-id> rule <rule-id> description none
nv set interface <interface-id> link breakout (1x|2x20G|2x40G|2x50G|2x100G|2x200G|4x10G|4x25G|4x50G|4x100G|8x50G|disabled|loopback)
nv set interface <interface-id> link breakout (1x|2x|4x|8x|2x10G|2x25G|2x40G|2x50G|2x100G|2x200G|4x10G|4x25G|4x50G|4x100G|8x50G|disabled|loopback)
nv set interface <interface-id> link speed (auto|10M|100M|1G|10G|25G|40G|50G|100G|200G|400G)
nv set interface <interface-id> link speed (auto|10M|100M|1G|10G|25G|40G|50G|100G|200G|400G|800G)
nv set interface <interface-id> link lanes (1|2|4|8)
nv set interface <interface-id> ptp message-mode (multicast|unicast|mixed)
nv set interface <interface-id> ptp mixed-multicast-unicast (on|off)
nv set interface <interface-id> ptp unicast-service-mode (client|server)
nv set interface <interface-id> ptp unicast-request-duration 10-1000
nv set interface <interface-id> ptp unicast-master-table-id <integer>
nv set service ptp <instance-id> unicast-master <table-id>
nv set service ptp <instance-id> unicast-master <table-id> address <ip-mac-address-id>
nv set service ptp <instance-id> unicast-master <table-id> query-interval -3-4
nv set service ptp <instance-id> unicast-master <table-id> peer-address (<ipv4>|<ipv6>)
nv set service ptp <instance-id> profile <profile-id>
nv set service ptp <instance-id> profile <profile-id> profile-type (ieee-1588|itu-g-8275-1)
nv set service ptp <instance-id> profile <profile-id> priority1 <value>
nv set service ptp <instance-id> profile <profile-id> priority2 <value>
nv set service ptp <instance-id> profile <profile-id> local-priority <value>
nv set service ptp <instance-id> profile <profile-id> domain 0-255
nv set service ptp <instance-id> profile <profile-id> delay-mechanism end-to-end
nv set service ptp <instance-id> profile <profile-id> transport (ipv4|ipv6|802.3)
nv set service ptp <instance-id> profile <profile-id> announce-interval -7-7
nv set service ptp <instance-id> profile <profile-id> sync-interval -7-7
nv set service ptp <instance-id> profile <profile-id> delay-req-interval -7-7
nv set service ptp <instance-id> profile <profile-id> announce-timeout 2-255
nv set service ptp <instance-id> current-profile <value>
nv set system control-plane policer <policer-id> rate 10-10000
nv set system control-plane policer <policer-id> rate 10-50000
nv set system forwarding
nv set system forwarding lag-hash
nv set system forwarding lag-hash ip-protocol (on|off)
nv set system forwarding lag-hash source-mac (on|off)
nv set system forwarding lag-hash destination-mac (on|off)
nv set system forwarding lag-hash source-ip (on|off)
nv set system forwarding lag-hash destination-ip (on|off)
nv set system forwarding lag-hash source-port (on|off)
nv set system forwarding lag-hash destination-port (on|off)
nv set system forwarding lag-hash ether-type (on|off)
nv set system forwarding lag-hash vlan (on|off)
nv set system forwarding lag-hash gtp-teid (on|off)
nv set system forwarding ecmp-hash
nv set system forwarding ecmp-hash ip-protocol (on|off)
nv set system forwarding ecmp-hash source-ip (on|off)
nv set system forwarding ecmp-hash destination-ip (on|off)
nv set system forwarding ecmp-hash source-port (on|off)
nv set system forwarding ecmp-hash destination-port (on|off)
nv set system forwarding ecmp-hash ipv6-label (on|off)
nv set system forwarding ecmp-hash ingress-interface (on|off)
nv set system forwarding ecmp-hash gtp-teid (on|off)
nv set system forwarding ecmp-hash inner-ip-protocol (on|off)
nv set system forwarding ecmp-hash inner-source-ip (on|off)
nv set system forwarding ecmp-hash inner-destination-ip (on|off)
nv set system forwarding ecmp-hash inner-source-port (on|off)
nv set system forwarding ecmp-hash inner-destination-port (on|off)
nv set system forwarding ecmp-hash inner-ipv6-label (on|off)
nv set system forwarding hash-seed 0-4294967295
nv set vrf <vrf-id> router bgp address-family ipv4-unicast network <static-network-id> route-map (none|<instance-name>)
nv set vrf <vrf-id> router bgp address-family ipv4-unicast network <static-network-id> route-map <instance-name>
nv set vrf <vrf-id> router bgp address-family ipv6-unicast network <static-network-id> route-map (none|<instance-name>)
nv set vrf <vrf-id> router bgp address-family ipv6-unicast network <static-network-id> route-map <instance-name>
```

{{< /tab >}}
{{< tab "unset commands ">}}

```
nv unset router policy route-map <route-map-id> rule <rule-id> match evpn-default-route
nv unset router policy route-map <route-map-id> rule <rule-id> set originator-id
nv unset router policy route-map <route-map-id> rule <rule-id> set label-index
nv unset router policy route-map <route-map-id> rule <rule-id> set forwarding-address
nv unset router policy route-map <route-map-id> rule <rule-id> description
nv unset interface <interface-id> link lanes
nv unset interface <interface-id> ptp message-mode
nv unset interface <interface-id> ptp mixed-multicast-unicast
nv unset interface <interface-id> ptp unicast-service-mode
nv unset interface <interface-id> ptp unicast-request-duration
nv unset interface <interface-id> ptp unicast-master-table-id
nv unset service ptp <instance-id> unicast-master
nv unset service ptp <instance-id> unicast-master <table-id>
nv unset service ptp <instance-id> unicast-master <table-id> address
nv unset service ptp <instance-id> unicast-master <table-id> address <ip-mac-address-id>
nv unset service ptp <instance-id> unicast-master <table-id> query-interval
nv unset service ptp <instance-id> unicast-master <table-id> peer-address
nv unset service ptp <instance-id> profile
nv unset service ptp <instance-id> profile <profile-id>
nv unset service ptp <instance-id> profile <profile-id> profile-type
nv unset service ptp <instance-id> profile <profile-id> priority1
nv unset service ptp <instance-id> profile <profile-id> priority2
nv unset service ptp <instance-id> profile <profile-id> local-priority
nv unset service ptp <instance-id> profile <profile-id> domain
nv unset service ptp <instance-id> profile <profile-id> delay-mechanism
nv unset service ptp <instance-id> profile <profile-id> transport
nv unset service ptp <instance-id> profile <profile-id> announce-interval
nv unset service ptp <instance-id> profile <profile-id> sync-interval
nv unset service ptp <instance-id> profile <profile-id> delay-req-interval
nv unset service ptp <instance-id> profile <profile-id> announce-timeout
nv unset service ptp <instance-id> current-profile
nv unset system forwarding
nv unset system forwarding lag-hash
nv unset system forwarding lag-hash ip-protocol
nv unset system forwarding lag-hash source-mac
nv unset system forwarding lag-hash destination-mac
nv unset system forwarding lag-hash source-ip
nv unset system forwarding lag-hash destination-ip
nv unset system forwarding lag-hash source-port
nv unset system forwarding lag-hash destination-port
nv unset system forwarding lag-hash ether-type
nv unset system forwarding lag-hash vlan
nv unset system forwarding lag-hash gtp-teid
nv unset system forwarding ecmp-hash
nv unset system forwarding ecmp-hash ip-protocol
nv unset system forwarding ecmp-hash source-ip
nv unset system forwarding ecmp-hash destination-ip
nv unset system forwarding ecmp-hash source-port
nv unset system forwarding ecmp-hash destination-port
nv unset system forwarding ecmp-hash ipv6-label
nv unset system forwarding ecmp-hash ingress-interface
nv unset system forwarding ecmp-hash gtp-teid
nv unset system forwarding ecmp-hash inner-ip-protocol
nv unset system forwarding ecmp-hash inner-source-ip
nv unset system forwarding ecmp-hash inner-destination-ip
nv unset system forwarding ecmp-hash inner-source-port
nv unset system forwarding ecmp-hash inner-destination-port
nv unset system forwarding ecmp-hash inner-ipv6-label
nv unset system forwarding hash-seed
nv config history [<revision>]
```

{{< /tab >}}
{{< /tabs >}}

{{%notice info%}}
Cumulus Linux 5.2 includes the NVUE object model. After you upgrade to Cumulus Linux 5.2, running NVUE configuration commands replaces the configuration in files such as `/etc/network/interfaces` and `/etc/frr/frr.conf` and removes any configuration you add manually or with automation tools like Ansible, Chef, or Puppet. To keep your configuration, you can do one of the following:

- Update your automation tools to use NVUE.
- {{<link url="NVIDIA-User-Experience-NVUE/#configure-nvue-to-ignore-linux-files" text="Configure NVUE to ignore certain underlying Linux files">}} when applying configuration changes.
- Use Linux and FRR (vtysh) commands instead of NVUE for **all** switch configuration.

Cumulus Linux 3.7, 4.3, and 4.4 continue to support NCLU. For more information, contact your NVIDIA Spectrum platform sales representative.
{{%/notice%}}
