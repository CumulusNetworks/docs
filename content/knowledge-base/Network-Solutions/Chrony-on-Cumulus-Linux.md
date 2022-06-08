---
title: Chrony on Cumulus Linux
author: NVIDIA
weight: 92
toc: 3
---
On ARM-based platforms running Cumulus Linux 4.3.0, you can use Chrony as the time provider.

To use Chrony, you need to:
- Edit the `/etc/apt/sources.list` file to allow upstream repositories.
- Update the local index from source with the apt command-line utility.
- Remove and `purge` NTP with the apt command-line utility.
- Install Chrony.
- Edit the system configuration to establish Chrony as a management service.
- Add a low latency time source to the Chrony configuration.

Follow these steps:

1. Edit the `/etc/apt/sources.list` file to allow upstream repositories:

   ```
   root@cumulus:mgmt:/home/cumulus# sudo vi /etc/apt/sources.list
   # Cumulus Linux package repository
   deb      http://apt.cumulusnetworks.com/repo CumulusLinux-4-latest cumulus upstream netq
   deb-src  http://apt.cumulusnetworks.com/repo CumulusLinux-4-latest cumulus upstream netq
   
   # NetQ package repository
   #
   deb  http://apps3.cumulusnetworks.com/repos/deb/ CumulusLinux-4 netq-latest
   
   # Debian 10 Buster main package repositories
   # Uncomment these if you want to install upstream Debian packages
   # that are not mirrored in the Cumulus Linux repositories.
   # Packages installed this way may cause problems, and are not
   # officially supported by Cumulus Networks, Inc.
   deb     http://deb.debian.org/debian buster main
   deb     http://deb.debian.org/debian buster-updates main
   deb     http://security.debian.org buster/updates main
   deb     http://deb.debian.org/debian buster-backports main
   
   # Debian 10 Buster main package source repositories
   # Only need to uncomment these if you want to install
   # upstream Debian source packages
   #deb-src http://deb.debian.org/debian buster main
   #deb-src http://deb.debian.org/debian buster-updates main
   #deb-src http://security.debian.org buster/updates main
   #deb-src http://deb.debian.org/debian buster-backports main
   ```

2. Update the local index from source:

   ```
   root@cumulus:mgmt:/home/cumulus# sudo -E apt-get update
   ```

3. Remove and `purge` NTP from the system:

   ```
   root@cumulus:mgmt:/home/cumulus# sudo -E apt-get -y purge --auto-remove ntp
   ```

4. Install Chrony:

   ```
   root@cumulus:mgmt:/home/cumulus# sudo -E apt-get -y install chrony
   ```

5. Add Chrony as a management VRF service to the system startup configuration in the `/etc/vrf/systemd.conf` file:

   ```
   root@cumulus:mgmt:/home/cumulus# sudo vi /etc/vrf/systemd.conf
   # Systemd-based services that are expected to be run in a VRF context.
   #
   # If changes are made to this file run systemctl daemon-reload
   # to re-generate systemd files.
   
   chef-client
   collectd
   dhcpd
   dhcrelay
   docker
   hsflowd
   netq-agent
   netq-notifier
   netqd
   nslcd
   ntp
   puppet
   salt-minion
   snmpd
   snmptrapd
   ssh
   zabbix-agent
   chrony <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
   ```

   ```
   root@cumulus:mgmt:/home/cumulus# systemctl stop chronyd
   root@cumulus:mgmt:/home/cumulus# systemctl disable chronyd
   root@cumulus:mgmt:/home/cumulus# systemctl enable chrony@mgmt
   root@cumulus:mgmt:/home/cumulus# systemctl restart chrony@mgmt
   root@cumulus:mgmt:/home/cumulus# systemctl daemon-reload
   ```

6. For optimal performance, add a low latency time source `/etc/chrony/chrony.conf` configuration file. Use the `chronyc sources -v` syntax to verify the configuration.

   ```
   root@cumulus:mgmt:/home/cumulus# chronyc sources -v
   210 Number of sources = 1
   
     .-- Source mode  '^' = server, '=' = peer, '#' = local clock.
    / .- Source state '*' = current synced, '+' = combined , '-' = not combined,
   | /   '?' = unreachable, 'x' = time may be in error, '~' = time too variable.
   ||                                                 .- xxxx [ yyyy ] +/- zzzz
   ||      Reachability register (octal) -.           |  xxxx = adjusted offset,
   ||      Log2(Polling interval) --.      |          |  yyyy = measured offset,
   ||                                \     |          |  zzzz = estimated error.
   ||                                 |    |           \
   MS Name/IP address         Stratum Poll Reach LastRx Last sample
   ===============================================================================
   ^* master_source.local.>     2   6    77     6  -1102us[ -108ms] +/- 2754us
   ```

For information about Chrony, refer to the {{<exlink url="https://chrony.tuxfamily.org" text="Chrony project page">}}.
