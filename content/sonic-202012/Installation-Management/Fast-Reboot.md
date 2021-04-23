---
title: Fast Reboot
author: NVIDIA
weight: 230
product: SONiC
version: 202012
siteSlug: sonic
---

Fast reboot updates the control plane while briefly disrupting the data plane (30 seconds or less).

## Features and Requirements

- Data plane disruption lasts no more than 25 seconds for a 32 port platform.
- Control plane disruption lasts no more than 90 seconds; the data plane uses stale RIB/FIB information while the control plane reboots.
- Up to 2000 hosts connected to VLAN interfaces.
- Up to 6000 IPv4 or up to 3000 IPv6 /64 BGP routes.
- LACP in slow mode:
  - Updates every 30 seconds.
  - Times out in 90 seconds.
- BGP stack supports BGP graceful restart, as per RFC4724.
- BGP stack supports announcing of the preserved forwarding state.
- Linux kernel with `kexec` enabled, which provides for the loading of another Linux kernel without a cold reboot of the switch.

{{<img src="/images/sonic/fast-reboot.png">}}

## Fast Reboot before Control Plane Reboot

Fast reboot is initiated by running the `/usr/bin/fast-reboot` executable, a bash script. This script must be run when a switch is stable. The `fast-reboot` script does the following:

- Dumps FDB and ARP entries from the ASIC DB tables into the SWSS container.
- Stops (-9) the `bgpd` process to force a BGP graceful restart.
- Stops the `teamd` process, allowing `teamd` to send one last update to its peers.
- Stops the `docker` service. This prevents the filesystem of the Docker containers from getting corrupted.
- Loads a new kernel from the disk, sets the `fast-reboot` argument for the kernel and reboots into the new kernel. The data plane is still working during this process.

## Fast Reboot after Control Plane Reboot

1. SONiC loads normally after `kexec` executes; the data plane is still working.
2. `syncd` determines that SONiC is loaded after the fast reboot and initializes the ASIC in fast reboot mode. Only the ASIC is initialized, not the PHY.

   At this point, the data plane is disrupted.
3. SONiC starts normally, but the SWSS container loads the FDB and ARP dumps, which were saved before the reboot. It allows SONiC to save around 10 seconds for 500 hosts under a VLAN.
4. After the LAG member interfaces go up, LACP restores LACP LAG interfaces in 1 second. BGP forms new sessions and exchanges BGP information in 1-6 seconds. 

   At this point, the data plane is restored.
