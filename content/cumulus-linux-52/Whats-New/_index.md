---
title: What's New
author: NVIDIA
weight: 5
toc: 2
---
This document supports the Cumulus Linux 5.2 release, and lists new platforms, features, and enhancements.

- For a list of all the platforms supported in Cumulus Linux 5.2, see the {{<exlink url="www.nvidia.com/en-us/networking/ethernet-switching/hardware-compatibility-list/" text="Hardware Compatibility List (HCL)">}}.
- For a list of open and fixed issues in Cumulus Linux 5.2, see the {{<link title="Cumulus Linux 5.2 Release Notes" text="Cumulus Linux 5.2 Release Notes">}}.
- To upgrade to Cumulus Linux 5.2, follow the steps in {{<link url="Upgrading-Cumulus-Linux">}}.
<!-- vale off -->
## What's New in Cumulus Linux 5.2.0
<!-- vale on -->
Cumulus Linux 5.2.0 supports new platforms, provides bug fixes, and contains several new features and improvements.

### Platforms

- {{<link url="Interface-Configuration-and-Management/#chassis-management" text="NVIDIA SN4800 (100G Spectrum-3) now generally available">}}
- NVIDIA SN2201 (1G and 100G Spectrum-1)

### New Features and Enhancements

- Support for signed images on secured switches and support for SecureApt to update individual packages
- {{<link url="Zero-Touch-Provisioning-ZTP/#dhcp-on-front-panel-ports" text="ZTP on front panel ports">}}
- PTP enhancements include:
   - {{<link url="Precision-Time-Protocol-PTP/#ptp-profiles" text="Pre-defined PTP profiles and custom profiles">}}
   - {{<link url="Precision-Time-Protocol-PTP/#message-mode" text="PTP unicast message mode">}}
- {{<link url="NVUE-Object-Model" text="NVUE">}} enhancements include:
  - {{<link url="NVUE-CLI/#command-abbreviation" text="Command abbreviation">}}
  - {{<link url="NVUE-CLI/#command-question-mark" text="Command question mark (?)">}} to show required information quickly and concisely, such as the command value type, range, and options with a brief description of each. `?` also indicates if you need to provide specific values for the command.
  - {{<link url="Configure-SNMP" text="SNMP configuration commands">}} available for early access.
  - {{< expand "New and changed NVUE commands" >}}
  
```
nv show service snmp-server
nv show service snmp-server listening-address
nv show service snmp-server listening-address <listening-address-id>
nv show service snmp-server username
nv show service snmp-server username <username-id>
nv show service snmp-server username <username-id> auth-none
nv show service snmp-server username <username-id> auth-md5
nv show service snmp-server username <username-id> auth-md5 <auth-id>
nv show service snmp-server username <username-id> auth-md5 <auth-id> encrypt-des
nv show service snmp-server username <username-id> auth-md5 <auth-id> encrypt-des <encrypt-id>
nv show service snmp-server username <username-id> auth-md5 <auth-id> encrypt-aes
nv show service snmp-server username <username-id> auth-md5 <auth-id> encrypt-aes <encrypt-id>
nv show service snmp-server username <username-id> auth-sha
nv show service snmp-server username <username-id> auth-sha <auth-id>
nv show service snmp-server username <username-id> auth-sha <auth-id> encrypt-des
nv show service snmp-server username <username-id> auth-sha <auth-id> encrypt-des <encrypt-id>
nv show service snmp-server username <username-id> auth-sha <auth-id> encrypt-aes
nv show service snmp-server username <username-id> auth-sha <auth-id> encrypt-aes <encrypt-id>
nv show service snmp-server mibs
nv show service snmp-server viewname
nv show service snmp-server viewname <viewname-id>
nv show service snmp-server readonly-community
nv show service snmp-server readonly-community <readonly-community-id>
nv show service snmp-server readonly-community <readonly-community-id> access
nv show service snmp-server readonly-community <readonly-community-id> access <access-id>
nv show service snmp-server readonly-community-v6
nv show service snmp-server readonly-community-v6 <readonly-community-id>
nv show service snmp-server readonly-community-v6 <readonly-community-id> access
nv show service snmp-server readonly-community-v6 <readonly-community-id> access <access-id>
nv show service snmp-server trap-link-down
nv show service snmp-server trap-link-up
nv show service snmp-server trap-snmp-auth-failures
nv show service snmp-server trap-cpu-load-average
nv show service snmp-server trap-cpu-load-average one-minute
nv show service snmp-server trap-cpu-load-average one-minute <one-minute-id>
nv show service snmp-server trap-cpu-load-average one-minute <one-minute-id> five-minute
nv show service snmp-server trap-cpu-load-average one-minute <one-minute-id> five-minute <five-minute-id>
nv show service snmp-server trap-cpu-load-average one-minute <one-minute-id> five-minute <five-minute-id> fifteen-minute
nv show service snmp-server trap-cpu-load-average one-minute <one-minute-id> five-minute <five-minute-id> fifteen-minute <fifteen-minute-id>
nv show service snmp-server trap-destination
nv show service snmp-server trap-destination <trap-destination-id>
nv show service snmp-server trap-destination <trap-destination-id> community-password
nv show service snmp-server trap-destination <trap-destination-id> community-password <community-password-id>
nv show service snmp-server trap-destination <trap-destination-id> vrf
nv show service snmp-server trap-destination <trap-destination-id> vrf <vrf-name>
nv show service snmp-server trap-destination <trap-destination-id> vrf <vrf-name> community-password
nv show service snmp-server trap-destination <trap-destination-id> vrf <vrf-name> community-password <community-password-id>
nv show service snmp-server trap-destination <trap-destination-id> vrf <vrf-name> username
nv show service snmp-server trap-destination <trap-destination-id> vrf <vrf-name> username <username-id>
nv show service snmp-server trap-destination <trap-destination-id> vrf <vrf-name> username <username-id> auth-md5
nv show service snmp-server trap-destination <trap-destination-id> vrf <vrf-name> username <username-id> auth-md5 <auth-id>
nv show service snmp-server trap-destination <trap-destination-id> vrf <vrf-name> username <username-id> auth-md5 <auth-id> engine-id
nv show service snmp-server trap-destination <trap-destination-id> vrf <vrf-name> username <username-id> auth-md5 <auth-id> engine-id <engine-id>
nv show service snmp-server trap-destination <trap-destination-id> vrf <vrf-name> username <username-id> auth-md5 <auth-id> encrypt-des
nv show service snmp-server trap-destination <trap-destination-id> vrf <vrf-name> username <username-id> auth-md5 <auth-id> encrypt-des <encrypt-id>
nv show service snmp-server trap-destination <trap-destination-id> vrf <vrf-name> username <username-id> auth-md5 <auth-id> encrypt-des <encrypt-id> engine-id
nv show service snmp-server trap-destination <trap-destination-id> vrf <vrf-name> username <username-id> auth-md5 <auth-id> encrypt-des <encrypt-id> engine-id <engine-id>
nv show service snmp-server trap-destination <trap-destination-id> vrf <vrf-name> username <username-id> auth-md5 <auth-id> encrypt-aes
nv show service snmp-server trap-destination <trap-destination-id> vrf <vrf-name> username <username-id> auth-md5 <auth-id> encrypt-aes <encrypt-id>
nv show service snmp-server trap-destination <trap-destination-id> vrf <vrf-name> username <username-id> auth-md5 <auth-id> encrypt-aes <encrypt-id> engine-id
nv show service snmp-server trap-destination <trap-destination-id> vrf <vrf-name> username <username-id> auth-md5 <auth-id> encrypt-aes <encrypt-id> engine-id <engine-id>
nv show service snmp-server trap-destination <trap-destination-id> vrf <vrf-name> username <username-id> auth-sha
nv show service snmp-server trap-destination <trap-destination-id> vrf <vrf-name> username <username-id> auth-sha <auth-id>
nv show service snmp-server trap-destination <trap-destination-id> vrf <vrf-name> username <username-id> auth-sha <auth-id> engine-id
nv show service snmp-server trap-destination <trap-destination-id> vrf <vrf-name> username <username-id> auth-sha <auth-id> engine-id <engine-id>
nv show service snmp-server trap-destination <trap-destination-id> vrf <vrf-name> username <username-id> auth-sha <auth-id> encrypt-des
nv show service snmp-server trap-destination <trap-destination-id> vrf <vrf-name> username <username-id> auth-sha <auth-id> encrypt-des <encrypt-id>
nv show service snmp-server trap-destination <trap-destination-id> vrf <vrf-name> username <username-id> auth-sha <auth-id> encrypt-des <encrypt-id> engine-id
nv show service snmp-server trap-destination <trap-destination-id> vrf <vrf-name> username <username-id> auth-sha <auth-id> encrypt-des <encrypt-id> engine-id <engine-id>
nv show service snmp-server trap-destination <trap-destination-id> vrf <vrf-name> username <username-id> auth-sha <auth-id> encrypt-aes
nv show service snmp-server trap-destination <trap-destination-id> vrf <vrf-name> username <username-id> auth-sha <auth-id> encrypt-aes <encrypt-id>
nv show service snmp-server trap-destination <trap-destination-id> vrf <vrf-name> username <username-id> auth-sha <auth-id> encrypt-aes <encrypt-id> engine-id
nv show service snmp-server trap-destination <trap-destination-id> vrf <vrf-name> username <username-id> auth-sha <auth-id> encrypt-aes <encrypt-id> engine-id <engine-id>
nv show service snmp-server trap-destination <trap-destination-id> username
nv show service snmp-server trap-destination <trap-destination-id> username <username-id>
nv show service snmp-server trap-destination <trap-destination-id> username <username-id> auth-md5
nv show service snmp-server trap-destination <trap-destination-id> username <username-id> auth-md5 <auth-id>
nv show service snmp-server trap-destination <trap-destination-id> username <username-id> auth-md5 <auth-id> engine-id
nv show service snmp-server trap-destination <trap-destination-id> username <username-id> auth-md5 <auth-id> engine-id <engine-id>
nv show service snmp-server trap-destination <trap-destination-id> username <username-id> auth-md5 <auth-id> encrypt-des
nv show service snmp-server trap-destination <trap-destination-id> username <username-id> auth-md5 <auth-id> encrypt-des <encrypt-id>
nv show service snmp-server trap-destination <trap-destination-id> username <username-id> auth-md5 <auth-id> encrypt-des <encrypt-id> engine-id
nv show service snmp-server trap-destination <trap-destination-id> username <username-id> auth-md5 <auth-id> encrypt-des <encrypt-id> engine-id <engine-id>
nv show service snmp-server trap-destination <trap-destination-id> username <username-id> auth-md5 <auth-id> encrypt-aes
nv show service snmp-server trap-destination <trap-destination-id> username <username-id> auth-md5 <auth-id> encrypt-aes <encrypt-id>
nv show service snmp-server trap-destination <trap-destination-id> username <username-id> auth-md5 <auth-id> encrypt-aes <encrypt-id> engine-id
nv show service snmp-server trap-destination <trap-destination-id> username <username-id> auth-md5 <auth-id> encrypt-aes <encrypt-id> engine-id <engine-id>
nv show service snmp-server trap-destination <trap-destination-id> username <username-id> auth-sha
nv show service snmp-server trap-destination <trap-destination-id> username <username-id> auth-sha <auth-id>
nv show service snmp-server trap-destination <trap-destination-id> username <username-id> auth-sha <auth-id> engine-id
nv show service snmp-server trap-destination <trap-destination-id> username <username-id> auth-sha <auth-id> engine-id <engine-id>
nv show service snmp-server trap-destination <trap-destination-id> username <username-id> auth-sha <auth-id> encrypt-des
nv show service snmp-server trap-destination <trap-destination-id> username <username-id> auth-sha <auth-id> encrypt-des <encrypt-id>
nv show service snmp-server trap-destination <trap-destination-id> username <username-id> auth-sha <auth-id> encrypt-des <encrypt-id> engine-id
nv show service snmp-server trap-destination <trap-destination-id> username <username-id> auth-sha <auth-id> encrypt-des <encrypt-id> engine-id <engine-id>
nv show service snmp-server trap-destination <trap-destination-id> username <username-id> auth-sha <auth-id> encrypt-aes
nv show service snmp-server trap-destination <trap-destination-id> username <username-id> auth-sha <auth-id> encrypt-aes <encrypt-id>
nv show service snmp-server trap-destination <trap-destination-id> username <username-id> auth-sha <auth-id> encrypt-aes <encrypt-id> engine-id
nv show service snmp-server trap-destination <trap-destination-id> username <username-id> auth-sha <auth-id> encrypt-aes <encrypt-id> engine-id <engine-id>
nv show service ptp <instance-id> unicast-master
nv show service ptp <instance-id> unicast-master <table-id>
nv show service ptp <instance-id> unicast-master <table-id> address
nv show service ptp <instance-id> unicast-master <table-id> address <ip-mac-address-id>
nv show service ptp <instance-id> profile
nv show service ptp <instance-id> profile <profile-id>
nv show system global l3svd
nv show system forwarding
nv show system forwarding lag-hash
nv show system forwarding ecmp-hash
nv show system nat
nv show system reflexive-acl
nv show acl <acl-id> rule <rule-id> match conntrack
nv show acl <acl-id> rule <rule-id> match conntrack <conntrack-id>
nv show acl <acl-id> rule <rule-id> action source-nat
nv show acl <acl-id> rule <rule-id> action source-nat translate-ip
nv show acl <acl-id> rule <rule-id> action source-nat translate-ip <range-id>
nv show acl <acl-id> rule <rule-id> action source-nat translate-port
nv show acl <acl-id> rule <rule-id> action source-nat translate-port <ip-port-id>
nv show acl <acl-id> rule <rule-id> action dest-nat
nv show acl <acl-id> rule <rule-id> action dest-nat translate-ip
nv show acl <acl-id> rule <rule-id> action dest-nat translate-ip <range-id>
nv show acl <acl-id> rule <rule-id> action dest-nat translate-port
nv show acl <acl-id> rule <rule-id> action dest-nat translate-port <ip-port-id>
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
nv set service snmp-server
nv set service snmp-server listening-address <listening-address-id>
nv set service snmp-server listening-address <listening-address-id> vrf <vrf-name>
nv set service snmp-server username <username-id>
nv set service snmp-server username <username-id> auth-none
nv set service snmp-server username <username-id> auth-none oid <oid>
nv set service snmp-server username <username-id> auth-none view <value>
nv set service snmp-server username <username-id> auth-md5 <auth-id>
nv set service snmp-server username <username-id> auth-md5 <auth-id> encrypt-des <encrypt-id>
nv set service snmp-server username <username-id> auth-md5 <auth-id> encrypt-des <encrypt-id> oid <oid>
nv set service snmp-server username <username-id> auth-md5 <auth-id> encrypt-des <encrypt-id> view <value>
nv set service snmp-server username <username-id> auth-md5 <auth-id> encrypt-aes <encrypt-id>
nv set service snmp-server username <username-id> auth-md5 <auth-id> encrypt-aes <encrypt-id> oid <oid>
nv set service snmp-server username <username-id> auth-md5 <auth-id> encrypt-aes <encrypt-id> view <value>
nv set service snmp-server username <username-id> auth-md5 <auth-id> oid <oid>
nv set service snmp-server username <username-id> auth-md5 <auth-id> view <value>
nv set service snmp-server username <username-id> auth-sha <auth-id>
nv set service snmp-server username <username-id> auth-sha <auth-id> encrypt-des <encrypt-id>
nv set service snmp-server username <username-id> auth-sha <auth-id> encrypt-des <encrypt-id> oid <oid>
nv set service snmp-server username <username-id> auth-sha <auth-id> encrypt-des <encrypt-id> view <value>
nv set service snmp-server username <username-id> auth-sha <auth-id> encrypt-aes <encrypt-id>
nv set service snmp-server username <username-id> auth-sha <auth-id> encrypt-aes <encrypt-id> oid <oid>
nv set service snmp-server username <username-id> auth-sha <auth-id> encrypt-aes <encrypt-id> view <value>
nv set service snmp-server username <username-id> auth-sha <auth-id> oid <oid>
nv set service snmp-server username <username-id> auth-sha <auth-id> view <value>
nv set service snmp-server mibs (cumulus-sensor-mib|cumulus-status-mib)
nv set service snmp-server viewname <viewname-id>
nv set service snmp-server viewname <viewname-id> excluded <snmp-branch>
nv set service snmp-server viewname <viewname-id> included <snmp-branch>
nv set service snmp-server readonly-community <readonly-community-id>
nv set service snmp-server readonly-community <readonly-community-id> access <access-id>
nv set service snmp-server readonly-community <readonly-community-id> access <access-id> oid <oid>
nv set service snmp-server readonly-community <readonly-community-id> access <access-id> view <value>
nv set service snmp-server readonly-community-v6 <readonly-community-id>
nv set service snmp-server readonly-community-v6 <readonly-community-id> access <access-id>
nv set service snmp-server readonly-community-v6 <readonly-community-id> access <access-id> oid <oid>
nv set service snmp-server readonly-community-v6 <readonly-community-id> access <access-id> view <value>
nv set service snmp-server trap-link-down
nv set service snmp-server trap-link-down check-frequency 5-300
nv set service snmp-server trap-link-up
nv set service snmp-server trap-link-up check-frequency 5-300
nv set service snmp-server trap-snmp-auth-failures
nv set service snmp-server trap-cpu-load-average
nv set service snmp-server trap-cpu-load-average one-minute <one-minute-id>
nv set service snmp-server trap-cpu-load-average one-minute <one-minute-id> five-minute <five-minute-id>
nv set service snmp-server trap-cpu-load-average one-minute <one-minute-id> five-minute <five-minute-id> fifteen-minute <fifteen-minute-id>
nv set service snmp-server trap-destination <trap-destination-id>
nv set service snmp-server trap-destination <trap-destination-id> community-password <community-password-id>
nv set service snmp-server trap-destination <trap-destination-id> community-password <community-password-id> version (1|2c)
nv set service snmp-server trap-destination <trap-destination-id> vrf <vrf-name>
nv set service snmp-server trap-destination <trap-destination-id> vrf <vrf-name> community-password <community-password-id>
nv set service snmp-server trap-destination <trap-destination-id> vrf <vrf-name> community-password <community-password-id> version (1|2c)
nv set service snmp-server trap-destination <trap-destination-id> vrf <vrf-name> username <username-id>
nv set service snmp-server trap-destination <trap-destination-id> vrf <vrf-name> username <username-id> auth-md5 <auth-id>
nv set service snmp-server trap-destination <trap-destination-id> vrf <vrf-name> username <username-id> auth-md5 <auth-id> engine-id <engine-id>
nv set service snmp-server trap-destination <trap-destination-id> vrf <vrf-name> username <username-id> auth-md5 <auth-id> engine-id <engine-id> inform (on|off)
nv set service snmp-server trap-destination <trap-destination-id> vrf <vrf-name> username <username-id> auth-md5 <auth-id> encrypt-des <encrypt-id>
nv set service snmp-server trap-destination <trap-destination-id> vrf <vrf-name> username <username-id> auth-md5 <auth-id> encrypt-des <encrypt-id> engine-id <engine-id>
nv set service snmp-server trap-destination <trap-destination-id> vrf <vrf-name> username <username-id> auth-md5 <auth-id> encrypt-des <encrypt-id> engine-id <engine-id> inform (on|off)
nv set service snmp-server trap-destination <trap-destination-id> vrf <vrf-name> username <username-id> auth-md5 <auth-id> encrypt-aes <encrypt-id>
nv set service snmp-server trap-destination <trap-destination-id> vrf <vrf-name> username <username-id> auth-md5 <auth-id> encrypt-aes <encrypt-id> engine-id <engine-id>
nv set service snmp-server trap-destination <trap-destination-id> vrf <vrf-name> username <username-id> auth-md5 <auth-id> encrypt-aes <encrypt-id> engine-id <engine-id> inform (on|off)
nv set service snmp-server trap-destination <trap-destination-id> vrf <vrf-name> username <username-id> auth-sha <auth-id>
nv set service snmp-server trap-destination <trap-destination-id> vrf <vrf-name> username <username-id> auth-sha <auth-id> engine-id <engine-id>
nv set service snmp-server trap-destination <trap-destination-id> vrf <vrf-name> username <username-id> auth-sha <auth-id> engine-id <engine-id> inform (on|off)
nv set service snmp-server trap-destination <trap-destination-id> vrf <vrf-name> username <username-id> auth-sha <auth-id> encrypt-des <encrypt-id>
nv set service snmp-server trap-destination <trap-destination-id> vrf <vrf-name> username <username-id> auth-sha <auth-id> encrypt-des <encrypt-id> engine-id <engine-id>
nv set service snmp-server trap-destination <trap-destination-id> vrf <vrf-name> username <username-id> auth-sha <auth-id> encrypt-des <encrypt-id> engine-id <engine-id> inform (on|off)
nv set service snmp-server trap-destination <trap-destination-id> vrf <vrf-name> username <username-id> auth-sha <auth-id> encrypt-aes <encrypt-id>
nv set service snmp-server trap-destination <trap-destination-id> vrf <vrf-name> username <username-id> auth-sha <auth-id> encrypt-aes <encrypt-id> engine-id <engine-id>
nv set service snmp-server trap-destination <trap-destination-id> vrf <vrf-name> username <username-id> auth-sha <auth-id> encrypt-aes <encrypt-id> engine-id <engine-id> inform (on|off)
nv set service snmp-server trap-destination <trap-destination-id> username <username-id>
nv set service snmp-server trap-destination <trap-destination-id> username <username-id> auth-md5 <auth-id>
nv set service snmp-server trap-destination <trap-destination-id> username <username-id> auth-md5 <auth-id> engine-id <engine-id>
nv set service snmp-server trap-destination <trap-destination-id> username <username-id> auth-md5 <auth-id> engine-id <engine-id> inform (on|off)
nv set service snmp-server trap-destination <trap-destination-id> username <username-id> auth-md5 <auth-id> encrypt-des <encrypt-id>
nv set service snmp-server trap-destination <trap-destination-id> username <username-id> auth-md5 <auth-id> encrypt-des <encrypt-id> engine-id <engine-id>
nv set service snmp-server trap-destination <trap-destination-id> username <username-id> auth-md5 <auth-id> encrypt-des <encrypt-id> engine-id <engine-id> inform (on|off)
nv set service snmp-server trap-destination <trap-destination-id> username <username-id> auth-md5 <auth-id> encrypt-aes <encrypt-id>
nv set service snmp-server trap-destination <trap-destination-id> username <username-id> auth-md5 <auth-id> encrypt-aes <encrypt-id> engine-id <engine-id>
nv set service snmp-server trap-destination <trap-destination-id> username <username-id> auth-md5 <auth-id> encrypt-aes <encrypt-id> engine-id <engine-id> inform (on|off)
nv set service snmp-server trap-destination <trap-destination-id> username <username-id> auth-sha <auth-id>
nv set service snmp-server trap-destination <trap-destination-id> username <username-id> auth-sha <auth-id> engine-id <engine-id>
nv set service snmp-server trap-destination <trap-destination-id> username <username-id> auth-sha <auth-id> engine-id <engine-id> inform (on|off)
nv set service snmp-server trap-destination <trap-destination-id> username <username-id> auth-sha <auth-id> encrypt-des <encrypt-id>
nv set service snmp-server trap-destination <trap-destination-id> username <username-id> auth-sha <auth-id> encrypt-des <encrypt-id> engine-id <engine-id>
nv set service snmp-server trap-destination <trap-destination-id> username <username-id> auth-sha <auth-id> encrypt-des <encrypt-id> engine-id <engine-id> inform (on|off)
nv set service snmp-server trap-destination <trap-destination-id> username <username-id> auth-sha <auth-id> encrypt-aes <encrypt-id>
nv set service snmp-server trap-destination <trap-destination-id> username <username-id> auth-sha <auth-id> encrypt-aes <encrypt-id> engine-id <engine-id>
nv set service snmp-server trap-destination <trap-destination-id> username <username-id> auth-sha <auth-id> encrypt-aes <encrypt-id> engine-id <engine-id> inform (on|off)
nv set service snmp-server system-contact <value>
nv set service snmp-server system-location <value>
nv set service snmp-server system-name <value>
nv set service ptp <instance-id> unicast-master <table-id>
nv set service ptp <instance-id> unicast-master <table-id> address <ip-mac-address-id>
nv set service ptp <instance-id> unicast-master <table-id> query-interval -3-4
nv set service ptp <instance-id> unicast-master <table-id> peer-address (<ipv4>|<ipv6>)
nv set service ptp <instance-id> profile <profile-id>
nv set service ptp <instance-id> profile <profile-id> profile-type (ieee-1588|smpte-st-2059-2|itu-g-8275-1|itu-g-8275-2)
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
nv set system global l3svd
nv set system global l3svd enable (on|off)
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
nv set system nat
nv set system nat enable (on|off)
nv set system nat age-poll-interval 1-1440
nv set system nat table-size 512-8192
nv set system nat config-table-size 64-1024
nv set system nat mode (dynamic|static)
nv set system reflexive-acl
nv set system reflexive-acl enable (on|off)
nv set system reflexive-acl age-poll-interval 1-15
nv set system reflexive-acl cpu-trap-policer-rate 100-1000
nv set system reflexive-acl unestablished-flow-rate 1000-5000
nv set acl <acl-id> rule <rule-id> match conntrack <conntrack-id>
nv set acl <acl-id> rule <rule-id> action source-nat
nv set acl <acl-id> rule <rule-id> action source-nat translate-ip <range-id>
nv set acl <acl-id> rule <rule-id> action source-nat translate-ip <range-id> to <ipv4>
nv set acl <acl-id> rule <rule-id> action source-nat translate-port <ip-port-id>
nv set acl <acl-id> rule <rule-id> action dest-nat
nv set acl <acl-id> rule <rule-id> action dest-nat translate-ip <range-id>
nv set acl <acl-id> rule <rule-id> action dest-nat translate-ip <range-id> to <ipv4>
nv set acl <acl-id> rule <rule-id> action dest-nat translate-port <ip-port-id>
nv set acl <acl-id> rule <rule-id> action police sw-action accept
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
nv unset service snmp-server
nv unset service snmp-server listening-address
nv unset service snmp-server listening-address <listening-address-id>
nv unset service snmp-server listening-address <listening-address-id> vrf
nv unset service snmp-server username
nv unset service snmp-server username <username-id>
nv unset service snmp-server username <username-id> auth-none
nv unset service snmp-server username <username-id> auth-none oid
nv unset service snmp-server username <username-id> auth-none view
nv unset service snmp-server username <username-id> auth-md5
nv unset service snmp-server username <username-id> auth-md5 <auth-id>
nv unset service snmp-server username <username-id> auth-md5 <auth-id> encrypt-des
nv unset service snmp-server username <username-id> auth-md5 <auth-id> encrypt-des <encrypt-id>
nv unset service snmp-server username <username-id> auth-md5 <auth-id> encrypt-des <encrypt-id> oid
nv unset service snmp-server username <username-id> auth-md5 <auth-id> encrypt-des <encrypt-id> view
nv unset service snmp-server username <username-id> auth-md5 <auth-id> encrypt-aes
nv unset service snmp-server username <username-id> auth-md5 <auth-id> encrypt-aes <encrypt-id>
nv unset service snmp-server username <username-id> auth-md5 <auth-id> encrypt-aes <encrypt-id> oid
nv unset service snmp-server username <username-id> auth-md5 <auth-id> encrypt-aes <encrypt-id> view
nv unset service snmp-server username <username-id> auth-md5 <auth-id> oid
nv unset service snmp-server username <username-id> auth-md5 <auth-id> view
nv unset service snmp-server username <username-id> auth-sha
nv unset service snmp-server username <username-id> auth-sha <auth-id>
nv unset service snmp-server username <username-id> auth-sha <auth-id> encrypt-des
nv unset service snmp-server username <username-id> auth-sha <auth-id> encrypt-des <encrypt-id>
nv unset service snmp-server username <username-id> auth-sha <auth-id> encrypt-des <encrypt-id> oid
nv unset service snmp-server username <username-id> auth-sha <auth-id> encrypt-des <encrypt-id> view
nv unset service snmp-server username <username-id> auth-sha <auth-id> encrypt-aes
nv unset service snmp-server username <username-id> auth-sha <auth-id> encrypt-aes <encrypt-id>
nv unset service snmp-server username <username-id> auth-sha <auth-id> encrypt-aes <encrypt-id> oid
nv unset service snmp-server username <username-id> auth-sha <auth-id> encrypt-aes <encrypt-id> view
nv unset service snmp-server username <username-id> auth-sha <auth-id> oid
nv unset service snmp-server username <username-id> auth-sha <auth-id> view
nv unset service snmp-server mibs
nv unset service snmp-server viewname
nv unset service snmp-server viewname <viewname-id>
nv unset service snmp-server viewname <viewname-id> excluded
nv unset service snmp-server viewname <viewname-id> included
nv unset service snmp-server readonly-community
nv unset service snmp-server readonly-community <readonly-community-id>
nv unset service snmp-server readonly-community <readonly-community-id> access
nv unset service snmp-server readonly-community <readonly-community-id> access <access-id>
nv unset service snmp-server readonly-community <readonly-community-id> access <access-id> oid
nv unset service snmp-server readonly-community <readonly-community-id> access <access-id> view
nv unset service snmp-server readonly-community-v6
nv unset service snmp-server readonly-community-v6 <readonly-community-id>
nv unset service snmp-server readonly-community-v6 <readonly-community-id> access
nv unset service snmp-server readonly-community-v6 <readonly-community-id> access <access-id>
nv unset service snmp-server readonly-community-v6 <readonly-community-id> access <access-id> oid
nv unset service snmp-server readonly-community-v6 <readonly-community-id> access <access-id> view
nv unset service snmp-server trap-link-down
nv unset service snmp-server trap-link-down check-frequency
nv unset service snmp-server trap-link-up
nv unset service snmp-server trap-link-up check-frequency
nv unset service snmp-server trap-snmp-auth-failures
nv unset service snmp-server trap-cpu-load-average
nv unset service snmp-server trap-cpu-load-average one-minute
nv unset service snmp-server trap-cpu-load-average one-minute <one-minute-id>
nv unset service snmp-server trap-cpu-load-average one-minute <one-minute-id> five-minute
nv unset service snmp-server trap-cpu-load-average one-minute <one-minute-id> five-minute <five-minute-id>
nv unset service snmp-server trap-cpu-load-average one-minute <one-minute-id> five-minute <five-minute-id> fifteen-minute
nv unset service snmp-server trap-cpu-load-average one-minute <one-minute-id> five-minute <five-minute-id> fifteen-minute <fifteen-minute-id>
nv unset service snmp-server trap-destination
nv unset service snmp-server trap-destination <trap-destination-id>
nv unset service snmp-server trap-destination <trap-destination-id> community-password
nv unset service snmp-server trap-destination <trap-destination-id> community-password <community-password-id>
nv unset service snmp-server trap-destination <trap-destination-id> community-password <community-password-id> version
nv unset service snmp-server trap-destination <trap-destination-id> vrf
nv unset service snmp-server trap-destination <trap-destination-id> vrf <vrf-name>
nv unset service snmp-server trap-destination <trap-destination-id> vrf <vrf-name> community-password
nv unset service snmp-server trap-destination <trap-destination-id> vrf <vrf-name> community-password <community-password-id>
nv unset service snmp-server trap-destination <trap-destination-id> vrf <vrf-name> community-password <community-password-id> version
nv unset service snmp-server trap-destination <trap-destination-id> vrf <vrf-name> username
nv unset service snmp-server trap-destination <trap-destination-id> vrf <vrf-name> username <username-id>
nv unset service snmp-server trap-destination <trap-destination-id> vrf <vrf-name> username <username-id> auth-md5
nv unset service snmp-server trap-destination <trap-destination-id> vrf <vrf-name> username <username-id> auth-md5 <auth-id>
nv unset service snmp-server trap-destination <trap-destination-id> vrf <vrf-name> username <username-id> auth-md5 <auth-id> engine-id
nv unset service snmp-server trap-destination <trap-destination-id> vrf <vrf-name> username <username-id> auth-md5 <auth-id> engine-id <engine-id>
nv unset service snmp-server trap-destination <trap-destination-id> vrf <vrf-name> username <username-id> auth-md5 <auth-id> engine-id <engine-id> inform
nv unset service snmp-server trap-destination <trap-destination-id> vrf <vrf-name> username <username-id> auth-md5 <auth-id> encrypt-des
nv unset service snmp-server trap-destination <trap-destination-id> vrf <vrf-name> username <username-id> auth-md5 <auth-id> encrypt-des <encrypt-id>
nv unset service snmp-server trap-destination <trap-destination-id> vrf <vrf-name> username <username-id> auth-md5 <auth-id> encrypt-des <encrypt-id> engine-id
nv unset service snmp-server trap-destination <trap-destination-id> vrf <vrf-name> username <username-id> auth-md5 <auth-id> encrypt-des <encrypt-id> engine-id <engine-id>
nv unset service snmp-server trap-destination <trap-destination-id> vrf <vrf-name> username <username-id> auth-md5 <auth-id> encrypt-des <encrypt-id> engine-id <engine-id> inform
nv unset service snmp-server trap-destination <trap-destination-id> vrf <vrf-name> username <username-id> auth-md5 <auth-id> encrypt-aes
nv unset service snmp-server trap-destination <trap-destination-id> vrf <vrf-name> username <username-id> auth-md5 <auth-id> encrypt-aes <encrypt-id>
nv unset service snmp-server trap-destination <trap-destination-id> vrf <vrf-name> username <username-id> auth-md5 <auth-id> encrypt-aes <encrypt-id> engine-id
nv unset service snmp-server trap-destination <trap-destination-id> vrf <vrf-name> username <username-id> auth-md5 <auth-id> encrypt-aes <encrypt-id> engine-id <engine-id>
nv unset service snmp-server trap-destination <trap-destination-id> vrf <vrf-name> username <username-id> auth-md5 <auth-id> encrypt-aes <encrypt-id> engine-id <engine-id> inform
nv unset service snmp-server trap-destination <trap-destination-id> vrf <vrf-name> username <username-id> auth-sha
nv unset service snmp-server trap-destination <trap-destination-id> vrf <vrf-name> username <username-id> auth-sha <auth-id>
nv unset service snmp-server trap-destination <trap-destination-id> vrf <vrf-name> username <username-id> auth-sha <auth-id> engine-id
nv unset service snmp-server trap-destination <trap-destination-id> vrf <vrf-name> username <username-id> auth-sha <auth-id> engine-id <engine-id>
nv unset service snmp-server trap-destination <trap-destination-id> vrf <vrf-name> username <username-id> auth-sha <auth-id> engine-id <engine-id> inform
nv unset service snmp-server trap-destination <trap-destination-id> vrf <vrf-name> username <username-id> auth-sha <auth-id> encrypt-des
nv unset service snmp-server trap-destination <trap-destination-id> vrf <vrf-name> username <username-id> auth-sha <auth-id> encrypt-des <encrypt-id>
nv unset service snmp-server trap-destination <trap-destination-id> vrf <vrf-name> username <username-id> auth-sha <auth-id> encrypt-des <encrypt-id> engine-id
nv unset service snmp-server trap-destination <trap-destination-id> vrf <vrf-name> username <username-id> auth-sha <auth-id> encrypt-des <encrypt-id> engine-id <engine-id>
nv unset service snmp-server trap-destination <trap-destination-id> vrf <vrf-name> username <username-id> auth-sha <auth-id> encrypt-des <encrypt-id> engine-id <engine-id> inform
nv unset service snmp-server trap-destination <trap-destination-id> vrf <vrf-name> username <username-id> auth-sha <auth-id> encrypt-aes
nv unset service snmp-server trap-destination <trap-destination-id> vrf <vrf-name> username <username-id> auth-sha <auth-id> encrypt-aes <encrypt-id>
nv unset service snmp-server trap-destination <trap-destination-id> vrf <vrf-name> username <username-id> auth-sha <auth-id> encrypt-aes <encrypt-id> engine-id
nv unset service snmp-server trap-destination <trap-destination-id> vrf <vrf-name> username <username-id> auth-sha <auth-id> encrypt-aes <encrypt-id> engine-id <engine-id>
nv unset service snmp-server trap-destination <trap-destination-id> vrf <vrf-name> username <username-id> auth-sha <auth-id> encrypt-aes <encrypt-id> engine-id <engine-id> inform
nv unset service snmp-server trap-destination <trap-destination-id> username
nv unset service snmp-server trap-destination <trap-destination-id> username <username-id>
nv unset service snmp-server trap-destination <trap-destination-id> username <username-id> auth-md5
nv unset service snmp-server trap-destination <trap-destination-id> username <username-id> auth-md5 <auth-id>
nv unset service snmp-server trap-destination <trap-destination-id> username <username-id> auth-md5 <auth-id> engine-id
nv unset service snmp-server trap-destination <trap-destination-id> username <username-id> auth-md5 <auth-id> engine-id <engine-id>
nv unset service snmp-server trap-destination <trap-destination-id> username <username-id> auth-md5 <auth-id> engine-id <engine-id> inform
nv unset service snmp-server trap-destination <trap-destination-id> username <username-id> auth-md5 <auth-id> encrypt-des
nv unset service snmp-server trap-destination <trap-destination-id> username <username-id> auth-md5 <auth-id> encrypt-des <encrypt-id>
nv unset service snmp-server trap-destination <trap-destination-id> username <username-id> auth-md5 <auth-id> encrypt-des <encrypt-id> engine-id
nv unset service snmp-server trap-destination <trap-destination-id> username <username-id> auth-md5 <auth-id> encrypt-des <encrypt-id> engine-id <engine-id>
nv unset service snmp-server trap-destination <trap-destination-id> username <username-id> auth-md5 <auth-id> encrypt-des <encrypt-id> engine-id <engine-id> inform
nv unset service snmp-server trap-destination <trap-destination-id> username <username-id> auth-md5 <auth-id> encrypt-aes
nv unset service snmp-server trap-destination <trap-destination-id> username <username-id> auth-md5 <auth-id> encrypt-aes <encrypt-id>
nv unset service snmp-server trap-destination <trap-destination-id> username <username-id> auth-md5 <auth-id> encrypt-aes <encrypt-id> engine-id
nv unset service snmp-server trap-destination <trap-destination-id> username <username-id> auth-md5 <auth-id> encrypt-aes <encrypt-id> engine-id <engine-id>
nv unset service snmp-server trap-destination <trap-destination-id> username <username-id> auth-md5 <auth-id> encrypt-aes <encrypt-id> engine-id <engine-id> inform
nv unset service snmp-server trap-destination <trap-destination-id> username <username-id> auth-sha
nv unset service snmp-server trap-destination <trap-destination-id> username <username-id> auth-sha <auth-id>
nv unset service snmp-server trap-destination <trap-destination-id> username <username-id> auth-sha <auth-id> engine-id
nv unset service snmp-server trap-destination <trap-destination-id> username <username-id> auth-sha <auth-id> engine-id <engine-id>
nv unset service snmp-server trap-destination <trap-destination-id> username <username-id> auth-sha <auth-id> engine-id <engine-id> inform
nv unset service snmp-server trap-destination <trap-destination-id> username <username-id> auth-sha <auth-id> encrypt-des
nv unset service snmp-server trap-destination <trap-destination-id> username <username-id> auth-sha <auth-id> encrypt-des <encrypt-id>
nv unset service snmp-server trap-destination <trap-destination-id> username <username-id> auth-sha <auth-id> encrypt-des <encrypt-id> engine-id
nv unset service snmp-server trap-destination <trap-destination-id> username <username-id> auth-sha <auth-id> encrypt-des <encrypt-id> engine-id <engine-id>
nv unset service snmp-server trap-destination <trap-destination-id> username <username-id> auth-sha <auth-id> encrypt-des <encrypt-id> engine-id <engine-id> inform
nv unset service snmp-server trap-destination <trap-destination-id> username <username-id> auth-sha <auth-id> encrypt-aes
nv unset service snmp-server trap-destination <trap-destination-id> username <username-id> auth-sha <auth-id> encrypt-aes <encrypt-id>
nv unset service snmp-server trap-destination <trap-destination-id> username <username-id> auth-sha <auth-id> encrypt-aes <encrypt-id> engine-id
nv unset service snmp-server trap-destination <trap-destination-id> username <username-id> auth-sha <auth-id> encrypt-aes <encrypt-id> engine-id <engine-id>
nv unset service snmp-server trap-destination <trap-destination-id> username <username-id> auth-sha <auth-id> encrypt-aes <encrypt-id> engine-id <engine-id> inform
nv unset service snmp-server system-contact
nv unset service snmp-server system-location
nv unset service snmp-server system-name
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
nv unset system global l3svd
nv unset system global l3svd enable
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
nv unset system nat
nv unset system nat enable
nv unset system nat age-poll-interval
nv unset system nat table-size
nv unset system nat config-table-size
nv unset system nat mode
nv unset system reflexive-acl
nv unset system reflexive-acl enable
nv unset system reflexive-acl age-poll-interval
nv unset system reflexive-acl cpu-trap-policer-rate
nv unset system reflexive-acl unestablished-flow-rate
nv unset acl <acl-id> rule <rule-id> match conntrack
nv unset acl <acl-id> rule <rule-id> match conntrack <conntrack-id>
nv unset acl <acl-id> rule <rule-id> action source-nat
nv unset acl <acl-id> rule <rule-id> action source-nat translate-ip
nv unset acl <acl-id> rule <rule-id> action source-nat translate-ip <range-id>
nv unset acl <acl-id> rule <rule-id> action source-nat translate-ip <range-id> to
nv unset acl <acl-id> rule <rule-id> action source-nat translate-port
nv unset acl <acl-id> rule <rule-id> action source-nat translate-port <ip-port-id>
nv unset acl <acl-id> rule <rule-id> action dest-nat
nv unset acl <acl-id> rule <rule-id> action dest-nat translate-ip
nv unset acl <acl-id> rule <rule-id> action dest-nat translate-ip <range-id>
nv unset acl <acl-id> rule <rule-id> action dest-nat translate-ip <range-id> to
nv unset acl <acl-id> rule <rule-id> action dest-nat translate-port
nv unset acl <acl-id> rule <rule-id> action dest-nat translate-port <ip-port-id>
nv unset acl <acl-id> rule <rule-id> action police sw-action
```
{{< /expand >}}

{{%notice info%}}
Cumulus Linux 5.2 includes the NVUE object model. After you upgrade to Cumulus Linux 5.2, running NVUE configuration commands replaces the configuration in files such as `/etc/network/interfaces` and `/etc/frr/frr.conf` and removes any configuration you add manually or with automation tools like Ansible, Chef, or Puppet. To keep your configuration, you can do one of the following:

- Update your automation tools to use NVUE.
- {{<link url="NVIDIA-User-Experience-NVUE/#configure-nvue-to-ignore-linux-files" text="Configure NVUE to ignore certain underlying Linux files">}} when applying configuration changes.
- Use Linux and FRR (vtysh) commands instead of NVUE for **all** switch configuration.

Cumulus Linux 3.7, 4.3, and 4.4 continue to support NCLU. For more information, contact your NVIDIA Spectrum platform sales representative.
{{%/notice%}}
