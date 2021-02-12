---
title: Fast Reboot
author: Cumulus Networks
weight: 53
product: SONiC
version: 4.0
siteSlug: sonic
---

Fast-Reboot updates the control plane with a short (<=30 secs) disruption of the data plane.

{{<img src="/images/sonic/fast-reboot.png">}}

## Requirements
- Data plane disruption not more than 25 seconds for 32 ports platform
- Control plane disruption not more than 90 seconds:
  - data plane will use stale RIB/FIB information while control plane reboots
- Up to 2000 hosts connected to VLAN interfaces
- Up to 6000 IPv4 or up to 3000 IPv6 /64 BGP routes
- LACP in slow mode:
  - updates every 30 seconds
  - timeout in 90 seconds
- BGP stack supports BGP graceful restart: rfc4724
- BGP stack supports announcing of preserved Forwarding state 
- Linux Kernel with kexec enabled which enables loading another Linux kernel without cold reboot of the switch 

## Fast-Reboot Before Control Plane Reboot

Fast-reboot is initiated by running the `/usr/bin/fast-reboot` executable (bash script). This script must be run when a switch is stable. The fast-reboot script does the following:

1. Dumps FDB and ARP entries from the ASIC DB tables into the swss container.
2. Stops (-9) BGPD process to force BGP graceful restart.
3. Stops teamd process allowing teamd to send last update to its peers.
4. Stops docker service otherwise the filesystem of the docker containers will be corrupted.
5. Loads a new kernel from the disk, set fast-reboot argument for the kernel and reboot into the new kernel.

   In this process the data plane is still working

## Fast-Reboot After Control Plane Reboot

1. SONiC loads in the normal way after kexec (the data plane is still working).
2. syncd determines SONiC is loaded after fast-reboot and initializes ASIC in fast-reboot mode (initialize ASIC only, not PHY part).

   At this point, the data plane is disrupted.
3. SONiC starts in the normal way, but SWSS loads FDB and ARP dumps which were saved before the reboot. It allows us to save ~10 seconds for 500 hosts under VLAN.
4. After the LAG member interfaces go up, LACP restores LACP LAG interfaces in a second. BGP forms new sessions and exchanges BGP information in 1-6 seconds. 

   At this point, the data plane is restored.
