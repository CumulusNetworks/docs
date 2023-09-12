---
title: Configure NTP for On-premises Appliances
author: NVIDIA
weight: 346
toc: 4
---

## Issue

NVIDIA NetQ uses `{{<exlink url="https://chrony.tuxfamily.org/" text="chrony">}}` to synchronize time on NetQ appliances. `chrony` syncs with NTP to keep the system clock correct in the appliance, as having the correct system clock is necessary for NetQ to function.

By default, NetQ configures `chrony` with public NTP pool servers. However, this does not work for air gapped on-premises environments, as they block egress traffic to NTP pool servers on the internet. If you are using the NetQ On-premises Appliance, you need to verify NTP points to internal NTP pool servers and not to external public servers.

##  Environment

- NetQ 3.2.0 and later

## Resolution

To configure NTP in `chrony`:

1. Edit the `chrony` configuration file:

       cumulus@appliance:~$ sudo nano /etc/chrony/chrony.conf

2. Change the server pool to your internal NTP servers:

       \# About using servers from the NTP Pool Project in general see (LP: #104525).
       \# Approved by Ubuntu Technical Board on 2011-02-08.
       \# See http://www.pool.ntp.org/join.html for more information.
       pool ntp.ubuntu.com        iburst maxsources 4
       pool 0.ubuntu.pool.ntp.org iburst maxsources 1
       pool 1.ubuntu.pool.ntp.org iburst maxsources 1
       pool 2.ubuntu.pool.ntp.org iburst maxsources 2

3. Save the file then restart the `chronyd` service:

       cumulus@appliance:~$ sudo systemctl restart chronyd

For more information about NTP, read the [Cumulus Linux user guide]({{<ref "/cumulus-linux-43/System-Configuration/Setting-Date-and-Time#use-ntp" >}}).
