---
title: Hostname Configured in hostname File Is Superseded by the DHCP hostname Option
author: NVIDIA
weight: 251
toc: 4
---

If a Cumulus Linux switch receives a DHCP lease containing the *hostname* option, the received DHCP hostname supersedes any hostname applied in `/etc/hostname.`

## Issue

Changing the system hostname via `/etc/hostname` in Cumulus Linux does not have any effect while an active DHCP lease containing the hostname option exists, or if an active DHCP server continues to offer the hostname option in assigned leases.

## Environment

- Cumulus Linux 2.5.x and later
- Active DHCP lease containing the hostname option cached in `/var/lib/dhcp/dhclient.eth0.leases`, and/or a DHCP server offering a lease containing the hostname option
- DHCP client configuration in `/etc/dhcp/dhclient.conf` containing default parameters *send host-name* and *request host-name*

## Cause

This condition can occur when a switch running Cumulus Linux obtains a DHCP lease on management port eth0 and you attempt to change the hostname by editing `/etc/hostname`.
<!-- vale off -->
If you try to reboot the switch to change to the new hostname configured in `/etc/hostname` while the previous DHCP lease is still active, the DHCP hostname option cached locally on the switch in `/var/lib/dhcp/dhclient.eth0.leases` and/or the hostname option received from an active DHCP server supersedes the name manually configured in `/etc/hostname`.
<!-- vale on -->
Note that even if the DHCP server is not explicitly configured to offer a lease containing the hostname option, it might continue to send a previous version of the switch hostname configured in `/etc/hostname` because Cumulus Linux enables the *send-hostname* option by default in `/etc/dhcp/dhclient.conf`. This causes the switch to send the locally configured hostname in DHCP Discover and Request messages. The DHCP server might cache this value and continue to offer it back in subsequent DHCP offers to the switch as long as the original lease is active, which supersedes any new changes made to `/etc/hostname` on the switch.

## Resolution

You have two ways to work around this issue. You can configure `dhclient.conf` to:

- Supersede the hostname option received from DHCP
- Not request the hostname option in DHCP Discover and Request packets

### Superseding the hostname Option

After configuring the desired hostname in `/etc/hostname`, add the following line to `/etc/dhcp/dhclient.conf` to supersede any received hostname option from DHCP with the desired hostname configured in `/etc/hostname` instead:

    supersede host-name "configured-hostname";

### Not Requesting the hostname Option

If preferred, you can configure `/etc/dhcp/dhclient.conf` to not request the hostname option in the Parameter Request List \[option 55\] in DHCP Discover and Request packets.

To do this, edit `/etc/dhcp/dhclient.conf `and remove \"host-name\" from the Request option list, as highlighted here:

    request subnet-mask, broadcast-address, time-offset, routers,
     domain-name, domain-name-servers, domain-search, host-name,
     dhcp6.name-servers, dhcp6.domain-search,
     netbios-name-servers, netbios-scope, interface-mtu,
     rfc3442-classless-static-routes, ntp-servers, cumulus-provision-url;
