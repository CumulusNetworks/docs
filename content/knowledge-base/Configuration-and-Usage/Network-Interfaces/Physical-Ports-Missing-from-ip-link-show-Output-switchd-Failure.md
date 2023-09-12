---
title: Physical Ports Missing from ip link show Output - switchd Failure
author: NVIDIA
weight: 416
toc: 4
---

## Issue

`ip link show` displays only the loopback and management (ethX) ports. Physical switch ports — the interfaces starting with `swp` — are not visible to the operating system.

    $ sudo ip link show
    1: lo: <LOOPBACK,UP,LOWER_UP> mtu 16436 qdisc noqueue state UNKNOWN mode DEFAULT 
        link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    2: eth0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc pfifo_fast state UP mode DEFAULT qlen 1000
        link/ether 44:38:39:00:25:d7 brd ff:ff:ff:ff:ff:ff

## Environment

  - Cumulus Linux, all versions

## Cause

The `switchd` daemon sets up the physical ports. When `switchd` fails to start, the physical ports are not visible to the operating system.

## Resolution

Typically, `switchd` fails to start when the Cumulus Linux license is missing.

If you installed your license and `switchd` still fails to start, capture any errors that might occur and generate the `cl-support` files, then send them to the NVIDIA support team.

Follow the appropriate steps below.

### If the Cumulus Linux License Is not Installed

If you do not install a valid license, the physical ports cannot come up. Verify that you installed the license using the `cl-license` command.

    $ sudo cl-license
    No license installed!

Contact the NVIDIA support team to obtain a license.
<!-- vale off -->
### switchd Fails to Start with the Error: *Syntax error parsing "thdi\_input\_port\_xon\_enables.xe0-xe127"*
<!-- vale on -->
This error occurs when the port capacity configured on the switch exceeds the capability of the ASIC. Read the heading in the `/etc/cumulus/ports.conf` file for details on how to configure the `ports.conf` file. If the header is missing, run the `cl-img-clear-overlay` command to restore the switch back to its original configuration. Make sure to remove the `/mnt/persist/etc/cumulus/ports.conf` file if it exists.
<!-- vale off -->
### Error: "No attached units. BDE found 0 switch devices."
<!-- vale on -->
An error like this indicates the kernel cannot find the Broadcom ASIC. After you manually start the `switchd` service using the `service switchd start` command, check the `/var/log/switchd.log` for the following error:

    Platform: Cumulus_Networks_LLC
    OS: Unix (Posix)
    Boot flags: Cold boot
    No attached units.
    BDE found 0 switch device(s)
    1421276331.445789 2014-01-11 10:33:51 hal.c:169 CRIT No backends found.
    1421276331.445857 2014-01-11 10:33:51 switchd.c:632 Switchd exiting.

If you see the above error, confirm that the Broadcom ASIC is not seen by the kernel by running the `lspci -v` command. Look for the following output:

    01:00.0 Ethernet controller: Broadcom Corporation Device b850 (rev 03) 
    Subsystem: Broadcom Corporation Device b850 
    Flags: bus master, fast devsel, latency 0, IRQ 21 
    Memory at ff600000 (64-bit, non-prefetchable) [size=256K] 
    Capabilities: [48] Power Management version 3 
    Capabilities: [50] Vital Product Data 
    Capabilities: [58] MSI: Enable- Count=1/1 Maskable- 64bit+ 
    Capabilities: [ac] Express Endpoint, MSI 00 
    Kernel driver in use: linux-kernel-bde

If the above output is missing, replace the switch.

### If switchd Fails to Start for Another Reason

Manually start the `switchd` service using the `service switchd start` command. You must have root/sudo access.

    $ sudo service switchd restart

    can not execute decode-syseeprom
    .py", line 544, in check_output
    raise CalledProcessError(retcode, cmd, output=output)
    subprocess.CalledProcessError: Command '('/usr/cumulus/bin/decode-syseeprom', '-r')' returned non-zero exit status 1
    -m requires a MAC address as an argument
    usage: /usr/sbin/switchd [-n] [-d] [-V] [-L BACKEND=LEVEL [BACKEND=LEVEL]] [-t TABLE_NUM] [-s]

If an error occurs:

1.  Save the entire error message.
2.  Download any Cumulus Linux support files. The support files are
    located in `/var/support/core`.
3.  Open a case with Cumulus Support and upload the above information.
