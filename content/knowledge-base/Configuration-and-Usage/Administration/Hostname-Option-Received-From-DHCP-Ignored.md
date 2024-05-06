---
title: Host-name DHCP Option Ignored on Cumulus Linux
author: NVIDIA
weight: 251
toc: 4
---

## Issue

If a Cumulus Linux switch running 5.9.0 or later with NVUE enabled receives a DHCP lease containing the `host-name` option, it ignores the received hostname and does not apply it.

## Environment

- Cumulus Linux 5.9.0 and later.
- Active DHCP lease containing the `host-name` option cached in `/var/lib/dhcp/dhclient.eth0.leases`, and, or a DHCP server offering a lease containing the `host-name` option.
- You use NVUE to manage the switch or the {{nvued}} and {{nvue-startup}} services are enabled.

## Cause and Resolution

Cumulus Linux 5.9.0 and later ignores the DHCP `host-name` option because NVUE manages the hostname in the `/etc/nvue.d/startup.yaml` file and prevents DHCP from overwriting it. If you do not manage your switch with NVUE, you can enable the DHCP hostname as follows:

1. Disable and stop the `nvued` and `nvue-startup` services:

```
cumulus@switch:~$ sudo systemctl stop nvued.service
cumulus@switch:~$ sudo systemctl stop nvue-startup.service
cumulus@switch:~$ sudo systemctl disable nvued.service
cumulus@switch:~$ sudo systemctl disable nvue-startup.service
```

2. Edit the `/etc/dhcp/dhclient-exit-hooks.d/dhcp-sethostname` file and change the `SETHOSTNAME` variable to `yes`:

```
cumulus@switch:~$ sudo nano /etc/dhcp/dhclient-exit-hooks.d/dhcp-sethostname 
...
SETHOSTNAME="yes"
if [ $SETHOSTNAME = "yes" ] && [ ! -z $new_host_name ]
then
    hostname $new_host_name
    sed --in-place -e "/127\.0\.1\.1/s/^.*$/127.0.1.1  $new_host_name/" /etc/hosts
fi
```

3. Reboot the switch with the `sudo reboot` command or renew the DHCP lease on the interface by bringing it down and up again:

```
cumulus@switch:~$ sudo ifdown eth0; sudo ifup eth0
```
